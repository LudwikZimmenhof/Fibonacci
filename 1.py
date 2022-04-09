import sys, os
from math import log

def fibo(n):
    fibo = [int(sys.argv[1]), int(sys.argv[2])]
    logfibo = []
    for i in [1, 2]:
        try:
            logfibo.append(log(fibo[i-1]))
        except ValueError:
            logfibo.append(0)
    logfibo = [0, 0]
    print(f"1: {sys.argv[1]}    log: {logfibo[0]}\n2: {sys.argv[2]}    log: {logfibo[1]}")
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
        logfibo.append(log(fibo[i]))
        print(f"{i+1}: {fibo[i]}    log: {logfibo[i]}")
    print(f"\nSpelling of the {n} element of table:")
    print(os.system(f"number {fibo[n-1]}"))
    print("")
    phi = fibo[n-1] / fibo[n-2]
    print(f"Golden ratio/Phi: {phi}")

def main():
    try:
        fibo(int(sys.argv[3]))
    except IndexError:
        print("You have to provide 3 parameters:\n'filename.py firstNumberInSeqence secoundNumberInSeqence howManyNumbersToCalculate'\n(eg. 'fibonacci.py 0 1 100')")

main()
