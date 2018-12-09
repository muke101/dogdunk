import numpy as np
import requests
import json
import random

server = 'http://36f5229b.ngrok.io/'

class dog:
	def __init__(self, userData):
		self.userData = userData
		self.level = int(userData['level'])
		self.experience = int(userData['experience'])
		self.jumpHeight = self.calculateJumpHeight(userData['level'])

	def calculateJumpHeight(self, level):
		return np.log(level)+1 #function offset at y0=1 that rises quickly at first but levels off quickly too

	def levelUp(self):
		self.level+=1
		self.userData['level'] = self.level
		self.experience = 0
		self.userData['experience'] = self.experience
		self.jumpHeight = self.calculateJumpHeight(self.level)
		requests.put(server+self.userData['userName'], data=json.JSONEncoder().encode(self.userData))

	def dunk(self, playerData):
		playerJumpHeight = self.calculateJumpHeight(playerData['level'])
		heightDifference = self.jumpHeight - playerJumpHeight
		successProbablity = (self.jumpHeight**heightDifference)*random.random() # negative difference reduces chance, positive increases
		if successProbablity > 0.5:
			self.experience+=10*playerData['level'] #recived xp scales with level defeated
			self.userData['experience'] = self.experience
			if self.experience >= (30*(self.level**2))/3:
				self.levelUp()
			else:
				requests.put(server+self.userData['userName'], data=json.JSONEncoder().encode(self.userData))
			return True
		else:
			playerData['experience']+=10*self.userData['level']
			if playerData['experience'] >= (30*(playerData['level']**2))/3:
				playerData['experience'] = 0
				playerData['level']+=1
			requests.put(server+playerData['userName'], data=json.JSONEncoder().encode(playerData))
			return False

def login(userName):
	userData = requests.get(server+userName)
	if userData.status_code == 404:
		print('user not found') #repromt for name
	userData = json.JSONDecoder().decode(userData.text)
	Dog = dog(userData)

def createUser(userName):
	userData = {}
	userData['userName'] = userName
	userData['experience'] = 0
	userData['level'] = 1 #new dogs have zero experience and are level 1
	requests.put(server+userData['userName'], data=json.JSONEncoder().encode(userData))
	Dog = dog(userData)

Dog = dog(json.JSONDecoder().decode(requests.get(server+'muke').text))

def dunker():
	return Dog.dunk(json.JSONDecoder().decode(requests.get(server+'bikeboi').text))







