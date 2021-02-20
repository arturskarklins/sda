# Task

Create racing simulation with Dataclass and some loops. General idea object must have model name (car of participant) as only field, can hav some default as well. Class should have two class variables (note: not private, but class variables), that can't be redefined by object `self.track` (as length of race, ex. 50) and `self.kms` (driven kms per participant, always 0).

Must have method `driving()` which accepts one argument as number. If number can be divided by 2 - car goes 5km, if can be divided by 3 - car goes 3km, by 5 - car goes 1km. Increment `self.kms` accordingly.

Other method is `finnish()` if driver has reached track end (`self.kms >= self.track`?), it should return `True` otherwise `False`.

Generate the number to parse for `driving()` randomly, to get movement of car.

Print out participants position (how far the car is, the model and kms) after each increment.

NOTE: participants in race shouldn't be limited, so it's one to whatever, hint: use list, that will make things much more easier.

When first car reached the finnish (that is track length) it should give message `*** Driver Audi won the race! ***` and exit the race.

You can add `time.sleep(1)` after each increment to follow more easily and see the progress.

# Result (fragment)
The way how you log the progress is optional and up to you, this is just an option.

```
BMV => 30 km | Audi => 31 km | Volga => 22 km | 
BMV => 35 km | Audi => 31 km | Volga => 22 km | 
BMV => 35 km | Audi => 36 km | Volga => 27 km | 
BMV => 36 km | Audi => 39 km | Volga => 32 km | 
BMV => 37 km | Audi => 44 km | Volga => 37 km | 
BMV => 42 km | Audi => 49 km | Volga => 40 km | 
BMV => 45 km | Audi => 49 km | Volga => 40 km | 
*** Driver Audi won the race! ***
```

# Hints

- class variables in Dataclasses are defined "differently", look for `typing.ClassVar`
- for random int generation use `import random` and then `random.random()`, might need some fine-tuning here
- to keep the race going `while True` might come handy with `break` at "some" point 