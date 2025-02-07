# Aggressive Cow Problem

Write a Python program to solve the “AGGRESSIVE COW PROBLEM” using two different
approaches (basic method and binary search) and execute them. First, implement the
solution with the “First Approach”, where you attempt to place the cows, verifying the
distance at each stall. Then, implement the “Second Approach”, which refines the solution
through binary search to find the optimal minimum distance between cows.

For each approach, you must incorporate the appropriate functions, such as for placing cows
and validating distances, along with data items mentioned in the problem statement. Assume
we always start by placing the first cow at the first stall available in both the approaches.

## Implementation

```
main.py                   -- benchmarking tests exercising both approaches
aggressive_cows.py        -- facade to implementation of both approaches
aggressive_cows_linear.py -- implementation of "First Approach" (linear or basic method)
aggressive_cows_binary.py -- implementation of "Second Approach" (binary search method)
distance_ok.py            -- common implementation to determine if cow can fit in stall

test/test_aggressive_cows.py -- unit tests
```

Benchmarking tests in [main.py](main.py) create a collection of increasing numbered stalls 
and attempts to fit cows into the stalls to discover the largest minimum distance between
stalls. Output is written to CSV file for ease of analysis to compare two approaches.

# To Test
```
python3 -m unittest discover -s tests
```

# To Run
```
python3 main.py
```