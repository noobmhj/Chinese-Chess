# -*- coding:utf-8 -*-

import tkinter
import time
import _thread

try:  import winsound
except:  pass


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


class piece:
    def __init__(self, place, camp):
        x, y = place
        pieces[y][x] = self
        
        self.place = place
        self.camp = camp

        self.special()


    
    def killking(self):
        rx, ry = redking.place
        bx, by = blackking.place

        killred = False
        killblack = False
        
        for i in pieces:
            for p in i:
                if p != null:
                    if p.move(rx, ry):
                        killred = True
                    if p.move(bx, by):
                        killblack = True

        if rx == bx:
            if self.twoppn(rx, ry, bx, by) == 0:
                killred = True
                killblack = True

        return {"red" : killred, "black" : killblack}
        

    def cango(self):
        result = []
        for y in range(0, 10):
            for x in range(0, 9):
                if self.move(x, y):
                    result.append((x, y))

        return result


    def pps(self, ps=pieces):
        for i in ps:
            for p in i:
                if p == null:
                    print("空", end='')
                else:
                    print(p.label, end='')
            print()
        print()


    def twoppn(self, x, y, m, n):
        sm = 0
        dire = 'x' if y == n else 'y'
        l = abs((x - m) if dire == 'x' else (y - n)) - 1
        add = 1 if (x < m) or (y < n) else -1
        for i in range(l):
            if dire == 'x':  x += add
            else:  y += add
            p = pieces[y][x]                
            if p != null:  sm += 1

        return sm


    
    def kill(self, x, y):
        _ = pieces[y][x]
        m, n = self.place

        pieces[y][x] = self
        pieces[n][m] = null
        self.place = [x, y]
        if _ != null:
            if _.pid == '5':  _.place = [-1, -1]

        result = (not (self.killking()[self.camp]))

        pieces[y][x] = _
        pieces[n][m] = self
        self.place = [m, n]
        if _ != null:
            if _.pid == '5':  _.place = [x, y]

        return result
    

        
    state = False
    drawoval = False
    drawtext = False


    twopl = lambda self, x, y, m, n : ((x - m) ** 2 + (y - n) ** 2) ** 0.5
    direction = lambda self, x, y, m, n : 'x' if y == n else 'y'
    getside = lambda self : redside if self.camp == "red" else ("up" if redside == "down" else "down")
            

class che(piece):
    def special(self):
        self.label = "車"
        self.pid = '1'

        
    def move(self, x, y):
        result = False
        m, n = self.place
        if m == x or n == y:
            psm = self.twoppn(x, y, m, n)
            if psm == 0:
                if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                    if self.kill(x, y):
                        result = True

        return result
        
    
class ma(piece):
    def special(self):
        self.label = ("傌" if self.camp == "red" else "馬") if fontto else "馬"
        self.pid = '2'

    
    def move(self, x, y):
        result = False
        m, n = self.place
        if self.twopl(x, y, m, n) == (5 ** 0.5):
            zx = (x - 1) if x > m else (x + 1)
            zy = (y - 1) if y > n else (y + 1)
            if pieces[zy][zx] == null:
                if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                    if self.kill(x, y):
                        result = True

        return result
            
    
class xiang(piece):
    def special(self):
        self.side = self.getside()
        self.label = "相" if self.camp == "red" else "象"
        self.pid = '3'


    def move(self, x, y):
        result = False
        m, n = self.place
        if self.twopl(x, y, m, n) == (8 ** 0.5):
            zx = (x - 1) if x > m else (x + 1)
            zy = (y - 1) if y > n else (y + 1) 
            if pieces[zy][zx] == null:
                if (self.side == "down" and y > 4) or (self.side == "up" and y < 5):
                    if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                        if self.kill(x, y):
                            result = True

        return result
                

class shi(piece):
    def special(self):
        self.side = self.getside()
        self.label = "仕" if self.camp == "red" else "士"
        self.pid = '4'


    def move(self, x, y):
        result = False
        m, n = self.place

        if self.twopl(x, y, m, n) == (2 ** 0.5):
            if (self.side == "down" and y > 6) or (self.side == "up" and y < 3):
                if x > 2 and x < 6:
                    if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                        if self.kill(x, y):
                            result = True

        return result


class zu(piece):
    def special(self):
        self.side = self.getside()
        self.label = "兵" if self.camp == "red" else "卒"
        self.pid = '6'


    def move(self, x, y):
        result = False
        m, n = self.place

        if self.twopl(x, y, m, n) == 1:
            k, j = (m, 0) if self.side == "up" else (m, 9)
            if self.twopl(k, j, x, y) > self.twopl(k, j, m, n):
                k, j = (m, 9) if self.side == "up" else (m, 0)
                
                if (((self.place[1] > 4) if self.side == "down" else (self.place[1] < 5)) and self.twopl(k, j, x, y) < self.twopl(k, j, m, n)) \
                    or ((self.place[1] < 5) if self.side == "down" else (self.place[1] > 4)):
                    
                    if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                        if self.kill(x, y):
                            result = True
                                
        return result
        

