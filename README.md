imgup
=====

Usage:  
`imgup [-c] FILE1 FILE2 ...`

**-c** - Copy the image URL to the clipboard afterwards

Dependencies:
-------------
* Python 3+
	* pyclip
		* xsel (Linux only)
	* pyimgur

XFCE Screenshooter
------------------
This script can be used with `xfce4-screenshooter` to auto-upload screenshots. Simply bind hotkeys to:

* Fullscreen: `xfce4-screenshooter -f -o "/path/to/imgup.py -c"`
* Selection: `xfce4-screenshooter -r -o "/path/to/imgup.py -c"`
* Active Window: `xfce4-screenshooter -w -o "/path/to/imgup.py -c"`
