# NOTES
# 2^2 + 2^3 + x^4 < 50M
# x^4 < (50M - 12)
# X^4 max integer is 84

# Check
# 84^4 + 12 < 50M
# 85^4 + 12 > 50M

# Primes below 84 for 4 root

# Primes below ? For 3 root

# x^3 < 50M - 20
# X^3 Max integer is 368


# x^2 < 50M -24

# x^2 max integer is 7071

# Primes below 7071 ~ 1000
# Primes below 368 ~ 73
# Primes below 84 ~ 12

# 12 * 73 * 1000

# 876000 combinations

# Somewhat brute-forcible with easy check.



FOURTH_ROOT_LIMIT = 84
CUBE_ROOT_LIMIT = 368
SQUARE_ROOT_LIMIT = 7071
FIFTY_MIL = 50_000_000


# Calculate all primes
all_primes = []

def is_prime(n):
    return not any(n % i == 0 for i in all_primes)

for i in range(2, SQUARE_ROOT_LIMIT + 1):
    if is_prime(i):
        all_primes.append(i)

# 908 total
# 73 under 368
# 23 under 84
# 1524532 combinations
# print(len([i for i in all_primes if i < 84]))


distinct_number_set = set()
# Iterate 4th roots first.
for x in filter(lambda p: p < FOURTH_ROOT_LIMIT, all_primes):
    fourth_root_term = x ** 4
    for y in filter(lambda p: p < CUBE_ROOT_LIMIT, all_primes):
        cube_root_term = y ** 3
        for z in filter(lambda p: p < SQUARE_ROOT_LIMIT, all_primes):
            square_root_term = z ** 2
            value = square_root_term + cube_root_term + fourth_root_term
            if value < FIFTY_MIL:
                distinct_number_set.add(value)                
            else:
                break

print(len(distinct_number_set))