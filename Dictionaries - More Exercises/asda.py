import numpy as np

dictionary = { 'A':1,'ABC':3,'ABCD':4,'AB':2 }
sorted_value_index = np.argsort(dictionary.values())
print(sorted_value_index)
dictionary_keys = list(dictionary.keys())
print(dictionary_keys)
sort_dictionary = {dictionary_keys[i]:sorted(dictionary.values())[i] for i in range(len(dictionary_keys))}
print("Sorted Dictionary by value: ", sort_dictionary)