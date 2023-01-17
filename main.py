import numpy
import pandas
import networkx
import matplotlib.pyplot as plt

source = "Balbuena"
target = "Universidad"
weight = "Longitud de interestación"

#pip install openpyxl
#Open data
#https://metro.cdmx.gob.mx/longitud-de-estacion
dataframe = pandas.read_excel("metro.xlsx")
METRO = networkx.from_pandas_edgelist(dataframe, source='Origen', 
                                      target='Destino', edge_attr='Longitud de interestación')


path = networkx.dijkstra_path(METRO, source = source, target = target, weight = weight)

rute = METRO.subgraph(path)
networkx.draw(rute, with_labels=True)
networkx.draw_networkx_edges(rute, pos=networkx.spring_layout(rute), edge_color='red')

plt.show()