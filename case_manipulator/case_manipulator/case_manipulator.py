import sys
# sys.path.append(r"C:\Users\Temp\Work\Temporary\scratch_area\lowerise")
# sys.path.append(r"C:\Users\Temp\Work\Temporary\scratch_area\capitalize")
print(sys.path)



def capitalize_name(name: str):
    from capitalize import capitalize
    print("Captialized name is {}".format(capitalize.Capitalize(name)))

def lowerize_name(name: str):
    from lowerise import lowerise
    print("Lowerized name is {}".format(lowerise.Lowerise(name)))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        if "--lower" == sys.argv[1]:
            lowerize_name(sys.argv[2])
        elif "--upper" == sys.argv[1]:
            capitalize_name(sys.argv[2])
        else:
            sys.exit(-1)
    else:
        sys.exit(-1)