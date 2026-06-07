"""
Configuració global per la PAC
Aquest fitxer emmagatzema totes les variables globals del projecte
"""

from datetime import datetime
from pathlib import Path

# Variables globals
nom_alumne = "Jonathan_Mir"
date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# Rutes de fitxers
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = (BASE_DIR / "." / "data" / "raw" / "").resolve()
DATA_FILE = DATA_DIR / "LaLiga_Matches.csv"
OUTPUT_PATH = (BASE_DIR / "." / "data" / "results").resolve()
IMG_PATH = (BASE_DIR / "." / "img").resolve()

# Rutes del projecte
PROJECT_DIR = BASE_DIR.parent
IMG_DIR = IMG_PATH
OUTPUT_DIR = OUTPUT_PATH

# Paràmetres de visualització
PLOT_FIGSIZE = (12, 6)
PLOT_DPI = 100
PLOT_STYLE = "seaborn-v0_8-darkgrid"

# Missatges i constants
PROJECT_NAME = "PAC4"

# Format de noms de fitxers per a les gràfiques
FILENAME_FORMAT = "grafica_ex{ex_num}_{nom_alumne}_{date_time}.png"
VERSION = "1.0"
