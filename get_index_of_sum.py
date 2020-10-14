group = [2, 6, 7, 15, 5, 3]
target = 11


def get_index():
    for first_pos, num in enumerate(group):
        for second_pos, item in enumerate(group):
            if num + item == target:
                # print(first_pos, second_pos)
                return [first_pos, second_pos]
            else:
                pass
    print("Sorry no numbers added up to", target)


print(get_index())

