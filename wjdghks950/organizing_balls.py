def organizingContainers(container):
    n = len(container)
    col_sum = sorted([sum(x) for x in zip(*container)])
    row_sum = sorted([sum(r) for r in container])
    if col_sum = row_sum:
        return "Possible"
    return "Impossible"

if __name__ == "__main__":
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

            result = organizingContainers(container)

            print(result)

