if __name__ == '__main__':
    resultList = []

    for _ in range(int(input("Enter"))):
        tempList = []  # Create a new tempList for each iteration
        name = input()  # Enter a name
        score = float(input())  # Enter a score

        tempList.append(name)
        tempList.append(score)

        resultList.append(tempList)

    # Sort the list based on scores (ascending order)
    resultList.sort(key=lambda x: x[1])

    # Find the second-lowest grade
    lowestGrade = resultList[0][1]
    for entry in resultList:
        if entry[1] > lowestGrade:
            secondLowestGrade = entry[1]
            break

    # Create a list of names with the second-lowest grade
    secondLowestNames = [entry[0] for entry in resultList if entry[1] == secondLowestGrade]

    # Sort the names alphabetically
    secondLowestNames.sort()

    for name in secondLowestNames:
        print(name)