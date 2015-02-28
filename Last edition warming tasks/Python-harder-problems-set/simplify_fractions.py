def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    i = 2
    while i <= fraction[0]:
        if nominator % i == 0 and denominator % i == 0:
            nominator = nominator / i
            denominator = denominator / i
        else:
            i += 1
    result = (int(nominator), int(denominator))
    return result

print(simplify_fraction((63,462)))
