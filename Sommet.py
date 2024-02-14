class Sommet:
    def __init__(self, name, weight):
        self.name = name
        self.Gamma = set()
        self.GammaMinusOne = set()
        self.weight = weight
    def GamaN(self,n=1):
        res = set()
        if (n == 1):
            return self.Gamma
        elif (n > 1):
            for i in self.Gamma:
                res.add(i.GamaN(n-1))
        return res
    def GamaMinusN(self, n=-1):
        res = set()
        if (n == -1):
            return self.GammaMinusOne
        elif (n < -1):
            for i in self.GammaMinusOne:
                res.add(i.GamaMinusN(n - 1))
        return res