import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Line Plot
def line_plot(x, y, title="Line Plot", xlabel="X-axis", ylabel="Y-axis"):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Scatter Plot
def scatter_plot(x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Bar Chart
def bar_chart(categories, values, title="Bar Chart"):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=categories, y=values)
    plt.title(title)
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.show()

# Histogram
def histogram(data, bins=10, title="Histogram"):
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, alpha=0.7, color="blue", edgecolor="black")
    plt.title(title)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()

# Pie Chart
def pie_chart(labels, sizes, title="Pie Chart"):
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    plt.title(title)
    plt.show()

# Box Plot
def box_plot(data, title="Box Plot"):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=data)
    plt.title(title)
    plt.show()

# Heatmap
def heatmap(data, title="Heatmap"):
    plt.figure(figsize=(8, 5))
    sns.heatmap(data, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title(title)
    plt.show()

# 3D Surface Plot
def surface_plot(x, y, z, title="3D Surface Plot"):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap="viridis")
    ax.set_title(title)
    plt.show()
