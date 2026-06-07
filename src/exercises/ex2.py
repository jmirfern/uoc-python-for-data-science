"""
Exercici 2: Partits totals jugats per equip.
"""

import matplotlib.pyplot as plt
import pandas as pd

import config


def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula el nombre total de partits jugats per cada equip.

    Args:
        data: Dataset de partits amb les columnes HomeTeam i AwayTeam.

    Returns:
        DataFrame amb l'índex dels equips i la columna matches_total.
    """
    home_counts = data["HomeTeam"].value_counts()
    away_counts = data["AwayTeam"].value_counts()

    matches_team_total = pd.concat([home_counts, away_counts], axis=1).fillna(0)
    matches_team_total["matches_total"] = matches_team_total.sum(axis=1).astype(int)
    matches_team_total = matches_team_total[["matches_total"]].sort_values(
        by="matches_total", ascending=False
    )

    return matches_team_total


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """Genera i desa una gràfica del nombre total de partits per equip.

    Args:
        matches_team_total: DataFrame amb la columna matches_total.
    """
    plt.style.use(config.PLOT_STYLE)
    fig, ax = plt.subplots(figsize=config.PLOT_FIGSIZE)

    ax.bar(matches_team_total.index, matches_team_total["matches_total"])
    ax.set_title("Nombre total de partits jugats per equip")
    ax.set_xlabel("Equip")
    ax.set_ylabel("Partits totals")
    ax.tick_params(axis="x", rotation=90)

    plt.tight_layout()

    filename = config.FILENAME_FORMAT.format(
        ex_num=2,
        nom_alumne=config.nom_alumne,
        date_time=config.date_time,
    )
    filepath = config.IMG_DIR / filename
    plt.savefig(filepath, dpi=config.PLOT_DPI)
    plt.close(fig)
