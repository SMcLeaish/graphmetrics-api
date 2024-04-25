"""
This module contains the graph construction and metrics calculation 
functions.
"""

from typing import Dict, Any
import networkx as nx # type: ignore
from networkx.algorithms.cluster import clustering # type: ignore
from community import community_louvain as community # type: ignore
from .models import GraphInput


def calculate_metrics(g: nx.Graph) -> Dict[str, Any]:
    """
    Calculate various network metrics for the given graph.

    Args:
    g (nx.Graph): The networkx graph object.

    Returns:
    Dict[str, Any]: A dictionary containing network metrics.
    """
    metrics = {
        "degreeCentrality": nx.degree_centrality(g),
        "closenessCentrality": nx.closeness_centrality(g),
        "betweennessCentrality": nx.betweenness_centrality(g),
        "clusteringCoefficient": clustering(g),
        "community": community.best_partition(g),
    }
    return metrics


def construct_graph(data: GraphInput) -> Dict[str, Any]:
    """
    Construct a graph from given data using Pydantic models for nodes
    and edges.

    Args:
    data (GraphInput): The input data containing nodes and edges.

    Returns:
    Dict[str, Any]: A serialized graph that includes nodes with their
    metrics.
    """

    g = nx.DiGraph() if data.directed else nx.Graph()
    if data.transform:
        for project, investors in data.transform.items():
            for i, investor in enumerate(investors):
                for second_investor in enumerate(investors[i+1:], start=i+1):
                    g.add_edge(investor, second_investor, project=project)
    else:
        for node in data.nodes:
            g.add_node(node.id, label=node.label, **node.attributes)
        for edge in data.edges:
            g.add_edge(edge.source, edge.target, weight=edge.weight)

    metrics = calculate_metrics(g)
    for node_id in g.nodes():
        g.nodes[node_id].update({metric: values[node_id] for metric, values in metrics.items()})

    return nx.node_link_data(g)
