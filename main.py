"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  """Compute the value of the recurrence $W(n) = aW(n/b) + n

  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor

  Return"""
  
  if n==0:
    return 0
  elif n==1:
    return 1
  else: 
    return a*simple_work_calc(n//b, a, b) + n

def work_calc(n, a, b, f):
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
           the work done at each node 

  Returns: the value of W(n).
  """
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return a*work_calc(n//b, a, b, f) + f(n)

def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
           the work done at each node 
  
  Returns: the value of W(n).
  """
  if n == 1:
    return 1
  else:
    return (
        span_calc(n // b, a, b, f) + f(n)
    ) 

import math
fn1 = lambda n : 1
fn2 = lambda n : math.log2(n)
fn3 = lambda n : n
fn4 = lambda n : n**0.5
fn5 = lambda n : n**1
fn6 = lambda n : n**2

def compare_work(work_fn1, work_fn2, work_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		result.append((
			n,
      work_calc(n, 2, 2, work_fn1),
      work_calc(n, 2, 2, work_fn2),
      work_calc(n, 2, 2, work_fn3)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n','f(n)=1', 'f(n)=log_2(n)','f(n)=n'],
							floatfmt=".3f",
							tablefmt="github"))


print_results(compare_work(fn4, fn5, fn6))



def compare_span(span_fn1, span_fn2, span_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
  Compare the values of different recurrences for 
  given input sizes.

  Returns:
  A list of tuples of the form
  (n, work_fn1(n), work_fn2(n), ...)

  """
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((n, span_fn1(n), span_fn2(n), span_fn3(n)))

  #print_results(result)
  return result
