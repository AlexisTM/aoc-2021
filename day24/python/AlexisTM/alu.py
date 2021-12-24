class ALU:
    def __init__(self):
        self.input = []

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

    def inp(self, a, val):
        value_read = self.input.pop(0)
        self.internals[a] = int(value_read)

    def add(self, a, val):
        self.internals[a] = self.internals[a] + val

    def mul(self, a, val):
        self.internals[a] = self.internals[a] * val

    def div(self, a, val):
        self.internals[a] = int(self.internals[a]/val)

    def mod(self, a, val):
        self.internals[a] = self.internals[a] % val

    def eql(self, a, val):
        self.internals[a] = 1 if self.internals[a] == val else 0

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

        val = 0
        try:
            if(b):
                val = int(b)
        except Exception as ex:
            val = self.internals[b]

        self.functions[command](a, val)

    def get(self, a):
        return self.internals[a]
