import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_groupedbar(xlabels, title, train, test, label, plot_size):
    x = np.arange(len(xlabels))
    width = 0.35

    fig, ax = plt.subplots(figsize=plot_size)

    bars1 = ax.bar(x - width / 2, train, width, label="Train " + label, color="blue")
    bars2 = ax.bar(x + width / 2, test, width, label="Test " + label, color="orange")

    for rect in bars1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0,
                 height, '%.4f' % float(height), ha='center', va='bottom')

    for rect in bars2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0,
                 height, '%.4f' % float(height), ha='center', va='bottom')

    ax.set_ylabel('Scores')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(xlabels)
    ax.legend()
    plt.legend(loc="center")
    plt.show()


def plot_validation(grids, train_results, test_results, metrics, labels=None, plot_size=(15, 10)):
    grid_names = []
    title_constant = " Train-Validation Scores"

    if labels is not None:
        grid_names = labels
    else:
        for number in range(len(grids)):
            grid_names.append("Grid" + str(number))

    for train, test, metric in zip(train_results, test_results, metrics):
        plot_groupedbar(grid_names, metric + title_constant, train, test, metric, plot_size)

    for grid_name, grid in zip(grid_names, grids):
        print("{name}: {grid}".format(name=grid_name, grid=grid))