from pypresence import Presence
import time
import sys, os, subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--delay', type=int, default=5, help='Delay value')
parser.add_argument('--player', type=str, default="firefox", help='Player name to detect')
parser.add_argument('--client', type=int, default=0, help='Discord client ID')
args = parser.parse_args()
delay = args.delay
player = args.player
client_id = args.client

print(f"Connecting to discord via {client_id} / DELAY {delay} / PLAYER {player}")
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

last_details = ""

while True: 
    details = ""
    
    try:
        output = subprocess.check_output(["playerctl", "metadata", "--format", "{{artist}} - {{title}}", "-p", player])
        details = output.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        details = "No media playing"
        
    if details != last_details:
        d = RPC.update(state=f"Playing in {player}", details=f"🎵 {details}")
        update = d['data']
        print(f"state update @ {update['name']}: {update['state']} / {update['details']}")
        last_details = details
        
    time.sleep(delay)
