# Exercise 4
1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan
    > Divide-and-conquer is used first based on the sign, then a linear search is used to find the room.
2. How many “steps” it will take to find room EY128? And what is a “step” in this case?
    > 15 steps, a step is a move from one room to another (Walking from main door to the first room also counts as one step).
3. Is this a best-case scenario, worst-case scenario, or neither?
    > Worst-case scenario.
4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like
    > Trying to find EY100 and EY138 are best cases; trying to find EY128 is the worst case.
5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient?
    > I would change the sign in my mind to the graph below, after the new divide-and-conquer, I would do linear search to find the room. 

| ⬅ EY 100-118 | EY 120-138 ➡ |
|--------------|--------------|
 