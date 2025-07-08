import csv
import json
from pathlib import Path

import networkx as nx

from .model import Card, Motif

DATA_DIR = Path(__file__).resolve().parent / "data"


def build_graph(data_dir: Path = DATA_DIR) -> nx.MultiDiGraph:
    """Load cards, motifs and links from data files into a MultiDiGraph."""
    graph = nx.MultiDiGraph()

    cards_path = data_dir / "brain.json"
    with cards_path.open("r", encoding="utf-8") as f:
        cards = [Card(**c) for c in json.load(f)]
    for card in cards:
        graph.add_node(card.id, **card.__dict__)

    motifs_path = data_dir / "motifs.csv"
    motifs = {}
    if motifs_path.exists():
        with motifs_path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                motifs[row["code"]] = Motif(code=row["code"], description=row["description"])

    links_path = data_dir / "links.csv"
    with links_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            src = int(row["src"])
            dst = int(row["dst"])
            rtype = row["type"]
            graph.add_edge(src, dst, rtype=rtype)

    graph.graph["motifs"] = motifs
    return graph
