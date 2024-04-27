"""
This module contains the logic to construct a networkx graph from the 
input data and calculate the metrics for each node in the graph.
"""

from typing import Dict, Any
from itertools import combinations
import networkx as nx  # type: ignore
from networkx.algorithms.cluster import clustering  # type: ignore
#from community import community_louvain  # type: ignore
from .models import GraphInput


def undirected_metrics(g: nx.Graph)->Dict[str, Any]:
    """
    This function calculates metrics for each node in the graph.
    """
    metrics = {
        "Degree Centrality": nx.degree_centrality(g),
        "Closeness Centrality": nx.closeness_centrality(g),
        "Betweenness Centrality": nx.betweenness_centrality(g),
        "Clustering Coefficient": clustering(g),
        "Eigenvector Centrality": nx.eigenvector_centrality(g),
    }
    return metrics

def construct_graph(data: GraphInput) -> Dict[str, Any]:
    """
    This function constructs a networkx graph from the input data and
    appends the calculated metrics for each node in the graph.
    """

    if data.directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    for node in data.nodes:
        g.add_node(node.id, label=node.label, **node.attributes)

    for edge in data.edges:
        g.add_edge(
            edge.source, edge.target, weight=edge.weight, label=edge.label
        )
    if data.associate is not None:
        for common_key, associates in data.associate.items():
            for pair in combinations(associates, 2):
                g.add_edge(pair[0], pair[1], weight=1, label=common_key)

    if not data.directed:
        metrics = undirected_metrics(g)
        for node_id, node_data in g.nodes(data=True):
            node_data.update({metric: values[node_id] for metric, values in metrics.items()})

    return nx.node_link_data(g)
