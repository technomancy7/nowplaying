# nowplaying
A simple python script to show your current playing media as a Discord.<br>
![2023-08-20_16-57](https://github.com/technomancy7/nowplaying/assets/34060097/279bdefd-a470-4bec-a2a1-dfdab9977c61)

Do you remember the old days of MSN, where you could have your status update with your current music?<br>
I'm trying to create the modern version of that for Discord.<br>

Thanks to the MPRIS (Media Player Remote Interfacing Specification) protocol, this script can read the current playing media from almost any source that the OS can detect, and using Discord RPC, we can connect that information to your client, without even needing access to your account, same way it detects verified games, just in this case, the "game" is a media player.

## Usage

```sh
usage: nowplaying.py [-h] [--delay DELAY] [--fmt FMT] [--player PLAYER] [--displayer DISPLAYER] [--icon ICON] [--client CLIENT]

options:
  -h, --help            show this help message and exit
  --delay DELAY         Delay value
  --fmt FMT             playerctl format string
  --player PLAYER       Player name to detect
  --displayer DISPLAYER
                        Player name to show to the client
  --icon ICON           Icon to use. [Currently supported: kde, firefox, chromium, vlc]
  --client CLIENT       Discord client ID

```

Delay is the number of seconds between calls to MPRIS, *not* Discord. Discord is updated whenever the script detects a change in MPRIS.<br>
Player is the ID of the player. You can list all available players by running `playerctl -l`.<br>
Client is the discord client ID of the app which is used to connect to their API. It uses mine by default, but you can change it to your own.<br>

## Requirements
- Probably only works on Linux, but I haven't tested on Windows as I don't have a Windows system.
- Needs Python to run it, and the pypresence library installed through pip.
- Also needs the `playerctl` binary available in PATH, which should be installable through the Linux package manager of your choice.
