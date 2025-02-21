# Random Restart Hill Climbing to solve the Scales Problem

Design your algorithm for RRHC and implement it to solve the problem. Your algorithm design should cover the following areas:
1. Explain the problem and the fitness function.
1. What is the solution representation?
1. What data structure do you use for the solution?
1. What is the strategy for small change you use for the algorithm?
1. What is the number of restarts you use in the experiment?
1. What is the number of iterations you use in the experiment?
1. Consider writing auxiliary methods in your program to support the experiment for exceptional marks. Examples:
- writing the raw dataset to a CSV file
- reading datasets from the CSV file
- writing results to a CSV file, etc.,

## Implementation

```
main.py           -- benchmarking tests exercising the approach
hill_climbing.py  -- implementation of Random Restart Hill Climbing
scales_problem.py -- implementation of Scales Problem
aux.py            -- file I/O
analysis.py       -- graphing the results

test/*.py         -- unit tests
```

# To Test
```
python3 -m unittest discover -s tests
```

# To Run
```
python3 main.py
```