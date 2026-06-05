"""
Exercici 1: Càrrega del dataset i anàlisi exploratòria de les dades (EDA).
"""

from typing import Union

import matplotlib.pyplot as plt
import pandas as pd

import config


def load_and_eda(file: Union[str, object]) -> pd.DataFrame:
    """Carrega el dataset, elimina columnes del descans i mostra una EDA bàsica.

    Args:
        file: Ruta relativa o absoluta del fitxer CSV amb els resultats de LaLiga.

    Returns:
        Dataset carregat sense les columnes HTHG, HTAG i HTR.
    """
    data = pd.read_csv(file)
    data = data.drop(columns=["HTHG", "HTAG", "HTR"], errors="ignore")
    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """Genera i desa un boxplot dels gols locals i visitants.

    Args:
        data: Dataset de partits amb les columnes FTHG i FTAG.
    """
    plt.style.use(config.PLOT_STYLE)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=config.PLOT_FIGSIZE, sharey=True)

    axes[0].boxplot(data["FTHG"].dropna())
    axes[0].set_title("Gols equip local")
    axes[0].set_ylabel("Nombre de gols")

    axes[1].boxplot(data["FTAG"].dropna())
    axes[1].set_title("Gols equip visitant")
    axes[1].set_ylabel("Nombre de gols")

    fig.suptitle("Distribució de gols: local vs visitant")
    plt.tight_layout()

    filename = config.FILENAME_FORMAT.format(
        ex_num=1,
        nom_alumne=config.nom_alumne,
        date_time=config.date_time,
    )
    filepath = config.IMG_DIR / filename
    plt.savefig(filepath, dpi=config.PLOT_DPI)
    plt.close()
