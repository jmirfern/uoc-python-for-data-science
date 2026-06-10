#!/usr/bin/env python3
"""
PAC4 - LaLiga Data Analysis Project
Punt d'entrada principal de l'aplicació.

Permet executar els exercicis de forma seqüencial mitjançant arguments de línia de comandes..
"""

import argparse
import sys
import traceback

from IPython.display import display

import config
from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7


def print_header(num_exercise: int) -> None:
    """Imprimeix una capçalera formatada per a cada exercici.

    Args:
        num_exercise: Número de l'exercici que s'ha d'executar.
    """
    print(f"\n{'='*70}")
    print(f"EXERCICI {num_exercise}")
    print(f"{'='*70}\n")


def execute_exercise_1() -> dict:
    """Executa l'exercici 1: Càrrega i EDA.

    Returns:
        Diccionari amb les dades necessàries per a exercicis posteriors.
    """
    print_header(1)
    print("Carregant el dataset i realitzant l'anàlisi exploratòria...")

    data = ex1.load_and_eda(config.DATA_FILE)

    print("\nPrimers valors del dataset:")
    display(data.head())

    print("\nÚltims valors del dataset:")
    display(data.tail())

    print("\nInformació del dataset:")
    data.info()

    print("\nResum estadístic de les variables numèriques:")
    display(data.describe())

    print("\nValors nuls per columna:")
    display(data.isnull().sum())

    print("\nGenerant la gràfica de distribució de gols...")
    ex1.plot_home_away_goals(data)

    return {"data": data}


def execute_exercise_2(context: dict) -> dict:
    """Executa l'exercici 2: Partits totals per equip.

    Args:
        context: Diccionari amb el context d'exercicis anteriors.

    Returns:
        Diccionari actualitzat amb noves dades.
    """
    print_header(2)
    data = context["data"]

    print("Calculant partits totals per equip...")
    matches_team_total = ex2.total_matches(data)

    print("\nPrimers 10 equips per partits totals:")
    display(matches_team_total.head(10))

    max_matches = matches_team_total["matches_total"].max()
    teams_always_in_first_division = matches_team_total[
        matches_team_total["matches_total"] == max_matches
    ]
    print("\nEquips amb el nombre màxim de partits (sempre a primera divisió):")
    display(teams_always_in_first_division)

    print("\nGenerant la gràfica de partits totals...")
    ex2.plot_matches_team_total(matches_team_total)

    context["matches_team_total"] = matches_team_total
    context["max_matches"] = max_matches
    context["teams_always_in_first_division"] = teams_always_in_first_division
    return context


def execute_exercise_3(context: dict) -> dict:
    """Executa l'exercici 3: Distribució de gols.

    Args:
        context: Diccionari amb el context d'exercicis anteriors.

    Returns:
        Diccionari actualitzat amb noves dades.
    """
    print_header(3)
    data = context["data"]

    print("Calculant la distribució de gols...")
    distr_goals_home, distr_goals_away = ex3.goals_distribution(data)

    print("\nDistribució de gols locals:")
    display(distr_goals_home)

    print("\nDistribució de gols visitants:")
    display(distr_goals_away)

    print("\nGenerant la gràfica de distribució...")
    ex3.plot_goals_ditribution(distr_goals_home, distr_goals_away)

    context["distr_goals_home"] = distr_goals_home
    context["distr_goals_away"] = distr_goals_away
    return context


def execute_exercise_4(context: dict) -> dict:
    """Executa l'exercici 4: Partits guanyats pels locals/visitants.

    Args:
        context: Diccionari amb el context d'exercicis anteriors.

    Returns:
        Diccionari actualitzat amb noves dades.
    """
    print_header(4)
    data = context["data"]

    print("Calculant resultats FTR...")
    ftr = ex4.FTR(data)

    print("\nDistribució de resultats FTR:")
    display(ftr)

    home_win_percentage = (ftr.loc["H", "matches"] / ftr["matches"].sum()) * 100
    print(f"\nPercentatge de partits guanyats pels equips locals: {home_win_percentage:.2f}%")

    print("\nGenerant la gràfica de resultats...")
    ex4.plot_FTR(ftr)

    context["ftr"] = ftr
    context["home_win_percentage"] = home_win_percentage
    return context


