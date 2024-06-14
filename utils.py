import json

def get_data():
	with open("count.json", "r") as file:
		data = json.load(file)
		return data

def push_data(data):
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

def create_new_player(name, data):
	data[name] = {
		"CountDeath": 0,
		"Boss": {}
	}

def create_boss(boss, data):
	data["Boss"][boss] = {
		"CountDeath": 0,
		"Status": "Not start"
	}

def is_start(name, data):
	for Boss in data[name]["Boss"]:
		if data[name]["Boss"][Boss]["Status"] == "Start":
			return Boss
	return False

async def validate_boss_and_data(ctx, name, check_for_in):
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		await ctx.send("You don't have a profile !")
		return None, None
	if check_for_in is True:
		if name in data[author]["Boss"]:
			await ctx.send(f"{name} already exists !")
			return None, None
	else:
		if name not in data[author]["Boss"]:
			await ctx.send(f"{name} doesn't exists !")
			return None, None
	return data, author

icons={
	"Not start": "🛑",
	"Start": "🟢",
	"Pause": "⏸️",
	"Win": "✅"
}