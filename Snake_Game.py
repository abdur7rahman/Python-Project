# Import the Required Packages
import turtle
import time
import random

# set Delay time as 0.1 Second
delay = 0.1

# Create the Window Screeen
wd = turtle.Screen()
wd.title("Snake Game using Turtle")
wd.bgcolor("sky blue")
wd.setup(width = 700, height = 700)
wd.tracer(0)

# Snake Body part with Empty List 
parts = []

# Variables
score = 0
high_score = 0

# Create a Snake head
head = turtle.Turtle()
head.speed(0)
head.penup()
head.color("black")
head.shape("square")
head.goto(0,0)
head.direction = 'stop'

# Create a Snake's Food
food = turtle.Turtle()
food.speed(0)
food.penup()
food.color("blue")
food.shape("square")
food.goto(58,20)

# Dispaly the Score Box of the Game 
score_box = turtle.Turtle()
score_box.speed(0)
score_box.color("black")
score_box.shape("circle")
score_box.penup()
score_box.goto(0,275)
score_box.hideturtle()
score_box.write("Score:0 High Score:0", align="center", font=("Comic Sans", 20, "normal"))

# Fuction to Move Diection
def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

# Fuctions to Move the Snake with Key Arrows
def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

#Listen the User Input key arrows
wd.listen()
wd.onkeypress(go_right,"Right")
wd.onkeypress(go_left,"Left")
wd.onkeypress(go_up,"Up")
wd.onkeypress(go_down,"Down")

# Main Program
while True:
    wd.update()
    
    # Collision with Border
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        
        # Hide the Parts
        for part in parts:
            part.goto(1000,1000)

        # Clear the Parts
        parts.clear()

        # Reset the Score Box
        score = 0
        score_box.clear()
        score_box.write(f"Score:{score} High Score:{high_score}", align="center", font=("Comic Sans", 20, "bold"))

        #Reset the Delay
        delay = 0.1

    # Collision wih Food
    if head.distance(food) < 20:

        # Move Fod to random Place
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        food.goto(x,y)

        # Create a New part for Snake's Body
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.penup()
        new_part.color("white")
        new_part.shape("square")
        parts.append(new_part)

        #Increase the Score value
        score +=1
        if score > high_score:
            high_score = score
        score_box.clear()
        score_box.write(f"Score:{score} High Score:{high_score}", align="center", font=("Comic Sans", 20, "bold"))

        # Eating Food Everytime can Shorthen the Delay
        delay -= 0.001

    # joint the New Part into End Part
    for i in range(len(parts)-1,0,-1):
        x = parts[i-1].xcor()
        y = parts[i-1].ycor()
        parts[i].goto(x,y)

    # Part 0 is Head
    if len(parts) > 0:
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x,y)

    # Call the Move Fuction
    move()

    #Collision With It's Part (Body) 
    for part in parts:
        if part.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            # Hide the Parts
            for part in parts:
                part.goto(1000,1000)

            # Clear the Parts
            parts.clear()

            # Reset the Score Box
            score = 0
            score_box.clear()
            score_box.write(f"Score:{score} High Score:{high_score}", align="center", font=("Comic Sans", 20, "bold"))

            # Reset the Delay
            delay = 0.1
        
    #Time Delay  
    time.sleep(delay)
    
wd.mainloop()
