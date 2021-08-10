StudentAges = [46, 21, 24, 26, 31]
StudentShoeSizes = [41, 38, 42, 43, 44]

def PrintStuff(NumberToprint,
               TextToprintBefore,
               TextToPrintAfter,
               NumberOfEmptyLinesBefore,
               NumberOfEmptyLinesAfter = 1):
    for EmptyLines in range(NumberOfEmptyLinesBefore):
        print("")

    # I funktionen her udskriver vi med metode 3 !!!
    print("{} er {} {} !!!!!" .format(TextToprintBefore, NumberToprint, TextToPrintAfter))

    for EmptyLines in range(NumberOfEmptyLinesAfter):
        print("")


if __name__ == '__main__':
    print("hej h9sd081221 så starter vi vores Pythom rejse !!!")

    Index = 0
    TotalAge = 0
    AverageAge = 0.0
    TotalShoeSize = 0
    AverageShoeSize = 0.0

    while Index < len(StudentAges):
        TotalAge += StudentAges[Index]
        Index += 1

    AverageAge = TotalAge / len(StudentAges)

    for ShoeSize in StudentShoeSizes:
        TotalShoeSize += ShoeSize

    AverageShoeSize = TotalShoeSize / len(StudentShoeSizes)

    # Metode 1
    print("Print Metode 1 : Gennemsnitsalder er %.1f år !!!" % (AverageAge))

    # Metode 2
    print("Print Metode 2 : Gennemsnitsalder er", AverageAge, "år !!!")

    # Metode 3
    print("Print Metode 3 : Gennemsnitsalder er {} år !!!" .format(AverageAge))

    # Metode 4
    print("Print Metode 4 : Gennemsnitsalder er " + str(AverageAge) + " år !!!")

    # Metode 5
    print(f"Print Metode 5 : Gennemsnitsalder er {AverageAge} år !!!")

    print("")

    # Metode 1
    print("Print Metode 1 : Gennemsnit sko størrelse er %.1f !!!" % (AverageShoeSize))

    # Metode 2
    print("Print Metode 2 : Gennemsnit sko størrelse er", AverageShoeSize, "!!!")

    # Metode 3
    print("Print Metode 3 : Gennemsnit sko størrelse er {} !!!".format(AverageShoeSize))

    # Metode 4
    print("Print Metode 4 : Gennemsnit sko størrelse er " + str(AverageShoeSize) + " !!!")

    # Metode 5
    print(f"Print Metode 5 : Gennemsnit sko størrelse er {AverageShoeSize} !!!")

    PrintStuff(AverageAge, "Gennemsnitsalder er", "år ", 1, 4)

    PrintStuff(AverageShoeSize, "Gennemsnit sko størrelse", '', 1)