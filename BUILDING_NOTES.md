# Avatap image and firmware combined build process for avatap ESP8266 boxes

You can see the routine called by `makeimages.py` at

`https://github.com/cefn/avatap/blob/master/cross/frozen/export.sh`

It relies on

 * The machine being configured to be able to build Micropython from source ( https://github.com/micropython/micropython/wiki/Getting-Started ) and having the source placed in a 'micropython' folder alongside the 'avatap' folder

 * The source should not be the original micropython source. But 6 Avatap-specific changes to the micropython source, as indicated at https://github.com/ShrimpingIt/micropython/tree/memorymax to maximise memory, so getting this specific memorymax version is important to being able to load Avatap-size stories. 

 * The source should also follow ESP8266-specific instructions at https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/overview Following these you should be able to make a Micropython firmware image for the NodeMCU board, not just a regular micropython program to run on your desktop as per the more general instructions at https://github.com/micropython/micropython/wiki/Getting-Started

 * The Avatap file python/loader.py specifying the correct 'storyUid' to load the correct story file templates from python/stories/{id}.py ( see https://github.com/cefn/avatap/blob/master/python/loader.py )

 * Make the VM following the adafruit guide above then remove the micropython their vagrantfile provides and replace with memorymax branch of micropython with git clone -b memorymax https://github.com/ShrimpingIt/micropython.git

 * Place the Avatap repo in home directory, which we'll want to build into the firmware

 * Follow guide up to the Compiling Firmware bit but after compiling the ESP Open SDK

 * Add shrimping screen and reader and font libraries in home/vagrant
```
# SCREEN LIBRARY
micropython-st7920
# READER LIBRARY
micropython-mfrc522
# FONT LIBRARY
bitfont
```
 * update a VagrantFile so it adds all these extras

 * change path in `cross/frozen/export.sh`

```
export PATH=/home/cefn/Documents/shrimping/git/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
```
to 
```
export PATH=(pwd)/esp-open-sdk/xtensa-lx106-elf/bin:$PATH`
```

 * Make a new branch for each game in cheapjack/avatap, then it can be pulled into the VM easily when a game has been successfully emulated

 * Change `python/loader.py` to the storyUid's you require with `boxUid` set to max number of boxes.

 * Change the `boxCounts` dict in `makeimages.py` to reflect the games I want to build in appropriate branch

 * Install `sudo apt-get install realpath` as its no longer part of ubuntu distrib it seems

 * Use these lines in `export.sh` on first run otherwise comment out as those elements will be already built in the image so makeimages.py just builds all the templating and avatap routines
```
 #$MAKECMD clean
 #$MAKECMD axtls
```
This reflects the compilation process in the [Compiling Firmware tutorial](https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/build-firmware#compile-micropython-firmware) below?

```
cd ~/micropython
git submodule update --init
make -C mpy-cross
cd ~/micropython/esp8266
make axtls
make
```
 * Make sure you complete the `git submodule update` and `make -C mpy-cross` in the memorymax `micropython` repo as we are doing a custom build

 * Make sure that there is a __main__.py file in the templates folder

 * Ignore any templates, makeimages.py does this in building proces

 * `mkdir nameOfStory` for a new storys firmware.

 * Refer to the [babeltest](https://github.com/cheapjack/avatap/tree/babeltest) branch for the right avatap setup if necessary

 * Run `cross/frozen/makeimages.py` On first run the firmware build will verbosely throw unused variable errors on each img but then you'll see the template building etc. and after about 5 minutes you'll get 3-4 fresh new firmwares for respective boxes.

 * Now push the firmwares back up to the game branch or transfer the files from vagrant ready for using `esptool.py` to flash the avatap boxes

eg
```
esptool.py --port /dev/tty.SLAB_USBtoUART --baud 115200 write_flash --flash_mode dio --flash_size=32m 0 hyperloop1.bin
```
