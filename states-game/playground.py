# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

paris_dict = {}
pairs = 0

for sock in [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]:
    if paris_dict.get(sock):
        paris_dict[sock] = paris_dict[sock] + 1
        if paris_dict.get(sock) % 2 == 0:
            print('pair: ' + str(sock))
            pairs += 1
            paris_dict[sock] = None
    else:
        paris_dict[sock] = 1

print(pairs)
# paris_dict[1] = 1
# print(paris_dict.get(1))

# for n in [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]:
#     print(n)