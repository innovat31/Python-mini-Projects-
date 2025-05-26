import time
from decimal import Decimal, getcontext


def compute_pi_chudnovsky(precision):
    getcontext().prec = precision + 5
    C = 426880 * Decimal(10005).sqrt()
    K, M, X, L = 6, 1, 1, 13591409
    S = L

    for i in range(1, precision):
        M = (K**3 - 16*K) * M // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return str(+pi)[:precision + 2]  # 3. + n digits


def compute_pi_leibniz(terms):
    getcontext().prec = terms + 5
    pi = Decimal(0)
    for k in range(terms):
        pi += Decimal((-1)**k) / (2*k + 1)
    pi *= 4
    return str(+pi)


def benchmark(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, round(end - start, 4)


def format_pi(pi_str, group=50):
    pi_digits = pi_str[2:]  # Exclude "3."
    grouped = [pi_digits[i:i+group] for i in range(0, len(pi_digits), group)]
    return f"3.{pi_digits[:group]}\n" + '\n'.join(grouped[1:])


def main():
    print("=== Pi Calculator (Intermediate Edition) ===")
    try:
        digits = int(input("Enter number of digits to calculate (10–1000): "))
        if digits < 10 or digits > 1000:
            print("Range too wide. Try between 10–1000.")
            return

        print("\nChoose algorithm:")
        print("1. Chudnovsky (fast & accurate)")
        print("2. Leibniz (slow & simple)")
        algo_choice = input("Enter choice (1 or 2): ")

        if algo_choice == '2':
            print("Note: Leibniz series is very slow. Be patient.")
            pi_str, duration = benchmark(compute_pi_leibniz, digits)
        else:
            pi_str, duration = benchmark(compute_pi_chudnovsky, digits)

        formatted_pi = format_pi(pi_str)
        print("\nResult:\n")
        print(formatted_pi)
        print(f"\nTime taken: {duration} seconds")

        save = input("\nSave result to file? (y/n): ").lower()
        if save == 'y':
            with open("pi_digits_output.txt", "w") as f:
                f.write(f"Pi to {digits} digits:\n{formatted_pi}\nTime: {duration}s\n")
            print("Saved to pi_digits_output.txt")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
