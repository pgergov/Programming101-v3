def nan_expand(times):
    result = ""
    if times == 0:
        return ""

    for i in range(times):
        result += "Not a "
    result += "NaN"

    return result


def iterations_of_nan_expand(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")
    return False

def main():
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN "))
    print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))

if __name__ == '__main__':
    main()