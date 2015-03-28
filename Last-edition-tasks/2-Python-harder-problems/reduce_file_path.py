def reduce_file_path(path):
    path = path.split('/')
    result = ["/"]
    final_path = ""
    
    for item in path:
        if item == "" or item == ".":
            pass
        elif item == "..":
            if result == ["/"]:
                pass
            else:
                del result[len(result) - 1]
        else:
            result.append(item + "/")

    for index, word in enumerate(result):
        if index == len(result) - 1 and word != "/":
            word = word.replace("/", "")
        final_path += word

    return final_path
print(reduce_file_path("/home//radorado/code/./hackbulgaria/week0/../"))
