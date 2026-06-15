def build_graph(components):

    graph = {}

    for component in components:
        graph[component.id] = []

    for component in components:
        for dependency in component.dependencies:
            graph.setdefault(dependency, [])
            graph[dependency].append(component.id)

    return graph