import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnm_random_graph(100, 400, seed=82, directed=False)
pos = nx.circular_layout(G, scale=4)

time_step = 0
k = 5
# Suppose we are drawing k = 3 unraveling process
while time_step <= 10:
    nodes_leave_list = []
    node_color_list = []
    for i in G.nodes:
        if G.degree[i] <= k:
            nodes_leave_list.append(i)
    for node in G:
        if node in nodes_leave_list:
            node_color_list.append('red')
        else:
            node_color_list.append('green')
    plt.figure(int(2 * time_step + 1), figsize=(8, 8))
    plt.title("t = " + str(time_step))
    nx.draw(G, node_color='green',
            pos=pos, with_labels=True)
    plt.savefig(str(int(2 * time_step + 1)) + '.png')
    plt.cla()
    plt.close()
    plt.figure(int(2 * time_step + 2), figsize=(8, 8))
    plt.title("t = " + str(time_step))
    nx.draw(G, node_color=node_color_list,
            pos=pos, with_labels=True)
    plt.savefig(str(int(2 * time_step + 2)) + '.png')
    plt.cla()
    plt.close()
    G.remove_nodes_from(nodes_leave_list)
    for i in nodes_leave_list:
        pos[i] = None
    time_step += 1

plt.figure(int(2 * time_step + 3), figsize=(8, 8))
plt.title("t = " + str(time_step))
nx.draw(G, node_color=node_color_list,
            pos=pos, with_labels=True)
plt.savefig(str(int(2 * time_step + 3)) + '.png')

