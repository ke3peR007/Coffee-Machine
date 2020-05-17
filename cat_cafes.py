my_list = []

i = 0
counter = 0
while i < 2:
    cafe_name = input()
    counter += 1
    if cafe_name == "MEOW":
        break
    my_list.append(cafe_name)

print(my_list)
cat_cafe = []
max_num = 0
j = 0
cat_club = ""
while j < counter:
    for word in my_list:
        cat_cafe = word.split(" ")
        cat_number = int(cat_cafe[1])
        # print(cat_number)
        temp_num = cat_number

        if temp_num > max_num:
            max_num = int(cat_cafe[1])
            cat_club = cat_cafe[0]
            max_num = temp_num

    j += 1

print(cat_club)
# print(max_num)
