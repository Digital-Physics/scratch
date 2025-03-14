import matplotlib.pyplot as plt
import networkx as nx

def draw_flowchart():
    G = nx.DiGraph()
    
    # Nodes with wrapped labels
    labels = {
        "Cork Board Ideas": "Cork\nBoard\nIdeas",
        "Generate Outline w/ AI": "Generate\nOutline\nw/ AI",
        "Develop Each Scene w/ Context": "Develop\nEach Scene w/\nContext"
    }
    
    G.add_nodes_from(labels.keys())
    
    # Node positions
    pos = {
        "Cork Board Ideas": (0, 2),
        "Generate Outline w/ AI": (0, 1),
        "Develop Each Scene w/ Context": (0, 0)
    }
    
    # Main flow
    G.add_edges_from([
        ("Cork Board Ideas", "Generate Outline w/ AI"),
        ("Generate Outline w/ AI", "Develop Each Scene w/ Context")
    ])
    
    # Feedback loops (self-loops)
    G.add_edge("Cork Board Ideas", "Cork Board Ideas", weight=0.5)
    G.add_edge("Generate Outline w/ AI", "Generate Outline w/ AI", weight=0.5)
    G.add_edge("Develop Each Scene w/ Context", "Develop Each Scene w/ Context", weight=0.5)
    
    plt.figure(figsize=(8, 6))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=5000, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')
    
    # Draw regular edges (main flow)
    regular_edges = [(u, v) for u, v in G.edges() if u != v]
    nx.draw_networkx_edges(G, pos, edgelist=regular_edges, edge_color='black', width=2)
    
    # Draw self-loops (feedback loops) with high visibility
    loop_edges = [(n, n) for n in labels if G.has_edge(n, n)]
    
    # Using connectionstyle with appropriate rad value to make loops very visible
    for edge in loop_edges:
        nx.draw_networkx_edges(G, pos, edgelist=[edge], 
                              edge_color='red', 
                              width=2,
                              arrows=True,
                              arrowsize=20,
                              arrowstyle='-|>',
                              connectionstyle='arc3,rad=0.5')
    
    # Add a legend for feedback loops
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color='red', lw=2, label='Feedback Loop')]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.title("Writing Process with Feedback Loops")
    plt.axis('off')
    plt.tight_layout()
    
    return plt

# Execute the function to generate the chart
fig = draw_flowchart()
plt.show()