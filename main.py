import matplotlib.pyplot as plt

class ScatterPlotter:
    def __init__(self, file_path):
        """Initialize the ScatterPlotter with a file path."""
        self.file_path = file_path
        self.x = []
        self.y = []
        self.translated_x = []
        self.translated_y = []

        # Load coordinates from the file
        self.load_coordinates()

    def load_coordinates(self):
        """Load coordinates from the specified file."""
        with open(self.file_path, 'r') as file:
            next(file)  # Skip header
            for line in file:
                values = line.strip().split(',')
                if len(values) == 2:
                    try:
                        x_val = float(values[0])
                        y_val = float(values[1])
                        self.x.append(x_val)
                        self.y.append(y_val)
                    except ValueError:
                        print(f"Could not convert values to float: {values}")
                else:
                    print(f"Unexpected number of values: {values}")

    def plot(self):
        """Plot the original and translated points."""
        plt.scatter(self.x, self.y, color='blue', label='Original Points')
        plt.scatter(self.translated_x, self.translated_y, color='red', label='Translated Points')
        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')
        plt.title('Scatterplot of X and Y Coordinates')
        plt.grid()
        plt.legend()
        plt.show()

    def translate_points(self, dx, dy):
        """Translate the points by a given offset (dx, dy)."""
        self.translated_x = [x + dx for x in self.x]
        self.translated_y = [y + dy for y in self.y]

# Usage
if __name__ == "__main__":
    scatter_plotter = ScatterPlotter('C:/Users/user/Documents/x_y_coordinates')
    scatter_plotter.translate_points(1, 1)  # Example translation
    scatter_plotter.plot()