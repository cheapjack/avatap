#!/bin/bash
set -e 

# Start in script current directory
cd "$(dirname "$(realpath "$0")")";

# prepare paths
GITDIR=$(realpath ../../../)
MODULEDIR="micropython/esp8266/modules"

# prepare commands
ECHO=""
COPYPATHCMD="$ECHO cp -v"
CREATEPATHCMD="$ECHO mkdir -p"
RMPATHCMD="$ECHO rm"
MAKECMD="$ECHO make"
ESPTOOLCMD="$ECHO esptool.py"

# switch to top level folder containing all git repositories
cd $GITDIR

# descend into avatap/python to cache templates, generate QString declarations then return
# If doing this in the VM and populating the avatap folder from the 
# new git branch for our game
# we'll have to remove avatap/python/templates/.gitignore so that after emulation and testing locally not in the building VM  we've actually got the templates
cd avatap/python
# might have to enclose {} with single quotes accorging to the man page like this '{}'
find templates -type f -name 't_*.py' -exec $RMPATHCMD {} \;
python3 -m templates > ../../micropython/esp8266/qstrdefsport.h
cd ../../

# SCREEN LIBRARY
$COPYPATHCMD micropython-st7920/canvas.py $MODULEDIR
$COPYPATHCMD micropython-st7920/st7920.py $MODULEDIR

# READER LIBRARY
$COPYPATHCMD micropython-mfrc522/mfrc522.py $MODULEDIR
$COPYPATHCMD micropython-mfrc522/vault.py $MODULEDIR
# CH TODO REMOVE READER EXAMPLES
$COPYPATHCMD micropython-mfrc522/examples/read.py $MODULEDIR
$COPYPATHCMD micropython-mfrc522/examples/write.py $MODULEDIR

# FONT LIBRARY
$COPYPATHCMD bitfont/python/bitfont.py $MODULEDIR
# FONT FACES
#$RMPATHCMD -R $MODULEDIR/faces || true
$CREATEPATHCMD $MODULEDIR/faces
$COPYPATHCMD bitfont/python/faces/__init__.py $MODULEDIR/faces/
$COPYPATHCMD bitfont/python/faces/font_5x7.py $MODULEDIR/faces/
$COPYPATHCMD bitfont/python/faces/font_timB14.py $MODULEDIR/faces/

# MUSEUM STORIES
$RMPATHCMD -rf $MODULEDIR/stories
$CREATEPATHCMD $MODULEDIR/stories
find avatap/python/stories -maxdepth 1 -type f -name '*.py' -exec $COPYPATHCMD -R {} $MODULEDIR/stories \;

# MUSEUM TEMPLATES
$RMPATHCMD -rf $MODULEDIR/templates
$CREATEPATHCMD $MODULEDIR/templates
find avatap/python/templates -maxdepth 1 -type f -name '*.py' -exec $COPYPATHCMD -R {} $MODULEDIR/templates \;

# MUSEUM STORIES
$RMPATHCMD -rf $MODULEDIR/regimes
$CREATEPATHCMD $MODULEDIR/regimes
find avatap/python/regimes -maxdepth 1 -type f -name '*.py' -exec $COPYPATHCMD -R {} $MODULEDIR/regimes \;

# AVATAP LIBRARIES
find avatap/python -maxdepth 1 -type f -name '*.py' -exec $COPYPATHCMD {} $MODULEDIR \;

# AVATAP HOST LIB (COCKLE-SPECIFIC AVATAP PLATFORM)
#$RMPATHCMD -R $MODULEDIR/host || true
$RMPATHCMD -rf $MODULEDIR/host
$CREATEPATHCMD $MODULEDIR/host
$COPYPATHCMD avatap/python/host/__init__.py $MODULEDIR/host/
$COPYPATHCMD avatap/python/host/cockle.py $MODULEDIR/host/

# AVATAP REGIMES (e.g. INTEGRATION TEST)
#$RMPATHCMD -R $MODULEDIR/regimes || true
$RMPATHCMD -rf $MODULEDIR/regimes
$CREATEPATHCMD $MODULEDIR/regimes
$COPYPATHCMD avatap/python/regimes/integration_test.py $MODULEDIR/regimes/


# TRIGGER FREEZING OF MODULES INTO FIRMWARE IMAGE AND UPLOAD IT
cd micropython/esp8266/
set -e
#new VM path
export PATH=/home/vagrant/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
#export PATH=/home/cefn/Documents/shrimping/git/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
#$MAKECMD clean
#$MAKECMD axtls
$MAKECMD build/firmware-combined.bin
#$MAKECMD PORT=/dev/ttyUSB0 FLASH_MODE=dio FLASH_SIZE=32m deploy
#CH below invocation is faster
# Commented the below out, so that combined .bin image can be deployed locally.
# $ESPTOOLCMD --port /dev/ttyUSB0 --baud 1500000 write_flash --flash_mode dio --flash_size=32m 0 build/firmware-combined.bin

