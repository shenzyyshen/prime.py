# Dev Notes

## Algorithm
- Trial division: check divisibility up to sqrt(n)
- `number ** 0.5` avoids checking every number up to n
- Any factor above sqrt(n) would have a corresponding factor below it

## Time Complexity
- `is_prime(n)` runs in O(√n) time
- `primes_in_range(start, end)` runs in O((end - start) × √end)
- Much more efficient than checking all numbers up to n

## Edge Cases
- Numbers ≤ 1 are not prime (handled by the `if number <= 1` guard)
- 2 is the only even prime — the loop starts at 2 so it's caught correctly
- Negative numbers return False
