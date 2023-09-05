import matplotlib.pyplot as plt
import json

# Example string-to-frequency map
string_frequency_map = {
    "apple": 10,
    "banana": 15,
    "orange": 5,
    "grape": 8,
    "kiwi": 3
}

# Sort the map by frequency in descending order
sorted_map = sorted(string_frequency_map.items(), key=lambda x: x[1], reverse=True)

# Extract the strings and frequencies for plotting
strings = [item[0] for item in sorted_map]
frequencies = [item[1] for item in sorted_map]

# Plotting
plt.bar(strings, frequencies)
plt.xlabel('Strings')
plt.ylabel('Frequency')
plt.title('String vs. String Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.save("output.pdf")
