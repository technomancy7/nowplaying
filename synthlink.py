from pypresence import Presence
import time
import sys, os, subprocess
import argparse

def notify(title, text):
    cmd = f'notify-send --app-name=Athena "{title}" "{text}"'
    os.system(cmd)

parser = argparse.ArgumentParser()
parser.add_argument('--delay', type=int, default=5, help='Delay value')
parser.add_argument('--fmt', type=str, default="{{artist}} - {{title}}", help='playerctl format string')
parser.add_argument('--player', type=str, default="firefox", help='Player name to detect')
parser.add_argument('--displayer', type=str, default="", help='Player name to show to the client')
parser.add_argument('--icon', type=str, default="kde", help='Icon to use. [Currently supported: kde, firefox, chromium, vlc]')
parser.add_argument('--client', type=int, default=1142046335017685072, help='Discord client ID')

args = parser.parse_args()
delay = args.delay
player = args.player
displayer = args.displayer or args.player
icon = args.icon
fmt = args.fmt
client_id = args.client

print(f"Connecting to discord via {client_id} / DELAY {delay} / PLAYER {player} ({displayer}) / ICON {icon} / FMT {fmt}")
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
notify("Status update", f"Connected to Discord RPC.")
last_details = ""

while True:
    details = ""

    try:
        output = subprocess.check_output(["playerctl", "metadata", "--format", fmt, "-p", player])
        details = output.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        details = "No media playing"

    if details != last_details:
        d = RPC.update(state=f"Playing in {displayer}", details=f"{details}", large_image="infinity-transparent", large_text="Designed by @_technomancer",  small_image=icon, small_text=displayer, start=time.time(), buttons=[{"label": "Source", "url": "https://github.com/technomancy7/synthlink"}])
        update = d['data']
        print(f"state update @ {update['name']}: {update['state']} / {update['details']}")
        last_details = details
        notify("Status update", f"{update['name']}: {update['state']} / {update['details']}")
    time.sleep(delay)
