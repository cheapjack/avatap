# Document the avatap img build process for avatap ESP8266 boxes


Owner

@cefn provided some notes on this:

"I mentioned that I would point you to the command which generates all the images for a given museum. You can see the routine at

`https://github.com/cefn/avatap/blob/master/cross/frozen/export.sh`

It relies on at least...

    The machine being configured to be able to build Micropython from source ( https://github.com/micropython/micropython/wiki/Getting-Started ) and having the source placed in a 'micropython' folder alongside the 'avatap' folder
    The source should not be the original micropython source. I made 6 Avatap-specific changes to the micropython source, as indicated at https://github.com/ShrimpingIt/micropython/tree/memorymax to maximise memory, so getting this specific memorymax version is important to being able to load Avatap-size stories. At this stage I am not sure if Avatap can even be loaded without this maximising step.
    the source should also follow ESP8266-specific instructions at https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/overview Following these you should be able to make a Micropython firmware image for the NodeMCU board, not just a regular micropython program to run on your desktop as per the more general instructions at https://github.com/micropython/micropython/wiki/Getting-Started
    The Avatap file python/loader.py specifying the correct 'storyUid' to load the correct story file templates from python/stories/{id}.py ( see https://github.com/cefn/avatap/blob/master/python/loader.py )

This is by no means a simple-to-replicate operation, which is why I hadn't steered you towards using it locally, and have been generating images myself, after you have proven the stories in emulation. Probably there will be additional configuration steps needed if you tried to replicate the build that I haven't recalled, though these should present as clear errors (e.g. something not there) and it should be straightforward to identify the missing element when those errors are hit when configuring a machine for the first time."


I've made the VM then I've just removed the micropython their vagrantfile provides and replaced with your memorymax branch of micropython with git clone -b memorymax https://github.com/ShrimpingIt/micropython.git

I've assumed you need the avatap repo nearby, which we'll want to build into the firmware in my case a new branch arcadeofbabel in the cheapjack/avatap repo with a new test game

## Questions

Just wondered how and when I run your export.sh command; assumed it needs to happen prior to the Compiling Firmware bit but after compiling the ESP Open SDK

I've done everything up to compiling the ESP Open SDK am I right that your export shell script replaces this step?

Alongside avatap repo next to the `memorymax` ShrimpingIt flavour `micropython`, Ill also be needing the 

```
# SCREEN LIBRARY
micropython-st7920
# READER LIBRARY
micropython-mfrc522
# FONT LIBRARY
bitfont
```

Also, in our case with the `export.sh`, I've commented out the last `esptool` flashing CMD out as we'll be doing the flashing locally and not in a Virtual Machine `$ESPTOOLCMD --port /dev/ttyUSB0 --baud 1500000 write_flash --flash_mode dio --flash_size=32m 0 build/firmware-combined.bin`

Thinking about it wrt how we'll work in future, at least on the memory limits of ESP8266 imagine we'll make images for 3-4 box games as we go along

Ive updated a VagrantFile so it adds all these extras

I have madified this line in `export.sh` 
```
export PATH=/home/cefn/Documents/shrimping/git/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
```
to 
```
export PATH=(pwd)/esp-open-sdk/xtensa-lx106-elf/bin:$PATH`
```
# Summary

Can see that the `makeimages.py` is doing the calling of `export.sh`, so I guess running `python3 ~/avatap/cross/frozen/makeimages.py` would make it start building? just a few thoughts if im building this in the Ubuntu Virtual Machine which seems like best bet for us

 * I've made a new branch for each game in cheapjack/avatap, then it can be pulled into the VM easily
 * If populating the avatap folder in the VM from the appropriate git branch for our game will we need to remove `avatap/python/templates/.gitignore` and push templates to the repo in that branch, so that after emulation and testing locally (ie not in the building VM) we've actually got the templates we need? Dont think this applies anywhere else, can't see .gitignore anywhere else.
 * I've changed the path for the esp-open-sdk to reflect my machine to `export PATH=/home/vagrant/esp-open-sdk/xtensa-lx106-elf/bin:$PATH`
 * I changed `imageName` in `makeimages.py` to what I need? Currently hyperloop
 * I changed the `boxCounts` dict in `makeimages.py` to reflect the games I want to build in appropriate branch?
 * I installed realpath as its no longer part of ubuntu distrib it seems

# QUESTION
 * Should I uncomment or change order of these lines in `export.sh`
```
 #$MAKECMD clean
 #$MAKECMD axtls
```
to reflect the compilation in the [Compiling Firmware tutorial](https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/build-firmware#compile-micropython-firmware) below?

```
cd ~/micropython
git submodule update --init
make -C mpy-cross
cd ~/micropython/esp8266
make axtls
make
```
 * And I guess we ignore the `git submodule update` and `make -C mpy-cross` as we are doing a custom build



