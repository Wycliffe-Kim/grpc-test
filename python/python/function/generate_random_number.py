from random import random

def generate_random_number(*, min: float = 0.0, max: float = 100.0):
    return (random() * (max - min)) + min