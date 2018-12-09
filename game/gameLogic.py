import numpy as np
import requests
import json
import random

server = 'http://36f5229b.ngrok.io/'

class dog:
	def __init__(self, userData):
		self.userData = userData
		self.level = int(userData['level'])
		self.experiance = int(userData['experiance'])
		self.jumpHeight = self.calculateJumpHeight(userData['level'])

	def calculateJumpHeight(self, level):
		return np.log(level)+1 #function offset at y0=1 that rises quickly at first but levels off quickly too

	def levelUp(self):
		self.level+=1
		self.userData['level'] = self.level
		self.experiance = 0
		self.userData['experiance'] = self.experiance
		self.jumpHeight = self.calculateJumpHeight(self.level)
		requests.put(server+self.userData['userName'], data=json.JSONEncoder().encode(userData))

	def dunk(self, playerData):
		playerJumpHeight = self.calculateJumpHeight(playerData['level'])
		heightDifference = self.jumpHeight - playerJumpHeight
		successProbablity = (self.jumpHeight**heightDifference)*random.random() # negative difference reduces chance, positive increases
		if successProbablity > 0.5:
			self.experiance+=10*playerData['level'] #recived xp scales with level defeated
			self.userData['experiance'] = self.experiance
			if self.experiance >= (30*(self.level**2))/3:
				self.levelUp()
			else:
				requests.put(server+userData['userName'], data=json.JSONEncoder().encode(userData))
			return True
		else:
			playerData['experiance']+=10*self.userData['level']
			if playerData['experiance'] >= (30*(playerData['level']**2))/3:
				playerData['experiance'] = 0
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
	userData['experiance'] = 0
	userData['level'] = 1 #new dogs have zero experiance and are level 1
	requests.put(server+userData['userName'], data=json.JSONEncoder().encode(userData))
	Dog = dog(userData)

Dog = dog(json.JSONDecoder().decode(requests.get(server+'muke').text))

def dunker():
	return Dog.dunk(json.JSONDecoder().decode(requests.get(server+'bikeboi').text))







