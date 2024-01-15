import random

def generate_prisoners():
    return [{'number': i, 'found': False} for i in range(1, 101)]

if __name__=='__main__':
    print(generate_prisoners())