class pao(piece):
    def special(self):
        self.label = ("炮" if self.camp == "red" else "砲") if fontto else "炮"
        self.pid = '7'


    def move(self, x, y):
        result = False
        m, n = self.place
        if m == x or n == y:
            psm = self.twoppn(x, y, m, n)
            if (pieces[y][x] == null and psm == 0) or (pieces[y][x] != null and psm == 1):
                if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                    if self.kill(x, y):
                        result = True

        return result
                

class wang(piece):
    def special(self):
        self.side = self.getside()
        self.label = ("帥" if fontto else "帅") if self.camp == "red" else "将"
        self.pid = '5'


    def move(self, x, y):
        result = False
        m, n = self.place

        if self.twopl(x, y, m, n) == 1:
            if (self.side == "down" and y > 6) or (self.side == "up" and y < 3):
                if x > 2 and x < 6:
                    if ((self.camp != pieces[y][x].camp) if pieces[y][x] != null else True):
                        if self.kill(x, y):
                            result = True

        return result

        
class gui:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(tle)
        self.root.geometry(gery)
        self.root.resizable(0, 0)
        self.root.bind("<Button - 1>", self.began)
        
        try:  self.root.iconbitmap(iconfile)
        except:  pass

        expressone = tkinter.Label(master=self.root, text="中  国  象  棋", font=("华文行楷", 60))
        expressone.place(relx=0.5, rely=0.2, anchor="center")
        expressthree = tkinter.Label(master=self.root, text="Powered by NOOBMHJ", font=("Segoe Script", 20))
        expressthree.place(relx=0.5, rely=0.3, anchor="center")

        expressthree = tkinter.Label(master=self.root, text="按下鼠标开始游戏", font=("楷体", 15))
        expressthree.place(relx=0.5, rely=0.7, anchor="center")
        expressthree = tkinter.Label(master=self.root, text="Press the mouse to start game", font=("Segoe Script", 15))
        expressthree.place(relx=0.5, rely=0.75, anchor="center")
        
        self.pids = {
                     '0' : null,
                     '1' : che,
                     '2' : ma,
                     '3' : xiang,
                     '4' : shi,
                     '5' : wang,
                     '6' : zu,
                     '7' : pao
                    }

        self.loadcodepi()

        self.onp = False


    def began(self, _):
        self.canvas = tkinter.Canvas(master=self.root)
        self.canvas.bind("<Button - 1>", self.op)
        self.canvas.place(x=0, y=0, relw=1, relh=1)

        self.root.unbind("<Button - 1>")
        
        self.update()
        

    def playsound(self, sound):
        try:  _thread.start_new_thread(winsound.PlaySound, (sound, winsound.SND_FILENAME))
        except:  pass
        
        
    def twopxy(self, x, y, m, n, k_):
        if x == m or y == n:
            if x == m:
                c = x
                rx = c
                ry = n + (y - n) * k_
            if y == n:
                c = y
                rx = m + (x - m) * k_
                ry = c
        else:
            y *= -1
            n *= -1
            
            k = (y - n) / (x - m)
            b = ((x * n) - (y * m)) / (x - m)

            rx = m + (x - m) * k_
            ry = k * rx + b

            ry *= -1
                        
        return rx, ry

        
    def op(self, _):
        global steps
        
        x, y = _.x, _.y
        x, y = self.to(x, y, mode="re")

        if ((0 <= x <= 8) and (0 <= y <= 9)):
            p = pieces[y][x]
            if self.onp:
                if p != null and p.camp == self.onp.camp:
                    self.onp.state = False
                    self.onp = p
                    self.onp.state = True
                else:
                    if self.onp.move(x, y):
                        m, n = self.onp.place

                        self.onp = False
                        self.update()
                        self.onp = pieces[n][m]

                        if ani:
                            for i in range(aninum):
                                self.canvas.delete(pieces[n][m].drawoval)
                                self.canvas.delete(pieces[n][m].drawtext)
                                
                                _x, _y = self.twopxy(x, y, m, n, (i + 1) / 10)
                                self.onp.place = [_x, _y]
                                self.pdraw(self.onp)

                                time.sleep(anitime / aninum)
                                self.root.update()
                                                    
                        pieces[y][x] = self.onp
                        pieces[n][m] = null

                        self.onp.place = [x, y]
                        self.onp.state = False
                        self.onp = False

                        steps += 1

                        self.playsound(wavfile["move"])

                        rsu = 0
                        bsu = 0
                        for i in pieces:
                            for p in i:
                                if p != null:
                                    if p.camp == "red":
                                        rsu += len(p.cango())
                                    else:
                                        bsu += len(p.cango())
                        if rsu == 0 or bsu == 0:
                            # print("绝杀")
                            self.playsound(wavfile["killover"])
                        else:
                            if redking.killking()["red"] or blackking.killking()["black"]:
                                # print("将军")
                                self.playsound(wavfile["kill"])
                        
                    else:
                        self.onp.state = False
                        self.onp = False
            else:
                if p != null:
                    if (p.camp == "red" and steps % 2 == 0) or (p.camp == "black" and (steps - 1) % 2 == 0):
                        p.state = True
                        self.onp = p
                
            self.update()


    def to(self, x, y, mode="to"):
        if mode == "to":
            m = fpx + x * length
            n = fpy + y * length
        else:
            m = round((x - fpx) / length)
            n = round((y - fpy) / length)
            
        return (m, n) if displaymode == 'y' else (n, m)

    
    def pdraw(self, piece):
        k, j = piece.place

        if theme == "draw":
            le = 0 if piece.state else 0.1
            f = [pfont[0], round(pfont[1] * 1.2)] if piece.state else pfont
            x, y = self.to(k - (0.5 - le), j - (0.5 - le))
            m, n = self.to(k + (0.5 - le), j + (0.5 - le))
            piece.drawoval = self.canvas.create_oval(x, y, m, n, fill=pcolor)
            x, y = self.to(k, j)
            piece.drawtext = self.canvas.create_text(x, y, text=piece.label, font=f, fill=piece.camp)
        elif theme == "image" and piece.camp == "red":
            imagename = piece.camp + piece.pid
    
        

    def ovaldraw(self, place):
        x, y = place
        le = 0.2
        m, n = self.to(x - le, y - le)
        k, j = self.to(x + le, y + le)
        self.canvas.create_oval(m, n, k, j, fill=pcolor)
        
        
    def getcodepi(self):
        codepi = ''
        for y in range(10):
            for x in range(9):
                p = pieces[y][x]
                if p != null:
                    codepi += p.pid
                    codepi += ''.join([str(i)for i in p.place])
                    codepi += '0' if p.camp == "red" else '1'

        codepi += '0' if redside == "down" else '1'
                
        return codepi


    def loadcodepi(self, codepi=orangecodepi):
        global redside, pieces, steps, redking, blackking
        
        sidecode = codepi[-1]
        redside = "down" if sidecode == '0' else "up"
        
        codepi = codepi[:-1]

        pieces = [[null] * 9 for i in range(10)]
        for i in range(0, int(len(codepi) / 4)):
            _ = codepi[i * 4 : i * 4 + 4]
            t, x, y, s = _
            x = int(x)
            y = int(y)
            p = self.pids[t](place=[x, y], camp="red" if s == '0' else "black")
            pieces[y][x] = p

            if t == '5':
                if s == '0':  redking = p
                if s == '1':  blackking = p
                
        steps = 0

        self.update

        
    def update(self):
        self.canvas.delete(tkinter.ALL)

        line = lambda x, y, m, n, fill=pcont_color, width=wcont : self.canvas.create_line(x, y, m, n, fill=fill, width=width)

        lines = [(0, 0, 0, 9), (1, 0, 1, 4), (1, 5, 1, 9), (2, 0, 2, 4),
                 (2, 5, 2, 9), (3, 0, 3, 4), (3, 5, 3, 9), (4, 0, 4, 4),
                 (4, 5, 4, 9), (5, 0, 5, 4), (5, 5, 5, 9), (6, 0, 6, 4),
                 (6, 5, 6, 9), (7, 0, 7, 4), (7, 5, 7, 9), (8, 0, 8, 9),
                 (0, 0, 8, 0), (0, 1, 8, 1), (0, 2, 8, 2), (0, 3, 8, 3),
                 (0, 4, 8, 4), (0, 5, 8, 5), (0, 6, 8, 6), (0, 7, 8, 7),
                 (0, 8, 8, 8), (0, 9, 8, 9), (3, 0, 5, 2), (5, 0, 3, 2),
                 (3, 9, 5, 7), (5, 9, 3, 7)]
        
        for i in lines:
            x, y, m, n = i
            x, y, m, n = self.to(x, y) + self.to(m, n)
            line(x, y, m, n)
 
        for i in pieces:
            for l in i:
                if l != null:
                    self.pdraw(l)
                    
        if tips:
            if self.onp:
                _ = self.onp.cango()
                for i in _:
                    self.ovaldraw(i)


def main():
    _ = gui()
    _.root.mainloop()


if __name__ == "__main__":
    main()
