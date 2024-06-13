import icons

def CreateNewPlayer(name, data):
	data[name] = {
		"CountDeath": 0,
		"Boss": {}
	}

def CreateNewBoss(boss, data):
	data["Boss"][boss] = {
		"CountDeath": 0,
		"Status": "Not start"
	}