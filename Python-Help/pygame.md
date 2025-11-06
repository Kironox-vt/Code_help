# Pygame Help page

First you need to download pygame into your virtual environment or your pc, to download to your pc, do this in the command line
```
pip install pygame
```

In your code you then need to import the module by doing the following command
```python
import pygame
```
## Starting pygame and using it

To initialize the module we will then put in
```python
pygame.init()
```

To choose which aspect ratio to make the screen do this, you will configure the screen size by changing the width and the height 
```python
screen = pygame.display.set_mode((width, height))
```

To put the name of the app, we will use another command
```python
pygame.display.set_caption('App name')
```

To keep the game running forever or until we want to close it we will make a loop
```python
#set a variable to True
running = True

#create the loop
while running:
    #the rest of the game code
```

All of the code for our game will reside in the game loop, before we continue, this is what the basic structure of the game should look like before adding the actual game
```python
import pygame
pygame.init()

screen = pygame.display.set_mode((width, height))

running = True
while running:

```

In the loop, there is an essential command that you need to keep to be able to update the screen every time something happens
```python
running = True
while running:
    pygame.display.update() # this makes the screen update each frame of the game according to what is happening. This line of code should also be at the end of the loop
```

From now on, everything that i am typing is going to be in the loop and before the display update

## Closing the game

To close the game we need to write a specific command
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        running = False
```
## Capping the Frame rate

To cap the frame rate, we should write this:
```python
#before the while loop
clock = pygame.time.clock
while True:
    #after while loop
    clock.tick(60) #You can put any vaulue
```
this caps the frame rate at 60 fps
in total we should have this:

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((width, height))

running = True

clock = pygame.time.clock
while running:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        running = False
    pygame.display.update()
    
    clock.tick(60)
```