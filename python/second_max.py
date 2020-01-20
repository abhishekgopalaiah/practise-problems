if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr_max = max(arr)
    remove_max = [i for i in arr if i!=arr_max]
    print(max(remove_max))