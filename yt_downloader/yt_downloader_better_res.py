# import yt_dlp

# url = input("Enter video URL you want to be downloaded: ")

# ydl_opts = {
#     # Magia dzieje się tutaj: pobierz najlepszy obraz i najlepszy dźwięk, a potem je połącz
#     'format': 'bestvideo+bestaudio/best', 
#     # Nazwij plik na podstawie tytułu i zachowaj oryginalne rozszerzenie
#     'outtmpl': '%(title)s.%(ext)s',       
# }

# print("Rozpoczynam pobieranie... (łączenie wysokiej jakości może chwilę potrwać)")

# try:
#     # Uruchamiamy yt-dlp z naszymi opcjami
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     print("Pobieranie zakończone sukcesem!")
# except Exception as e:
#     print(f"Wystąpił błąd: {e}")


import yt_dlp
import os

# 1. Tworzymy naszą własną, prostą funkcję (ukrywamy w niej skomplikowany kod yt-dlp)
def pobierz_wideo_z_youtube(url, folder_docelowy):
    
    # Konfiguracja maszyny yt-dlp
    opcje = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        
        # TUTAJ USTWIAMY MIEJSCE DOCELOWE:
        'paths': {'home': folder_docelowy}
    }

    print("\nRozpoczynam pobieranie...")
    print(f"Plik trafi do folderu: {folder_docelowy}")

    try:
        # Odpalamy maszynę z naszymi ustawieniami
        with yt_dlp.YoutubeDL(opcje) as ydl:
            ydl.download([url])
        print("\nSukces! Pobieranie zakończone.")
        
    except Exception as e:
        print(f"\nCoś poszło nie tak: {e}")

# =====================================================================
# 2. GŁÓWNA (LUDZKA) CZĘŚĆ PROGRAMU
# =====================================================================

# Zapytaj użytkownika o link
link = input("Podaj link do wideo z YouTube: ")

# Zdefiniuj gdzie chcesz to pobrać (użyj 'r' przed cudzysłowem dla ścieżek Windows!)
moj_folder = "C:\\Users\\bkozi\\Desktop\\Nauka\\PYTHON BARTEK\\yt_downloader\\Pobrane filmy"

# Upewniamy się, że folder istnieje (jeśli nie, Python sam go stworzy)
os.makedirs(moj_folder, exist_ok=True)

# Wywołaj naszą prostą funkcję
pobierz_wideo_z_youtube(link, moj_folder)