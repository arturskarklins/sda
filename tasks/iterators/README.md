# Task
Create a solution for iterator, which takes argument `number` (as amount) and returns random numbers (must be `int`) based on the input argument. Add default 1, so if user doesn't give input it returns at least one randomly generated number.
Please, re-create the same solution with generator functions.

Additionally create function that sums all digits per given number and print together with the randomly created number. This can be a separate function, outside the iterator class.
That is, sum for 12345 is 15, for 67890 it's 30, etc.

# Result
Should be like:
```
Number's 009384158649228813 sum is 81
Number's 7234965590355266 sum is 77
Number's 7854001348904018 sum is 62
Number's 06202532767415192 sum is 62
Number's 19066650624093717 sum is 72
```

# Hints

- random number generation is done by `import random` and `random.random()`. Note that the returned value is float, handle so that returned value is `int`.

# Solution

Attached to as .py file to this directory.