import pandas as pd
from typing import Optional
import matplotlib.pyplot as plt



def plot_numeric_data(
        df: pd.DataFrame, 
        col_to_plot: str, 
        chart_title: str, 
        x_label: str, 
        y_label: str,
        bins: Optional[int] = None
) -> None:
    if col_to_plot not in df.columns:
        raise ValueError("Column not present in the data set")
    
    # Create a dictionary for the plot arguments
    plot_kwargs = {}
    if bins is not None:
        plot_kwargs['bins'] = bins
    
    fig, ax = plt.subplots(figsize=(10, 6))
    df[col_to_plot].plot(kind="hist", ax=ax, **plot_kwargs)
    ax.set_title(f"{chart_title}")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)




def plot_categorical_data(
    df: pd.DataFrame,
    col_to_plot: str,
    chart_title: str,
    x_label: str,
    y_label: str = "Share (%)",
    top_n: Optional[int] = None,        # show only top N categories
    dropna: bool = True,                # ignore NaN categories
    show_counts: bool = True,           # add raw counts to the labels
) -> None:
    if col_to_plot not in df.columns:
        raise ValueError(f"The column {col_to_plot} is not present in the dataset.")

    s = df[col_to_plot]
    counts = s.value_counts(dropna=not dropna)  # dropna=True -> hides NaN
    if top_n is not None:
        counts = counts.head(top_n)

    pct = (counts / counts.sum() * 100).round(1)

    fig, ax = plt.subplots(figsize=(10, 6))
    pct.plot(kind="bar", rot=45, ax=ax)

    ax.set_title(chart_title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ymax = pct.max()
    ax.set_ylim(0, ymax * 1.12)
    ax.set_yticks([]) 

    # Annotate bars with percentages (and counts if requested)
    for p, val, n in zip(ax.patches, pct.values, counts.values):
        label = f"{val:.1f}%"
        if show_counts:
            label += f"\n(n={n})"
        ax.annotate(
            label,
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center", va="bottom",
            fontsize=9, xytext=(0, 3), textcoords="offset points"
        )

    plt.tight_layout()