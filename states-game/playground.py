# paris_dict = {}
# pairs = 0

# for sock in [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]:
#     if paris_dict.get(sock):
#         paris_dict[sock] = paris_dict[sock] + 1
#         if paris_dict.get(sock) % 2 == 0:
#             print('pair: ' + str(sock))
#             pairs += 1
#             paris_dict[sock] = None
#     else:
#         paris_dict[sock] = 1

# print(pairs)
# paris_dict[1] = 1
# print(paris_dict.get(1))

# for n in [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]:
#     print(n)

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     df = pd.DataFrame(data)

#     print(df)

# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['condition'])
# print(data.condition)
# max_temp = data['temp'].max()
# print(data[data.day == 'Monday'])
# print(data[data.temp == max_temp])

# Create a Data Frame from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231111.csv')

grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'colors': ['Grey', 'Red', 'Black'],
    'count': [grey_count, red_count, black_count]
}

colors = pd.DataFrame(data_dict)
colors.to_csv('squirrel_count.csv')
