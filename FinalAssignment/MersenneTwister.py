class MersenneTwister:

    def __init__(self, seed=1234):
        self.seed = seed
        self.w = 32
        self.r = 31
        self.n = 624
        self.m = 397
        self.u = 11
        self.s = 7
        self.t = 15
        self.l = 18
        self.a = 0x9908b0df
        self.b = 0x9d2c5680
        self.c = 0xefc60000
        self.f = 0x6c078965
        self.lower = 4294967295
        self.upper = 0
        self.array = self.init_array()
        self.generate_numbers()
        self.amount_of_numbers_requested = 0

    def init_array(self):
        """
        Initialization of the seed array
        :return: Seed array (length = n)
        """
        array = [self.seed]  # First value of the seed array is the input seed
        for i in range(1, self.n):
            array.append(0)
            array[i] = (self.f * (array[i - 1] ^ (array[i - 1] >> (self.w - 2))) + i) & 0xffffffff
        return array

    def generate_numbers(self):
        """
        Generates n amount of random int32
        :return: List of random int32
        """
        y = []
        for i in range(self.n):
            y1 = self.array[i]
            y2 = self.array[(i + 1) % self.n]  # When i+1 is out of index it needs to start again by 0
            y3 = (self.array[(i + self.m) % self.n])  # When i+m is out of index it needs to start again by 0
            x = str(bin((y1 & self.upper) + (y2 & self.lower)))[2:]
            if x[-1] == '0':
                x = int(x, 2) >> 1
            elif x[-1] == '1':
                x = int(x, 2) ^ self.a
            x = x ^ y3
            curr_y = x
            curr_y = curr_y ^ (curr_y >> self.u)
            curr_y = curr_y ^ ((curr_y << self.s) & self.b)
            curr_y = curr_y ^ ((curr_y << self.t) & self.c)
            curr_y = curr_y ^ (curr_y >> self.l)
            y.append(curr_y)
        self.array = y  # Set the seed array to current output
        return y

    def get_random_number(self):
        """
        Gives one random int32
        This class makes n amount of random numbers
        When all the produced random numbers are used it creates a new array of n random numbers
        :return: Unused random int32
        """
        if self.amount_of_numbers_requested >= len(self.array):
            self.amount_of_numbers_requested = 0
            self.generate_numbers()
        self.amount_of_numbers_requested += 1
        return self.array[self.amount_of_numbers_requested - 1]

    def get_random_number_0_1(self):
        return self.get_random_number() / 4294967295

