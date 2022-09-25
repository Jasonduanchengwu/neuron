from random import random
from io import open
from pathlib import Path

class NeuronBot:
    def __init__(self):
        # Preset parameters
        self.cat_num = 10
        self.weights_count = 2
        self.x_min, self.x_range = -90, 180
        self.y_min, self.y_range = -180, 360

        # Initialization
        self.weights = [[0 for i in range(self.weights_count)] for j in range(self.cat_num)]
        self.current_coords = [0 for i in range(self.weights_count)]
        self.expected_outputs = [0  for i in range(self.cat_num)]
        self.calculated_outputs = [0  for i in range(self.cat_num)]
    
    def initialize_weights(self):
        for i in range(self.cat_num):
            weights[i][0] = w[i][0] + learning_rate * (correct_output[i] - output[i]) * x
            weights[i][1] = w[i][1] + learning_rate * (correct_output[i] - output[i]) * y

    def update_coords(self, coords):
        self.current_coords[0] = coords[0]
        self.current_coords[1] = coords[1]
        return

    def allocate_category(self, cat_val):
        if cat_val == "Africa":
            return 0
        elif cat_val == "America":
            return 1
        elif cat_val == "Antarctica":
            return 2
        elif cat_val == "Asia":
            return 3
        elif cat_val == "Australia":
            return 4
        elif cat_val == "Europe":
            return 5
        elif cat_val == "Arctic":
            return 6
        elif cat_val == "Atlantic":
            return 7
        elif cat_val == "Indian":
            return 8
        elif cat_val == "Pacific":
            return 9
        else: return -1

    def update_outputs(self, category):
        self.expected_outputs[self.allocate_category(category)] = 1
        return

    def update_weights(self):
        # learning_rate = 0.5
        for i in range(self.cat_num):
            self.weights[i][0] = self.weights[i][0] + 0.5 * (self.expected_outputs[i] - self.calculated_outputs[i]) * self.current_coords[0]
            self.weights[i][1] = self.weights[i][1] + 0.5 * (self.expected_outputs[i] - self.calculated_outputs[i]) * self.current_coords[1]

    def normalize_coords(self, coords):
        coords[0]=round((float(coords[0])-self.x_min)/self.x_range,6)
        coords[1]=round((float(coords[1])-self.y_min)/self.y_range,6)
        return coords

    def parse_data(self, file_path):
        # opening file using path obj
        training_file = open(file_path, "r")

        # Parsing data
        coords = training_file.readline().split()[:-1]
        ex_outputs = training_file.readline().split()[-1]

        # Always gonna be number of weights + 1 amount of data
        self.update_coords(self.normalize_coords(coords))
        self.update_outputs(ex_outputs)
        return
    
def main():
    neuron_bot = NeuronBot()
    file_path = Path('nnTrainData.txt')
    neuron_bot.parse_data(str(file_path))
    return

if __name__ == '__main__':
    main()
