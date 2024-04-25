"""
This module contains the FastAPI application that serves as the API
endpoint for the graph construction and metrics calculation.
"""
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .models import GraphInput
from .graph import construct_graph

app = FastAPI()

# Figure out how we need to lock this down

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create-graph/")
async def create_graph(graph_input: GraphInput)-> dict[str, Any]:
    """
    Receives a JSON payload describing the graph, constructs the graph,
    calculates metrics, and returns the graph with added metrics.
    
    Args:
    graph_input (GraphInput): Pydantic model to enforce input structure.

    Returns:
    dict: A dictionary representing the node-link data of the graph.
    """
    try:
        graph_data = construct_graph(graph_input)
        return graph_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
