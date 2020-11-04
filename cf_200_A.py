if __name__ == '__main__':
    n,m,k = list(map(int, input().split()))
    selected_seat = []

    for i in range(k):
        s = list(map(int, input().split()))
        if s not in selected_seat:
            selected_seat.append(s)
        else:
            p =
            # p = abs(s[0]-s[1]) + abs(s[0]-s[1])
    print(selected_seat)
