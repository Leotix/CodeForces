def numOfProblemsSolved():
    numOfProblems = int(input())
    numOfSolved = 0
    for i in range(numOfProblems):
        sureSolution = [int(x) for x in input().split()]
        if sureSolution.count(1) >= 2:
            numOfSolved += 1
    print(numOfSolved)

if __name__ == "__main__":
    numOfProblemsSolved()
