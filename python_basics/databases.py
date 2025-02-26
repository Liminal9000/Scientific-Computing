# Create variables of each data type
int_var = 42
float_var = 3.14
complex_var = 2 + 3j
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dict_var = {"one": 1, "two": 2}
set_var = {7, 8, 9}
bool_var = True

# Print the type of each variable
print("Type of int_var:", type(int_var))
print("Type of float_var:", type(float_var))
print("Type of complex_var:", type(complex_var))
print("Type of list_var:", type(list_var))
print("Type of tuple_var:", type(tuple_var))
print("Type of dict_var:", type(dict_var))
print("Type of set_var:", type(set_var))
print("Type of bool_var:", type(bool_var))

# Convert the integer variable to a float and vice versa
converted_to_float = float(int_var)
converted_to_int = int(float_var)

# Print the conversion results
print("Converted int_var to float:", converted_to_float)
print("Converted float_var to int:", converted_to_int)
