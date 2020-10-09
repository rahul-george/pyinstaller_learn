def funky_lowerise(name):
    name_low = name.lower()
    nList = []
    for i, c in enumerate(name_low):
        if i%2==0:
            nList.append(c)
        else:
            nList.append(c.upper())
    return "".join(nList)


if __name__ == "__main__":
    print(funky_lowerise("meenakshi"))