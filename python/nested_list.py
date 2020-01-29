if __name__ == '__main__':
    marksheet =[]
    scorelist= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name,score])
        scorelist.append(score)

    second_least = sorted(set(scorelist))[1]

    least_marks = []
    for i,j in sorted(marksheet):
        if second_least == j:
            print(i)
