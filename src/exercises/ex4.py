"""
Exercici 4: Partits guanyats a casa/fora.
"""

import matplotlib.pyplot as plt
import pandas as pd

import config


def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula el nombre de partits guanyats pels locals, visitants i empatats.

    Args:
        data: Dataset amb la columna FTR.

    Returns:
        DataFrame amb l'índex H (locals), A (visitants), D (empatats)
        i la columna matches.
    """
    ftr = (
        data["FTR"]
        .value_counts()
        .reindex(["H", "A", "D"], fill_value=0)
        .rename("matches")
        .to_frame()
    )
    return ftr


def plot_FTR(ftr: pd.DataFrame) -> None:
    """Genera i desa una gràfica del resultat dels partits.

    Args:
        ftr: DataFrame amb la distribució de resultats FTR.
    """
    plt.style.use(config.PLOT_STYLE)
    fig, ax = plt.subplots(figsize=config.PLOT_FIGSIZE)

    ax.bar(ftr.index, ftr["matches"], color=["#1f77b4", "#ff7f0e", "#2ca02c"])
    ax.set_title("Resultats finals dels partits (FTR)")
    ax.set_xlabel("Resultat")
    ax.set_ylabel("Nombre de partits")

    for idx, value in enumerate(ftr["matches"]):
        ax.text(idx, value + value * 0.01, str(value), ha="center", va="bottom")

    plt.tight_layout()

    filename = config.FILENAME_FORMAT.format(
        ex_num=4,
        nom_alumne=config.nom_alumne,
        date_time=config.date_time,
    )
    filepath = config.IMG_DIR / filename
    plt.savefig(filepath, dpi=config.PLOT_DPI)
    plt.close()
