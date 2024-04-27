"""
This module contains the node and edge classes for the graph.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class Node(BaseModel):
    """
    Defines the node class
    """

    id: str 
    label: Optional[str] = None
    attributes: Dict[str, Any] = {}


class Edge(BaseModel):
    """
    Defines the edge class
    """

    source: str
    target: str
    label: Optional[str] = None
    weight: Optional[float] = 1.0


class GraphInput(BaseModel):
    """
    Defines the input graph class
    """

    nodes: Optional[List[Node]] = []
    edges: List[Edge]
    directed: bool = False
    associate: Optional[Dict[str, List[str]]] = None
