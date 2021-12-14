
def read_input(filepath):
    numbers = list()
    with open(filepath, "r") as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def sliding_window(puzzle):
    puzzle_sliding = list()
    for i in range(len(puzzle) - 2):
        puzzle_sliding.append(puzzle[i] + puzzle[i+1] + puzzle[i+2])
    return puzzle_sliding

if __name__ == '__main__':
    puzzle = read_input("input.txt")
    total = 0
    last_val = 0
    puzzle = sliding_window(puzzle)
    for i in range(len(puzzle)):
        val = puzzle[i]
        if i == 0: 
            last_val = val
            continue
        if val > last_val:
            total += 1
        last_val = val
    print(total)
