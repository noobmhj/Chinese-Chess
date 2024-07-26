***Translate by Baidu***
***由百度翻译进行机器翻译***

#Chinese Chess



---



##Project Introduction

-A simple Chinese chess game implemented in Python**

##Function implementation

-The basic rules of Chinese chess and simple animation sound effects**

##How to use

-* * Just run __main__. py**

-* * Third party packages all use standard libraries**

-The sound effects are implemented using the standard library __winsound__ and seem to only run on the Windows platform**

##Parameter configuration

-There are many global variables in the header of the __main__. py file, such as**

```python3

wavfile = {

"killover" : "./data/wavs/piecekillover.wav",

"kill" : "./data/wavs/piecekill.wav",

"move" : "./data/wavs/piecemove.wav"

}

iconfile = "./ data/images/icon.ico"

imagefiles = "./ data/images/"



displaymode = 'y'



bs = 1

minheight = 600

minwidth = 540



if displaymode == 'x': minheight, minwidth = minwidth, minheight



Tle="Chinese Chess"

gery = "{}x{}".format(int(minwidth * bs), int(minheight * bs))



fpx = 50 * bs

fpy = 50 * bs



length = 55 * bs



null = ' '

pieces = [[null] * 9 for i in range(10)]



wcont = 5

pcont_color = "#7d1d14"

pcolor = "#f0a254"

Pfont=("Kai font", int (20 * bs))



orangecodepi = "100121013201430154014501360127011801712177216031623164316631683160606260646066606860717077701090219032904390549045903690279018900"



redside = "down"

steps = 0



tips = True

fontto = True



redking = None

blackking = None



ani = True

anitime = 0.1

aninum = 10



theme = "draw"

```

-You can make the program present different effects by modifying global variables**

-* * Parameter Description**

- `wavfile`

-Dictionary of Sound Effects Files**

-Killlover is the ultimate sound effect**

-Kill stands for General Sound Effect**

-Move is the sound effect of chess piece movement**

- `iconfile`

-* * Icon file**

- `imagefiles`

-Please stay tuned for the mysterious parameters**

- `displaymode`

-Display mode

-* * ` y ` represents filling with the ` y ` axis**

-* * * 'x' represents filling with the 'x' axis**

- `bs`

-The magnification factor is used for screen adaptation and adjusting window size**

- `minheight`

-* * Minimum height**

- `minwidth`

-* * Minimum width**

- `tle`

-* * i.e. 'title', window title**

- `fpx`

-The 'x' coordinate of the first chess piece in the upper left corner**

- `fpy`

-The 'y' coordinate of the first chess piece in the upper left corner**

- `length`

-The side length of a square in a chessboard composed of squares**

- `null`

-* * Blank placeholder**

- `pieces`

-* * Two dimensional array stores chess pieces**

- `wcont`

-The width of the side length of a square in a chessboard composed of squares**

- `pcont_color`

-The color of a chessboard composed of squares**

- `pcolor`

-The color of the chess piece**

- `pfont`

-Chess font**

- `orangecodepi`

-Please stay tuned for the mysterious parameters**

- `redside`

-* * Direction of the first move**

- `steps`

-* * Steps**

- `tips`

-* * Falling tip**

- `fontto`

-Significant differences in the display of red and black chess pieces**

- `ani`

-* * Animation**

- `anitime`

-Animation duration**

- `aninum`

-* * Animation frame rate**

- `theme`

-Please stay tuned for the mysterious parameters**



##Test environment

- __Windows 10 Python 3.8.10__

-Linux has not been tested**

>Okay, I don't know Linux (-. -), just laugh at me to your heart's content~**

>If you could test it for me on Linux, I would be extremely grateful**

##Update Summary

- **Version 1.0.0**

-* * Update time: ` 20240726`**

-Update Summary**

-* * None**



---

-* * Version 1. x.x Next Version Preview**

-Expected update time: 202408xx`**

-* * Expected Update Summary**

-LAN connection function**

-* * Save and load the game, which is the endgame function**

-* * Join AI Chess Robot**