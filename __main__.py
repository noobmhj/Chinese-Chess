import tkinter
import winsound
import _thread
import time


class config:
    def __init__(self):
        self.tle = "中国象棋"
        self.bs = 1
        self.minheight = 600
        self.minwidth = 540
        self.displaymode = 'y'
        self.killover = "./data/wavs/piecekillover.wav"
        self.kill = "./data/wavs/piecekill.wav"
        self.move = "./data/wavs/piecemove.wav"
        self.iconfile = "./data/images/icon.ico"
        self.null = ' '
        self.contwide = 5
        self.contcolor = "#7d1d14"
        self.piececolor = "#f0a254"
        self.orangecodepi = "100121013201430154014501360127011801712177216031623164316631683160606260646066606860717077701090219032904390549045903690279018900"
        self.redside = "down"
        self.steps = 0
        self.tips = True
        self.fontto = True
        self.ani = True
        self.sound = True
        self.anitime = 0.1
        self.aninum = 10
        self.lines = [(0, 0, 0, 9), (1, 0, 1, 4), (1, 5, 1, 9), (2, 0, 2, 4),
                      (2, 5, 2, 9), (3, 0, 3, 4), (3, 5, 3, 9), (4, 0, 4, 4),
                      (4, 5, 4, 9), (5, 0, 5, 4), (5, 5, 5, 9), (6, 0, 6, 4),
                      (6, 5, 6, 9), (7, 0, 7, 4), (7, 5, 7, 9), (8, 0, 8, 9),
                      (0, 0, 8, 0), (0, 1, 8, 1), (0, 2, 8, 2), (0, 3, 8, 3),
                      (0, 4, 8, 4), (0, 5, 8, 5), (0, 6, 8, 6), (0, 7, 8, 7),
                      (0, 8, 8, 8), (0, 9, 8, 9), (3, 0, 5, 2), (5, 0, 3, 2),
                      (3, 9, 5, 7), (5, 9, 3, 7)]
        self.pids = {
                     '0' : self.null,
                     '1' : che,
                     '2' : ma,
                     '3' : xiang,
                     '4' : shi,
                     '5' : wang,
                     '6' : zu,
                     '7' : pao
                    }


    def make(self):
        self.minheight, self.minwidth = (self.minwidth, self.minheight) if self.displaymode == 'x' else (self.minheight, self.minwidth)
        self.gery = "{}x{}".format(int(self.minwidth * self.bs), int(self.minheight * self.bs))
        self.fpx = 50 * self.bs
        self.fpy = 50 * self.bs
        self.length = 55 * self.bs
        self.pieces = [[self.null] * 9 for i in range(10)]
        self.piecefont = ("楷体", int(20 * self.bs))


class piece:
    def __init__(self, place, camp):
        self.place = place
        self.camp = camp

        self.special()

    
    def killking(self):
        rx, ry = cfg.redking.place
        bx, by = cfg.blackking.place

        killred = False
        killblack = False
        
        for i in cfg.pieces:
            for p in i:
                if p != cfg.null:
                    if p.move(rx, ry):
                        killred = True
                    if p.move(bx, by):
                        killblack = True

        if rx == bx:
            if self.twoppn(rx, ry, bx, by) == 0:
                killred = True
                killblack = True

        return {"red" : killred, "black" : killblack}
        

    def twoppn(self, x, y, m, n):
        sm = 0
        dire = 'x' if y == n else 'y'
        l = abs((x - m) if dire == 'x' else (y - n)) - 1
        add = 1 if (x < m) or (y < n) else -1
        for i in range(l):
            if dire == 'x':
                x += add
            else:
                y += add
            p = cfg.pieces[y][x]                
            if p != cfg.null:
                sm += 1

        return sm


    def kill(self, x, y):
        _ = cfg.pieces[y][x]
        m, n = self.place

        cfg.pieces[y][x] = self
        cfg.pieces[n][m] = cfg.null
        self.place = [x, y]
        
        if _ != cfg.null:
            if _.pid == '5':
                _.place = [-1, -1]

        result = (not (self.killking()[self.camp]))

        cfg.pieces[y][x] = _
        cfg.pieces[n][m] = self
        self.place = [m, n]
        
        if _ != cfg.null:
            if _.pid == '5':  _.place = [x, y]

        return result

            
    state = False
    drawoval = False
    drawtext = False

    twopl = lambda self, x, y, m, n : ((x - m) ** 2 + (y - n) ** 2) ** 0.5
    getside = lambda self : cfg.redside if self.camp == "red" else ("up" if cfg.redside == "down" else "down")
    cango = lambda self : [(x, y)for y in range(0, 10)for x in range(0, 9)if self.move(x, y)]

    
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
                if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
                    if self.kill(x, y):
                        result = True

        return result
        
    
