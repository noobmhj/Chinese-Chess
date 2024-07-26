# 中国象棋 Chinese Chess

---

## 项目介绍
- **一个用Python实现的简单中国象棋游戏**
## 功能实现
- **中国象棋的基本规则和简单的动画音效**
## 如何使用
- **运行 __main__.py 即可**
- **第三方包均使用标准库**
- **音效是使用的标准库 __winsound__ 实现， 貌似只能在Windows平台运行**
## 参数配置
- **在 __main__.py 文件的头部存在很多全局变量 例如**
```python3
wavfile = {
           "killover" : "./data/wavs/piecekillover.wav",
           "kill" : "./data/wavs/piecekill.wav",
           "move" : "./data/wavs/piecemove.wav"
          }
iconfile = "./data/images/icon.ico"
imagefiles = "./data/images/"

displaymode = 'y'

bs = 1
minheight = 600
minwidth = 540

if displaymode == 'x':  minheight, minwidth = minwidth, minheight

tle = "中国象棋"
gery = "{}x{}".format(int(minwidth * bs), int(minheight * bs))

fpx = 50 * bs
fpy = 50 * bs

length = 55 * bs

null = ' '
pieces = [[null] * 9 for i in range(10)]

wcont = 5
pcont_color = "#7d1d14"
pcolor = "#f0a254"
pfont = ("楷体", int(20 * bs))

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
- **您可以通过修改全局变量的方式让程序呈现出不同的效果**
- **参数说明**
    - `wavfile`
            - **音效文件字典**
            - **killover 即 绝杀音效**
            - **kill 即 将军音效**
            - **move 即 棋子移动音效**
    - `iconfile`
        - **图标文件**
    - `imagefiles`
        - **神秘参数敬请期待**
    - `displaymode`
        - 显示模式
        - **`y` 代表以`y`轴填充**
        - **`x` 代表以`x`轴填充**
    - `bs`
        - **放大倍数用来进行屏幕适配, 调整窗口大小**
    - `minheight` 
        - **最小高度**
    - `minwidth`
        - **最小宽度**
    - `tle`
        - **即`title`, 窗口标题**
    - `fpx`
        - **左上角第一个棋子的`x`坐标**
    - `fpy`
        - **左上角第一个棋子的`y`坐标**
    - `length`
        - **正方形组成的棋盘中正方形的边长**
    - `null`
        - **空白占位符**
    - `pieces`
        - **二维数组存储棋子**
    - `wcont`
        - **正方形组成的棋盘中正方形的边长的宽度**
    - `pcont_color`
        - **正方形组成的棋盘的颜色**
    - `pcolor`
        - **棋子的颜色**        
    - `pfont`
        - **棋子字体**
    - `orangecodepi`
        - **神秘参数敬请期待**
    - `redside`
        - **先手所在方向**
    - `steps`
        - **步数**
    - `tips`
        - **落子提示**
    - `fontto`
        - **红黑棋子 显示 上的明显差异**
    - `ani`
        - **动画**
    - `anitime`
        - **动画持续时间**
    - `aninum`
        - **动画帧数**
    - `theme`
        - **神秘参数敬请期待**

## 测试环境
- __Windows 10 Python 3.8.10__
- **Linux 没有测试**
> **好吧我不会Linux(-.-)， 尽情的嘲笑我吧 www~**
    > **如果您可以替我在Linux上测试的话 我将感激不尽**
## 更新摘要
- **Version 1.0.0**
    - **更新时间: `20240726`**
    - **更新摘要**
        - **无**

---
- **Version 1.x.x 下一个版本预告**
    - **预计更新时间: `202408xx`**
    - **预计更新摘要**
        - **局域网联机功能**
        - **棋局的保存, 载入, 即 残局功能**
        - **加入AI下棋机器人**


  