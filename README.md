# prime.py
Prime Number Checker. This project identifies prime numbers. Generating a list of prime numbers from two given points. Useful for learning basic algorithms, practicing Python.

## Usage

```bash
python main.py
```

Enter a start and end range when prompted. All prime numbers in that range will be printed.

## Example

```
Enter start range: 1
Enter end range: 50
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
```

## How it works

1. `is_divisible_by(n, by)` — checks if n is divisible by a number
2. `is_prime(n)` — returns True if n has no factors up to √n
3. `primes_in_range(start, end)` — iterates the range and prints primes
