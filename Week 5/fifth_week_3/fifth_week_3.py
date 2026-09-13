import json

def load_config(filename:str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        return {
            "app_name": "Student Management System",
            "version": "1.0.0",
            "settings": {
                "theme": "dark",
                "language": "English",
                "notifications": True
            }
        }


#============================================================
# {1} config.json file was created
#============================================================

# {2} loading configuration when the program starts
config = load_config("config.json")
print(config)

#============================================================

# {3} reading nested settings
print(config["settings"])
print(config["settings"]["theme"])
print(config["settings"]["language"])
print(config["settings"]["notifications"])

#============================================================

# {4} modifying one setting in the memory
config["settings"]["theme"] = "light"
print(config["settings"]["theme"])

#============================================================

# {5} writing the updated configuration back into memory
with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)

#============================================================

# {6} handle a missing configuration file with a reasonable default
# I used try and except, so that if a file doesn't exist we return the default configuration

