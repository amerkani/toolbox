import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_trace(
    x1,
    y1,
    names1=None,
    x2=None,
    y2=None,
    names2=None,
    template="plotly_dark",
    xlabel="",
    y1label="",
    y2label="",
):
    # Need to add error checking

    # Create figure
    fig = go.Figure()
    if x2 != None:  # dual y-axes
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.update_yaxes(title_text=y1label, secondary_y=False)
        fig.update_yaxes(title_text=y2label, secondary_y=True)
    else:
        fig.update_yaxes(title_text=y1label)

    # Plot primary y-axis
    if isinstance(x1, list):
        for i in range(len(x1)):
            fig.add_trace(
                go.Scatter(
                    x=x1[i],
                    y=y1[i],
                    mode="lines",
                    name=names1[i],
                )
            )
    else:
        fig.add_trace(
            go.Scatter(
                x=x1,
                y=y1,
                mode="lines",
                name=names1,
            )
        )

    # Plot secondary y-axis
    if isinstance(x2, list):
        for i in range(len(x2)):
            fig.add_trace(
                go.Scatter(
                    x=x2[i],
                    y=y2[i],
                    mode="lines",
                    name=names2[i],
                )
            )
    elif x2 != None:
        fig.add_trace(
            go.Scatter(
                x=x1,
                y=y1,
                mode="lines",
                name=names1,
            )
        )

    fig.update_layout(template=template, xaxis_title=xlabel)

    return fig
