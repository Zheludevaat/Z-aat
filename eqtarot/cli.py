import argparse

from .ingest import build_graph


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print Tarot knowledge graph")
    parser.parse_args(argv)

    graph = build_graph()
    print("Nodes:")
    for nid, data in graph.nodes(data=True):
        print(nid, data.get("name"))
    print("Edges:")
    for src, dst, data in graph.edges(data=True):
        print(src, dst, data["rtype"])


if __name__ == "__main__":
    main()
