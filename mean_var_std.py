import numpy as np
def calculate(arr):
  arr = np.array(arr)
  if len(arr) != 9:
    raise ValueError("List must contain nine numbers.")
  matrix = arr.reshape(3,3)
  mean_axis1 = np.mean(matrix, axis = 0).tolist()
  mean_axis2 = np.mean(matrix, axis = 1).tolist()
  mean_flat = np.mean(arr)
  var_axis1 = np.var(matrix, axis = 0).tolist()
  var_axis2 = np.var(matrix, axis = 1).tolist()
  var_flat = np.var(arr)
  std_axis1 = np.std(matrix, axis = 0).tolist()
  std_axis2 = np.std(matrix, axis = 1).tolist()
  std_flat = np.std(arr)
  max_axis1 = np.max(matrix, axis = 0).tolist()
  max_axis2 = np.max(matrix, axis = 1).tolist()
  max_flat = np.max(arr)
  min_axis1 = np.min(matrix, axis = 0).tolist()
  min_axis2 = np.min(matrix, axis = 1).tolist()
  min_flat = np.min(arr)
  sum_axis1 = np.sum(matrix, axis = 0).tolist()
  sum_axis2 = np.sum(matrix, axis = 1).tolist()
  sum_flat = np.sum(arr)
  
  calculation = {
    'mean': [mean_axis1, mean_axis2, mean_flat],
    'variance': [var_axis1, var_axis2, var_flat],
    'standard deviation': [std_axis1, std_axis2, std_flat],
    'max': [max_axis1, max_axis2, max_flat],
    'min': [min_axis1, min_axis2, min_flat],
    'sum': [sum_axis1, sum_axis2, sum_flat]
  }
  return calculation



