import sys
from math import*
import time
from tkinter import *
from tkinter import messagebox
import os
from sys import argv
from pyopengltk import OpenGLFrame

try:
    from OpenGL.GL import*
    from OpenGL.GLU import*
    from OpenGL.GLUT import*

except:
    print("Error: PyOpengl was not installed correctly")
    sys.exit()

### Line ###
class DDALine():
    def __init__(self, x1, y1, x2, y2):
        self.width = 800
        self.height = 600
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        
    def drawDDA(self, x1, y1, x2, y2):
        '''dx=0.0
        dy=0.0
        steps=0.0
        xInc=0.0
        yInc=0.0
        x=0.0
        y=0.0'''
        
        dx = x1 - x2
        dy = y1 - y2
        
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
            
        #first point
        xInc = dx/steps
        yInc = dy/steps
        
        x = self.x1
        y = self.y1
        
        glPointSize(3.0)
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2d(x, y)
        
        for i in range(1, steps+1):
            x -= xInc
            y -= yInc
            glVertex2d(round(x), round(y))
        
        glEnd()
        glFlush()
        
    def Axis(self):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(0, -500)
        glVertex2f(0, 500)
        glEnd()
        
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(-500, 0)
        glVertex2f(500, 0)
        glEnd()
    
    
    def Display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.Axis()
        
        glColor3f(1.0, 1.0, 0.0)
        self.drawDDA(self.x1, self.y1, self.x2, self.y2)
        glutSwapBuffers()
        
    def MyInit(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def keyPressed(self, *args):
        if args[0]==b'q':
            print("\nRestarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        if args[0]==b'Q':
            print("\nExit confirmed")
            os._exit(1)
        
    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100,100)
        glutCreateWindow(b'DDA Line Drawing')
        self.MyInit()
        gluOrtho2D(-500.0,500.0,-500.0,500.0)
        glutDisplayFunc(self.Display)
        glutIdleFunc(self.Display)
        glutKeyboardFunc(self.keyPressed)
        glutMainLoop()

class BresenhamLine():
    def __init__(self, x1, y1, x2, y2):
        self.width = 800
        self.height = 600
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        
    def drawBresenham(self, x1, y1, x2, y2):  
        if (self.x2-self.x1) == 0:
            self.M = (self.y2-self.y1)
        else:
            self.M = (self.y2-self.y1)/(self.x2-self.x1)
        
        if abs(self.M)<1:
            if self.x1>self.x2:
                self.t=self.x1
                self.x1=self.x2
                self.x2=self.t
                
                self.t=self.y1
                self.y1=self.y2
                self.y2=self.t
            
            self.dx=abs(self.x2-self.x1)
            self.dy=abs(self.y2-self.y1)
            
            self.p = 2*self.dy-self.dx
            
            self.x=self.x1
            self.y=self.y1
            
            glPointSize(3.0)
            glBegin(GL_POINTS)
            while self.x<=self.x2:
                glVertex2f(self.x,self.y)
                self.x=self.x+1
                    
                if self.p>=0:
                    if self.M<1:
                        self.y=self.y+1
                    else:
                        self.y=self.y-1
                    self.p=self.p+2*self.dy-2*self.dx
                else:
                    self.y=self.y
                    self.p=self.p+2*self.dy
            glEnd()

        if abs(self.M)>=1:
            if self.y1>self.y2:
                self.t=self.x1
                self.x1=self.x2
                self.x2=self.t
                
                self.t=self.y1
                self.y1=self.y2
                self.y2=self.t
            
            self.dx=abs(self.x2-self.x1)
            self.dy=abs(self.y2-self.y1)
            
            self.p = 2*self.dx-self.dy
            
            self.x=self.x1
            self.y=self.y1
            
            glPointSize(3.0)
            glBegin(GL_POINTS)
            while self.y<=self.y2:
                glVertex2f(self.x,self.y)
                self.y=self.y+1
                    
                if self.p>=0:
                    if self.M>=1:
                        self.x=self.x+1
                    else:
                        self.x=self.x-1
                    self.p=self.p+2*self.dx-2*self.dy
                else:
                    self.x=self.x
                    self.p=self.p+2*self.dx
            glEnd()
        
        glFlush()
    
    def Axis(self):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(0, -500)
        glVertex2f(0, 500)
        glEnd()
        
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(-500, 0)
        glVertex2f(500, 0)
        glEnd()
    
    
    def Display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.Axis()
        
        glColor3f(1.0, 1.0, 0.0)
        self.drawBresenham(self.x1, self.y1, self.x2, self.y2)
        glutSwapBuffers()
        
    def MyInit(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def keyPressed(self, *args):
        if args[0]==b'q':
            print("\nRestarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        if args[0]==b'Q':
            print("\nExit confirmed")
            os._exit(1)
        
    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100,100)
        glutCreateWindow(b'Bresenham Line Drawing')
        self.MyInit()
        gluOrtho2D(-500,500,-500,500)
        glutDisplayFunc(self.Display)
        glutIdleFunc(self.Display)
        glutKeyboardFunc(self.keyPressed)
        glutMainLoop()
        
class LinedrawWindow():
    def __init__(self,window):
        self.window=window
        self.win = Toplevel(window,bg="#c0f0f0")
    
    def detail(self):
        win=self.win
        win.title("Line Drawing")
        win.geometry("520x630")
        win.resizable(False, False)
    
    def option(self,option): 
        if option == 1:
            try:
                num1 = int(self.valx1.get())
                num2 = int(self.valy1.get())
                num3 = int(self.valx2.get())
                num4 = int(self.valy2.get())
                self.win.withdraw()
                DDALine(num1,num2,num3,num4).main()
                
            except ValueError:
                self.lblerror.config(text="Please enter integer number only.")
        
        
        if option == 2:
            try:
                num1 = int(self.valx1.get())
                num2 = int(self.valy1.get())
                num3 = int(self.valx2.get())
                num4 = int(self.valy2.get())
                self.win.withdraw()
                BresenhamLine(num1,num2,num3,num4).main()
            
            except ValueError:
                self.lblerror.config(text="Please enter integer number only.")
    
    def show(self):
        win=self.win
        self.detail()
        self.window.withdraw()
        #Create option buttons
        lbl1 = Label(win, text="Enter Coordinate Values Below:", font=('Verdana',12,'bold'),bg="#5cb4f2",bd=5,relief=RIDGE,padx=10,pady=10)
        lbl1.place(x=70, y=90) 
        
        labelx1 = Label(win, text="x1 =", font=('Verdana',12,'bold'), bg="#c0f0f0").place(x=60, y=170)
        self.valx1 = Entry(win, width=8,bg="white",fg="black",font=('Arial',12),bd=5,justify=CENTER)
        self.valx1.place(x=130, y=170)
        
        labely1 = Label(win, text="y1 =", font=('Verdana',12,'bold'), bg="#c0f0f0").place(x=60, y=220)
        self.valy1 = Entry(win, width=8,bg="white",fg="black",font=('Arial',12),bd=5,justify=CENTER)
        self.valy1.place(x=130, y=220)
        
        labelx2 = Label(win, text="x2 =", font=('Verdana',12,'bold'), bg="#c0f0f0").place(x=280, y=170)
        self.valx2 = Entry(win, width=8,bg="white",fg="black",font=('Arial',12),bd=5,justify=CENTER)
        self.valx2.place(x=350, y=170)
        
        labely2 = Label(win, text="y2 =", font=('Verdana',12,'bold'), bg="#c0f0f0").place(x=280, y=220)
        self.valy2 = Entry(win, width=8,bg="white",fg="black",font=('Arial',12),bd=5,justify=CENTER)
        self.valy2.place(x=350, y=220)
        
        btnInfo = Button(win, text="Important Info: Please Click!", font=('bold'),bg='light blue', bd=5,fg='red', command=self.Informations)
        btnInfo.place(x=120, y=30)
        
        lbl2 = Label(win, text="Choose Your Line Drawing Method", font=('Verdana',12,'bold'),bg="#5cb4f2",bd=5,relief=RIDGE,padx=10,pady=10)
        lbl2.place(x=50, y=300)
        
        btn1 = Button(win, text="DDA (Digital Differential Analyzer)",font=('bold'),bg='light blue',bd=5,command=lambda:(self.option(1)))
        btn1.place(x=100, y=370) 
        btn2 = Button(win, text="Bresenham", font=('bold'),bg='light blue',bd=5,command=lambda:(self.option(2)))
        btn2.place(x=200, y=430)
        btn3 = Button(win, text="Back", font=('bold'),bg='light blue',bd=5, command=lambda:(self.window.deiconify(),win.destroy()))
        btn3.place(x=435, y=570)
        btn4 = Button(win, text="Clear", font=('bold'),bg='white',bd=5,fg="red", command=lambda:self.clearAll())
        btn4.place(x=20, y=570)
        
        self.lblerror = Label(win, text="", bg="#c0f0f0",pady=5,font=('Oswald',11,'bold'),fg='red')
        self.lblerror.place(x=120, y=500)
        
    def Informations(self):
        messagebox.showinfo("Informations",
                            "Notes: Range for coordinates value is "
                            "between -500 to 500 only. Use integer number "
                            "only (no decimal number).\n"
                            "Press 'q' to return from the Line Drawing Method.")
        
    def clearAll(self):
        self.valx1.delete(0, END)
        self.valy1.delete(0, END)
        self.valx2.delete(0, END)
        self.valy2.delete(0, END)

### End of line ###

### Cicle ###
class Circle:
    def __init__(self,xC,yC,Radius):
        self.xC=xC
        self.yC=yC
        self.R=Radius
        
    def setPixel(self, xcoordinate,ycoordinate):
        
        glBegin(GL_POINTS)
        glVertex2i(xcoordinate,ycoordinate)
        glEnd()
        glFlush()

    def drawCircle(self, xc,yc,x,y):
        self.setPixel(xc+x,yc+y)
        self.setPixel(xc-x,yc+y)
        self.setPixel(xc+x,yc-y)
        self.setPixel(xc-x,yc-y)
        self.setPixel(xc+y,yc+x)
        self.setPixel(xc-y,yc+x)
        self.setPixel(xc+y,yc-x)
        self.setPixel(xc-y,yc-x)

    def circle(self):
        xC=self.xC
        yC=self.yC
        
        x=0
        y=self.R
        
        p0=5/4-self.R
        
        self.drawCircle(xC,yC,x,y)
        while x<=y:
            x=x+1
            if p0<0:
                p0=p0+2*(x+1)+1
            else:
                y=y-1
                p0=p0+2*(x+1)+1-2*(y-1)
                
            self.drawCircle(xC,yC,x,y)
            
class circleWidget():
    def __init__(self, Radius):
        self.width=600
        self.height=600
        self.Radius=Radius
        
    def initScene(self):

        glClearColor(1.0,1.0,1.0,1.0)
        glColor3f(0.0,0.0,0.0)
        glPointSize(1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
   
    def Display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        Circle(300,300, self.Radius).circle()
            

    def setPixelColor(self,x,y,color):
        glColor3f(0,0,0)
        glBegin(GL_POINTS)
        glVertex2i(x,y)
        glEnd()
        glFlush()

    
    def keyPressed(self, *args):
        
        if args[0]==b'q':
            print("\nRestarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        if args[0]==b'Q':
            print("\nExit confirmed")
            os._exit(1)
            

    def sceneLoop(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(600,600)
        glutInitWindowPosition(50,50)
        glutCreateWindow("Circle")
        glutDisplayFunc(self.Display)
        self.initScene()
        glutKeyboardFunc(self.keyPressed)
        glutMainLoop()
            
class widgetCircle():
    def __init__(self, window):
        self.window=window
        self.window1 = Toplevel(window)
        
    def detail(self):
        window1=self.window1
        window1.title("Circle primitives")
        window1.geometry("500x400+50+50")
        window1.resizable(False, False)
        window1.configure(bg="darkslategray")
        
    def option(self):
        self.window1.withdraw()
        messagebox.showinfo("Important message before execute",
                            "Press 'q' to restart after see\n"+
                            "Press 'Q' to quit")
        print("\nPress 'q' to restart after see\nPress 'Q' to quit")

        circleWidget(self.radius.get()).sceneLoop()
        
    
    def info(self):
        messagebox.showinfo("Information",
                            "Slide to determine the radius for circle\n")
    
    def show(self):
        #for frame
        window1=self.window1
        self.window.withdraw()
        self.detail()
        frame=LabelFrame(window1,text="Welcome to Primitives",bg='darkslategray',fg='cyan', padx=30,pady=30)
        frame.grid(row=0, column=0, columnspan=3)
        
        myLabel=Label(frame,text="Please choose radius for circle",bg='darkslategray',fg='white',font=('bold')).pack(padx=2,pady=2)
        self.radius=Scale(frame, from_=10, to=250, orient=HORIZONTAL)
        self.radius.pack()
        #Create option buttons
        
        Button(window1, text="Circle", font=('bold'),bd=5,command=lambda:(self.option())).grid(row=2, column=0) 
        
        Button(window1, text="Info", command=self.info).grid(row=3, column=1,pady=20) 
        Button(window1, text="Back", command=lambda:(self.window.deiconify(),window1.destroy())).grid(row=3, column=2,pady=20)

### End of circle ###

### Area Filling ###
class Triangle1:
    def __init__(self,xC,yC,size, Round):
        self.xC=xC
        self.yC=yC
        self.size=size
        self.Round=Round
        
    def setPixel(self,xcoordinate,ycoordinate):
        glBegin(GL_POINTS)
        glVertex2i(round(xcoordinate,self.Round),round(ycoordinate,self.Round))
        glEnd()
        glFlush()

    def lineDDA(self,x1,y1,x2,y2):
        
        x1=int(x1)
        y1=int(y1)
        x2=int(x2)
        y2=int(y2)
        delta_x = x2 - x1
        delta_y = y2 - y1
        dx=abs(x1-x2)
        dy=abs(y1-y2)
        
        x,y=x1,y1
        
        if dx>dy:
            steps=dx
        else: steps= dy
        
        if steps !=0:
            xInc=dx/float(steps)
            yInc=dy/float(steps)
        else:
            xInc=0
            yInc=0
        self.setPixel(round(x),round(y))

        for k in range(steps):
            if delta_x >= 0:
                x+=xInc
            else:
                x-=xInc
            if delta_y >= 0:
                y+=yInc
            else:
                y-=yInc
            self.setPixel(round(x),round(y))
        
    
    def drawTriangle(self):
        xC=self.xC
        yC=self.yC
        s=self.size
        
        self.lineDDA(xC-25*s, yC-25*s,xC,yC+25*s)
        self.lineDDA(xC, yC+25*s,xC+25*s,yC-25*s)
        self.lineDDA(xC+25*s, yC-25*s,xC-25*s,yC-25*s)
        glFlush()

class Circle1:
    def __init__(self,xC,yC,Radius, Round):
        self.xC=xC
        self.yC=yC
        self.R=Radius
        self.Round=Round
        
    def setPixel(self, xcoordinate,ycoordinate):
        
        glBegin(GL_POINTS)
        glVertex2i(round(xcoordinate,self.Round),round(ycoordinate,self.Round))
        glEnd()
        glFlush()

    def drawCircle(self, xc,yc,x,y):
        self.setPixel(xc+x,yc+y)
        self.setPixel(xc-x,yc+y)
        self.setPixel(xc+x,yc-y)
        self.setPixel(xc-x,yc-y)
        self.setPixel(xc+y,yc+x)
        self.setPixel(xc-y,yc+x)
        self.setPixel(xc+y,yc-x)
        self.setPixel(xc-y,yc-x)

    def circle(self):
        xC=self.xC
        yC=self.yC
        
        x=0
        y=self.R
        
        p0=5/4-self.R
        
        self.drawCircle(xC,yC,x,y)
        while x<=y:
            x=x+1
            if p0<0:
                p0=p0+2*(x+1)+1
            else:
                y=y-1
                p0=p0+2*(x+1)+1-2*(y-1)
                
            self.drawCircle(xC,yC,x,y)
    
    
class floodFill():
    def __init__(self, bigS, CriTri, Radius):
        self.width=600
        self.height=600
        self.bigS=bigS #big and small 0 if small,1 if big
        self.CriTri=CriTri #circle or triangle, 0 if circle; 1 if triangle
        self.Radius=Radius
        
        if CriTri==0:
            if Radius<=26:
                self.pos=1 #position
                self.size=1 #size of pixel
                self.Round=0 #rounding
            if Radius>26:
                self.pos=10
                self.size=10
                self.Round=-1
                
        if CriTri==1:
            if bigS==0: 
                self.pos=1 #position
                self.size=1 #size of pixel
                self.Round=0 #rounding
            if bigS==1: 
                self.pos=10
                self.size=10
                self.Round=-1
        
    def initScene(self):

        glClearColor(1.0,1.0,1.0,1.0)
        glColor3f(0.0,0.0,0.0)
        glPointSize(self.size)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
   
    def Display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.CriTri==0:
            Circle1(300,300, self.Radius, self.Round).circle()
            #Circle1(300,300, self.Radius+self.pos, self.Round).circle() #for 8 connected
        if self.CriTri==1:
            Triangle1(300,300,self.size,self.Round).drawTriangle()
            #Triangle1(300,300,self.size*26/25,self.Round).drawTriangle() #for 8 connected
        

    def floodFill(self,x,y,old_color,new_color):
        color=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
        try:
            if((color[0][0][0]==old_color[0][0][0]) and (color[0][0][1]==old_color[0][0][1]) and (color[0][0][2]==old_color[0][0][2])):
                self.setPixelColor(x,y,new_color)
                self.floodFill(x + self.pos, y, old_color, new_color)
                self.floodFill(x, y + self.pos, old_color, new_color)
                self.floodFill(x - self.pos, y, old_color, new_color)
                self.floodFill(x, y - self.pos,old_color, new_color)
                #for 8 connected
                '''
                self.floodFill(x + self.pos, y+ self.pos, old_color, new_color)
                self.floodFill(x-self.pos, y + self.pos, old_color, new_color)
                self.floodFill(x - self.pos, y+ self.pos, old_color, new_color)
                self.floodFill(x+ self.pos, y - self.pos,old_color, new_color)
                '''
        except:
            print("\nAvoid mouse click at the big surface, recursive already reach maximun")
            print("\nrestarting")
            os.execl(sys.executable, sys.executable, *sys.argv)
            

    def setPixelColor(self,x,y,color):
        glColor3f(color[0][0][0],color[0][0][1],color[0][0][2])
        glBegin(GL_POINTS)
        glVertex2i(int(round(x,self.Round)),int(round(y,self.Round)))
        glEnd()
        glFlush()

    def onMouseClick(self,button,state,x,y):
        new_color=[[[1.0,0.0,0.0]]]
        old_color=[[[1.0,1.0,1.0]]]
        x=round(x,self.Round)
        y=round(y,self.Round)
        self.floodFill(x,600-y,old_color,new_color)
    
    def keyPressed(self, *args):
        
        if args[0]==b'q':
            print("\nRestarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        if args[0]==b'Q':
            print("\nExit confirmed")
            os._exit(1)

    def sceneLoop(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(600,600)
        glutInitWindowPosition(50,50)
        glutCreateWindow("Floodfill")
        glutDisplayFunc(self.Display)
        new_color=[[[1.0,0.0,0.0]]]
        old_color=[[[1.0,1.0,1.0]]]
        self.initScene()
        sys.setrecursionlimit(2**16-1)
        glutMouseFunc(self.onMouseClick)
        glutKeyboardFunc(self.keyPressed)
        glutMainLoop()
        
class windowFloodfill():

    def __init__(self, window):
        self.window=window
        self.window1 = Toplevel(window)
        
    def detail(self):
        window1=self.window1
        window1.title("opengl primitives")
        window1.geometry("500x400+50+50")
        window1.resizable(False, False)
        window1.configure(bg="darkslategray")
        
    def option(self, option):
        self.window1.withdraw()
        messagebox.showinfo("Important message before execute",
                            "Mouseclick on the shape to proceed area filling,\nPress 'q' to return and"+
                            "\nwill restart the program if the error detected")
        print("\nMouseclick on the shape to proceed area filling,\nPress 'q' to return and"+
              "\nwill restart the program if the error detected")
        if option==1:
            floodFill(0,0,self.radius.get()).sceneLoop()
        if option==2:
            floodFill(1,1,0).sceneLoop() #(big or small, circle or triangle, radius)
        if option==3:
            floodFill(0,1,0).sceneLoop()
    
    def info(self):
        messagebox.showinfo("Information",
                            "Slide to determine the radius for circle\n"+
                            "then choose the shape user want\n"+
                            "Area filling is to fill up the color in a shape")
    
    def show(self):
        #for frame
        window1=self.window1
        self.window.withdraw()
        self.detail()
        frame=LabelFrame(window1,text="Welcome to Primitives",bg='darkslategray',fg='cyan', padx=30,pady=30)
        frame.grid(row=0, column=0, columnspan=3)
        
        myLabel=Label(frame,text="Please choose radius for circle, ignore if triangle.",bg='darkslategray',fg='white',font=('bold')).pack(padx=2,pady=2)
        self.radius=Scale(frame, from_=10, to=250, orient=HORIZONTAL)
        self.radius.pack()
        #Create option buttons
        
        Label(window1, text="Choose the shape by clicking it", font=('bold')).grid(row=1, column=0, columnspan=3,pady=30) 
        Button(window1, text="Circle", font=('bold'),bd=5,command=lambda:(self.option(1))).grid(row=2, column=0) 
        Button(window1, text="Big triangle", font=('bold'),bd=5,command=lambda:(self.option(2))).grid(row=2, column=1)
        Button(window1, text="Small triangle", font=('bold'),bd=5,command=lambda:(self.option(3))).grid(row=2, column=2)
        
        Button(window1, text="Info", command=self.info).grid(row=3, column=1,pady=20) 
        Button(window1, text="Back", command=lambda:(self.window.deiconify(),window1.destroy())).grid(row=3, column=2,pady=20)

### end of area filling ###
        
class lineClipping:
    def __init__ (self, width=800, height=600):
        glutInit((argv), argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(400, 200)
        glutCreateWindow(title='Line Clipping')
        glutDisplayFunc(self.draw)
        glutReshapeFunc(self.reshape)
        glutMouseFunc(self.mouse_click)
        glutMotionFunc(self.mouse_move)
        glutKeyboardFunc(self.keyPressed)
        glClearColor(1, 1, 1, 1)
        
        #line starting and ending parameters
        self.t1, self.t2 = None, None
        #line start end coordinate
        self.x_start, self.y_start = None, None
        self.y_start, self.y_end = None, None
        self.can_draw = False
        self.rect = (150, 100, 600, 500) #clipping window, lb x, y, rt x, y
        
    def mouse_click(self, button, state, x, y):
        if button != GLUT_LEFT_BUTTON:
            #only respond of LMB
            return
        if state == GLUT_DOWN:
            #when LMB down, set line start coordinate (top left = origin)
            self.x_start = x
            self.y_start =y
            self.x_end, self.y_end = x, y
            
        elif state == GLUT_UP:
            #LMB up = end drawing
            self.clip()
            glutPostRedisplay()
            
    def mouse_move(self, x, y):
        self.x_end = x
        self.y_end = y
        #line draw when mouse move)
        self.can_draw = True
        glutPostRedisplay()
        
    def keyPressed(self,*args): #exit function
        if args[0]==b'q':
            print("\nRestarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        if args[0]==b'Q':
            print("\nExit confirmed")
            os._exit(1)

    def reshape(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, w, h, 0)
        glMatrixMode(GL_MODELVIEW)
        
    def calc_t(self, LB, RB): # LB = left border, RB = right border
        #True=clipped, False=throw
        flag = True
        if LB == 0:
            if RB < 0:
                flag = False
                
        else:
            #cacl line and clipping border paramtr
            tk = RB / LB
            if LB < 0: #when this, calc line with initial border intersec para
                if tk > self.t2:
                    flag = False
                elif tk > self.t1:
                    self.t1 = tk
                    
            else: #when LB>0 calc line with end border intersec para
                if tk < self.t1:
                    flag = False
                elif tk < self.t2:
                    self.t2 = tk
                    
        return flag
    
    def clip(self):
        self.can_draw = False
        self.t1, self.t2 = 0, 1
        dx = self.x_end - self.x_start#dx = difference ofx
        #window left end and right end
        if (self.calc_t(-dx, self.x_start-self.rect[0])) and (self.calc_t(dx, self.rect[2]-self.x_start)):
            dy = self.y_end - self.y_start
            #window top and bot end
            if (self.calc_t(-dy, self.y_start-self.rect[1]) and self.calc_t(dy, self.rect[3]-self.y_start)):
                if self.t2 < 1:
                    self.x_end = self.x_start + self.t2*dx #x= x1 + t*dx
                    self.y_end = self.y_start + self.t2*dy #y= y1 + t*dy
                if self.t1 > 0:
                    self.x_start = self.x_start + self.t1*dx
                    self.y_start = self.y_start + self.t1*dy

                # clipped
                self.can_draw = True
        
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(255, 0, 0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        #set clipping window rectangle
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(3) #rect width
        glRectf(*self.rect)
        
        glLineWidth(3)
        if self.can_draw:
            glColor3f(0, 0, 0)
            glBegin(GL_LINES)
            glVertex2f(self.x_start, self.y_start)
            glVertex2f(self.x_end, self.y_end)
            glEnd()
            
        glutSwapBuffers()
        
    def mainloop(self):
        glutMainLoop()     
    
### end of clipping of line ###
        
### clipping of traingle ###

class TriangleClipping(OpenGLFrame):
    
    def initgl(self):
        glutInit(sys.argv)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glColor3f(0.0,0.0,0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
        
        
        
    def Clipbox(self):
        glColor3f(0.0, 0.0, 0.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(2)
        glBegin(GL_QUADS)
        glVertex3f(150, 400, 0.0)
        glVertex3f(450, 400, 0.0)
        glVertex3f(450, 120, 0.0)
        glVertex3f(150, 120, 0.0)
        glEnd()
        
        
    def drawTriangle(self):
        glColor3f(255, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glBegin(GL_TRIANGLES)
        x1 = windowT(0).getX1()
        x2 = windowT(0).getX2()
        x3 = windowT(0).getX3()
        y1 = windowT(0).getY1()
        y2 = windowT(0).getY2()
        y3 = windowT(0).getY3()
        
        glVertex3f(x1, y1, 0.0)
        glVertex3f(x2, y2, 0.0)
        glVertex3f(x3, y3, 0.0)
        glEnd()
        
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glColor3f(0,255,255)
        glVertex3f(x1, y1, 0.0)
        glColor3f(0,255,0)
        glVertex3f(x2, y2, 0.0)
        glColor3f(0,0,255)
        glVertex3f(x3, y3, 0.0)
        glEnd()
      
    def reshape(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, w, h, 0)
        glMatrixMode(GL_MODELVIEW)
        
    def clip(self):
        ix1=x1.get()
        ix2=x2.get()
        ix3=x3.get()
        iy1=y1.get()
        iy2=y2.get()
        iy3=y3.get()
        cx1,cx2,cx3,cy1,cy2,cy3 = ix1,ix2,ix3,iy1,iy2,iy3
         
            
        glColor3f(255,0,0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_TRIANGLES)
        glVertex3f(cx1, cy1, 0.0)
        glVertex3f(cx2, cy2, 0.0)
        glVertex3f(cx3, cy3, 0.0)
        glEnd()
        
    def cover(self):
            
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(0, 400, 0.0)
        glVertex3f(600, 400, 0.0)
        glVertex3f(600, 600, 0.0)
        glVertex3f(0, 600, 0.0)
        glEnd()
        
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(0, 0, 0.0)
        glVertex3f(0, 600, 0.0)
        glVertex3f(150, 600, 0.0)
        glVertex3f(150, 0, 0.0)
        glEnd()
        
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(450, 0, 0.0)
        glVertex3f(450, 600, 0.0)
        glVertex3f(600, 600, 0.0)
        glVertex3f(600, 0, 0.0)
        glEnd()
        
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(0, 120, 0.0)
        glVertex3f(600, 120, 0.0)
        glVertex3f(600, 0, 0.0)
        glVertex3f(0, 0, 0.0)
        glEnd()
        
        
    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glColor3f(255, 0, 0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.clip()
        self.cover()
        self.drawTriangle()
        self.Clipbox()
        
        
        

class windowT:
    def __init__(self, window):
        self.window=window
        
    def option(self):
        window=self.window
            
        x1.set(300)
        y1.set(250)
        x2.set(220)
        y2.set(150)
        x3.set(400)
        y3.set(150)
        
        app1 = TriangleClipping(window, width=600, height=600)
        app1.grid(row=0,column=0,rowspan=3)
        app1.animate = 1
        app1.after(100, app1.printContext)
        app1.mainloop()
        
        
    def getX1(self):
        a = int(x1.get())
        return a
    
    def getX2(self):
        b = int(x2.get())
        return b
    
    def getX3(self):
        c = int(x3.get())
        return c
    
    def getY1(self):
        d = int(y1.get())
        return d
    
    def getY2(self):
        e = int(y2.get())
        return e
    
    def getY3(self):
        f = int(y3.get())
        return f
    
    def back(self):
        print("\nRestarting...")
        os.execl(sys.executable, sys.executable, *sys.argv)
        
        
        
    def show(self):
        global x1,x2,y1,y2,x3,y3,clip,varx1,varx2,varx3,vary1,vary2,vary3
        x1= DoubleVar()
        x2= DoubleVar()
        x3= DoubleVar()
        y1= DoubleVar()
        y2= DoubleVar()
        y3= DoubleVar()
        
        #for frame
        window = self.window
        window.resizable(0,0)
        window.title("TriangleClipping")

        frame=LabelFrame(window,bg='darkslategray',fg='cyan')
        frame.grid(row=1, column=1)
            

        
        #Create option buttons
            
        Label(frame, text="Press", font=('bold'),bg='darkslategray',fg='white').grid(column=0, row=0)
        Button(frame, text="Reset", font=('bold'),bd=5,command=self.option).grid(column=1, row=0)
        Label(frame, text="x1", font=('bold'),bg='darkslategray',fg='white').grid(row=1, column=0)
        Label(frame, text="y1", font=('bold'),bg='darkslategray',fg='white').grid(row=2, column=0)
        Label(frame, text="x2", font=('bold'),bg='darkslategray',fg='white').grid(row=3, column=0)
        Label(frame, text="y2", font=('bold'),bg='darkslategray',fg='white').grid(row=4, column=0)
        Label(frame, text="x3", font=('bold'),bg='darkslategray',fg='white').grid(row=5, column=0)
        Label(frame, text="y3", font=('bold'),bg='darkslategray',fg='white').grid(row=6, column=0)
        x1=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,   highlightbackground='light blue')
        x1.grid(row=1, column=1)
        y1=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,   highlightbackground='light blue')
        y1.grid(row=2, column=1)
        x2=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='green')
        x2.grid(row=3, column=1)
        y2=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='green')
        y2.grid(row=4, column=1)
        x3=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='blue')
        x3.grid(row=5, column=1)
        y3=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='blue')
        y3.grid(row=6, column=1)
        
        Button(window, text="Back", font=('bold'),bd=5,command=self.back).grid( row=2, column=1)
        
        
class AppOgl(OpenGLFrame):

    def initgl(self):
        
        """Initalize gl states when the frame is created"""
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glColor3f(0.0,0.0,0.0)
        glPointSize(10.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
        
    def redraw(self):
        """Render a single frame"""
        glClear(GL_COLOR_BUFFER_BIT)     

        
        
class windowTriangleClipping():
    def __init__(self,window):
        self.window=window
        
    def main(self):
        window=self.window
        window = Toplevel()
        app = AppOgl(window, width=600, height=600)
        app.grid(row=0,column=0,rowspan=3)
        windowT(window).show()
        app.animate = 1
        app.after(100, app.printContext)
        app.mainloop()
        
### end of clipping of triangle ###
        
        
### Another design ###
        
class windowLine():
    def __init__(self, window):
        self.window=window


        
        
    def option(self):
        window=self.window
        
        x1.set(0)
        y1.set(0)
        x2.set(600)
        y2.set(600)

            
        app1 = AppLine(window, width=600, height=600)
        app1.grid(row=0,column=0,rowspan=3)
        app1.animate = 1
        app1.after(100, app1.printContext)
        app1.mainloop()
        
        return app1
        
        
    def getX1(self):
        a= int(x1.get())
        return a
    
    def getX2(self):
        b= int(x2.get())
        return b
    
    def getY1(self):
        c= int(y1.get())
        return c
    
    def getY2(self):
        d= int(y2.get())
        return d
    
    def getSize(self):
        s= int(size.get())
        return s
    
    def show(self):
        global x1,x2,y1,y2,size
        #for frame
        window=self.window

        frame=LabelFrame(window,bg='darkslategray',fg='cyan')
        frame.grid(row=1, column=1)
        

    
        #Create option buttons
        
        Label(frame, text="Press", font=('bold'),bg='darkslategray',fg='white').grid(column=0, row=0)
        Button(frame, text="Line", font=('bold'),bd=5,command=self.option).grid(column=1, row=0)
        Label(frame, text="x1", font=('bold'),bg='darkslategray',fg='white').grid(row=1, column=0)
        Label(frame, text="y1", font=('bold'),bg='darkslategray',fg='white').grid(row=2, column=0)
        Label(frame, text="x2", font=('bold'),bg='darkslategray',fg='white').grid(row=3, column=0)
        Label(frame, text="y2", font=('bold'),bg='darkslategray',fg='white').grid(row=4, column=0)
        x1=Scale(frame, from_=0, to=600, orient=HORIZONTAL,  highlightbackground='green')
        x1.grid(row=1, column=1)
        y1=Scale(frame, from_=0, to=600, orient=HORIZONTAL,  highlightbackground='red')
        y1.grid(row=2, column=1)
        x2=Scale(frame, from_=0, to=600, orient=HORIZONTAL,  highlightbackground='blue')
        x2.grid(row=3, column=1)
        y2=Scale(frame, from_=0, to=600, orient=HORIZONTAL,  highlightbackground='pink')
        y2.grid(row=4, column=1)
        
        Label(frame, text="Size", font=('bold'),bg='darkslategray',fg='white').grid(row=5, column=0)
        size=Scale(frame, from_=1, to=20, orient=HORIZONTAL,  highlightbackground='white')
        size.grid(row=5, column=1)
        
        return frame
        

class windowCircle():
    def __init__(self, window):
        self.window=window


        
        
    def option(self):
        window=self.window
            
        app1 = AppCir(window, width=600, height=600)
        app1.grid(row=0,column=0,rowspan=3)
        app1.animate = 1
        app1.after(100, app1.printContext)
        app1.mainloop()
        
        
    def getRadius(self):
        r= int(radius.get())
        return r
    
    def getSize(self):
        s= int(size.get())
        return s
    
    def show(self):
        global radius, size
        #for frame
        window=self.window

        frame=LabelFrame(window,bg='darkslategray',fg='cyan')
        frame.grid(row=1, column=1)
        

    
        #Create option buttons
        
        Label(frame, text="Press", font=('bold'),bg='darkslategray',fg='white').pack(padx=55)
        Button(frame, text="Circle", font=('bold'),bd=5,command=self.option).pack()
        Label(frame, text="Radius", font=('bold'),bg='darkslategray',fg='white').pack()
        radius=Scale(frame, from_=50, to=250, orient=HORIZONTAL)
        radius.pack()
        Label(frame, text="Size", font=('bold'),bg='darkslategray',fg='white').pack(pady=28)
        size=Scale(frame, from_=1, to=20, orient=HORIZONTAL)
        size.pack()
        
        return frame
        
        
        

class windowTK:
    def __init__(self, window):
        self.window=window
        
    def option(self):
        window=self.window
            
        x1.set(300)
        y1.set(250)
        x2.set(220)
        y2.set(150)
        x3.set(400)
        y3.set(150)
        
        
        app1 = TriangleClipping(window, width=600, height=600)
        app1.grid(row=0,column=0,rowspan=3)
        app1.animate = 1
        app1.after(100, app1.printContext)
        app1.mainloop()
        
        
    def getX1(self):
        a = int(x1.get())
        return a
    
    def getX2(self):
        b = int(x2.get())
        return b
    
    def getX3(self):
        c = int(x3.get())
        return c
    
    def getY1(self):
        d = int(y1.get())
        return d
    
    def getY2(self):
        e = int(y2.get())
        return e
    
    def getY3(self):
        f = int(y3.get())
        return f
    

        
        
        
    def show(self):
        global x1,x2,y1,y2,x3,y3,clip,varx1,varx2,varx3,vary1,vary2,vary3
        x1= DoubleVar()
        x2= DoubleVar()
        x3= DoubleVar()
        y1= DoubleVar()
        y2= DoubleVar()
        y3= DoubleVar()
        
        #for frame
        window = self.window

        frame=LabelFrame(window,bg='darkslategray',fg='cyan')
        frame.grid(row=1, column=1)
            

        
        #Create option buttons
            
        Label(frame, text="Press", font=('bold'),bg='darkslategray',fg='white').grid(column=0, row=0)
        Button(frame, text="Reset", font=('bold'),bd=5,command=self.option).grid(column=1, row=0)
        Label(frame, text="x1", font=('bold'),bg='darkslategray',fg='white').grid(row=1, column=0)
        Label(frame, text="y1", font=('bold'),bg='darkslategray',fg='white').grid(row=2, column=0)
        Label(frame, text="x2", font=('bold'),bg='darkslategray',fg='white').grid(row=3, column=0)
        Label(frame, text="y2", font=('bold'),bg='darkslategray',fg='white').grid(row=4, column=0)
        Label(frame, text="x3", font=('bold'),bg='darkslategray',fg='white').grid(row=5, column=0)
        Label(frame, text="y3", font=('bold'),bg='darkslategray',fg='white').grid(row=6, column=0)
        x1=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,   highlightbackground='light blue')
        x1.grid(row=1, column=1)
        y1=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,   highlightbackground='light blue')
        y1.grid(row=2, column=1)
        x2=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='green')
        x2.grid(row=3, column=1)
        y2=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='green')
        y2.grid(row=4, column=1)
        x3=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='blue')
        x3.grid(row=5, column=1)
        y3=Scale(frame, from_=0, to=600, orient=HORIZONTAL, resolution=1,  highlightbackground='blue')
        y3.grid(row=6, column=1)
        
        return frame
        

    
class rightWindowTK(Frame):
    def __init__(self,window):
        self.window=window
    
    def detail(self):
        window=self.window
        window.geometry("800x600")
        window.title("opengl primitives")
        window.resizable(False, False)
        window.configure(bg="darkslategray")
    
    def option(self, option):
        window=self.window
        if option==1:
            try:
                self.w2.grid_remove()
                self.w3.grid_remove()
            except: pass
            self.w1=windowLine(window).show()
        if option==2:
            try:
                self.w1.grid_remove()
                self.w3.grid_remove()
            except: pass
            self.w2=windowCircle(window).show()
            
        if option==3:
            try:
                self.w1.grid_remove()
                self.w2.grid_remove()
            except: pass
            self.w3=windowTK(window).show()
            
    def restart(self):
        print("\nRestarting...")
        os.execl(sys.executable, sys.executable, *sys.argv)
            
    def menu(self):
        messagebox.showinfo("Menu",
                            "Assignment 2\n"+
                            "choose to find out how the process")
        
    
    def show(self):
        #for frame
        window=self.window
        Frame.__init__(self, window, width=800, height=600)
        self.detail()
        frame=LabelFrame(window,text="Welcome to Primitives",bg='darkslategray',fg='cyan',padx=30)
        frame.grid(row=0,column=1,padx=10)
        
        myLabel=Label(frame,text="Please choose.",bg='darkslategray',fg='white',font=('bold')).pack(pady=2)
        
        #Create option buttons
        button1=Button(frame,text="  Line drawing  ",fg="white",bg="black",bd=6,command=lambda:self.option(1)).pack(pady=3)
        Button(frame,text=" Circle drawing ",fg="black",bg="white",bd=6,command=lambda:self.option(2)).pack(pady=3)
        Button(frame,text="    Clipping    ",fg="white",bg="black",bd=6,command=lambda:self.option(3)).pack(pady=3)
        
        Button(frame,text="Restart",fg="white",bd=6,bg="red",command=self.restart).pack(pady=3)
  
        
        
class TriangleClipping(OpenGLFrame):
    
    def initgl(self):
        glutInit(sys.argv)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glColor3f(0.0,0.0,0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
        
        
        
    def Clipbox(self):
        glColor3f(0.0, 0.0, 0.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(2)
        glBegin(GL_QUADS)
        glVertex3f(150, 400, 0.0)
        glVertex3f(600, 400, 0.0)
        glVertex3f(450, 120, 0.0)
        glVertex3f(150, 120, 0.0)
        glEnd()
        
        
    def drawTriangle(self):
        glColor3f(255, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glBegin(GL_TRIANGLES)
        x1 = windowT(0).getX1()
        x2 = windowT(0).getX2()
        x3 = windowT(0).getX3()
        y1 = windowT(0).getY1()
        y2 = windowT(0).getY2()
        y3 = windowT(0).getY3()
        
        
        glVertex3f(x1, y1, 0.0)
        glVertex3f(x2, y2, 0.0)
        glVertex3f(x3, y3, 0.0)
        glEnd()
        
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glColor3f(0,255,255)
        glVertex3f(x1, y1, 0.0)
        glColor3f(0,255,0)
        glVertex3f(x2, y2, 0.0)
        glColor3f(0,0,255)
        glVertex3f(x3, y3, 0.0)
        glEnd()
      
    def reshape(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, w, h, 0)
        glMatrixMode(GL_MODELVIEW)
        
    def clip(self):
        ix1=x1.get()
        ix2=x2.get()
        ix3=x3.get()
        iy1=y1.get()
        iy2=y2.get()
        iy3=y3.get()
        cx1,cx2,cx3,cy1,cy2,cy3 = ix1,ix2,ix3,iy1,iy2,iy3
        
        
            
            
        glColor3f(255,255,0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_TRIANGLES)
        glVertex3f(cx1, cy1, 0.0)
        glVertex3f(cx2, cy2, 0.0)
        glVertex3f(cx3, cy3, 0.0)
        glEnd()
        
    def cover(self):
            
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(0, 400, 0.0)
        glVertex3f(600, 400, 0.0)
        glVertex3f(600, 600, 0.0)
        glVertex3f(0, 600, 0.0)
        glEnd()
        
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(0, 0, 0.0)
        glVertex3f(0, 600, 0.0)
        glVertex3f(150, 600, 0.0)
        glVertex3f(150, 0, 0.0)
        glEnd()
        
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(450, 0, 0.0)
        glVertex3f(450, 600, 0.0)
        glVertex3f(600, 600, 0.0)
        glVertex3f(600, 0, 0.0)
        glEnd()
        
        glColor3f(255,255,255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(0, 120, 0.0)
        glVertex3f(600, 120, 0.0)
        glVertex3f(600, 0, 0.0)
        glVertex3f(0, 0, 0.0)
        glEnd()
        
        
    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glColor3f(255, 0, 0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.clip()
        self.cover()
        self.drawTriangle()
        self.Clipbox()

        
class AppCir(OpenGLFrame):

    def initgl(self):
        
        """Initalize gl states when the frame is created"""
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glColor3f(0.0,0.0,0.0)
        #glPointSize(10.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
        
    def redraw(self):
        """Render a single frame"""
        glClear(GL_COLOR_BUFFER_BIT)
        r = windowCircle(0).getRadius()
        s = windowCircle(0).getSize()
        glPointSize(s)
        Circle1(300,300,r,0).circle()
        
class AppLine(OpenGLFrame):

    def initgl(self):
        
        """Initalize gl states when the frame is created"""
        glutInit(sys.argv)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glColor3f(0.0,0.0,0.0)
        glPointSize(10.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,600,0,600)
        
        
    def redraw(self):
        """Render a single frame"""
        glClear(GL_COLOR_BUFFER_BIT)
        #glTranslatef(0,2,0)
        x1 = windowLine(0).getX1()
        y1 = windowLine(0).getY1()
        x2 = windowLine(0).getX2()
        y2 = windowLine(0).getY2()
        s = windowLine(0).getSize()
        glPointSize(s)
        

        Triangle1(300,300,0,0).lineDDA(x1,y1,x2,y2)
        
class mainWindowTK():
    def __init__(self,window):
        self.window=window
        
    def main(self):
        window=self.window
        window = Toplevel()
        app = AppOgl(window, width=600, height=600)
        app.grid(row=0,column=0,rowspan=3)
        rightWindowTK(window).show()
        app.animate = 1
        app.after(100, app.printContext)
        app.mainloop()
        
### end of another design

class mainWindow:
    def __init__(self,window):
        self.window=window
    
    def detail(self):
        window=self.window
        window.title("opengl primitives")
        window.geometry("800x600+50+50")
        window.resizable(False, False)
        window.configure(bg="darkslategray")
    
    def option(self, option):
        window=self.window
        if option==1:
            LinedrawWindow(window).show()
        if option==2:
            widgetCircle(window).show()
        if option==3:
            windowFloodfill(window).show()
        if option==4:
            window.withdraw()
            messagebox.showinfo("Important info", 'use mouse to draw the line,\n'+
                                'line outside the rectangle will be clipped.\n'+
                                'press Q to exit and q to restart')
            print('\nuse mouse to draw the line,\n'+
                  'line outside the rectangle will be clipped.\n'+
                  'press Q to exit and q to restart')
            lineClipping().mainloop()
            
        if option==5:
            window.withdraw()
            windowTriangleClipping(window).main()
            
    def another(self):
        self.window.withdraw()
        mainWindowTK(self.window).main()
            
    def menu(self):
        messagebox.showinfo("Menu",
                            "Assignment 2\n"+
                            "Line- to draw line using DDA and Bresenham\n"+
                            "Circle- to draw circle using midpoint\n"+
                            "Area filling- to fill color on a shape\n"+
                            "Clipping- clipping of a line and triangle on a shape")
        
    
    def show(self):
        #for frame
        window=self.window
        self.detail()
        frame=LabelFrame(window,text="Welcome to Primitives",bg='darkslategray',fg='cyan', padx=60,pady=30)
        frame.pack(padx=2,pady=2)
        
        myLabel=Label(frame,text="Please choose your plan.",bg='darkslategray',fg='white',font=('bold')).pack(padx=2,pady=2)
        
        #Create option buttons
        Button(frame,text="  Line drawing  ",fg="white",bg="black",bd=6, command=lambda:self.option(1)).pack(padx=5,pady=3)
        Button(frame,text=" Circle drawing ",fg="black",bg="white",bd=6, command=lambda:self.option(2)).pack(padx=5,pady=3)
        Button(frame,text="  Area Filling  ",fg="white",bg="black",bd=6, command=lambda:self.option(3)).pack(padx=5,pady=3)
        Button(frame,text="Clipping of line",fg="black",bg="white",bd=6, command=lambda:self.option(4)).pack(padx=5,pady=3)
        Button(frame,text="Clipping of triangle",fg="black",bg="white",bd=6, command=lambda:self.option(5)).pack(padx=5,pady=3)
        
        Button(window, text="Menu", command=self.menu).pack(pady=10)
        Button(window, text="Another Design", command=self.another).pack(pady=10)
        


def main():
    window= Tk()
    mainWindow(window).show()
    window.mainloop()
    
    
if __name__=="__main__":
    main()