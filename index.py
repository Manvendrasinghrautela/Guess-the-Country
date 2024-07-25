import random

name = input("Enter the name : ")

print("Welcome in the game ", name)

countries = ['germany','pakistan','india','spain','Afghanistan','Argentina','Australia','Armenia','Austria','Bangladesh','Barbados','Belgium','Belarus',
           'Brazil','Bulgaria','Cambodia','Cameroon','Canada','Chile','Colombia','China','Croatia','Cuba','Czechoslovakia','Democratic Republic of the Congo',
           'Denmark','Egypt','Estonia','Finland','France','Georgia','Germany','Greece','Hungary','Iceland','Indonesia','Iran','Iraq','Ireland',
           'Israel','Italy','Jamaica','Japan','Kenya','Kazakhstan','Korea','Kosovo','Kuwait','Lebanon','Luxembourg','Malaysia','Maldives','Malta',
           'Mauritius','Mexico','Mongolia','Morocco','Namibia','Nepal','Netherlands','NewZealand','Nigeria','Norway','Oman','Philippines','Poland',
           'Portugal','Qatar','SouthKorea','Romania','Russia','SaudiArabia','Serbia','Slovakia','Singapore','Slovenia','SouthAfrica','SriLanka','Sweden',
           'Switzerland','Syria','Tajikistan','Thailand','Turkey','Ukraine','UnitedKingdom','Uruguay','UnitedArabEmirates','Uganda','Vietnam','Uzbekistan',
           'Venezuela','Zimbabwe']


country = random.choice(countries)

print('Guess the Country')

guesses = ''

turns = 12

while turns > 0:
    failed = 0
    for char in country:
        if char in guesses:
            print("You chose right character")
            print(char,end=' ')

        else:
            print('_')

            failed += 1

    if failed == 0:
        print("you won the game")
        print("The country is ",country)
        break

    print()
    guess = input("Guess the Character of the country : ")

    guesses += guess

    if guess not in countries:
        turns -= 1
        # print("Wrong Guess")
        print("You have ",turns,"turns left")

        if turns == 0:
            print("you loose the game")    
            print("The country is ",country)        

