import pyexcel
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sheet = pyexcel.Sheet(array)
sheet.save_as("output.csv")
