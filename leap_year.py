def leap_year(year):

    if (year == 2100):
        print("False")
    else:
        if (year%4 == 0):
            if (year%100 != 0 and year%400 == 0):
                print("false")
            else:
                print("true")
        else:
            print("false")


n = int(input())

leap_year(n)