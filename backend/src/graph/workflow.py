"""
This module defines the DAG(Directed Acyclic Graph): which orchestrates the video compliance audit process.
It connects the nodes using the StateGraph from LangGraph.
START -> index_video_node -> audit_content_node -> END
"""

from langgraph.graph import StateGraph,END
from backend.src.graph.state import VideoAuditState
from backend.src.graph.nodes import index_video_node, audio_content_node


def  create_graph():
    """
    constructs and compiles the langgraph workflow
    Returns:
    Compiled Graph: runnable graph object for execution
    """

    # initalise the graph with state schema
    workflow = StateGraph(VideoAuditState)
    # add the nodes
    workflow.add_node("indexer",index_video_node)
    workflow.add_node("auditor",audio_content_node)

    # define the entry point
    workflow.set_entry_point("indexer")

    # define edges
    workflow.add_edge("indexer","auditor")

    # workflow ends
    workflow.add_edge("auditor",END)

    # compile the graph
    app = workflow.compile()
    return app

# expose this runnable graph
app = create_graph()