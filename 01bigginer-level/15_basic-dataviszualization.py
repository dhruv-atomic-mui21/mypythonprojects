import matplotlib.pyplot as plt

def basic_data_visualization():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y_line = [2, 3, 5, 7, 11]
    y_bar = [5, 7, 3, 8, 4]
    y_scatter = [1, 4, 2, 5, 7]

    # Line plot
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 3, 1)
    plt.plot(x, y_line, marker='o')
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Bar chart
    plt.subplot(1, 3, 2)
    plt.bar(x, y_bar, color='orange')
    plt.title('Bar Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Values')

    # Scatter plot
    plt.subplot(1, 3, 3)
    plt.scatter(x, y_scatter, color='green')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    basic_data_visualization()
