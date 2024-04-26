from typing import Dict, Any
import networkx as nx
from networkx.algorithms.cluster import clustering
from community import community_louvain
from .models import GraphInput  

def calculate_metrics(g: nx.Graph) -> Dict[str, Any]:
    return {
        "degreeCentrality": nx.degree_centrality(g),
        "closenessCentrality": nx.closeness_centrality(g),
        "betweennessCentrality": nx.betweenness_centrality(g),
        "clusteringCoefficient": clustering(g),
        "community": community_louvain.best_partition(g),
    }

def construct_graph(data: GraphInput) -> Dict[str, Any]:
    g = nx.Graph()
    for node in data.nodes:
        g.add_node(node.id, label=node.label, **node.attributes)

    for edge in data.edges:
        g.add_edge(edge.source, edge.target, weight=edge.weight, label=edge.label)

    metrics = calculate_metrics(g)
    for node_id in g.nodes():
        g.nodes[node_id].update({
            'metrics': {metric: values[node_id] for metric, values in metrics.items()}
        })

    return nx.node_link_data(g)

