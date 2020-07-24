'''
Name: Grant Reuter

This program produces a space invaders like game. You will be
moving a ship with mouse clicks and firing lasers using the spacebar
to shoot at enemy ships and be careful you dont want the enemy ships to run into
your ship.  
'''



from graphics import *
import time
import random
import math


ENEMY_SPEED = 10
SHIP_SPEED = 25
LASER_SPEED = 25
NUM_WIN = 20
STALL_TIME = 0.05
WINDOW_WIDTH = 666
WINDOW_HEIGHT = 666

def distanceBetween(point1, point2):
    '''
    Calculates the distance between two points
    
    Params:
    point1 (Point): the first point
    point2 (Point): the second point
    
    Returns:
    the distance between the two points
    '''
    diffX = point2.getX() - point1.getX()
    diffY = point2.getY() - point1.getY()
    return math.sqrt(diffX**2 + diffY**2)


def firstWindow(win):
    '''
    This function draws a window to start the game and gives instruction to the user. The last two lines of code
    check for a mouse click, then closes the window and moves to the next function. 
    '''
    win.setBackground("black")
    texts = Text(Point(333, 233), 'INSTRUCTIONS').draw(win)
    texts.setSize(20)
    texts.setTextColor("purple")
    
    texts = Text(Point(333, 270), '1. Use the mouse to move the ship left to right.').draw(win)
    texts.setSize(20)
    texts.setTextColor("purple")
    
    texts = Text(Point(333, 300), '2. Press the space bar to shoot lasers.').draw(win)
    texts.setSize(20)
    texts.setTextColor("purple")
    
    texts = Text(Point(333, 330), '3. Use the lasers to destroy the enemy ships.').draw(win)
    texts.setSize(20)
    texts.setTextColor("purple")
    
    texts = Text(Point(333, 360), '4. Do not let the enemy ship run into your ship or else you lose.').draw(win)
    texts.setSize(20)
    texts.setTextColor("purple")
    
    texts = Text(Point(333, 390), '5. In order to win you need to destroy '+ str(NUM_WIN) +" enemy ships.").draw(win)
    texts.setSize(20)
    texts.setTextColor("purple")
    
    mouse = win.getMouse()
    win.close()
    
