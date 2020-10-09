def CountVowels(name:str):
    vcount = 0
    for c in name.lower():
        if c in {'a', 'e', 'i', 'o', 'u'}:
            vcount+=1
    return vcount


if __name__ == "__main__":
    print(CountVowels("RAHUL"))