#! /usr/bin/python3

# Copyright Burcea Marian-Gabriel 2019

import pygame
import random

BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)

pygame.init()

win = pygame.display.set_mode((850, 480))
pygame.display.set_caption("Goblin Assault")

walk_left = [pygame.image.load("Images/L1.png"), pygame.image.load("Images/L2.png"), pygame.image.load("Images/L3.png"),
			 pygame.image.load("Images/L4.png"), pygame.image.load("Images/L5.png"), pygame.image.load("Images/L6.png"),
			 pygame.image.load("Images/L7.png"), pygame.image.load("Images/L8.png"), pygame.image.load("Images/L9.png")]

walk_right = [pygame.image.load("Images/R1.png"), pygame.image.load("Images/R2.png"), pygame.image.load("Images/R3.png"),
			  pygame.image.load("Images/R4.png"), pygame.image.load("Images/R5.png"), pygame.image.load("Images/R6.png"),
			  pygame.image.load("Images/R7.png"), pygame.image.load("Images/R8.png"), pygame.image.load("Images/R9.png")]

bg = pygame.image.load("Images/bg.jpg")
bg_gray = pygame.image.load("Images/bg_gray.jpg")

bullet_sound = pygame.mixer.Sound("Music/bullet.wav")
hit_sound = pygame.mixer.Sound("Music/hit.wav")
music = pygame.mixer.music.load("Music/music.mp3")

class player(object):
	def __init__(self):
		self.x = random.randrange(790)
		self.y = 400
		self.width = 64
		self.height = 64
		self.step = 5
		self.is_jumping = False
		self.left = False
		self.right = False
		self.walk_count = 0
		self.jump_count = 10
		self.standing = True
		self.hitbox =(self.x + 17, self.y + 11, 29, 52)

	def reset_x(self):
		self.x = random.randrange(790)
		self.hitbox =(self.x + 17, self.y + 11, 29, 52)

	def hit(self):
		self.is_jumping = False
		self.jump_count = 10
		self.x = random.randrange(790)
		self.y = 400
		self.walk_count = 0

		font1 = pygame.font.SysFont("comicsans", 100)
		text = font1.render("-5", 1, RED)
		win.blit(text, (win.get_width() / 2 - text.get_width() / 2, 200))
		pygame.display.update()

		i = 0
		while i < 100:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 101
					pygame.quit()

	def draw(self, win):
		if self.walk_count + 1 >= 27:
			self.walk_count = 0
		if not self.standing:
			if self.left:
				win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
				self.walk_count += 1

			elif self.right:
				win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
				self.walk_count += 1

		else:
			if self.left:	
				win.blit(walk_left[0], (self.x, self.y))
			else:
				win.blit(walk_right[0], (self.x, self.y))

		self.hitbox = (self.x + 17, self.y + 11, 29, 52)


class projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.step = 8 * facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
	walk_left = [pygame.image.load("Images/L1E.png"), pygame.image.load("Images/L2E.png"), pygame.image.load("Images/L3E.png"),
				 pygame.image.load("Images/L4E.png"), pygame.image.load("Images/L5E.png"), pygame.image.load("Images/L6E.png"),
				 pygame.image.load("Images/L7E.png"), pygame.image.load("Images/L8E.png"), pygame.image.load("Images/L9E.png"),
				 pygame.image.load("Images/L10E.png"), pygame.image.load("Images/L11E.png")]

	walk_right = [pygame.image.load("Images/R1E.png"), pygame.image.load("Images/R2E.png"), pygame.image.load("Images/R3E.png"),
				  pygame.image.load("Images/R4E.png"), pygame.image.load("Images/R5E.png"), pygame.image.load("Images/R6E.png"),
				  pygame.image.load("Images/R7E.png"), pygame.image.load("Images/R8E.png"), pygame.image.load("Images/R9E.png"),
				  pygame.image.load("Images/R10E.png"), pygame.image.load("Images/R11E.png")]

	def __init__(self):
		self.x = random.randrange(790)
		self.y = 405
		self.width = 64
		self.height = 64
		self.path = [-20, 800]
		self.walk_count = 0
		self.step = 3 * random.choice([-1, 1])
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)
		self.healt = 9

	def reset_x(self):
		self.x = random.randrange(790)
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)

	def move(self):
		if self.step < 0:
			if self.x < self.path[0]:
				self.step = -self.step
				self.walkCount = 0
			self.x += self.step
		else:
			if self.x > self.path[1]:
				self.step = -self.step
				self.walkCount = 0
			self.x += self.step

	def hit(self):
		hit_sound.play()

		if self.healt > 0:
			self.healt -= 1
			return False
		else:
			return True

	def draw(self, win):
		self.move()
		if self.walk_count + 1 > 33:
			self.walk_count = 0

		if self.step < 0:
			win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
			self.walk_count += 1
		else:
			win.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
			self.walk_count += 1

		pygame.draw.rect(win, RED, (self.hitbox[0], self.hitbox[1] - 20, 45, 10))
		pygame.draw.rect(win, GREEN, (self.hitbox[0], self.hitbox[1] - 20, 50 - 4.5 * (10 - self.healt), 10))
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)


