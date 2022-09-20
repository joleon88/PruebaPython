import sys, pygame
import numpy as np

# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("Juego BALL")
# Inicializamos variables
width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255
# Crea un objeto imagen bate y obtengo su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
# Pongo el bate en el centro de la pantalla
baterect.move_ip(320, 550)
# Crea un objeto imagen pelota y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
# Pongo la pelota en el centro del bate
ballrect.move_ip((baterect.x + baterect.width/2)-10, baterect.y-ballrect.height)
#Cargar sonido
sound=pygame.mixer.Sound("tic.WAV")
# Crea un objeto imagen box y obtengo su rectángulo
boxes=[]
arrboxes=[]
level1=[0, 1, 2, 5, 6, 9, 15, 16, 17, 20]
level2=[[0,0], [1,1], [2,2], [3,3],[5,5], [7,7], [8,8], [10,10], [11,11], [13,13], [14,14], [0,15], [0,16], [17,17], [18,18], [19,19], [20,20]]
level3=[[0,0,0], [1,1,1], [2,2,2], [0,4,3],[0,5,4], [7,7,5], [8,8,6], [10,10,7], [11,11,8], [13,13,9], [15,15,10], [17,17,11], [18,18,12], [19,19,13], [20,20,14], [20,20,15], [20,20,16], [20,20,17], [20,20,18], [20,20,19], [20,20,20]]
level4=[[0,0,0,0], [1,1,1,1], [2,2,2,2], [0,4,3,3],[0,5,4,4], [7,7,5,5], [8,8,6,6], [10,10,7,7], [11,11,8,8], [13,13,9,9], [15,15,10,10], [17,17,11,11], [18,18,12,12], [19,19,13,13], [20,20,14,14], [20,20,15,15], [20,20,16,16], [20,20,17,17], [20,20,18,18], [20,20,19,19], [20,20,20,20]]
box = pygame.image.load("box.png")
#for i in range(len(level1)):
	#box = pygame.image.load("box.png")
	#boxrect = box.get_rect()
	#boxes.append(box)
	#val=100 + box.get_rect().width * level1[i]
	#boxrect.x = val
	#boxrect.y = 150
	#print(boxrect)
	#arrboxes.insert(i, boxrect)

#cartel de Game Over
perdio = pygame.image.load("gameover.png")
perdiorect = perdio.get_rect()

#Funcion para cargar el nivel
def nextLevel(level):
	i=0
	n=np.ndim(level)
	for var in level:
		if n>1:
			for	dim1 in range(len(var)):
				box = pygame.image.load("box.png")
				boxrect = box.get_rect()
				boxes.append(box)
				val = 100 + box.get_rect().width * var[dim1]
				boxrect.x = val
				boxrect.y = 150 + box.get_rect().height * dim1
				arrboxes.insert(i, boxrect)
				i += 1
		else:
			box = pygame.image.load("box.png")
			boxrect = box.get_rect()
			boxes.append(box)
			val = 100 + box.get_rect().width * var
			boxrect.x = val
			boxrect.y = 150
			arrboxes.insert(i, boxrect)
			i += 1


#nextLevel(level4)
# Comenzamos el bucle del juego
run=True
continuar=False
first=False
cont=0
contLevel=1
while run:
	# Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
	pygame.time.delay(1)
	# Capturamos los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir de la ventana, terminamos
		if event.type == pygame.QUIT: run = False

	#Cambio de nivel
	if len(arrboxes)<1:
		baterect.update(bate.get_rect())
		baterect.move_ip(320, 550)
		ballrect.update(bate.get_rect())
		ballrect.move_ip((baterect.x + baterect.width / 2) - 10, baterect.y - ballrect.height - 5)
		first = False
		if contLevel==1:
			nextLevel(level1)
		if contLevel == 2:
			nextLevel(level2)
		if contLevel==3:
			nextLevel(level3)
		if contLevel==4:
			nextLevel(level4)
		else:
			green=(0, 255, 0)
			blue=(0, 0, 128)
			font=pygame.font.Font("freesandsblod.ttf", 32)
			text=font.render("Has Ganado", True, green, blue)
			textrec=text.get_rect()
			textrec.center=(width // 2, height // 2)
			screen.blit(text, textrec)
		contLevel+=1

	# Compruebo si se ha pulsado alguna tecla
	keys = pygame.key.get_pressed()
	# Soltar la pelota
	if keys[pygame.K_SPACE] and not first and not continuar:
		# Muevo la pelota
		ballrect = ballrect.move(speed)
		speed[1] = -speed[1]
		first = True

	if keys[pygame.K_KP_ENTER]:
		cont=0
		continuar=False
		first = False

	if (first):
		ballrect = ballrect.move(speed)

	# Compruebo si hay colisión con el bate
	if baterect.colliderect(ballrect):
		speed[1] = -speed[1]

	# Compruebo si hay colisión con los box
	for p in arrboxes:
		if ballrect.colliderect(p):
			sound.play()
			speed[1] = -speed[1]
			arrboxes.remove(p)


	if ballrect.left < 0 or ballrect.right > screen.get_width():
		speed[0] = -speed[0]
	if ballrect.top < 0:
		speed[1] = -speed[1]

	#Deter porque perdio
	if ballrect.bottom > screen.get_height():
		first = False
		cont+=1
		baterect.update(bate.get_rect())
		baterect.move_ip(320, 550)
		ballrect.update(bate.get_rect())
		ballrect.move_ip((baterect.x + baterect.width / 2) - 10, baterect.y - ballrect.height-5)

		# Pongo el cartel en el centro de la pantalla
		if cont==3:
			continuar = True
			perdiorect.update(perdio.get_rect())
			perdiorect.move_ip(220, 150)


	#Muevo el bate si la pelota se movió
	if keys[pygame.K_LEFT] and first:
		baterect = baterect.move(-2, 0)
	if keys[pygame.K_RIGHT] and first:
		baterect = baterect.move(2, 0)


	#Mantener el bate dentro de la pantalla
	if baterect.left == 0:
		baterect=baterect.move(2, 0)
	if baterect.right > screen.get_width():
		baterect=baterect.move(-2, 0)

	#Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
	screen.fill(white)
	screen.blit(ball, ballrect)
	screen.blit(bate, baterect)
	for p in arrboxes:
		screen.blit(box, p)
	if continuar:
		screen.blit(perdio, perdiorect)
	pygame.display.flip()
# Salgo de pygame
pygame.quit()