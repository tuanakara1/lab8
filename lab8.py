from abc import ABC, abstractmethod


class FrequencyCounter(ABC):
    def __init__(self, file_address):
        self.address = file_address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_list = [0] * 26  # List to store frequencies for each letter (assuming lowercase English alphabets)
        with open(self.address, 'r') as file:
            data = file.read()
            for char in data:
                if char.isalpha():
                    index = ord(char.lower()) - ord('a')
                    frequency_list[index] += 1

        for i, frequency in enumerate(frequency_list):
            letter = chr(i + ord('a'))
            print(f"{letter} = {frequency}")


class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_dict = {}
        with open(self.address, 'r') as file:
            data = file.read()
            for char in data:
                if char.isalpha():
                    char = char.lower()
                    frequency_dict[char] = frequency_dict.get(char, 0) + 1

        for letter, frequency in frequency_dict.items():
            print(f"\"{letter}\" {frequency}")


file_address = "weirdWords.txt"

list_counter = ListCount(file_address)
dict_counter = DictCount(file_address)

print("Using ListCount:")
list_counter.calculateFreqs()

print("\nUsing DictCount:")
dict_counter.calculateFreqs()
