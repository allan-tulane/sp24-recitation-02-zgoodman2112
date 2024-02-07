from main import *

def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(1,1,1) == 1
  assert simple_work_calc(24, 8, 2) == 6136
  assert simple_work_calc(32, 6, 2) == 11648

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(20, 4, 2, lambda n: n*n) == 1712
  assert work_calc(40, 4, 2, lambda n: n*n*n) == 123072
  assert work_calc(100, 10, 5, lambda n: 3) == 333


import math
fn1 = lambda n : 1
fn2 = lambda n : math.log2(n)
fn3 = lambda n : n
def test_compare_span():
  def span_fn1(n):
    return span_calc(n, 2, 2, lambda n: n)

  def span_fn2(n):
    return span_calc(n, 2, 2, lambda n: math.log2(n))
  def span_fn3(n):
    return span_calc(n, 2, 2,lambda n: n)
  res = compare_span(span_fn1, span_fn2, span_fn3)
  print_results(res)



test_compare_span()
