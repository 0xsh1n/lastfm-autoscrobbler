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
    except pylast.WSError:
        return None

def scrobble_track(network, *scrob_params_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()

    try:
        while True:
            for current_params, next_params, scrob_type in scrob_params_list:

                details_line = f' Track: {current_params["TRACK"]} | Artist: {current_params["ARTIST"]} | Album: {current_params["ALBUM"]}'
                details_line = f'       {details_line}'
                print(details_line)

            
                network.scrobble(artist=current_params['ARTIST'], title=current_params['TRACK'],
                                 timestamp=int(time.time()), album=current_params['ALBUM'])
                time.sleep(2)
            

        

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    
        
    except pylast.NetworkError:
        scrobble_track(network, *scrob_params_list)


def menu(network, *scrob_params_list):
    banner()
    print("        1. Start")
    print("        2. Exit")
    choice = input("\n       [?] 0xsh1n: ")
    if choice == '1':
        scrobble_track(network, *scrob_params_list)
    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    else:
        print("\n" + R + "  Error" + W + ": Invalid choice. Please enter a valid option.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(network, *scrob_params_list)

def main():
    config = load_config()
    api_key = config['API_KEY']
    api_secret = config['API_SECRET']
    username = config['LASTFM_USERNAME']
    password = config['LASTFM_PASSWORD']
    

    scrob_params_list = [
        (config[f'SCROB{i}'], config[f'SCROB{(i % 9) + 1}'], f"Scrob{i}") for i in range(1, 10)
    ]

    network = authenticate_lastfm(api_key, api_secret, username, password)

    if network is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(network, *scrob_params_list)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{R}  Error{W}: login failed. Please check your credentials ")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
    