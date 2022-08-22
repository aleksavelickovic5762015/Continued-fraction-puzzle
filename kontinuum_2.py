from decimal import *
import time, operator, math
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n) - 1)))


def koren(x):
    getcontext().prec = 100
    return Decimal(x).sqrt()


def simplify_razlomak(seq):
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num * u, num
    return num, den


def mk_kontinualni(m_koren, M):
    seq = []
    irac = m_koren
    while True:
        seq.append(int(irac))
        irac = 1 / (irac - int(irac))
        num, den = simplify_razlomak(seq)
        if den > M:
            break
        else:
            num_max, den_max = num, den
    return num_max, den_max


def zajednicki_imenilac(M, N):
    razlomci = []
    razlomci_2 = []
    for m in islice(count(2), 10 ** 15):
        nekvadratni = math.sqrt(m)
        if nekvadratni != int(nekvadratni):
            num_M, den_M = mk_kontinualni(koren(m), M)
            if isPrime(den_M):
                razlomci.append((m, num_M, den_M))
        if m % 250 == 0:
            """
            prodji kroz listu razlomaka i proveri uslove na svakih __ iteracija
            """
            razlomci = sorted(razlomci, key=operator.itemgetter(2))
            len_razlomci = len(razlomci)
            for i in islice(count(0), len_razlomci):
                if i == len_razlomci - 1:
                    break
                if razlomci[i][2] == razlomci[i + 1][2]:
                    num_N_i, den_N_i = mk_kontinualni(koren(razlomci[i][0]), N)
                    num_N_i_1, den_N_i_1 = mk_kontinualni(koren(razlomci[i + 1][0]), N)
                    if den_N_i == den_N_i_1 and isPrime(den_N_i):
                        razlomci_2.append((razlomci[i][0], razlomci[i + 1][0]))
            razlomci_2 = sorted(razlomci_2, key=operator.itemgetter(0))
            print("brojevi su: {} i {}".format(razlomci_2[0][0], razlomci_2[0][1]))
            return


if __name__ == "__main__":
    M, N = 17.59 * 10 ** 9, 6.2415093414 * 10 ** 18

    pocetak = time.time()
    zajednicki_imenilac(M, N)
    print("\n")
    print("traje {0:.2f} sekundi".format(time.time() - pocetak))