def loseWindow():
    '''
    This window is activated when the user loses and informs the user they have lost.
    '''
    window = GraphWin("YOU LOSE!!!", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("black")
    lose = Image(Point(333, 333), "lose.gif")
    lose.draw(window)
    #stalls window by 3 seconds 
    time.sleep(3)
    window.close()
    exit(-1)
    
        
        
def winWindow():
    '''
    This window is activated when the user wins the game and is presented with a victory screen.
    '''
    window = GraphWin("YOU WIN!!!", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("black")
    win = Image(Point(333, 333), "win.gif")
    win.draw(window)
    #stalls window by 3 seconds 
    time.sleep(3)
    window.close()
    exit(-1)
    
    
def isCloseEnough(shipImg, enemyImg):
    '''
    This function ends the game when an enemy runs into the ship.
    '''
    threshold = shipImg.getWidth() / 2 + enemyImg.getWidth() / 2
    shipCenter = shipImg.getAnchor()
    enemyCenter = enemyImg.getAnchor()
    distance = distanceBetween(shipCenter, enemyCenter)
    
    # return distance < threshold
    if distance < threshold:
        return True
    else:
        return False

def moveEnemy(enemyImgList):
    '''
    This function moves the enemy from a list to the top of the window then to the bottom of the window.
    '''
    #adds enemy to window from enemy list
    for enemy in enemyImgList:
        enemy.move(0, ENEMY_SPEED)
        
def moveLaser(manyLaser):
    '''
    This function moves the laser from the laser list.
    '''
    #adds laser to window from laser list
    for laser in manyLaser:
        laser.move(0, -LASER_SPEED)
        
        

#anchor point
def moveShip(win, shipImg):
    '''
    This function moves the ship with a mouse click from either left to right.
    '''
    mouse = win.checkMouse()
    #Point(250.0, 300.0)
    #point is center of image
    if mouse != None:
        #ship achor gives x and y value, getX gets X value.
        x = shipImg.getAnchor().getX()
        #no need of getAnchor because it already a point, get X returns the X value from mouse
        xMouse = mouse.getX()
       #if statements used to move ship left to right depending on the mouse=checkmouse() function
        #ship starts at 333 which is middle
        if xMouse < x:
            shipImg.move(-SHIP_SPEED, 0)

        else:
            shipImg.move(SHIP_SPEED, 0)
            
    #want x value
        #y value stays the same which is stored in ship == 580




def whiteDots(window):
    '''
    This function adds white dots to the window to make it look like stars.
    '''
    for num in range(100):
        #draws little white dots for the program 
        x = random.randrange(WINDOW_WIDTH)
        y = random.randrange(WINDOW_HEIGHT)
        dot = Point(x, y)
        dot.setFill("white")
        dot.draw(window)
    

def addEnemyToWindow(win):
    '''
    This function adds an enemy to the window.
    '''
    #draws enemy to window then returns it to the enemyImg function 
    xEnemyLocation = random.randrange(40, 600)
    enemyImg = Image(Point(xEnemyLocation, -40),'enemyship.gif')
    enemyImg.draw(win)
    return enemyImg

def addLaserToWindow(win, ship):
    '''
    This function adds a laser to the window and this fucntion is accessed when the spacebar is pressed.
    '''
    #anchor is center of image
    #whole point X and Y 
    laserLocation = ship.getAnchor()
    #laserlocation is x and y becasue of Anchor 
    laserIMG = Image(laserLocation,"laser.gif")
    laserIMG.draw(win)
    return laserIMG
    

def gameLoop(window, ship):
    '''
    Loop continues to allow the enemy ships to fall and the ship to move
    until enough enemy ships escape or the ship shoots enough enemy ships to
    end the game.
    
    window (GraphWin): the window where game play takes place
    ship (Image): the ship image
    '''
    scoreLabel = Text(Point(550, 50), '0')
    scoreLabel.setTextColor("white")
    scoreLabel.draw(window)

    missed = 0
    score = 0
    enemyList = []
    laserList = []#reference to the image is stored-image is stored in single when pressing space
    #while missed < NUM_LOSE and score < NUM_WIN:
    while True:
        if random.randrange(100) < 10:
            enemy = addEnemyToWindow(window)
            enemyList.append(enemy)
    #gets key   
        key = window.checkKey()
    #if space add laser to list
        if key == "space" :
            #no laser is drawn in window until space bar is pressed then into addLaserToWindow function
            addlaser = addLaserToWindow(window, ship)
            laserList.append(addlaser)
        #calls the function 
        moveLaser(laserList)
        moveShip(window, ship)
        moveEnemy(enemyList)
        
        
        for enemy in enemyList:
            #removes laser and enemy ship from window if hit 
            for laser in laserList:
                if isCloseEnough(laser, enemy):
                    enemy.undraw()
                    laser.undraw()
                    enemyList.remove(enemy)
                    laserList.remove(laser)
                    score = score + 1
                    scoreLabel.setText(str(score))
                    if score == NUM_WIN:
                        window.close()
                        winWindow()
                        
                    
                
               #if enemy goes off window -1 point     
            if enemy.getAnchor().getY() > 700:
                enemyList.remove(enemy)
                missed = missed + 1
                score = score - 1
                scoreLabel.setText(str(score))

            #if enemy ship comes close enough game over
            if isCloseEnough(ship, enemy):
                for count in range(20): 
                    ship.move(0, -SHIP_SPEED*1)
                    time.sleep(STALL_TIME)
                window.close()
                loseWindow()
                 
                
        
        time.sleep(STALL_TIME)
    
def main():
    '''
    This function is my main function that draws the window for the game and draws the ship in the window
    and calls other fucnitons. 
    '''
    # setup the game
    newWindow = GraphWin("Instructions", WINDOW_WIDTH, WINDOW_HEIGHT)
    firstWindow(newWindow)
    window = GraphWin("Space The Final Froniter ", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("black")
    texts = Text(Point(333, 650), 'Use the mouse to move the ship left to right').draw(window)
    texts.setTextColor("white")
    ship = Image(Point(333,580), "ship.gif")
    whiteDots(window)
    ship.draw(window)
    gameLoop(window, ship)
    
    
   
    
    

if __name__ == "__main__":
    main()
