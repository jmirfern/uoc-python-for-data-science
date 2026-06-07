"""
Exercici 7: Gràfic de connexions entre equips.
"""

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

import config


def graf(data: pd.DataFrame, selected_teams: list[str]) -> None:
    """Genera i desa un gràfic de connexions entre els equips seleccionats.

    Args:
        data: Dataset amb les columnes HomeTeam i AwayTeam.
        selected_teams: Llista dels equips seleccionats per al gràfic.
    """
    data_filtered = data[
        data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)
    ].copy()

    data_filtered["pair"] = data_filtered.apply(
        lambda row: tuple(sorted([row["HomeTeam"], row["AwayTeam"]])), axis=1
    )
    edge_counts = data_filtered["pair"].value_counts().to_dict()

    graph = nx.Graph()
    graph.add_nodes_from(selected_teams)
    for (team1, team2), weight in edge_counts.items():
        graph.add_edge(team1, team2, weight=weight)

    pos = nx.spring_layout(graph, seed=42, k=0.6)

    plt.style.use(config.PLOT_STYLE)
    fig, ax = plt.subplots(figsize=config.PLOT_FIGSIZE)

    nx.draw_networkx_nodes(graph, pos, node_color="#1f77b4", node_size=1000, ax=ax)
    nx.draw_networkx_edges(
        graph,
        pos,
        width=[
            max(1, weight * 0.2)
            for weight in nx.get_edge_attributes(graph, "weight").values()
        ],
        ax=ax,
    )
    nx.draw_networkx_labels(graph, pos, font_size=10, ax=ax)

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8, ax=ax)

    ax.set_title("Gràfic de connexions entre els 5 millors equips")
    ax.set_axis_off()

    plt.tight_layout()

    filename = config.FILENAME_FORMAT.format(
        ex_num=7,
        nom_alumne=config.nom_alumne,
        date_time=config.date_time,
    )
    filepath = config.IMG_DIR / filename
    plt.savefig(filepath, dpi=config.PLOT_DPI)
    plt.close(fig)
