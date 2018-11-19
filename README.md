# Arris-POTD   [![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/MxLinux/Arris-POTD/blob/master/LICENSE) [![Icons8 License](https://img.shields.io/badge/icons-CC%20BY--ND%203.0-blue.svg)](http://icons8.com)
This is a Windows-specific project that I'm using at work to log into ARRIS data gateways with a pre-generated password-of-the-day stored in a text file on a shared drive. A keyboard command copies the password from a line in the file matching the current date to the clipboard. Debugging messages print to the console, and relevant indications of success or failure are sent via a toast notification. Some portions of this software including debug print statements and try/catch statements are excessive, but like... YOLO.

## Required Imports
`datetime` for dynamic loading of system tray icon based on date.

[`infi.systray`](https://github.com/Infinidat/infi.systray) for System Tray icon.

[`keyboard`](https://github.com/boppreh/keyboard) for registering keyboard shortcuts.

[`pyperclip`](https://github.com/asweigart/pyperclip) for copying text to clipboard.

[`win10toast`](https://github.com/jithurjacob/Windows-10-Toast-Notifications) for creating toast notifications.

## Password-Of-The-Day File Format
This script assumes the lines in the text file to be formatted as follows
```
11/16/18: ABCDE12345
11/17/18: BCDEF23456
11/18/18: CDEFG34567
...
```

## Icons
Icons provided free by [Icons8](http://icons8.com) under [Creative Commons Attribution-NoDerivs 3.0 Unported](https://creativecommons.org/licenses/by-nd/3.0/) license.
