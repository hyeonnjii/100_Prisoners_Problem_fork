import random

def generate_prisoners(num_prisoners=100):
    return list(range(1, num_prisoners + 1))


if __name__=='__main__':
    print(generate_prisoners())
