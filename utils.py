import random
import string


def _rand_str(n=6):
    return ''.join(random.choices(string.ascii_letters, k=n))