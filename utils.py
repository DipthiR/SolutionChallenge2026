import matplotlib.pyplot as plt
import os

def create_chart(group_stats):
    if not group_stats:
        return None

    labels = list(group_stats.keys())
    values = list(group_stats.values())

    plt.figure()
    plt.bar(labels, values)

    plt.xlabel("Groups")
    plt.ylabel("Approval Rate")
    plt.title("Bias Detection Chart")

    path = "static/chart.png"
    plt.savefig(path)
    plt.close()

    return path
