def what_is_my_sign(day, month):
    sign = ""
    if month == 1:
        if day >= 21:
            sign = "Aquarius"
        else:
            sign = "Capricorn"
    elif month == 2:
        if day >= 20:
            sign = "Pisces"
        else:
            sign = "Aquarius"
    elif month == 3:
        if day >= 21:
            sign = "Aries"
        else:
            sign = "Pisces"
    elif month == 4:
        if day >= 21:
            sign = "Taurus"
        else:
            sign = "Aries"
    elif month == 5:
        if day >= 22:
            sign = "Gemini"
        else:
            sign = "Taurus"
    elif month == 6:
        if day >= 22:
            sign = "Cancer"
        else:
            sign = "Gemini"
    elif month == 7:
        if day >= 23:
            sign = "Leo"
        else:
            sign = "Cancer"
    elif month == 8:
        if day >= 23:
            sign = "Virgo"
        else:
            sign = "Leo"
    elif month == 9:
        if day >= 24:
            sign = "Libra"
        else:
            sign = "Virgo"
    elif month == 10:
        if day >= 24:
            sign = "Scorpio"
        else:
            sign = "Libra"
    elif month == 11:
        if day >= 23:
            sign = "Sagittarius"
        else:
            sign = "Scorpio"
    elif month == 12:
        if day >= 22:
            sign = "Capricorn"
        else:
            sign = "Sagittarius"
    return sign

print(what_is_my_sign(15, 5))
    
