import os
import time
from pathlib import Path
import yt_dlp
from pystyle import *
import os
System.Title("ZWIX v2.0")
banner = """
 ▄▄▄▄▄▄     ▄ ▄   ▄█     ▄  
▀   ▄▄▀    █   █  ██ ▀▄   █ 
 ▄▀▀   ▄▀ █ ▄   █ ██   █ ▀  
 ▀▀▀▀▀▀   █  █  █ ▐█  ▄ █   
           █ █ █   ▐ █   ▀▄ 
            ▀ ▀       ▀     """
banner = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner))
def get_download_path():
    return str(Path.home() / "Desktop")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def download_video(url, format_choice):
    download_path = get_download_path()
    if format_choice == "mp4":
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',  # Cette option prend la meilleure vidéo et le meilleur audio
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'postprocessor_args': [
                '-c:v', 'copy',    # Copie la vidéo sans modification
                '-c:a', 'aac',     # Assure l'utilisation du codec audio aac (compatible avec mp4)
                '-strict', 'experimental'  # Nécessaire pour utiliser le codec aac
            ],
            'merge_output_format': 'mp4',  # Assure la fusion de la vidéo et de l'audio en un fichier mp4
        }
    elif format_choice == "mp3":
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'quiet': True,
            'no_warnings': True
        }
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, "Format invalide !"))
        time.sleep(3)
        clear_screen()
        main()
        return
    try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(Colorate.Horizontal(Colors.blue_to_cyan, "Done!"))
        time.sleep(3)
        clear_screen()
        main()
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid!"))
        time.sleep(3)
        clear_screen()
        main()
def main():
    print(banner)
    print(Center.XCenter("V2 | .gg/XJ48YQ9jvV"))
    print("")
    url = input(Colorate.Horizontal(Colors.blue_to_cyan, "URL > "))
    format_choice = input(Colorate.Horizontal(Colors.blue_to_cyan, "MP4 | MP3 > ")).strip().lower()
    download_video(url, format_choice)
if __name__ == "__main__":
    main()