def draw_button(color, x, y, width, height, content, size):
	pygame.draw.rect(win, color, (x, y, width, height))
	font = pygame.font.SysFont("comicsans", size, True)
	text = font.render(content, 1, BLACK)
	win.blit(text, (x + 100 - text.get_width() / 2, y + 13))


def redraw_world():
	win.blit(bg, (0, 0))

	font = pygame.font.SysFont("comicsans", 30, True)
	text = font.render("Score: " + str(score), 1, BLACK)
	win.blit(text, (370, 10))

	man.draw(win)
	for goblin in enemies:
		goblin.draw(win)
	for bullet in bullets:
		bullet.draw(win)

	pygame.display.update()


def start_menu():
	global choice, level

	press_loop = 0

	clock = pygame.time.Clock()
	while True:
		win.blit(bg_gray, (0, 0))
		clock.tick(27)

		press_loop += 1
		if press_loop > 1:
			press_loop = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN]:
			if choice == 1:
				level = 0
				select_level()
			else:
				quit()

		if (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and press_loop == 0:
			choice = 1 - choice

		relative_height = 0
		for i in range(2):
			if choice == i:
				pygame.draw.rect(win, RED, (win.get_width() / 2 - 105, win.get_height() / 2 - relative_height - 5, 210, 60))
				break
			relative_height += 100

		buttons = ["PLAY", "QUIT"]
		relative_height = -100
		for button in buttons:
			draw_button(YELLOW, win.get_width() / 2 - 100, win.get_height() / 2 + relative_height, 200, 50, button, 40)
			relative_height += 100

		pygame.display.update()


def pause_menu():
	global pause

	press_loop = 0

	clock = pygame.time.Clock()
	while True:
		win.blit(bg_gray, (0, 0))
		clock.tick(27)

		press_loop += 1
		if press_loop > 1:
			press_loop = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN]:
			if pause == 0:
				return
			elif pause == 1:
				pause = 0
				select_level()
			else:
				quit()

		if keys[pygame.K_UP] and press_loop == 0:
			pause -= 1
			if pause < 0:
				pause = 2

		elif keys[pygame.K_DOWN] and press_loop == 0:
			pause += 1
			if pause > 2:
				pause = 0

		relative_height = -155
		for i in range(3):
			if pause == i:
				pygame.draw.rect(win, RED, (win.get_width() / 2 - 105, win.get_height() / 2 + relative_height, 210, 60))
				break
			relative_height += 100

		buttons = ["RESUME", "RESTART", "QUIT"]
		relative_height = -150
		for button in buttons:
			draw_button(YELLOW, win.get_width() / 2 - 100, win.get_height() / 2 + relative_height, 200, 50, button, 40)
			relative_height += 100

		pygame.display.update()


def select_level():
	global level

	clock = pygame.time.Clock()

	press_loop = 0

	wait = 0

	while True:
		win.blit(bg_gray, (0, 0))
		clock.tick(27)
		wait += 1

		press_loop += 1
		if press_loop > 1:
			press_loop = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN] and wait > 10:
			game_level = level + 1
			pygame.mixer.music.play(-1)
			game_loop(game_level)

		if keys[pygame.K_UP]and press_loop == 0:
			level -= 1
			if level < 0:
				level = 4

		elif keys[pygame.K_DOWN] and press_loop == 0:
			level += 1
			if level > 4:
				level = 0

		relative_height = -180
		for i in range(5):
			if level == i:
				pygame.draw.rect(win, RED, (win.get_width() / 2 - 105, win.get_height() / 2 + relative_height, 210, 60))
				break
			relative_height += 75

		relative_height = -175
		for i in range(5):
			draw_button(YELLOW, win.get_width() / 2 - 100, win.get_height() / 2 + relative_height, 200, 50, "LEVEL " + str(i + 1), 35)
			relative_height += 75

		pygame.display.update()		


