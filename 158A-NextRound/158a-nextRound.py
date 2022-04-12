def advancedParticipants():
    x = input().split()
    n = int(x[0])
    k = int(x[1])
    howManyPasses = 0
    scores = input().split()
    for i in range(n):
        scores[i] = int(scores[i])
    limit = scores[k-1]
    for score in scores:
        if score >= limit and score > 0:
            howManyPasses += 1
    print(howManyPasses)

if __name__ == "__main__":
    advancedParticipants()
