try:
    from infi.systray import SysTrayIcon as s
except ImportError:
    print("Please install infi.systray library. Exiting.")
    exit()

import datetime as d

try:
    import keyboard as k
except ImportError:
    print("Please install keyboard library. Exiting.")
    exit()
try:
    import pyperclip as p
except ImportError:
    print("Please install pyperclip library. Exiting.")
    exit()
try:
    import zroya as z
except ImportError:
    print("Please install zroya library. Exiting.")
    exit()

fname = "potd.txt" # Filename for testing
now = d.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%y")
year = year[-2:]
date = month + "/" + day + "/" + year
icon = "icons/" + day + ".ico"
icon_short = day + ".ico"
k.add_hotkey('left alt+shift+d', lambda:  copy_potd())
z.init(" ", " ", " ", " ", " ")
template = z.Template(z.TemplateType.ImageAndText4)

try:
    template.setImage(icon)
    print("Icon should show as " + icon_short + " for today's date.")
except FileNotFoundError:
    print("Image: " + icon + " not found. Exiting.")
    exit()

def copy_potd(*SysTrayIcon):
    try:
        with open(fname) as search:
            total = sum(1 for lines in open(fname))
            count = 1
            for line in search:
                line = line.rstrip()
                if len(line) < 20 or len(line) > 20:
                    print("Line " + str(count) + " of " + str(total) + ", length " + str(len(line)) + ", did not match expected length of 20. Skipping.")
                    if count < total:
                        count += 1
                    else:
                        print("Reached EOF at line " + str(count))
                        template.setFirstLine("File search error:")
                        template.setSecondLine("Expected line length 20")
                        template.setThirdLine("Found line length " + str(len(line)) + " on line: " + str(count))
                        z.show(template)
                else:
                    if date == line[0:8]:
                        potd = line[-10:]
                        p.copy(potd)
                        print("Password '" + potd + "' found on line " + str(count))
                        template.setFirstLine("Password " + "'" + potd + "' copied!")
                        z.show(template)
                        break
                    else:
                        if count < total:
                            print("Line " + str(count) + " of " + str(total) +  " for date '" + line[0:8] + "' does not match current date. Skipping.")
                            count += 1
                            pass
                        else:
                            if count == total:
                                print("Line " + str(count) + " of " + str(total) + " for date '" + date + "' does not match current date. Skipping")
                                print("Reached EOF at line " + str(count))
                            else: 
                                count += 1
                            template.setFirstLine("File search error:")
                            template.setSecondLine("No line of appropriate length")
                            template.setThirdLine("matching today's date " + date)
                            z.show(template)
                            break
    except FileNotFoundError:
        print("Unable to open file " + fname + " for reading. Exiting.")
        template.setFirstLine("File not found error:")
        template.setSecondLine("Unable to open " + fname + " for reading")
        z.show(template)
        exit()

menu_options = (("ARRIS POTD", None, copy_potd),)
tray = s(icon, "POTD Copy", menu_options)
tray.start()
