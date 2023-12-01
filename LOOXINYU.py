import sys
import math

try:
    from OpenGL.GL import*
    from OpenGL.GLU import*
    from OpenGL.GLUT import*

except:
    print("Error: PyOpengl was not installed correctly")
    sys.exit()
    
class myGraphics:
    def __init__(self):
        self.width=600
        self.height=800
        
    def initScene(self):
        glClearColor(0.0, 0.0, 0.0, 1.0) #clear the color of the window
        glClearDepth(1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
    def drawKlccPart(self,x,y):
        #klcc
        glTranslatef(x,y,0.0)
        glBegin(GL_QUADS)
        glColor3ub(0,0,0)
        glVertex3f(-0.4,-1.0,0.0)
        glVertex3f(-0.2,-1.0,0.0)
        glColor3ub(200,200,200)
        glVertex3f(-0.2,0.2,0.0)
        glVertex3f(-0.4,0.13,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.2,-1.0,0.0)
        glVertex3f(-0.1,-1.0,0.0)
        glColor3ub(100,100,100)
        glVertex3f(-0.1,0.1,0.0)
        glVertex3f(-0.2,0.2,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(50,50,50)
        glVertex3f(-0.4,0.13,0.0)
        glVertex3f(-0.2,0.2,0.0)
        glColor3ub(200,200,200)
        glVertex3f(-0.2,0.7,0.0)
        glVertex3f(-0.4,0.6,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.2,0.2,0.0)
        glVertex3f(-0.1,0.1,0.0)
        glColor3ub(100,100,100)
        glVertex3f(-0.1,0.6,0.0)
        glVertex3f(-0.2,0.7,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(100,100,100)
        glVertex3f(-0.39,0.61,0.0)
        glVertex3f(-0.2,0.7,0.0)
        glColor3ub(200,200,200)
        glVertex3f(-0.2,1.05,0.0)
        glVertex3f(-0.39,1.0,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.2,0.7,0.0)
        glVertex3f(-0.1,0.6,0.0)
        glColor3ub(100,100,100)
        glVertex3f(-0.1,1.0,0.0)
        glVertex3f(-0.2,1.05,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(100,100,100)
        glVertex3f(-0.35,1.01,0.0)
        glVertex3f(-0.2,1.05,0.0)
        glColor3ub(200,200,200)
        glVertex3f(-0.2,1.25,0.0)
        glVertex3f(-0.35,1.2,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.2,1.05,0.0)
        glVertex3f(-0.1,1.0,0.0)
        glColor3ub(100,100,100)
        glVertex3f(-0.1,1.16,0.0)
        glVertex3f(-0.2,1.25,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(220,220,220)
        glVertex3f(-0.34,1.204,0.0)
        glVertex3f(-0.2,1.25,0.0)
        glVertex3f(-0.2,1.37,0.0)
        glVertex3f(-0.34,1.32,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.2,1.25,0.0)
        glVertex3f(-0.11,1.17,0.0)
        glColor3ub(100,100,100)
        glVertex3f(-0.11,1.31,0.0)
        glVertex3f(-0.2,1.37,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.30,1.32,0.0)
        glVertex3f(-0.2,1.37,0.0)
        glVertex3f(-0.2,1.42,0.0)
        glVertex3f(-0.30,1.42,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3ub(255,255,255)
        glVertex3f(-0.2,1.37,0.0)
        glVertex3f(-0.14,1.33,0.0)
        glColor3ub(100,100,100)
        glVertex3f(-0.14,1.42,0.0)
        glVertex3f(-0.2,1.42,0.0)
        glEnd()
        
        glBegin(GL_TRIANGLES)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(-0.30,1.42,0.0)
        glVertex3f(-0.14,1.42,0.0)
        glColor3f(1.0,1.0,1.0)
        glVertex3f(-0.22,1.54,0.0)
        glEnd()
        
        glColor3f(1.0,0.0,0.0)
        glLineWidth(5.0)
        glBegin(GL_LINES)
        glVertex3f(-0.22,1.52,0.0)
        glVertex3f(-0.22,1.60,0.0)
        glEnd()
        
        glTranslatef(-x,-y,0.0)
        
    def drawScene(self):
        # background
        glBegin(GL_QUADS)
        glColor3f(0.8,0.8,0.8)
        glVertex3f(-4.0,-4.0,0.0)
        glVertex3f(4.0,-4.0,0.0)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(4.0,4.0,0.0)
        glVertex3f(-4.0,4.0,0.0)
        glEnd()
        
        
        
        #KLCC
        self.drawKlccPart(0,0)
        
        #klcc bridge
        glColor3f(1.0,1.0,1.0)
        glLineWidth(5.0)
        glBegin(GL_LINES)
        glVertex3f(0.0,0.2,0.0)
        glVertex3f(-0.1,-0.3,0.0)
        glEnd()
        
        glColor3f(1.0,1.0,1.0)
        glLineWidth(5.0)
        glBegin(GL_LINES)
        glVertex3f(0.0,0.2,0.0)
        glVertex3f(0.3,-0.4,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.0)
        glVertex3f(-0.15,0.1,0.0)
        glVertex3f(0.5,0.2,0.0)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(0.5,0.3,0.0)
        glVertex3f(-0.15,0.2,0.0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.0)
        glVertex3f(-0.15,0.2,0.0)
        glVertex3f(0.5,0.3,0.0)
        glColor3f(0.2,0.2,0.2)
        glVertex3f(0.5,0.35,0.0)
        glVertex3f(-0.1,0.25,0.0)
        glEnd()
        
        self.drawKlccPart(0.6,0.1)

        #view under bridge
        glBegin(GL_QUADS)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(-2.0,-0.9,0.0)
        glVertex3f(2.0,-0.9,0.0)
        glColor3f(0.7,0.7,0.7)
        glVertex3f(2.0,-1.7,0.0)
        glVertex3f(-2.0,-1.7,0.0)
        glEnd()
        
        #water
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.0)
        glVertex3f(-2.0,-1.7,0.0)
        glVertex3f(2.0,-1.7,0.0)
        glColor3f(0.0,1.0,1.0)
        glVertex3f(2.0,-3.0,0.0)
        glVertex3f(-2.0,-3.0,0.0)
        glEnd()
        

        
    def display(self):
        self.initScene()
        glLoadIdentity()
        gluLookAt(0.0, 1.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        self.drawScene()
        #glFlush()
        glutSwapBuffers()
        
    def reshape(self,width,height):
        width=self.width
        height=self.height
        
        if height==0:
            height=1
            
        glViewport(0,0, (int)(width), (int)(height))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0,(float)(width)/(float)(height),0.1,100.0)
        glMatrixMode(GL_MODELVIEW)
        
    def sceneLoop(self):
        glutInit(sys.argv) #initialize the program.
        glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)#set up a basic display buffer(only singular for now)
        glutInitWindowSize(self.width, self.height)  # window size
        glutInitWindowPosition(100, 100)  # window position
        glutCreateWindow(b"KLCC")  # show window
        glutDisplayFunc(self.display)  # draw callback function call the display function to draw our world
        glutReshapeFunc(self.reshape)  # resize callback function
        glutMainLoop() # initialize the OpenGL loop cycle

def main():
    myCg=myGraphics()
    myCg.sceneLoop()
    
if __name__=="__main__":
    main()