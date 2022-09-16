#Please create a list, set, tuple, and dictionary to be built into numerous if,elif, else statements

carlist = ['Ferrari', 'Pagani', 'Lamborgini', 'porche', 'BMW']

carset = {'Ferrari', 'Pagani', 'Lamborgini', 'porche', 'BMW'}

cartuple = ('Ferrari', 'Pagani', 'Lamborgini', 'porche', 'BMW')

cardic = {
    'make': ('Ferrari', 'Pagani', 'Lamborgini', 'porche', 'BMW'),
    'model': ('F80 Spyder', 'Zonda', 'Aventador', '911', 'M5'),
    'year': ('2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022')
}
carwanted = input("do you want a car? ")
if carwanted.lower() == 'yes':
    print(carset)
    makewanted = input('Which make do you want? ')
    print(cardic['model'])
    modelwanted = input('Which model do you want? ')
    print(cardic['year'])
    yearwanted = input('Which year do you want? ')
    print('Your car is: ' + makewanted + ' ' + modelwanted + ' ' + yearwanted + '. Enjoy!!!')
else:
    print('ok bye')