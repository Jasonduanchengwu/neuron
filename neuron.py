from random import uniform
from io import open
from pathlib import Path

class NeuronBot:
    def __init__(self):
        # Preset parameters
        self.cat_num = 10
        self.weights_count = 2
        self.threshold = 0
        self.epoche = 100
        self.x_min, self.x_range = -90, 180
        self.y_min, self.y_range = -180, 360

        # Initialization
        self.weights = [[0 for i in range(self.weights_count)] for j in range(self.cat_num)]
        self.current_coords = [0 for i in range(self.weights_count)]
        self.expected_outputs = [0  for i in range(self.cat_num)]
        self.calculated_outputs = [0  for i in range(self.cat_num)]
    
    def initialize_weights(self):
        """
        Randomizing weights pre-training

        Parameters:
            None

        Returns:
            None
        """
        for i in range(self.cat_num):
            for j in range(self.weights_count):
                self.weights[i][j] = uniform(0,1)
        return

    def update_coords(self, coords):
        """
        Update coordinates variables with the current coordinates in the current readline

        Parameters:
            coords: this parameter is an array of two float elements representing the normalized latitude and longitude

        Returns:
            None
        """
        self.current_coords[0] = coords[0]
        self.current_coords[1] = coords[1]
        return

    def allocate_category(self, cat_val):
        """
        Identifies category of the current line of data and return corresponding index

        Parameters:
            cat_val: this is the category value which is a string variable used to be compared
        
        Returns:
            index of the correct category based on cat_val
            returns -1 when no category is matched
        """
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
        """
        This function updates the correct expected output for the current line of data

        Parameters:
            category: this is a string variable represeting the category read from the training file

        Returns:
            None
        """
        self.expected_outputs[self.allocate_category(category)] = 1
        return

    def update_weights(self):
        """
        update weights if the expected output mismatch the calculated output with learning rate of 0.5

        Parameters:
            None

        Returns:
            None
        """
        for i in range(self.cat_num):
            for j in range(self.weights_count):
                self.weights[i][j] = self.weights[i][j] + 0.5 * (self.expected_outputs[i] - self.calculated_outputs[i]) * self.current_coords[j]
        return

    def normalize_coords(self, coords):
        """
        Normalize coordinate values to make their weightage closer

        Parameters:
            coords: an array of 2 sring variables representing the latitude and longitude

        Returns:
            The normalized coordinates in type float rounded to 6 decimal place
        """
        coords[0]=round((float(coords[0])-self.x_min)/self.x_range,6)
        coords[1]=round((float(coords[1])-self.y_min)/self.y_range,6)
        return coords

    def parse_data(self, training_file):
        """
        Parses a line of data from the file path given

        Parameters:
            file_path: a Path object of the file to be read

        Returns:
            coords: an array of two string variables representing the current coords
            ex_outputs: a string variable of category
        """

        # Parsing data
        data = training_file.readline().split()
        coords = data[:-1]
        if data !=[]:
            ex_outputs = data[-1]
        else: ex_outputs = "eof"

        return coords, ex_outputs
    
    def calculate_outputs(self):
        """
        Calculates output based on normalized coords and current weights

        Parameters:
            None
        
        Returns:
            None
        """
        output = [0 for i in range(self.cat_num)]
        for i in range(self.cat_num):
            output[i] = self.current_coords[0] * self.weights[i][0] + self.current_coords[1] * self.weights[i][1]
            if output[i] < self.threshold:
                self.calculated_outputs[i]=0
            else: self.calculated_outputs[i]=1
        return

def main():
    neuron_bot = NeuronBot()
    file_path = Path('train_data.txt')

    # opening file using path obj
    training_file = open(file_path, "r")

    # repeating the process epoche number of times
    for i in range(neuron_bot.epoche):
        # adjust weights till the last line of the training file
        while True:
            coords, ex_outputs = neuron_bot.parse_data(training_file)
            if ex_outputs == "eof":
                break
            neuron_bot.update_coords(neuron_bot.normalize_coords(coords))
            neuron_bot.update_outputs(ex_outputs)
            neuron_bot.initialize_weights()
            neuron_bot.calculate_outputs()
            neuron_bot.update_weights()

    training_file.close()
    return

if __name__ == '__main__':
    main()
