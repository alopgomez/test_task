# test_task
## Repo to the test coding tasks

### Task 1
The worst-case scenario is when we iterate through the whole list, which leaves us with a complexity of $O(n)$, where $n$ is the number of elements on the first list.

### Task 2
I used numpy to get a somewhat efficient solution, but I doubt it has constant complexity. Another method is to use the *filter* built-in function, but I ignore if this is $O(1)$. If one assumes that there are no duplicates besides 0 in the list argument, then it is posible to convert the list to a set and then filter-out the remaining 0. Such method would be close to $O(1)$, but it loses the order of the original list.
