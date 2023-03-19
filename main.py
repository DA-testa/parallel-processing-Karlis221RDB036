# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    next_time = [0] * n
    for i in range(m):
        smallest = next_time.index(min(next_time))
        output.append([smallest, next_time[smallest]])
        next_time[smallest] += data[i]
    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    f_line = input()
    n = int(f_line.split()[0])
    m = int(f_line.split()[1])
    s_line = input()
    data = list(map(int, s_line.split()))
    assert len(data) == m

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
