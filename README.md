# nowplaying
A simple python script to show your current playing media as a Discord.
![2023-08-20_16-57](https://github.com/technomancy7/nowplaying/assets/34060097/279bdefd-a470-4bec-a2a1-dfdab9977c61)

Do you remember the old days of MSN, where you could have your status update with your current music?
I'm trying to create the modern version of that for Discord.

Thanks to the MPRIS (Media Player Remote Interfacing Specification) protocol, this script can read the current playing media from almost any source that the OS can detect, and using Discord RPC, we can connect that information to your client, without even needing access to your account, same way it detects verified games, just in this case, the "game" is a media player.

## Usage

```sh
python3 nowplaying.py [--delay DELAY] [--player PLAYER] [--client CLIENT]
```

Delay is the number of seconds between calls to MPRIS, *not* Discord. Discord is updated whenever the script detects a change in MPRIS.
Player is the ID of the player. You can list all available players by running `playerctl -l`.
Client is the discord client ID of the app which is used to connect to their API. It uses mine by default, but you can change it to your own.
