import json

def getData():
	with open("count.json", "r") as file:
		data = json.load(file)
		return data

def pushData(data):
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

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

def isStart(name, data):
	if name in data:
		if "Boss" in data[name]:
			for Boss in data[name]["Boss"]:
				if data[name]["Boss"][Boss]["Status"] == "Start":
					return Boss
	return False

icons={
	"Not start": "🛑",
	"Start": "🟢",
	"Pause": "⏸️",
	"End": "✅"
}