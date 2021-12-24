class MathALU:
    def __init__(self):
        self.input = []
        self.input_counter = 0

        self.internals = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
        }

        self.functions = {
            "inp": self.inp,
            "add": self.add,
            "mul": self.mul,
            "div": self.div,
            "mod": self.mod,
            "eql": self.eql,
        }

    def set_input(self, input_str):
        self.input = list(input_str)

    def reset(self):
        self.input = []
        self.internals = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
        }
        self.input_counter = 0

    def inp(self, a, b):
        math = "{} = input[{}]".format(a, str(self.input_counter))
        self.input_counter = self.input_counter + 1
        return math

    def add(self, a, b):
        math = "{} = {} + {}".format(a, a, b)
        return math

    def mul(self, a, b):
        math = "{} = {} * {}".format(a, a, b)
        return math

    def div(self, a, b):
        math = "{} = {} / {}".format(a, a, b)
        return math

    def mod(self, a, b):
        math = "{} = {} % {}".format(a, a, b)
        return math

    def eql(self, a, b):
        math = "{} = {} == {}".format(a, a, b)
        return math

    def run(self, request):
        request = request.split(" ")
        if len(request) < 2:
            print("Invalid instruction: ", request)
            return
        command = request[0]
        a = request[1]
        b = ""
        if len(request) > 2:
            b = request[2]

        return self.functions[command](a, b)

    def get(self):
        return self.internals