class ma(piece):
    def special(self):
        self.label = ("傌" if self.camp == "red" else "馬") if cfg.fontto else "馬"
        self.pid = '2'

    
    def move(self, x, y):
        result = False
        m, n = self.place
        if self.twopl(x, y, m, n) == (5 ** 0.5):
            zx = (x - 1) if x > m else (x + 1)
            zy = (y - 1) if y > n else (y + 1)
            if cfg.pieces[zy][zx] == cfg.null:
                if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
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
            if cfg.pieces[zy][zx] == cfg.null:
                if (self.side == "down" and y > 4) or (self.side == "up" and y < 5):
                    if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
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
                    if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
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
                    
                    if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
                        if self.kill(x, y):
                            result = True
                                
        return result
        

class pao(piece):
    def special(self):
        self.label = ("炮" if self.camp == "red" else "砲") if cfg.fontto else "炮"
        self.pid = '7'


    def move(self, x, y):
        result = False
        m, n = self.place
        if m == x or n == y:
            psm = self.twoppn(x, y, m, n)
            if (cfg.pieces[y][x] == cfg.null and psm == 0) or (cfg.pieces[y][x] != cfg.null and psm == 1):
                if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
                    if self.kill(x, y):
                        result = True

        return result
                

class wang(piece):
    def special(self):
        self.side = self.getside()
        self.label = ("帥" if cfg.fontto else "帅") if self.camp == "red" else "将"
        self.pid = '5'


    def move(self, x, y):
        result = False
        m, n = self.place

        if self.twopl(x, y, m, n) == 1:
            if (self.side == "down" and y > 6) or (self.side == "up" and y < 3):
                if x > 2 and x < 6:
                    if ((self.camp != cfg.pieces[y][x].camp) if cfg.pieces[y][x] != cfg.null else True):
                        if self.kill(x, y):
                            result = True

        return result