def game_loop(level):
	global score, man, enemies, bullets

	enemies = []
	for i in range(level):
		enemies.append(enemy())
	man = player()
	while True:
		ok = True
		for i in range(len(enemies)):
			if man.hitbox[0] + man.hitbox[2] > enemies[i].hitbox[0] - 50 and man.hitbox[0] - 50 < enemies[i].hitbox[0] + enemies[i].hitbox[2]:
				man.reset_x()
				ok = False
		if ok:
			break

	bullets = []
	shoot_loop = 0

	score = 0

	clock = pygame.time.Clock()

	while True:
		clock.tick(27)
		for i in range(len(enemies)):
			if man.hitbox[0] + man.hitbox[2] > enemies[i].hitbox[0] and man.hitbox[0] < enemies[i].hitbox[0] + enemies[i].hitbox[2]:
				if man.hitbox[1] + man.hitbox[3] > enemies[i].hitbox[1] and man.hitbox[1] < enemies[i].hitbox[1] + enemies[i].hitbox[3]:
					man.hit()

					while True:
						ok = True
						for i in range(len(enemies)):
							if man.hitbox[0] + man.hitbox[2] > enemies[i].hitbox[0] - 50 and man.hitbox[0] - 50 < enemies[i].hitbox[0] + enemies[i].hitbox[2]:
								man.reset_x()
								ok = False
						if ok:
							break

					score -= 5

		if shoot_loop > 0:
			shoot_loop += 1
			if shoot_loop > 3:
				shoot_loop = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		for bullet in bullets:
			for i in range(len(enemies)):
				if bullet.x + bullet.radius > enemies[i].hitbox[0] and bullet.x - bullet.radius < enemies[i].hitbox[0] + enemies[i].hitbox[2]:
					if bullet.y + bullet.radius > enemies[i].hitbox[1] and bullet.y - bullet.radius < enemies[i].hitbox[1] + enemies[i].hitbox[3]:
						if enemies[i].hit():
							enemies.pop(i)
							enemies.append(enemy())
							while True:
								if man.hitbox[0] + man.hitbox[2] > enemies[level - 1].hitbox[0] - 50 and man.hitbox[0] - 50 < enemies[level - 1].hitbox[0] + enemies[level - 1].hitbox[2]:
									enemies[level - 1].reset_x()
								else:
									break

						score += 1
						bullets.pop(bullets.index(bullet))
						break

			if bullet.x < 850 and bullet.x > 0:
				bullet.x += bullet.step
			else:
				if bullet in bullets:
					bullets.pop(bullets.index(bullet))

		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE] and shoot_loop == 0:
			bullet_sound.play()

			if man.left:
				facing = -1
			else:
				facing = 1

			if len(bullets) < 5:
				bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2) + 5, 6, BLUE, facing))

			shoot_loop = 1

		if keys[pygame.K_LEFT]:
			if man.x > -40:
				man.x -= man.step
			else:
				man.x = 825
			man.left = True
			man.right = False
			man.standing = False

		elif keys[pygame.K_RIGHT]:
			if man.x < 825:
				man.x += man.step
			else:
				man.x = -40
			man.left = False
			man.right = True
			man.standing = False

		else:
			man.standing = True
			man.walk_count = 0

		if keys[pygame.K_ESCAPE]:
			pause_menu()

		if not man.is_jumping:
			if keys[pygame.K_UP]:
				man.is_jumping = True
				man.left = False
				man.right = False
				man.walk_count = 0

		else:
			if man.jump_count >= -10:
				man.y -= man.jump_count * abs(man.jump_count) * 0.5
				man.jump_count -= 1
			else:
				man.jump_count = 10
				man.is_jumping = False

		redraw_world()

choice = 1
pause = 0
game_level = 1

start_menu()
pygame.quit()