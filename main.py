def city_name():
    cityName = input("What's the name of the city you grew up? ")
    return cityName


def pet_name():
    petName = input("What's your pet's name? ")
    return petName


def band_name():
    print("Your band name could be: " + city_name() + " " + pet_name())

print("Welcome to the BAND NAME GENERATOR!")
band_name()
