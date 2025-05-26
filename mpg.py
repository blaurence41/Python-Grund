def liters_100km_to_miles_gallon(liters):
    miles = 62.1371192237334
    gallons = liters / 3.785411784
    mpg = miles / gallons
    return mpg
def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    km = miles * 1.609344
    hkm = km / 100
    liters_per_100km = liters / hkm
    return liters_per_100km
    
    
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))