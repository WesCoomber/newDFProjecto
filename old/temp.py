addNode(regListNames[idx], 'box', 'filled', 'greenyellow', 5)


def addNode(name, shape, style, fillcolor, penwidth):
    datG.node(name, label = str(name), shape=str(shape),style=str(style), fillcolor = str(fillcolor), penwidth = str(penwidth))
    return