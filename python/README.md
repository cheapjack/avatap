# C'mon, 'AV-A-TAP

Getting Started with the Avatap emulator

### Requirements

Make sure you've installed 
 * `python3` 
 * `[pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home)` has nothing to install as it uses the standard python3 components  
 * `PIL` from `Pillow` for `python3` using `pip3` which you'll get from `python3`
  * Install with `$ pip3 install Pillow`

Download or clone these repos `$ git clone repo_address`
 * `[micropython-st7920](https://github.com/ShrimpingIt/micropython-st7920)`
 * `[bitfont](https://github.com/ShrimpingIt/bitfont)`

Add `~/bitfont/python` and `~/micropython-st7920` to your python3 path in your current shell with 

```
export PYTHONPATH=$PYTHONPATH:../../bitfont/python:../../micropython-st7920
```
while in `~/avatap/python`

Or add it permanently to your ~/.bash_profile (replace My_User_Home with your username so it's in your user home folder) with

```
echo -e '# avatap\nexport PYTHONPATH="/Users/My_User_Home/bitfont/python:$PYTHONPATH"\nexport PYTHONPATH="/Users/My_User_Home/micropython-st7920:$PYTHONPATH"' >> ~/.bash_profile
```

Update the paths in ~/.bash_profile with 

```
$ source ~/.bash_profile
```

### Running

Edit `~/avatap/python/loader.py` line 5 to emulate the avatap story file of your choice

Eg `storyUid = "senhouseDoes"` to load the game file you want to emulate

In `~/avatap/python` run the command `$ python3 -m host.laptop` and it should open up the avatap multiple emulator windows.

Then use `a`, `b`, `c` or `d` with `1`, `2`, `3`, `4` to simulate interacting with Box 1,2,3 or 4 with an RFID card/tag `a`

HAPPY TAPPING!

## Editing

### introText

The introText variable is in `stories/__init__/py`. Any other useful often used text and data can go here, then invoked in `stories` files with `from stories import usefulVariable`


Build Images

I would point you to the command which generates all the images for a given museum. You can see the routine at

https://github.com/cefn/avatap/blob/master/cross/frozen/export.sh

It relies on at least...

* The machine being configured to be able to build Micropython from source ( https://github.com/micropython/micropython/wiki/Getting-Started ) and having the source placed in a 'micropython' folder alongside the 'avatap' folder
 * The source should not be the original micropython source. I made 6 Avatap-specific changes to the micropython source, as indicated at https://github.com/ShrimpingIt/micropython/tree/memorymax to maximise memory, so getting this specific memorymax version is important to being able to load Avatap-size stories to the ESP8266. If we upgrade to ESP32 boards this may not be an issue.

Get the memorymax branch with `git clone -b memorymax https://github.com/ShrimpingIt/micropython.git`

 * the source should also follow ESP8266-specific instructions at https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/overview Following these you should be able to make a Micropython firmware image for the NodeMCU board, not just a regular micropython program to run on your desktop as per the more general instructions at https://github.com/micropython/micropython/wiki/Getting-Started
 * The Avatap file `python/loader.py` specifying the correct 'storyUid' to load the correct story file templates from `python/stories/{id}.py` ( see https://github.com/cefn/avatap/blob/master/python/loader.py )

