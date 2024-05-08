import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# print(squirrel_data['Primary Fur Color'])

gray_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray']
print(len(gray_squirrel))

cinnamon_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon']
print(len(cinnamon_squirrel))

black_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == 'Black']
print(len(black_squirrel))

squirrel_dictionary = {
    'Fur Color': ["Gray", "Cinnamon", "Black"],
    'Numbers': [len(gray_squirrel), len(cinnamon_squirrel), len(black_squirrel)]
}

data = pandas.DataFrame(squirrel_dictionary)
print(data)
data.to_csv("new_squirrel_number.csv")
