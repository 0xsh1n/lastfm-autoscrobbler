import pylast
import json
import os
import sys
import time

W = '\033[0m'
R = '\x1b[38;5;196m'

def banner():
    print("""
\n
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣔⣾⣿⣿⡇⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⣿⣿⣿⣿⣿⣿⣧⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢿⣿⣾⣯⡶⠒⢾⡟⣿⡿⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⢀⣴⣿⡷⣻⣿⢷⡏⣴⢲⠀⣿⢸⡇⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠄⠒⠊⠉⠍⣉⣩⣭⣿⣿⡿⡿⠿⢾⣿⣿⣿⣗⢬⣥⣴⣿⣿⡇⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠁⠀⠀⢀⣤⣶⣾⠟⠛⠉⠁⠁⣀⡀⠀⠀⣀⠈⠙⠢⢿⣿⣿⣿⣿⠁⠀⠀
\t⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣠⣔⣡⣤⣤⣤⣤⣶⡿⠋⢁⡠⠄⠒⠊⠉⠁⠀⠉⠙⠻⢿⣾⣷⣦⣤⣽⣿⣿⡿⠀⠀⠀
\t⢀⣤⣶⡾⣿⣽⣿⠖⠒⠛⣻⣟⣿⣛⣿⣿⡿⢟⣡⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣯⣸⣿⠀⠀⠀
\t⠸⣿⣿⣿⣿⣇⣿⠾⠋⠩⣿⡿⣿⣿⣿⢟⣵⠗⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣇⠀⠀
\t⠀⠹⣿⣿⣿⢹⡏⢼⣛⠆⢸⡇⣿⡟⢡⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⣿⡀⠀
\t⠀⠀⠈⢿⣿⣜⢾⣤⣤⣴⣿⣿⡿⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⡿⣇⠀
\t⠀⠀⠀⠀⠙⣿⣷⣿⣿⣿⣿⣿⠁⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣷⣮⣿⣿⣿⣸⠟⠀
\t⠀⠀⠀⠀⠀⠈⠹⣿⡿⣿⣿⣧⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⢿⣗⠚⡿⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⡀⣷⡀     LASTFM AUTO SCROBBLER
\t⠀⠀⠀⠀⠀⠀⠀⢻⣿⣶⣧⣿⠀⠀⣠⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡇⢳⢣         MADE BY 0XSH1N
\t⠀⠀⠀⠀⠀⠀⠀⢹⣿⣯⡟⢻⣆⣼⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠃⡞⢸
\t⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡏⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣾⠀⡇⣼
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣯⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⢸⣯⣿⣿⣿⣿⣿⣷⣶⣿⣿⣹⠙⡟⢠⠃
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠛⢛⡻⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣷⡄⣿⣿⣿⣿⡿⠋⢹⣿⣿⣫⢃⣴⠕⠃⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⡀⠈⠉⠛⢿⣿⣿⣿⣿⣿⡷⣭⡻⣿⣿⣿⠈⠻⢿⣿⣧⣾⣿⡿⠗⠓⠛⠁⠀⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⡂⢀⡀⠀⠈⢝⡂⠀⠉⠻⣿⡛⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢦⡈⠂⠀⠀⠉⠢⢄⠈⣸⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠢⠴⢦⣄⡠⠟⠁⠀⠀⠀⠀⠀⠀⠀
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")


def load_config():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'config.json')
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def authenticate_lastfm(api_key, api_secret, username, password):
    try:
        return pylast.LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret,
            username=username,
            password_hash=pylast.md5(password)
        )
    except pylast.WSError as e:
        
        return None

def scrobble_track(network, artist, track, album, limit, interval):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    try:
        scrobbles = 0
        while scrobbles < limit:
            network.scrobble(artist=artist, title=track, timestamp=int(time.time()), album=album)
            print(f'\r        Scrobbling {track} by {artist} {scrobbles+1}/{limit}', end='', flush=True)
            scrobbles += 1
            time.sleep(interval)

        print(f"\n        Successfully scrobbled {scrobbles} tracks\n\n")
        sys.exit()
    
    except KeyboardInterrupt:
         os.system('cls' if os.name == 'nt' else 'clear')
         sys.exit()


def menu(network, artist, track, album, limit, interval):
    
    print("        1. Start")
    print("        2. Exit")
    choice = input("\n       [?] 0xsh1n: ")
    if choice == '1':
        scrobble_track(network, artist, track, album, limit, interval)
    if choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
        
    else:
        print("\n" + R + "  Error" + W + ": Invalid choice. Please enter a valid option.")
        time.sleep(2)
        main()
def main():
    config = load_config()
    api_key = config['API_KEY']
    api_secret = config['API_SECRET']
    username = config['LASTFM_USERNAME']
    password = config['LASTFM_PASSWORD']
    artist = config['ARTIST']
    track = config['TRACK']
    album = config['ALBUM']
    limit = config['LIMIT']
    interval = config['INTERVAL']

    network = authenticate_lastfm(api_key, api_secret, username, password)

    if network is not None:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        menu(network, artist, track, album, limit, interval)
    else:
        print(f"{R}  Error{W}: login failed. Please check your username and password.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
           
if __name__ == "__main__":
    main()
    