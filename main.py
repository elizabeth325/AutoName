# Contructor for the main application.
# This application is designed to give a user name to the user. 
# Username that is common word to username already taken to common word already taken.
# Is for options to pull random usernames.
import json
import random
# Is used to download function for common words.
import hashlib
import urllib.request
import os

class MainApp:
    def __init__(self):
        # Initialize application properties
        self.title = "autoName"
        self.version = "0.0.1"
        # self.author = "elizabeth325"
        self.configJsonInit()
        self.inUseNameJsonInit()
        self.commonWordsJsonInit()
        self.alreadyUsedNamesJsonInit()
        self.commonWordAlreadyUsedNamesJsonInit()
        self.config = self.loadConfig()

        self.run()

    def author(self):
        # clear text in console
        if self.config["config"]["debug"] == "0":
            print("\033c", end="")
        # Print application information
        print(r"             _        _   _                          ")
        print(r"  __ _ _   _| |_ ___ | \ | | __ _ _ __ ___   ___     ")
        print(r" / _` | | | | __/ _ \|  \| |/ _` | '_ ` _ \ / _ \    ")
        print(r"| (_| | |_| | || (_) | |\  | (_| | | | | | |  __/    ")
        print(r" \__,_|\__,_|\__\___/|_| \_|\__,_|_| |_| |_|\___|    ")
        print("--------------------------------")
        print("  autoName - Username Generator")
        print("  Version: 0.0.1")
        print("  Author: elizabeth325")
        print("--------------------------------")
        # Print the application title, version, and author

        # print(f"Running {self.title} version {self.version} by {self.author}")
    
    def run(self):
        print("Application is running...")
        self.author()
        self.choose_option()
    
    #-----------------------------------------
    
    # Choose 1 out of 3 options
    def choose_option(self):
        print("Choose an option:")
        print("1. commonWord:")
        print("     Hardened usernames against osint attacks by using common words.")
        print("2. alreadyUsedName:")
        print("     Hardened usernames against osint attacks by hiding in someone else's shadow.")
        print("3. commonWordAlreadyUsedName:")
        print("     Hardened usernames against osint attacks by using common words with someone else's shadow.")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            self.commonWord_one()
        elif choice == '2':
            self.alreadyUsedName_two()
        elif choice == '3':
            self.commonWordAlreadyUsedName_three()
        else:
            print("Invalid choice, please try again.")
            self.choose_option()
    
    #----------------- Functions to buttons ------------------------
    
    # Its a common word that is already used. 
    # - Benefits of this method:
    #   - Its a common word meaning its not his shadow. Username look up impossible to finger print.
    def commonWord_one(self):
        print("You chose commonWord 1.")
        # Call the commonWordJsonFileUpdate_one method to update the common word JSON file
        self.commonWordJsonFileUpdate_one()
        #------------------------------------
        # what it looks like inside of json file:
        # {
        #   "commonWords": [
        #     "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
        #     "I", "you", "he", "she", "we", "they", "do", "say", "get", "make",
        #     "go", "know", "think", "see", "come", "want", "like", "time", "just",
        #     "now", "good", "new", "first", "last", "great", "little", "other",
        #     "people", "day", "year", "thing", "man", "woman", "life", "child",
        #     "world", "work", "use", "way", "look", "help", "love", "feel", "need",
        #     "back", "here", "there", "then", "when", "how", "why", "because", "so",
        #     "but", "or", "if", "with", "for", "on", "at", "by", "about", "as",
        #     "this", "that", "these", "those", "what", "which", "who", "where"
        #   ]
        # }
        # Implement logic for commonWord 1
        # Read commonWord_one.json file and randomly pull a username that is already taken.
        # Loop until a username is found that is not in use
        while True:
            # Open the commonWord_one.json file and load the data
            with open("commonWord_one.json", "r") as f:
                data = json.load(f)
                # Randomly select a username from the list
                username = random.choice(data["commonWords"])
                if self.checkInUseName(username):
                    # Continue to the next iteration to generate a new username
                    continue
                    
                else:
                    # Example: "work"
                    # if the username is not in use, print it

                    # Confirm username with the user
                    accept = input(f"Accept username: {username} (y/n) ")
                    if accept.lower() != 'y':
                        continue
                    elif(accept.lower() == 'y'):
                        # Add the username to the inUseName.json file
                        # Double check if the username is already in use
                        if self.addToInUseNameFile(username):
                            print(f"Generated username: {username}")
                            # Break the loop if a valid username is found
                            break
                        else:
                            # If the username is already in use, continue to the next iteration
                            continue
                    
                    

    # Its a common word that is already used. 
    # - Benefits of this method:
    #   - Hiding in some else shadow. They have a history.
    def alreadyUsedName_two(self):
        print("You chose alreadyUsedName 2.")
        # Call the alreadyUsedNameJsonFileUpdate_two method to update the already used names JSON file
        self.alreadyUsedNameJsonFileUpdate_two()
        #------------------------------------
        # what it looks like inside of json file:
        # {
        #   "takenUsernames": [
        #     "john", "jane", "guest", "test", "anonymous",
        #     "username", "default", "testuser", "hello",
        #     "world", "coolguy", "coolgirl", "gamer", "player", "champion",
        #     "winner", "loser", "random", "example", "sample", "demo", "first",
        #     "last", "newuser", "olduser", "pro", "noob", "master", "legend",
        #     "hero", "villain", "king", "queen", "prince", "princess", "ninja",
        #     "samurai", "warrior", "knight", "wizard", "witch", "dragon", "phoenix",
        #     "shadow", "light", "dark", "star", "moon", "sun", "earth", "fire",
        #     "water", "air", "space", "galaxy", "cosmos", "infinity", "zero",
        #     "one", "two", "three", "alpha", "beta", "gamma", "omega", "delta"
        #   ]
        # }
        # Loop until a username is found that is not in use
        while True:
            # Implement logic for alreadyUsedName 2
            # Read alreadyUsedName_two.json file and randomly pull a username that is already taken.
            with open("alreadyUsedName_two.json", "r") as f:
                data = json.load(f)
                # Randomly select a username from the list
                username = random.choice(data["takenUsernames"])
                if self.checkInUseName(username):
                    # Continue to the next iteration to generate a new username
                    continue
                    
                else:
                    # Confirm username with the user
                    accept = input(f"Accept username: {username} (y/n) ")
                    if accept.lower() != 'y':
                        continue
                    elif(accept.lower() == 'y'):
                        # Add the username to the inUseName.json file
                        # Double check if the username is already in use
                        if self.addToInUseNameFile(username):
                            # Example: "takenUser89"
                            # username = "takenUser89"
                            print(f"Generated username: {username}")
                            # Break the loop if a valid username is found
                            break
                        else:
                            # If the username is already in use, continue to the next iteration
                            continue

        
    
    # Its a common word that is already used. 
    # - Benefits of this method:
    #   - Its a common word meaning its not his shadow. Username look up impossible to finger print.
    #   - Hiding in some else shadow. They have a history.
    def commonWordAlreadyUsedName_three(self):
        print("You chose commonWordAlreadyUsedName 3.")
        # Call the commonWordAlreadyUsedNameJsonFileUpdate_three method to update the common word already used names JSON file
        self.commonWordAlreadyUsedNameJsonFileUpdate_three()
        #------------------------------------
        # Implement logic for commonWordAlreadyUsedName 3
        # Read commonWordAlreadyUsedName_three.json file and randomly pull a username that is already taken.
        # what it looks like inside of json file:
        # {
        #   "commonWordAlreadyUsedName": [
        #     "john", "jane", "guest", "test", "anonymous", "username", "default",
        #     "hello", "world", "coolguy", "coolgirl", "gamer", "player", "champion",
        #     "winner", "loser", "random", "example", "sample", "demo", "first",
        #     "last", "newuser", "olduser", "pro", "noob", "master", "legend",
        #     "hero", "villain", "king", "queen", "prince", "princess", "ninja",
        #     "samurai", "warrior", "knight", "wizard", "witch", "dragon", "phoenix",
        #     "shadow", "light", "dark", "star", "moon", "sun", "earth", "fire",
        #     "water", "air", "space", "galaxy", "cosmos", "infinity", "zero",
        #     "one", "two", "three", "alpha", "beta", "gamma", "omega", "delta",
        #     "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
        #     "I", "you", "he", "she", "we", "they", "do", "say", "get", "make",
        #     "go", "know", "think", "see", "come", "want", "like", "time", "just",
        #     "now", "good", "new", "great", "little", "other", "people", "day",
        #     "year", "thing", "man", "woman", "life", "child", "work", "use",
        #     "way", "look", "help", "love", "feel", "need", "back", "here", "there",
        #     "then", "when", "how", "why", "because", "so", "but", "or", "if",
        #     "with", "for", "on", "at", "by", "about", "as", "this", "that",
        #     "these", "those", "what", "which", "who", "where"
        #   ]
        # }
        # Loop until a username is found that is not in use
        while True:
            with open("commonWordAlreadyUsedName_three.json", "r") as f:
                data = json.load(f)
                # Randomly select a username from the list
                username = random.choice(data["commonWordAlreadyUsedName"])
                if self.checkInUseName(username):
                    # Continue to the next iteration to generate a new username
                    continue
                    
                else:
                    # Confirm username with the user
                    accept = input(f"Accept username: {username} (y/n) ")
                    if accept.lower() != 'y':
                        continue
                    elif(accept.lower() == 'y'):
                        # Add the username to the inUseName.json file
                        # Double check if the username is already in use
                        if self.addToInUseNameFile(username):
                            # Example: "duck"
                            # username = "duck"
                            print(f"Generated username: {username}")
                            # Break the loop if a valid username is found
                            break
                        else:
                            # If the username is already in use, continue to the next iteration
                            continue
    
    
    #-------------- Updating json files ---------------------------

    # Updates the json file to include common words.
    def commonWordJsonFileUpdate_one(self):
        print("Updating common word JSON file...")
        # Logic to update the common word JSON file
        # Download common words from a URL and save them to a JSON file
        if self.config["config"]["downloadCommonWords"] == "1":
            # If the config is set to download common words, then download them.
            self.downloadCommonWords()
            print("Common word JSON file updated successfully.")
        else:
            # If the config is not set to download usernames, then just download the already used names.
            print("Skipping download of already used names as per configuration.")

    # Updates the json file to include already used names.
    def alreadyUsedNameJsonFileUpdate_two(self):
        print("Updating already used names JSON file...")
        # Logic to update the already used names JSON file
        # Download already used names from a URL and save them to a JSON file
        if self.config["config"]["downloadUsernames"] == "1":
            # If the config is set to download usernames, then download them.
            self.downloadAlreadyUsedNames()
            print("Already used names JSON file updated successfully.")
        else:
            # If the config is not set to download usernames, then just download the already used names.
            print("Skipping download of already used names as per configuration.")

    # Updates the json file to include common words that are already used.
    def commonWordAlreadyUsedNameJsonFileUpdate_three(self):
        print("Updating common word already used names JSON file...")
        # Logic to update the common word already used names JSON file
        # Step 1:
        #   This could involve fetching new common words that are already taken
        #   from an API or a database and saving them to a local JSON file.
        if self.config["config"]["downloadUsernames"] == "1":
            # If the config  is set to download usernames, then download them.
            self.downloadAlreadyUsedNames()
            print("Already used names JSON file updated successfully.")
        else:
            # If the config is not set to download usernames, then just download the already used names.
            print("Skipping download of already used names as per configuration.")


        if self.config["config"]["downloadCommonWords"] == "1":
            # If the config is set to download common words, then download them.
            self.downloadCommonWords()
            print("Common word JSON file updated successfully.")
        else:
            # If the config is not set to download usernames, then just download the already used names.
            print("Skipping download of already used names as per configuration.")

        # Iterates over CommonWords to compare each word to AlreadyUsedNames
        # and if the word is already used, it will add it to commonWordAlreadyUsedName_three.json
        with open("commonWord_one.json", "r") as common_file, open("alreadyUsedName_two.json", "r") as used_file:
            common_data = json.load(common_file)
            used_data = json.load(used_file)

            common_words = set(common_data["commonWords"])
            already_used_names = set(used_data["takenUsernames"])

            # Find common words that are already used
            common_used_names = common_words.intersection(already_used_names)

            # Load existing data from commonWordAlreadyUsedName_three.json
            if os.path.exists("commonWordAlreadyUsedName_three.json"):
                with open("commonWordAlreadyUsedName_three.json", "r") as f:
                    existing_data = json.load(f)
            else:
                existing_data = {"commonWordAlreadyUsedName": []}

            # Add new common used names to the existing data
            existing_data["commonWordAlreadyUsedName"].extend(list(common_used_names))

            # Remove duplicates by converting to a set and back to a list
            existing_data["commonWordAlreadyUsedName"] = list(set(existing_data["commonWordAlreadyUsedName"]))

        #------------------------
        # Step 2:
        #   Calling the two methods above and passing username found.
        #   Lets say it found a username "duck"
        #   Example: "commonWord_one("duck") and alreadyUsedName_two("duck")"
        #   if commonWord_one("duck") is true and alreadyUsedName_two("duck") is true, then:
        #       update commonWordAlreadyUsedName_three.json

        

        # For now, we will just print a message for now due to already existing data.
        print("Common word already used names JSON file updated successfully.")
    
    # Use this json format when storing the downloaded common words:
    # {
    #     "commonWords": [
    #         "word1",
    #         "word2",
    #         ...
    #     ]
    # }
    # Download from this url https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-short.txt
    # Download common words from a URL and save them to a JSON file
    def downloadCommonWords(self):
        print("Downloading common words...")
        url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-short.txt"
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        words = list(set(data.splitlines()))
        words.sort()  # Ensure consistent order for checksum

        # Compute checksum of new data
        new_json = json.dumps({"commonWords": words}, sort_keys=True).encode('utf-8')
        new_checksum = hashlib.sha256(new_json).hexdigest()

        # Check if file exists and compare checksum
        file_path = "commonWord_one.json"
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                existing_data = f.read()
            existing_checksum = hashlib.sha256(existing_data).hexdigest()
            if existing_checksum == new_checksum:
                print("No update needed: commonWord_one.json is up to date.")
                return

        # Save the words to a JSON file
        with open(file_path, "w") as f:
            json.dump({"commonWords": words}, f, indent=4)
        print("Common words downloaded and saved successfully.")
        
    # Use this json format when storing the in-use names:
    # {
    #   "takenUsernames": [
    #     "john", "jane", "guest", "test", "anonymous",
    #     "username", "default", "testuser", "hello",
    #     "world", "coolguy", "coolgirl", "gamer", "player", "champion",
    #     "winner", "loser", "random", "example", "sample", "demo", "first",
    #     "last", "newuser", "olduser", "pro", "noob", "master", "legend",
    #     "hero", "villain", "king", "queen", "prince", "princess", "ninja",
    #     "samurai", "warrior", "knight", "wizard", "witch", "dragon", "phoenix",
    #     "shadow", "light", "dark", "star", "moon", "sun", "earth", "fire",
    #     "water", "air", "space", "galaxy", "cosmos", "infinity", "zero",
    #     "one", "two", "three", "alpha", "beta", "gamma", "omega", "delta"
    #   ]
    # }
    # Downloading txt file from gthub repository https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Usernames/xato-net-10-million-usernames.txt
    # This function will download the usernames from the URL and save them to a JSON file.
    # ISSUES text file contains usernames that are bad words or admin usernames. Places don't like forums DO NOT LIKE THIS. FIND REPLACEMENT
    def downloadAlreadyUsedNames(self):
        print("Downloading already used names...")
        url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Usernames/xato-net-10-million-usernames.txt"
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        usernames = list(set(data.splitlines()))
        usernames.sort()  # Ensure consistent order for checksum

        # Compute checksum of new data
        new_json = json.dumps({"takenUsernames": usernames}, sort_keys=True).encode('utf-8')
        new_checksum = hashlib.sha256(new_json).hexdigest()

        # Check if file exists and compare checksum
        file_path = "alreadyUsedName_two.json"
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                existing_data = f.read()
            existing_checksum = hashlib.sha256(existing_data).hexdigest()
            if existing_checksum == new_checksum:
                print("No update needed: alreadyUsedName_two.json is up to date.")
                return

        # Save the usernames to a JSON file
        with open(file_path, "w") as f:
            json.dump({"takenUsernames": usernames}, f, indent=4)
        print("Already used names downloaded and saved successfully.")

    

    #----------------- In use check ------------------------
    # Check if a username is already in use
    def checkInUseName(self, username):
        # Logic to check if a username is already in use
        # This involves checking inUseName.json file and looping through the usernames.
        with open("inUseName.json", "r") as f:
            data = json.load(f)
            # Check if the username exists in the list of in-use names
            if username in data["inUseNames"]:
                return True
        # For now, we will just return False to indicate the username is not in use
        return False

    # Add a username to the inUseName.json file
    def addToInUseNameFile(self, username):
        # Logic to add a username to the inUseName.json file
        with open("inUseName.json", "r") as f:
            data = json.load(f)
        
        # Check if the username is already in use
        if username not in data["inUseNames"]:
            data["inUseNames"].append(username)
            with open("inUseName.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Username {username} added to in-use names.")
            return True
        else:
            # If the username is already in use.
            return False
    
    #----------------- Initialization ------------------------
    # config.json file is meant to store configuration settings for the application.
    # Initialize the config.json file if it does not exist
    # This is the json format for config.json:
    # {
    #     "default_config": [
    #         "configVersion": "0",
    #         "regenerateCommonWord_one": "0",
    #         "regenerateAlreadyUsedNames_two": "0",
    #         "regenerateCommonWordAlreadyUsedName_three": "0",
    #     ]
    # }
    def configJsonInit(self):
        if not os.path.exists("config.json"):
            default_config = {
                "configVersion": "1.0.0",
                "regenerateCommonWord_one": "0",
                "regenerateAlreadyUsedNames_two": "0",
                "regenerateCommonWordAlreadyUsedName_three": "0",
                "regenerateInUseName": "0",
                "downloadCommonWords": "1",
                "downloadUsernames": "1",
                "debug": "0"
            }
            with open("config.json", "w") as f:
                json.dump({"config": default_config}, f, indent=4)
            print("config.json file created with default settings.")
        else:
            print("config.json file already exists.")
    
    # Initialize the inUseName.json file if it does not exist
    def inUseNameJsonInit(self):
        if not os.path.exists("inUseName.json"):
            default_in_use_names = {
                "bob"
            }
            with open("inUseName.json", "w") as f:
                json.dump({"inUseNames": default_in_use_names}, f, indent=4)
            print("inUseName.json file created with default settings.")
        else:
            print("inUseName.json file already exists.")

    # Initialize the JSON files for common words and already used names
    def commonWordsJsonInit(self):
        if not os.path.exists("commonWord_one.json"):
            default_common_words = {
                "commonWords": []
            }
            with open("commonWord_one.json", "w") as f:
                json.dump(default_common_words, f, indent=4)
            print("commonWord_one.json file created with default settings.")
        else:
            print("commonWord_one.json file already exists.")
    
    # Initialize the JSON files for already used names
    def alreadyUsedNamesJsonInit(self):
        if not os.path.exists("alreadyUsedName_two.json"):
            default_already_used_names = {
                "takenUsernames": []
            }
            with open("alreadyUsedName_two.json", "w") as f:
                json.dump(default_already_used_names, f, indent=4)
            print("alreadyUsedName_two.json file created with default settings.")
        else:
            print("alreadyUsedName_two.json file already exists.")
    
    # Initialize the JSON files for common words that are already used
    def commonWordAlreadyUsedNamesJsonInit(self):
        if not os.path.exists("commonWordAlreadyUsedName_three.json"):
            default_common_word_already_used_names = {
                "commonWordAlreadyUsedName": []
            }
            with open("commonWordAlreadyUsedName_three.json", "w") as f:
                json.dump(default_common_word_already_used_names, f, indent=4)
            print("commonWordAlreadyUsedName_three.json file created with default settings.")
        else:
            print("commonWordAlreadyUsedName_three.json file already exists.")

    #------------------------ Configuration Initialization ------------------------
    def loadConfig(self):
        # Load configuration settings from config.json
        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                config = json.load(f)
            print("Configuration loaded successfully.")
            return config
        else:
            print("config.json file does not exist. Initializing with default settings.")
            self.configJsonInit()
            return {
                "configVersion": "1.0.0",
                "regenerateCommonWord_one": "0",
                "regenerateAlreadyUsedNames_two": "0",
                "regenerateCommonWordAlreadyUsedName_three": "0",
                "regenerateInUseName": "0",
                "downloadCommonWords": "1",
                "downloadUsernames": "1",
                "debug": "0"
            }

# Run the application
if __name__ == "__main__":
    app = MainApp()
    print("Application has finished running.")