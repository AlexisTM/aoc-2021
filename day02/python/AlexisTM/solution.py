class Submarine:
    def __init__(self):
        self.depth = 0
        self.x = 0
        self.aim = 0
        
    def move(self, line_str):
        command, amount_str = line_str.split(' ');
        amount = int(amount_str)
        if command == "forward":
            self.x += amount
            self.depth += amount * self.aim
        elif command == "down":
            self.aim += amount
        elif command == "up":
            self.aim -= amount

if __name__ == '__main__':
    submarine = Submarine()
    with open('input.txt', 'r') as f:
        for line in f:
            submarine.move(line)
    print(submarine.x * submarine.depth)