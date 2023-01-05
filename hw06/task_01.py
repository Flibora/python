from typing import Union

def convSmToInches(chislo: Union[int, float]) -> float:
    return chislo * 0.39

def convInchesToSm(chislo: Union[int, float]) -> float:
    return chislo * 2.54

def convMilesToKilometers(chislo: Union[int, float]) -> float:
    return chislo * 1.609344

def convKiometrsToMiles(chislo: Union[int, float]) -> float:
    return chislo * 0.621371

def convFuntsToKilograms(chislo: Union[int, float]) -> float:
    return chislo * 0.45359237

def convKilogramsToFunts(chislo: Union[int, float]) -> float:
    return chislo * 2.20462262185

def convUnciiToGrams(chislo: Union[int, float]) -> float:
    return chislo * 28.34952

def convGramsToUncii(chislo: Union[int, float]) -> float:
    return chislo / 28.34952

def convGallonsToLitres(chislo: Union[int, float]) -> float:
    return chislo * 0.264172

def convLitresToGallons(chislo: Union[int, float]) -> float:
    return chislo * 3.785412

def convLitresToPinta(chislo: Union[int, float]) -> float:
    return chislo * 0.5683

def convPintToLitres(chislo: Union[int, float]) -> float:
    return chislo * 0.473176

if __name__ == "__main__":
    print("hello")
