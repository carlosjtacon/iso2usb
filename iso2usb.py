import os, sys

if len(sys.argv) != 2:
	sys.exit('Usage: sudo %s path-to-iso' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: ISO file %s was not found!' % sys.argv[1])

print 'Locate the disk identifier in the following list:'

f = os.popen('diskutil list')
print f.read()

diskid = raw_input("Type the disk identifier (Something like disk1 or disk1s1): ")

os.system('hdiutil convert -format UDRW -o bootable.img %s' % sys.argv[1])
os.system('mv bootable.img.dmg bootable.img')

os.system('sudo diskutil unmount /dev/%s' % diskid)
print 'It is not stuck, just wait until it finishes.'
print 'Creating bootable usb...'
os.system('sudo dd bs=1m if=bootable.img of=/dev/r%s' % diskid)
os.system('rm -f bootable.img')

print 'Done!'