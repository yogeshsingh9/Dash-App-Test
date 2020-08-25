import numpy as np

class Sim:
    def __compute_delay(self, S, T):
        size = S.shape[0]
        D = [max(S[0] - T[0], 0)]
        prev = 0
        for i in np.arange(1, size):
            D.append(max(S[i] + prev - T[i], 0))
            prev = D[i]
        return np.array(D)

    def simulateSSQ(self, lam=1.0, b=3.0, size=10000):
        S = np.random.poisson(lam=lam, size=size)
        T = np.random.uniform(low=1.0, high=b, size=size)
        D = self.__compute_delay(S, T)

        return S, T, D
