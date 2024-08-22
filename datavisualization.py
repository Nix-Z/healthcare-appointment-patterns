import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from data_preprocess import preprocess_data

def visualize_data():
    data, categorical_features, numerical_features = preprocess_data()

    # Create histogram for each categorical feature
    for categorical_feature in categorical_features:
        fig = px.histogram(data, x=categorical_feature)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        # fig.show()
        fig.write_image(f'fig_{categorical_feature}.jpg')

    return data

visualize_data()
