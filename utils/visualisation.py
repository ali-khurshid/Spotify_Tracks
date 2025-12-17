"""
Utility functions for graphing and visualization.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

MARGINS = dict(l=40,
               r=40,
               t=40,
               b=40)


def plot_scatter_with_regression(df: pd.DataFrame,
                                 x_col: str,
                                 y_col: str,
                                 title: str = "",
                                 xlabel: str = "",
                                 ylabel: str = "") -> None:
    """
    Plots a scatter plot with a trendline using Plotly Express.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        x_col (str): Column name for the x-axis.
        y_col (str): Column name for the y-axis.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        labels={x_col: xlabel, y_col: ylabel},
        trendline="ols",
        trendline_color_override="red",
        title=title
    )
    fig.update_layout(margin=MARGINS)
    return fig


def plot_violin(df: pd.DataFrame,
                x_col: str,
                y_col: str,
                title: str = "",
                xlabel: str = "",
                ylabel: str = "") -> None:
    """
    Plots a violin plot using Plotly Express.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        x_col (str): Column name for the x-axis (categorical).
        y_col (str): Column name for the y-axis (numerical).
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    fig = px.violin(
        df,
        x=x_col,
        y=y_col,
        labels={x_col: xlabel, y_col: ylabel},
        box=True,
        points="all",
        title=title
    )
    fig.update_layout(margin=MARGINS)
    return fig
