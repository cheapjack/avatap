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

