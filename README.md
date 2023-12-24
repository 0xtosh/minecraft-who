# minecraft-who
See who is online on your Linux Minecraft server using a simple Python3 Flask API and web front-end.

# Installation prerequisites
- sudo apt install grep coreutils python3 python3-pip netcat
- pip3 install requests beautifulsoup4 Flask flask_cors APScheduler tailer

# Files
## Folder api/ 
Runs on your minecraft server, requires Python3. In this example http://minecraft.server:5000 will be used to run the API.

## Folder www/
Runs on a home webserver e.g. NAS that you can use around the house which fetches its data from http://minecraft.server:5000/current_players

# Configuration
- Set LOG_FILE_PATH to your "latest.log" Minecraft log file location
- Change the IP address and port in script.js (fetch('http://minecraft.server:5000/current_players')) and minecraft_whosonline.py if you are running both on the same server. Same for minecraft_whosonline_fakedata_tester.sh if you are using it for testing.

# Testing
Run the minecraft_whosonline_fakedata_tester.sh instead of the minecraft_whosonline.py script to simulate users on your server for testing.

# Credit
Fox image from: https://minecraft.fandom.com/
