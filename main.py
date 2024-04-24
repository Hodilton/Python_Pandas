import pandas as pd
import plotly.io as pio
import plotly.express as px

from utilities import Utilities
from graph_config import GraphConfig

class DataHandler:
    def __init__(self, data_load_params, graph_params):
        self.data_path = Utilities.Data.pre_check(data_load_params)

        self.data = None
        if self.data_path is None:
            Utilities.Raise.data_load_error()
            return

        self.data = pd.read_csv(self.data_path)
        self.graph_params = graph_params

        pio.templates.default = "plotly_white"

    def check_head(self):
        if self.data is None:
            Utilities.Raise.data_load_error()
            return

        pd.set_option('display.max_columns', None)
        print(f"The first 5 entries:\n{self.data.head()}")

    def plot_graph(self, graph_key):
        if self.data is None:
            Utilities.Raise.data_load_error()
            return

        graph_info = self.graph_params.get(graph_key)

        if graph_info:
            graph_type = graph_info.pop("type")

            if graph_type == "box":
                fig = px.box(self.data, **graph_info)
            else:
                fig = getattr(px, graph_type)(self.data, **graph_info)

            fig.show()
        else:
            Utilities.Raise.graph_key_error(graph_key)

if __name__ == '__main__':
    data_load_params = {'folder_path': "data",
                        'file_name': "pokemons.csv"}
    graph_params = GraphConfig.get_graph_config()

    data_handler = DataHandler(data_load_params, graph_params)

    data_handler.check_head()

    for graph_key, graph_info in graph_params.items():
        data_handler.plot_graph(graph_key)
