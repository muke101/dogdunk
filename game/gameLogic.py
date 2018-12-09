import numpy as np
import requests
import json
import random

server = 'http://0a69cff3.ngrok.io/'

class dog:
	def __init__(self, userData):
		self.userData = userData
		self.image = userData[imagepath]
		self.level = userData[level]
		self.experiance = userData[experiance]
		self.jumpHeight = jumpHeight(self.level)

	def jumpHeight(self, level):
		return np.log(level)+1 #function offset at y0=1 that rises quickly at first but levels off quickly too

	def levelUp(self):
		self.level = self.userData[level]+=1
		self.jumpHeight = jumpHeight(self.level)
		requests.put(server+self.userData[userName], data=userData)

	def dunk(self, player):
		playerJumpHeight = jumpHeight(player[level])
		heightDifference = self.jumpHeight - playerJumpHeight
		successProbablity = (self.jumpHeight**heightDifference)*random.random() # negative difference reduces chance, positive increases
		if successProbablity > 0.5:
			return True
		else:
			return False

while True: 
	if login:
		userName = ''
		userData = requests.get(server+userName)
		if userData.status_code == 404:
			print('user not found') #repromt for name
		userData = json.decode(userData.text)
		Dog = dog(userData)
		break
	if createUser:
		userData = {}
		userData[userName] = ''
		userData[imagePath] = ''
		userData[experiance] = 0
		userData[level] = 1 #new dogs have zero experiance and are level 1
		requests.put(server+userData[userName], data=userData)
		Dog = dog(userData)
		break

while True:
	if dunk:
		if Dog.dunk(json.decode(requests.get(server+'bikeboi').text)):
			#carry out dunk
		else:
			#display text saying 'failed'
	if exit:
		exit()






