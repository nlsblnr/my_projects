my_list = ["aa", "bb", "cc", "dd", "ee", "ff"]

def some_algorithm():
    for item in my_list:
        yield(item)

develop = some_algorithm()

for x in range(len(my_list)):
    print(next(develop))

var_list = ["a", "b", "c", "d", "e", "f", "g"]
val_list = [1, 2, 3, 4, 5, 6, 7]

def generate_variables():
    for index, obj in enumerate(var_list):
        current_item = val_list[index]
        globals()[obj] = current_item
        yield(current_item)

main = generate_variables()

try:
    for generate in range(len(var_list)):
        next_iter = next(main)
        if val_list[generate] == next_iter:
            print(val_list[generate])
        else:
            print(val_list[generate])
            print(next_iter)
            print("\n")

except:
    print("UNEXPECTED ERROR OCCURRED")
