import os
import eel

from engine.features import *
from engine.command import *

def start():
    # Inisialisasi Eel dengan folder 'www' sebagai root directory
    eel.init("www")

    # Memutar suara asisten
    playAssistantSound()

    # Path ke executable Chrome, sesuaikan dengan sistem Anda
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    
    # Membuka Chrome dalam mode aplikasi
    os.system(f'start {chrome_path} --app="http://127.0.0.1:5500/www/index.html"')

    # Memulai Eel
    eel.start('index.html', mode=None, host='localhost', block=True)
