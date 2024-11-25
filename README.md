# somFreePy

Experimental somFree mapping for Python

somFreePy is a experiments of somFree usage under Python. For now it is handmade classes for SOM Run-time
classes SOMObject, SOMClass and SOMClassMgr as well as SOM.DLL functions.

# Prepare environment

- Install somFree Toolkit 32-bit version (https://sourceforge.net/projects/somfree/)
- Install Python 32-bit version

# Test

Run 'somenv.cmd'

# Current problems

If any of wrapper classes created for kernel classes then on exit Python tries to destroy them. Such think must
not be done.