from operator import ne
from random import random
from io import open
from pathlib import Path

class neuronBot:
    def __init__(self):
        # Preset parameters
        self.cat_num = 10
        self.weights_count = 2
        self.x_min, self.x_range = -90, 180
        self.y_min, self.y_range = -180, 360

        # Initialization
        self.weights = [[0 for i in range(self.weights_count)] for j in range(self.cat_num)]
        self.expected_outputs = [0  for i in range(self.cat_num)]
        self.calculated_outputs = [0  for i in range(self.cat_num)]
        self.current_coords = [0 for i in range(self.weights_count)]

    def update_coords(self, coords):
        self.current_coords[0] = coords[0]
        self.current_coords[1] = coords[1]

    def allocate_category(self, cat_val):
        if cat_val == "Asia":
            return 3

    def update_outputs(self, category):
        self.expected_outputs[self.allocate_category(category)] = 1

    def update_weights(self):
        pass

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
        # print(coords, ex_output)
        self.update_coords(self.normalize_coords(coords))
        self.update_outputs(ex_outputs)
    
def main():
    neuron_bot = neuronBot()
    file_path = Path('nnTrainData.txt')
    neuron_bot.parse_data(str(file_path))
    return

if __name__ == '__main__':
    main()
