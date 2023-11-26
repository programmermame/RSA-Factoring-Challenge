def factorize(number):
    # Implementation of a basic factorization logic
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return (i, int(number/i))
    return None

def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)

