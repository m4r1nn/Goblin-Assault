# League-of-OOP --- Burcea Marian Gabriel

**SHORT DESCRIPTION**\
	'Goblin Assault' is a mini-2d-game based on work with characters and physics
rules (gravity). The game is built in python3 pygame module and contains simple
and basics elements (image, draw.rect, event, clock, etc.).
	The logic consists in protecting the main character from enemies by constantly
moving apart from them, eventually shooting projectiles toward them. Being made
in pygame, the project engine needs to update the window every time (works with
frames).

**MAIN CLASSES**\
 - __Player__  class which implements the logic for the main character with main
 methods move and hit (when collides with an enemy) --> is controlled by human;
 - __Enemy__ class which implements the logic behind monsters behaviour with
 the same main methods move and hit (when collides with a projectile) --> is not
 controlled by human, having a regulate movement (left and right);
 - __Projectile__ class which represents the bullets shooted from player toward
 enemies;
 - all three classes has draw method that uses pygame resource to display the
 movement;

**GAME ENGINE and MENUS**\
 - __Game Engine__ consists in a while loop that keeps updating the displayed
 window regarding the player and enemies actions (move, shoot, collide).
 - the interaction with human is made with the keyboard by *pygame.key.get_pressed()*.
 - the three menus are: *Start Menu*, *Pause Menu* and *Select Level Menu*,
 which follow each other depending on what key is pressed. The level is given
 by the number of enemies that accompanies the main hero.
