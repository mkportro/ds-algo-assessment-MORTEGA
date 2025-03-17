# Big O Assessment

1. What is the time and space complexity of first_repeated_element? How does the use of a set affect performance? 
```
def first_repeated_element(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None
```

Answer:
<!-- Write your answer here -->

2. What is the time and space complexity for count_unique_pairs? How does the 
```
def count_unique_pairs(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count
```

Answer:
<!-- Write your answer here -->

3. What is the time and space complexity of divide_until_one? How does n influence the number of steps?
```
def divide_until_one(n):
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps
```

Answer:
<!-- Write your answer here -->

4. What is the time and space complexity of orangize_and_rank_students? How does each step of the function affect the overall runtime?
```
def organize_and_rank_students(students):
    # Step 1: Normalize names
    students = [name.strip().title() for name in students]

    # Step 2: Sort students alphabetically
    students.sort()

    # Step 3: Assign rankings based on sorted order
    rankings = {name: rank + 1 for rank, name in enumerate(students)}

    return rankings
```

Answer: 
<!-- Write your answer here -->

5. What is the time and space complexity of count_ways_to_climb? What happens to the number of recursive calls as n increases?
```
def count_ways_to_climb(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways_to_climb(n - 1) + count_ways_to_climb(n - 2)
```

Answer: 
<!-- Write your answer here -->