! I TESTED THIS WITH A RPI + A 32x64 ADAFRUIT RGB LED MATRIX I DON'T THINK IT WILL WORK WITH OTHER STUFF !

if you really want to try this, you must install the "rpi-led-rgb-matrix" library first, then move the .py into the rpi-led-rgb-matrix/bindings/python/samples/ folder (i think that you could clone the file here directly idk) , then, run with python3 sillyfacetest.py --led-cols=64 --led-gpio-mapping=adafuit-hat
