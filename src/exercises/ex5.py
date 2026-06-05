"""
Exercici 5: Classificació global 1995-2025.
"""

import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """Afegeix els punts guanyats com a local i com a visitant.

    Args:
        data: Dataset amb la columna FTR.

    Returns:
        DataFrame amb les columnes points_home i points_away.
    """
    data = data.copy()

    data["points_home"] = data["FTR"].map({"H": 3, "D": 1, "A": 0}).fillna(0).astype(int)
    data["points_away"] = data["FTR"].map({"H": 0, "D": 1, "A": 3}).fillna(0).astype(int)

    return data


def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """Calcula els punts totals acumulats per cada equip.

    Args:
        data: Dataset amb les columnes HomeTeam, AwayTeam, points_home, points_away.

    Returns:
        Tuple amb una Series i un DataFrame amb els punts totals per equip.
    """
    home_points = data.groupby("HomeTeam")["points_home"].sum()
    away_points = data.groupby("AwayTeam")["points_away"].sum()

    total_points_by_team = home_points.add(away_points, fill_value=0).astype(int)
    total_points_by_team = total_points_by_team.sort_values(ascending=False)

    df_total_points_by_team = total_points_by_team.to_frame("total_points")

    return total_points_by_team, df_total_points_by_team


def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """Retorna l'equip que ha acumulat més punts a la classificació històrica.

    Args:
        df_total_points: DataFrame amb la columna total_points o una Series equivalent.

    Returns:
        Nom de l'equip guanyador històric.
    """
    if isinstance(df_total_points, pd.DataFrame):
        if "total_points" in df_total_points.columns:
            total_points = df_total_points["total_points"]
        else:
            total_points = df_total_points.iloc[:, 0]
    else:
        total_points = df_total_points

    return total_points.idxmax()
