import numpy as np

# Example array
array = np.array([1, 2, "f", 4, 5, 6, 7, 8, 9])

# Convert array to a C-style string
c_array = ", ".join(map(str, array))
c_array_string = f"int myArray[] = {{ {c_array} }};\n"
c_array_string += f"const int myArraySize = {len(array)};\n"

# Save to a file
with open("C:/Users/rcpow/Documents/GitHub/NanoLab-GUI/NanoLab-GUI/Arduino/basic_hydrofuge_schedule/array_for_arduino.h", "w") as f:
    f.write(c_array_string)

print(f"Array saved to {f}")