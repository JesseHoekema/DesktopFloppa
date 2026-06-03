import os
import zipfile
import requests
import shutil

# Configuratie
VERSION_URL = "https://raw.githubusercontent.com/JesseHoekema/DesktopFloppa/refs/heads/main/version.txt"
BASE_ZIP_URL = "https://github.com/JesseHoekema/DesktopFloppa/releases/download/{}/Desktop.Floppa.Install.zip"
ZIP_FILE = "Desktop Floppa Install.zip"
EXTRACT_FOLDER = "update"
APP_NAME = "Desktop Floppa.app"

def get_desktop_path():
    """Bepaal het bureaubladpad van de huidige gebruiker."""
    return os.path.join(os.path.expanduser("~"), "Desktop")

def get_latest_version():
    """Haalt de nieuwste versie op uit version.txt."""
    print("🔍 Ophalen van nieuwste versie...")
    response = requests.get(VERSION_URL)
    if response.status_code == 200:
        latest_version = response.text.strip()
        print(f"✅ Nieuwste versie: {latest_version}")
        return latest_version
    else:
        print("❌ Kon de versie niet ophalen!")
        exit(1)

def download_zip(version):
    """Downloadt het ZIP-bestand met de juiste versie."""
    zip_url = BASE_ZIP_URL.format(version)
    print(f"📥 Downloaden van {zip_url}...")
    
    response = requests.get(zip_url, stream=True)
    if response.status_code == 200:
        with open(ZIP_FILE, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print("✅ Download voltooid!")
    else:
        print("❌ Download mislukt!")
        exit(1)

def extract_zip():
    """Pak de ZIP uit en zoek naar Desktop Floppa.app."""
    print("📦 Uitpakken...")
    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)
    print("✅ Uitpakken voltooid!")

def find_floppa_app():
    """Zoek naar Desktop Floppa.app in de uitgepakte bestanden."""
    for root, dirs, files in os.walk(EXTRACT_FOLDER):
        if APP_NAME in dirs:
            return os.path.join(root, APP_NAME)
    return None

def move_floppa_app():
    """Verplaats Desktop Floppa.app naar de Desktop."""
    floppa_path = find_floppa_app()
    if floppa_path:
        desktop_path = get_desktop_path()
        destination = os.path.join(desktop_path, APP_NAME)

        # Verplaats de app naar het bureaublad
        shutil.move(floppa_path, destination)
        print(f"🚀 Floppa geïnstalleerd op: {destination}")
    else:
        print("❌ Fout: Desktop Floppa.app niet gevonden!")

def cleanup():
    """Verwijder tijdelijke bestanden."""
    os.remove(ZIP_FILE)
    shutil.rmtree(EXTRACT_FOLDER)
    print("🧹 Opruimen voltooid!")

def main():
    latest_version = get_latest_version()
    download_zip(latest_version)
    extract_zip()
    move_floppa_app()
    cleanup()

if __name__ == "__main__":
    main()
