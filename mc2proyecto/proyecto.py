import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphVisualization(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Búsqueda en Anchura")
        self.master.attributes('-fullscreen', True)  # Hacer la ventana de pantalla completa
        self.master.configure(bg="#FFEEEE") # Cambiar el color de fondo de la ventana

        self.original_graph = nx.Graph()
        self.graph = nx.Graph()
        self.vertices = []
        self.edges = []
        self.canvas = None
        self.bfs_canvas = None
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para entrada de vértices
        self.vertex_label = tk.Label(self.master, text="Entrada de Vértices:")
        self.vertex_label.grid(row=0, column=0, padx=5, pady=5)
        # Entrada de vértices
        self.vertex_entry = tk.Entry(self.master)
        self.vertex_entry.grid(row=1, column=0, padx=5, pady=5)
        # Etiqueta para entrada de aristas
        self.edge_label = tk.Label(self.master, text="Entrada de Aristas:")
        self.edge_label.grid(row=0, column=1, padx=5, pady=5)
        self.edge_labelll = tk.Label(self.master, text="Grafo:")
        self.edge_label.grid(row=0, column=1, padx=5, pady=5)
        # Entrada de aristas
        self.edge_entry = tk.Entry(self.master)
        self.edge_entry.grid(row=1, column=1, padx=5, pady=5)
        # Botón para agregar aristas
        self.add_button = tk.Button(self.master, text="Agregar", command=self.add_graph)
        self.add_button.grid(row=1, column=2, padx=5, pady=5)
        # Tabla para mostrar vértices y aristas
        self.table_label = tk.Label(self.master, text="Vértices y Aristas:")
        self.table_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.treeview = ttk.Treeview(self.master, columns=("Vértices", "Aristas"), show="headings")
        self.treeview.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.treeview.heading("Vértices", text="Vértices")
        self.treeview.heading("Aristas", text="Aristas")
        # Área para mostrar el grafo original
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(row=5, column=0, padx=5, pady=5)

        # Área para mostrar el grafo de búsqueda en anchura
        self.bfs_figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.bfs_canvas = FigureCanvasTkAgg(self.bfs_figure, master=self.master)
        self.bfs_canvas.get_tk_widget().grid(row=5, column=1, padx=5, pady=5)

    def add_graph(self):
        vertices = self.vertex_entry.get().split(",")
        edges = self.edge_entry.get().split(",")
        for edge in edges:
            v1, v2 = edge.split("--")
            self.original_graph.add_edge(v1.strip(), v2.strip())
            self.edges.append(edge.strip())
        for vertex in vertices:
            self.original_graph.add_node(vertex.strip())
            self.vertices.append(vertex.strip())
        self.update_table()
        self.update_graph()
        self.update_bfs_graph()

    def update_bfs_graph(self):
        self.bfs_figure.clear()
        ax = self.bfs_figure.add_subplot(111)
        nx.draw(self.original_graph, with_labels=True, ax=ax)
        self.bfs_canvas.draw()

    def update_graph(self):
        self.graph = self.original_graph.copy()  
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        nx.draw(self.graph, with_labels=True, ax=ax)
        self.canvas.draw()

    def update_table(self):
        # Limpiar tabla
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        # Insertar vértices y aristas en la tabla
        for vertex in self.vertices:
            self.treeview.insert("", "end", values=(vertex, ""))
        for edge in self.edges:
            self.treeview.insert("", "end", values=("", edge))


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualization(master=root)
    app.mainloop()
