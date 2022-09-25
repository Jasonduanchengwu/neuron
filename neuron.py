from random import random
from io import open
from pathlib import Path

class neuronBot:
    def __init__(self) -> None:
        self.weights = [[0 for i in range(2)] for j in range(10)]
        
    def read_data(self, file_path):
        training_file = open(file_path, "r")
        training_file.readline()

def main():
    neuron_bot = neuronBot()
    file_path = Path('nnTrainData.txt')
    neuron_bot.read_data(str(file_path))
    return

if __name__ == '__main__':
    main()
