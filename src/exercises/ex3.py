"""
Exercici 3: Distribució de gols.
"""

import matplotlib.pyplot as plt
import pandas as pd

import config


def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Calcula la distribució de gols marcats a casa i fora.

    Args:
        data: Dataset amb les columnes FTHG i FTAG.

    Returns:
        Tuple amb dos dataframes:
        - distr_goals_home: índex = gols locals, columna = nombre de partits.
        - distr_goals_away: índex = gols visitants, columna = nombre de partits.
    """
    distr_goals_home = (
        data["FTHG"]
        .value_counts()
        .sort_index()
        .rename("matches_home")
        .to_frame()
    )
    distr_goals_away = (
        data["FTAG"]
        .value_counts()
        .sort_index()
        .rename("matches_away")
        .to_frame()
    )
    return distr_goals_home, distr_goals_away


def plot_goals_ditribution(
    distr_goals_home: pd.DataFrame, distr_goals_away: pd.DataFrame
) -> None:
    """Genera i desa una gràfica de la distribució de gols locals i visitants.

    Args:
        distr_goals_home: DataFrame amb la distribució de gols locals.
        distr_goals_away: DataFrame amb la distribució de gols visitants.
    """
    plt.style.use(config.PLOT_STYLE)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=config.PLOT_FIGSIZE, sharey=True)

    axes[0].bar(distr_goals_home.index, distr_goals_home["matches_home"], color="#1f77b4")
    axes[0].set_title("Distribució de gols locals")
    axes[0].set_xlabel("Gols marcats")
    axes[0].set_ylabel("Nombre de partits")

    axes[1].bar(distr_goals_away.index, distr_goals_away["matches_away"], color="#ff7f0e")
    axes[1].set_title("Distribució de gols visitants")
    axes[1].set_xlabel("Gols marcats")

    fig.suptitle("Distribució de gols marcats a casa i fora")
    plt.tight_layout()

    filename = config.FILENAME_FORMAT.format(
        ex_num=3,
        nom_alumne=config.nom_alumne,
        date_time=config.date_time,
    )
    filepath = config.IMG_DIR / filename
    plt.savefig(filepath, dpi=config.PLOT_DPI)
    plt.close()
