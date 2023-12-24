import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import tailer
import subprocess

app = Flask(__name__)
CORS(app)
LOG_FILE_PATH = '/usr/minecraft/logs/latest.log'
current_players = set()

def get_current_players():
    global current_players
    print("Updating current players...")  # Debugging statement
    command = f"grep -iE 'joined the game|left the game' {LOG_FILE_PATH} "
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()

    if err:
        print("Error executing grep: ", err)
        return

    temp_players = set()
    for line in out.decode('utf-8').split('\n'):
        if 'joined the game' in line.lower():
            player_name = line.split(']: ')[1].split(' joined the game')[0]
            if player_name not in temp_players:
                print(f"{player_name} has joined.")  # Debugging statement
                temp_players.add(player_name)
        elif 'left the game' in line.lower():
            player_name = line.split(']: ')[1].split(' left the game')[0]
            if player_name in temp_players:
                print(f"{player_name} has left.")  # Debugging statement
                temp_players.discard(player_name)

    current_players = temp_players
    if current_players:
        print(f"Current Players: {current_players}")  # Debugging statement
        return current_players
    else:
        return ""
    

@app.route('/current_players', methods=['GET'])
def current_players_endpoint():
    try:
        return jsonify({'players': list(get_current_players())}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

