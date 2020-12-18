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

    def init_array(self):
        pass

    def generate_number(self):
        pass
