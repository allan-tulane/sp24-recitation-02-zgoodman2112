# CMPS 2200  Recitation 02

**Name (Team Member 1):**______Kevin Skelly______ 
**Name (Team Member 2):**______Zach Goodman______

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

As seen below, f(n) exerts asymptotic dominance over f(n) = log n, which dominates f(n) = 1. This is because the total amount of work at each level is higher. It can also be seen that f(n) = 1 has more of a linear increase with increasing n, being leaf-dominated. f(n) is more of a balanced function, and f(n) = n has a geometric increase. 

|     n |   f(n)=1 |   f(n)=log(n) |   f(n)=n |
|-------|----------|---------------|----------|
|    10 |       15 |        19.966 |       36 |
|    20 |       31 |        44.253 |       92 |
|    50 |       63 |       107.311 |      276 |
|   100 |      127 |       221.265 |      652 |
|  1000 |     1023 |      1896.421 |     9120 |
|  5000 |     8191 |     12497.283 |    61728 |
| 10000 |    16383 |     25007.854 |   133456 |

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asymptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

From the chart below, one can conclude that W(n) is the most asymptotically dominant when c>log_b(a). The next highest asymptotic dominant work function is when c = log_b(a), while c < log_b(a) is the asymptotically weakest work function. As one could see, at each level of n, the value of work is highest in the most asymptotic function, and this holds true throughout all values of n.


|     n |   c<log_b(a) |   c=log_b(a) |   c>log_b(a) |
|-------|--------------|--------------|--------------|
|    10 |       21.291 |           36 |          174 |
|    20 |       47.055 |           92 |          748 |
|    50 |      110.236 |          276 |         4790 |
|   100 |      230.472 |          652 |        19580 |
|  1000 |     2075.117 |         9120 |      1990744 |
|  5000 |    14251.208 |        61728 |     49957880 |
| 10000 |    28602.416 |       133456 |    199915760 |



- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

|     n |    f(n)=1 |   f(n)=log_2(n) |    f(n)=n |
|-------|-----------|-----------------|-----------|
|    10 |    21.291 |              36 |       174 |
|    20 |    47.055 |              92 |       748 |
|    50 |   110.236 |             276 |      4790 |
|   100 |   230.472 |             652 |     19580 |
|  1000 |  2075.117 |            9120 |   1990744 |
|  5000 | 14251.208 |           61728 |  49957880 |
| 10000 | 28602.416 |          133456 | 199915760 |
