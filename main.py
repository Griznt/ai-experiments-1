import pandas

data = pandas.read_csv('src/_ea07570741a3ec966e284208f588e50e_titanic.csv', index_col='PassengerId')
 
print('1. Passengers grouped by sex:')
print(data['Sex'].value_counts())

print('2. Survived passangers in per cents:')
passengersCount,attributesCount = data.shape
survivedPassengersCount = data['Survived'].value_counts()[0]
print(survivedPassengersCount / passengersCount * 100)