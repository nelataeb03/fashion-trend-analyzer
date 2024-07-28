import matplotlib.pyplot as plt

def visualize_trends(trends):
    labels, values = zip(*trends)
    plt.bar(labels, values)
    plt.xlabel('Trends')
    plt.ylabel('Frequency')
    plt.title('Top Fashion Trends')
    plt.show()

# Example usage
# visualize_trends(trends)
