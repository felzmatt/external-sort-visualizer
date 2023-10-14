import random
import string

def generate_random_tuple():
    # Generate random elements based on the specified criteria
    rand_int = random.randint(1, 9999)
    rand_string_length = random.randint(3, 5)
    rand_string = ''.join(random.choices(string.ascii_uppercase, k=rand_string_length))
    rand_float = round(random.uniform(800.0, 3999.99), 2)

    return (rand_int, rand_string, rand_float)
