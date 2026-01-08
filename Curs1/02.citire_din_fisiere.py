
file_name = "01.numar.txt"

# r - read

# Versiunea 1 (citire) - invechita
file_handler = open(file_name, "r")
continut = file_handler.read()
print(continut)
file_handler.close()

# Versiunea 2 (citire) - noua, recomandata
with open(file_name, "r") as file_handler:
    continut = file_handler.read()
    print(continut)