def execute_exercise_5(context: dict) -> dict:
    """Executa l'exercici 5: Classificació global.

    Args:
        context: Diccionari amb el context d'exercicis anteriors.

    Returns:
        Diccionari actualitzat amb noves dades.
    """
    print_header(5)
    data = context["data"]

    print("Afegint punts al dataset...")
    data = ex5.add_points(data)

    print("\nPrimers 10 registres amb punts:")
    display(data.head(10))

    print("\nCalculant punts totals acumulats...")
    total_points_by_team, df_total_points_by_team = ex5.fun_total_points(data)

    print("\nTop 10 equips per punts totals acumulats:")
    display(df_total_points_by_team.head(10))

    winner = ex5.alltime_winner(df_total_points_by_team)
    print(f"\nGuanyador històric acumulat: {winner}")

    context["data"] = data
    context["total_points_by_team"] = total_points_by_team
    context["df_total_points_by_team"] = df_total_points_by_team
    context["winner"] = winner
    return context


def execute_exercise_6(context: dict) -> dict:
    """Executa l'exercici 6: Summary i Podi.

    Args:
        context: Diccionari amb el context d'exercicis anteriors.

    Returns:
        Diccionari actualitzat amb noves dades.
    """
    print_header(6)
    data = context["data"]

    print("Calculant gols totals...")
    home_goals, away_goals, total_goals = ex6.fun_total_goals(data)

    print(
        "Total de gols marcats:\n"
        f"- Gols locals: {home_goals}\n"
        f"- Gols visitants: {away_goals}\n"
        f"- Gols totals: {total_goals}"
    )

    print("\nCalculant gols per equip...")
    home_goals_by_team, away_goals_by_team, total_goals_by_team = ex6.fun_total_goals_by_team(data)

    print("\nTop 10 equips per gols totals acumulats:")
    display(total_goals_by_team.head(10))

    print("\nGenerant resum 1995-2025...")
    summary_1996_2025 = ex6.fun_summary_1996_2025(
        context["df_total_points_by_team"],
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team,
    )

    print("\nPrimeres files del resum:")
    display(summary_1996_2025.head())

    print("\nGenerant la gràfica del podi...")
    ex6.podium(summary_1996_2025)

    context["home_goals"] = home_goals
    context["away_goals"] = away_goals
    context["total_goals"] = total_goals
    context["home_goals_by_team"] = home_goals_by_team
    context["away_goals_by_team"] = away_goals_by_team
    context["total_goals_by_team"] = total_goals_by_team
    context["summary_1996_2025"] = summary_1996_2025
    return context


def execute_exercise_7(context: dict) -> dict:
    """Executa l'exercici 7: Gràfic de connexions.

    Args:
        context: Diccionari amb el context d'exercicis anteriors.

    Returns:
        Diccionari actualitzat amb noves dades.
    """
    print_header(7)
    data = context["data"]

    print("Obtenint el top 5 d'equips per punts acumulats...")
    selected_teams = context["total_points_by_team"].head(5).index.tolist()
    print(f"Equips seleccionats: {selected_teams}")

    print("\nGenerant el gràfic de connexions...")
    ex7.graf(data, selected_teams)

    context["selected_teams"] = selected_teams
    return context


def main() -> None:
    """Funció principal que gestiona els arguments de línia de comandes i executa els exercicis"""
    parser = argparse.ArgumentParser(
        description="PAC4 - LaLiga Data Analysis Project (1995-2025)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'ús:
  python main.py -ex 1       # Executa només l'exercici 1
  python main.py -ex 5       # Executa els exercicis 1-5
  python main.py -ex 7       # Executa tots els exercicis (1-7)
  python main.py --help      # Mostra aquesta ajuda
        """
    )

    parser.add_argument(
        "-ex", "--exercise",
        type=int,
        choices=[1, 2, 3, 4, 5, 6, 7],
        default=7,
        help=(
            "Número de l'exercici que s'ha d'executar "
            "(executa tots fins a aquest número). Per defecte: 7"
        ),
    )

    args = parser.parse_args()

    print(f"\n{'='*70}")
    print("PAC4 - LaLiga Data Analysis Project (1995-2025)")
    print(f"Alumne: {config.nom_alumne}")
    print(f"{'='*70}")

    # Diccionari per mantenir el context entre exercicis
    context = {}

    # Executar exercicis fins al número especificat
    try:
        for ex_num in range(1, args.exercise + 1):
            if ex_num == 1:
                context = execute_exercise_1()
            else:
                # Diccionari de funcions per a exercicis posteriors
                exercises_functions = {
                    2: execute_exercise_2,
                    3: execute_exercise_3,
                    4: execute_exercise_4,
                    5: execute_exercise_5,
                    6: execute_exercise_6,
                    7: execute_exercise_7,
                }
                context = exercises_functions[ex_num](context)
    except Exception as e:
        print(f"\n❌ Error en l'exercici {ex_num}: {e}")
        traceback.print_exc()
        sys.exit(1)

    print(f"\n{'='*70}")
    print("✅ Tots els exercicis s'han completat correctament!")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
