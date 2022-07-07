import pygame


#display pygame windows
pygame.init()
window = pygame.display.set_mode((600,600))

pygame.display.set_caption('TicTacToe By KaTODev')

#game variable
turn = None


int_table = ['1','2','3',
             '4','5','6',
             '7','8','9']



int_button = [pygame.Rect(0, 0, 200, 200),pygame.Rect(200, 0, 200, 200),pygame.Rect(400, 0, 200, 200),

	      pygame.Rect(0, 200, 200, 200),pygame.Rect(200, 200, 200, 200),pygame.Rect(400, 200, 200, 200),

	      pygame.Rect(0, 400, 200, 200),pygame.Rect(200, 400, 200, 200),pygame.Rect(400, 400, 200, 200)]


#load .png file 
bg = pygame.image.load('back.png')
x = pygame.image.load('x.png')
o = pygame.image.load('o.png')
nowin = pygame.image.load('nowinner.png')


winner = {}
winner['X'] = pygame.image.load('playerxwin.png')
winner['O'] = pygame.image.load('playerowin.png')

#draw the background
window.blit(bg, (0,0))

#founction to check the winner 
def check_winner(table , step):
	if (table[0] == table[1] == table[2]):
		window.blit(winner[table[0]], (0,225))
		return False
	elif (table[3] == table[4] == table[5]):
		window.blit(winner[table[3]], (0,225))
		return False
	elif (table[6] == table[7] == table[8]):
		window.blit(winner[table[6]], (0,225))
		return False



	elif (table[0] == table[3] == table[6]):
		window.blit(winner[table[2]], (0,225))
		return False
	elif (table[1] == table[4] == table[7]):
		window.blit(winner[table[1]], (0,225))
		return False
	elif (table[2] == table[5] == table[8]):
		window.blit(winner[table[2]], (0,225))
		return False


	elif (table[0] == table[4] == table[8]):
		window.blit(winner[table[0]], (0,225))
		return False
	elif (table[2] == table[4] == table[6]):
		window.blit(winner[table[2]], (0,225))
		return False


	elif step == 9:
		window.blit(nowin, (0,225))

	return True

#number of step played
step = 0

turn = x
run = True


in_game = True


table = int_table
button = int_button

#loop
while run:
	#update the window
	pygame.display.update()

	#check pygame events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#run = false so we quit the game
			run = False

		#check if mouse button clicked 	
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in button:
					if (not (i == 'full')) and in_game:

						if i.collidepoint(event.pos):
							window.blit(turn, i)
							if turn == x:
								table[button.index(i)] = 'X'
								button[button.index(i)] = 'full'
								turn = o
								step += 1
							elif turn == o:
								table[button.index(i)] = 'O'
								button[button.index(i)] = 'full'
								turn = x
								step += 1
							in_game = check_winner(table,step)

	
                

#quit game
pygame.quit()