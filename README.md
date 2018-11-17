# Arris-POTD
This is a Windows-specific project that I'm using at work to log into ARRIS data gateways with a pre-generated password-of-the-day stored in a text file on a shared drive. A keyboard command copies the password from a line in the file matching the current date to the clipboard. Debugging messages print to the console, notifications for major success or failure messages are sent via a toast notification. 

## Required Imports
`datetime` for dynamic loading of system tray icon based on date.
`keyboard` for registering 
[`infi.systray`](https://github.com/Infinidat/infi.systray) for System Tray icon.
[`pyperclip`](https://github.com/asweigart/pyperclip) for copying text to clipboard.
[`zroya`](https://github.com/malja/zroya) for creating toast notifications.

## Password-Of-The-Day File Format
This script assumes the lines in the text file to be formatted as follows
```
11/16/18: ABCDE12345
11/17/18: BCDEF23456
11/18/18: CDEFG34567
...
```
