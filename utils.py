import json

def get_data():
	with open("elden.json", "r") as file:
		data = json.load(file)
		return data

def push_data(data):
	with open("elden.json", "w") as file:
		json.dump(data, file, indent=4)

def create_new_user(name, data):
	data[name] = {
		"Current": None,
		"Profiles": []
	}
	push_data(data)

def get_data_user(author):
	data = get_data()
	user = str(author)
	if user not in data:
		create_new_user(user, data)
	return data, user

def get_profile(name, data):
	for profile in data["Profiles"]:
		if name == profile["Name"]:
			return profile
	return None

def get_boss(name, profile):
	for boss in profile["Bosses"]:
		if name == boss["Name"]:
			return boss
	return None

icons={
	"Paused": "🛑",
	"Started": "🟠",
	"Killed": "✅"
}