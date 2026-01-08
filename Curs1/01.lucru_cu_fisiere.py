

x = input("Introduceti un numar\n")
print("AI introdus: ", x)

file_name = "01.numar.txt"

# a - append
# w - write

## Varianta 1 - invechita
file_handler = open(file_name, "a")
file_handler.write(x)
file_handler.write("\n")
file_handler.close()


## Varianta 2 - cea mai noua
with open(file_name, "a") as file_handler:
    file_handler.write(x)
    file_handler.write("\n")