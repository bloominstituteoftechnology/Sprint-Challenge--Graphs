"""
General drawing methods for graphs using Bokeh.
"""

from math import ceil, floor, sqrt
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph
        
    def _setup_graph_renderer(self, circle_size, draw_components):
        graph_renderer = GraphRenderer()
        self.vertex_list = list(self.graph.vertices.keys())


        graph_renderer.node_renderer.data_source.add(
            [vertex.label for vertex in self.vertex_list], 'index')
        colors = (self._get_connected_component_colors() if draw_components
                  else self._get_random_colors())
        graph_renderer.node_renderer.data_source.add(colors, 'color')

        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')

        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()  
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self, num_colors=None):
        colors = []
        num_colors = num_colors or len(self.graph.vertices)
        for _ in range(num_colors):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex.label)
                    end_indices.append(destination.label)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex_label, (x_pos, y_pos) in self.pos.items():
            label_data['x'].append(x_pos)
            label_data['y'].append(y_pos)
            label_data['names'].append(vertex_label)
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle',
                          source=label_source, render_mode='canvas')
        self.plot.add_layout(labels)

    def show(self, output_path='./graph.html'):
        """Render the graph to a file on disk and open with default browser."""
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.vertex_list:
            # TODO make bounds and random draws less hacky
            self.pos[vertex.label] = (1 + random() * (self.width - 2),
                                      1 + random() * (self.height - 2))

    def _get_connected_component_colors(self):
        """Return same-colors for vertices in connected components."""
        self.graph.find_components()
        component_colors = self._get_random_colors(self.graph.components)
        vertex_colors = []
        for vertex in self.vertex_list:
            vertex_colors.append(component_colors[vertex.component])
        return vertex_colors
