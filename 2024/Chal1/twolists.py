
def main():
    f = open("./2024/Chal1/input.txt", "r")
    first = [0]
    second = [0]
    for line in f:
        for index, num in enumerate(line.split()):
            if (index == 0):
                first.append(int(num))
            elif (index == 1):
                second.append(int(num))
    f.close()
    first.sort()
    second.sort()
    sum = 0
    for num in range(len(first)):
        difference = abs(first[num] - second[num])
        sum += difference
    print(sum)

if __name__ == "__main__":
    main()