class gui:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(cfg.tle)
        self.root.geometry(cfg.gery)
        self.root.resizable(0, 0)
        self.root.bind("<Button - 1>", self.began)

        try:
            self.root.iconbitmap(cfg.iconfile)
        except:
            pass

        expressone = tkinter.Label(master=self.root, text="中 国 象 棋", font=("华文行楷", 60))
        expressone.place(relx=0.5, rely=0.2, anchor="center")
        expressthree = tkinter.Label(master=self.root, text="Powered by NOOBMHJ", font=("Segoe Script", 20))
        expressthree.place(relx=0.5, rely=0.3, anchor="center")

        expressthree = tkinter.Label(master=self.root, text="按下鼠标开始游戏", font=("楷体", 15))
        expressthree.place(relx=0.5, rely=0.7, anchor="center")
        expressthree = tkinter.Label(master=self.root, text="Press the mouse to start game", font=("Segoe Script", 15))
        expressthree.place(relx=0.5, rely=0.75, anchor="center")

        self.loadcodepi(codepi=cfg.orangecodepi)
        self.onpresspiece = False

        
    def began(self, _):
        self.canvas = tkinter.Canvas(master=self.root)
        self.canvas.bind("<Button - 1>", self.onpress)
        self.canvas.place(x=0, y=0, relw=1, relh=1)
        self.root.unbind("<Button - 1>")
        
        self.update()


    def playsound(self, path):
        if cfg.sound:
            try:
                _thread.start_new_thread(winsound.PlaySound, (path, winsound.SND_FILENAME))
            except:
                pass
                

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


    def onpress(self, _):
        x, y = _.x, _.y
        x, y = self.to(x, y, mode="re")

        if ((0 <= x <= 8) and (0 <= y <= 9)):
            p = cfg.pieces[y][x]
            if self.onpresspiece:
                if p != cfg.null and p.camp == self.onpresspiece.camp:
                    self.onpresspiece.state = False
                    self.onpresspiece = p
                    self.onpresspiece.state = True
                else:
                    if self.onpresspiece.move(x, y):
                        m, n = self.onpresspiece.place
                        if cfg.ani:
                            for i in range(cfg.aninum):
                                self.canvas.delete(cfg.pieces[n][m].drawoval)
                                self.canvas.delete(cfg.pieces[n][m].drawtext)

                                _x, _y = self.twopxy(x, y, m, n, (i + 1) / 10)
                                self.onpresspiece.place = [_x, _y]
                                self.drawpiece(self.onpresspiece)

                                time.sleep(cfg.anitime / cfg.aninum)
                                self.root.update()

                        cfg.pieces[y][x] = self.onpresspiece
                        cfg.pieces[n][m] = cfg.null
                        self.onpresspiece.place = [x, y]
                        self.onpresspiece.state = False
                        self.onpresspiece = False

                        cfg.steps += 1

                        self.playsound(cfg.move)

                        rsu = 0
                        bsu = 0
                        for i in cfg.pieces:
                            for p in i:
                                if p != cfg.null:
                                    if p.camp == "red":
                                        rsu += len(p.cango())
                                    else:
                                        bsu += len(p.cango())
                        if rsu == 0 or bsu == 0:
                            self.playsound(cfg.killover)
                        else:
                            if cfg.redking.killking()["red"] or cfg.blackking.killking()["black"]:
                                self.playsound(cfg.kill)

                    else:
                        self.onpresspiece.state = False
                        self.onpresspiece = False
            else:
                if p != cfg.null:
                    if (p.camp == "red" and cfg.steps % 2 == 0) or (p.camp == "black" and (cfg.steps - 1) % 2 == 0):
                        p.state = True
                        self.onpresspiece = p

        self.update()

                                
    def to(self, x, y, mode="to"):
        if mode == "to":
            m = cfg.fpx + x * cfg.length
            n = cfg.fpy + y * cfg.length
        else:
            m = round((x - cfg.fpx) / cfg.length)
            n = round((y - cfg.fpy) / cfg.length)

        result = (m, n) if cfg.displaymode == 'y' else (n, m)
            
        return result


    def drawcont(self):
        line = lambda x, y, m, n, fill=cfg.contcolor, width=cfg.contwide : self.canvas.create_line(x, y, m, n, fill=fill, width=width)
        for i in cfg.lines:
            x, y, m, n = i
            x, y, m, n = self.to(x, y) + self.to(m, n)
            line(x, y, m, n)


    def loadcodepi(self, codepi):
        sidecode = codepi[-1]
        cfg.redside = "down" if sidecode == '0' else "up"
        
        codepi = codepi[:-1]

        cfg.pieces = [[cfg.null] * 9 for i in range(10)]
        for i in range(0, int(len(codepi) / 4)):
            _ = codepi[i * 4 : i * 4 + 4]
            t, x, y, s = _
            x = int(x)
            y = int(y)
            p = cfg.pids[t](place=[x, y], camp="red" if s == '0' else "black")
            cfg.pieces[y][x] = p

            if t == '5':
                if s == '0':
                    cfg.redking = p
                if s == '1':
                    cfg.blackking = p
       
        steps = 0

    
    def drawpiece(self, p):
        k, j = p.place
        le = 0 if p.state else 0.1
        f = [cfg.piecefont[0], round(cfg.piecefont[1] * 1.2)] if p.state else cfg.piecefont
        x, y = self.to(k - (0.5 - le), j - (0.5 - le))
        m, n = self.to(k + (0.5 - le), j + (0.5 - le))
        p.drawoval = self.canvas.create_oval(x, y, m, n, fill=cfg.piececolor)
        x, y = self.to(k, j)
        p.drawtext = self.canvas.create_text(x, y, text=p.label, font=f, fill=p.camp)
        

    def drawpieces(self):
        for i in cfg.pieces:
            for l in i:
                if l != cfg.null:
                    self.drawpiece(l)
                    

    def ovaldraw(self, place):
        x, y = place
        le = 0.2
        m, n = self.to(x - le, y - le)
        k, j = self.to(x + le, y + le)
        self.canvas.create_oval(m, n, k, j, fill=cfg.piececolor)

                
    def update(self):
        self.canvas.delete(tkinter.ALL)

        self.drawcont()
        self.drawpieces()

        if cfg.tips:
            if self.onpresspiece:
                _ = self.onpresspiece.cango()
                for i in _:
                    self.ovaldraw(i)

        
def main():
    global cfg
    
    cfg = config()
    cfg.make()

    _ = gui()
    _.root.mainloop()


if __name__ == "__main__":
    main()
