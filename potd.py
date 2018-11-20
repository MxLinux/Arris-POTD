try:
    from infi.systray import SysTrayIcon as s
except ImportError:
    print("Please install infi.systray library. Exiting.")
    exit()
try:
    from win10toast import ToastNotifier
except ImportError:
    print("Please install win10toast. Exiting")
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
    
# Get raw string to support UNC paths
fname = r"potd.txt" 
now = d.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%y")
year = year[-2:]
date = month + "/" + day + "/" + year
icon = "icons/" + day + ".ico"
icon_short = day + ".ico"
k.add_hotkey('left alt+shift+d', lambda:  copy_potd())
t = ToastNotifier()

def copy_potd(*SysTrayIcon):
    try:
        with open(fname) as search:
            total = sum(1 for lines in open(fname))
            count = 1
            for line in search:
                line = line.rstrip()
                if line[0].isdigit():
                    if len(line) < 20 or len(line) > 20:
                        print("Line " + str(count) + " of " + str(total) + ", length " + str(len(line)) + ", did not match expected length of 20. Skipping.")
                        if count < total:
                            count += 1
                        else:
                            print("Reached EOF at line " + str(count))
                            t.show_toast("File search error:", "Expected line length of 20 characters,\nFound length of " + str(len(line)) + " on line " + str(line), icon_path=icon, duration=5)
                    else:
                        if date == line[0:8]:
                            potd = line[-10:]
                            p.copy(potd)
                            print("Password '" + potd + "' found on line " + str(count))
                            t.show_toast(potd, "Password-of-the-Day copied to clipboard.", icon_path=icon, duration=5)
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
                                    t.show_toast("File search error:", "No line of appropriate length\nmatching today's date " + date, icon_path=icon, duration=5)
                                    break
                                else: 
                                    count += 1
                else:
                    if count < total:
                        count += 1
                        pass
                    else:
                        print("No appropriately formatted lines found.")
                        t.show_toast("File search error:", "No appropriately formatted lines found.", icon_path=icon, duration=5)

    except FileNotFoundError:
        print("Unable to open file " + fname + " for reading. Exiting.")
        t.show_toast("File not found error:", "Unable to open " + fname + " for reading", icon_path=icon, duration=5)
        exit()

menu_options = (("ARRIS POTD", None, copy_potd),)
tray = s(icon, "POTD Copy", menu_options)
tray.start()
