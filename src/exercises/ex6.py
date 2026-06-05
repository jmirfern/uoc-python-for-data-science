"""
Exercici 6: DataFrame summary_1995_2025. Podi.
"""

import matplotlib.pyplot as plt
import pandas as pd

import config


def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """Calcula el total de gols marcats com a local, visitant i el total combinat.

    Args:
        data: Dataset amb les columnes FTHG i FTAG.

    Returns:
        Tuple amb els gols de local, visitant i el total.
    """
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals
    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(
    data: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Calcula els gols totals acumulats per equip com a local, visitant i en total.

    Args:
        data: Dataset amb les columnes HomeTeam, AwayTeam, FTHG i FTAG.

    Returns:
        Tuple amb tres DataFrames:
        - home_goals_by_team: gols marcats com a local per equip.
        - away_goals_by_team: gols marcats com a visitant per equip.
        - total_goals_by_team: gols totals per equip.
    """
    home_goals_by_team = (
        data.groupby("HomeTeam")["FTHG"].sum().rename("home_goals").to_frame()
    )
    away_goals_by_team = (
        data.groupby("AwayTeam")["FTAG"].sum().rename("away_goals").to_frame()
    )
    total_goals_by_team = (
        home_goals_by_team["home_goals"]
        .add(away_goals_by_team["away_goals"], fill_value=0)
        .astype(int)
        .rename("total_goals")
        .to_frame()
    )
    total_goals_by_team = total_goals_by_team.sort_values(
        by="total_goals", ascending=False
    )

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(
    total_points: pd.DataFrame,
    home_goals_by_team: pd.DataFrame,
    away_goals_by_team: pd.DataFrame,
    total_goals_by_team: pd.DataFrame,
) -> pd.DataFrame:
    """Concatena els quatre dataframes per generar un summary històric per equip.

    Args:
        total_points: DataFrame o Series amb els punts totals per equip.
        home_goals_by_team: DataFrame amb els gols locals per equip.
        away_goals_by_team: DataFrame amb els gols visitants per equip.
        total_goals_by_team: DataFrame amb els gols totals per equip.

    Returns:
        DataFrame summary_1996_2025 amb les columnes total_points, home_goals,
        away_goals i total_goals.
    """
    if isinstance(total_points, pd.Series):
        total_points_df = total_points.rename("total_points").to_frame()
    else:
        total_points_df = total_points.copy()
        if "total_points" not in total_points_df.columns:
            total_points_df.columns = ["total_points"]

    summary_1996_2025 = pd.concat(
        [total_points_df, home_goals_by_team, away_goals_by_team, total_goals_by_team],
        axis=1,
    ).fillna(0)

    summary_1996_2025 = summary_1996_2025.astype(
        {
            "total_points": int,
            "home_goals": int,
            "away_goals": int,
            "total_goals": int,
        }
    )
    summary_1996_2025 = summary_1996_2025.sort_values(
        by="total_points", ascending=False
    )
    return summary_1996_2025


def podium(summary_1996_2025: pd.DataFrame) -> None:
    """Genera i desa una gràfica de podi amb els tres primers equips per punts totals.

    Args:
        summary_1996_2025: DataFrame amb la columna total_points.
    """
    top3 = summary_1996_2025.nlargest(3, "total_points")
    top3_ordered = top3.iloc[[1, 0, 2]]

    names = top3_ordered.index.tolist()
    values = top3_ordered["total_points"].tolist()
    colors = ["#C0C0C0", "#FFD700", "#CD7F32"]

    plt.style.use(config.PLOT_STYLE)
    fig, ax = plt.subplots(figsize=config.PLOT_FIGSIZE)

    bars = ax.bar(range(3), values, color=colors, width=0.6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    for idx, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(values) * 0.01,
            names[idx],
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    fig.suptitle("Podi històric 1995-2025", fontsize=14)
    plt.tight_layout()

    filename = config.FILENAME_FORMAT.format(
        ex_num=6,
        nom_alumne=config.nom_alumne,
        date_time=config.date_time,
    )
    filepath = config.IMG_DIR / filename
    plt.savefig(filepath, dpi=config.PLOT_DPI)
    plt.close()
