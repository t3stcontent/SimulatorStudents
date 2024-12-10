print(9 ** 0.5)

try:
    apples = int(input("Enter a appple u have: "))
    if apples < 0:
        Exception("Як ти можеш мати яблук менше нуля?")
    part_numbers = int(input("Enter number of parts: "))
    part_amount = apples / part_numbers
except (ZeroDivisionError, ValueError):
    print("Куда ділиш і що воовдиш в цифру, АЛОООООО))))))))))))))))))))))))!!!!!!!!!!!")
except Exception as ex:
    print(ex)
except:
    print("bite")
finally:
    print("The program done")

