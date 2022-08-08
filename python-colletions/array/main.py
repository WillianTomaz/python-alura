# Evitar de usar array puro,
# se precisamos de trabalho numérico, 
# é costume usar o numpy (pip install numpy)


# Exemplo com array:
import array as arr
test_array = arr.array('d', [1, 3.5])
print("[array] => ", test_array)





# Exemplo com numpy:
import numpy as np
test_numpy = np.array([1, 3.5])
print("[numpy] => ", test_numpy)
test_numpy += 3
print("[numpy] => ", test_numpy)

