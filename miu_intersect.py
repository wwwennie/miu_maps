from sympy import Symbol, sympify, solve, Eq, symbols
from sympy.utilities.lambdify import lambdify


def linear_intersect(lambda1,lambda2):
  """ Given two lambda functions corresponding to linear y=mx+b
      Find the point of intersection 

      x_intersect = (b2-b1)/(m1 - m2)
      intersect = (tuple) (x,y) intersect
  """
  intersect = (None,None)

  # extract b's 
  b1 = lambda1(0.0)
  b2 = lambda2(0.0)
  # sample for m's
  m1 = lambda1(2.0)-lambda1(1.0)
  m2 = lambda2(2.0)-lambda2(1.0)
 
  x_intersect = (b2-b1)/(m1-m2)
  y1_intersect = lambda1(x_intersect)
  y2_intersect = lambda2(x_intersect)
  
  if abs(y1_intersect - y2_intersect) < 1e-8:
    intersect = (x_intersect,y1_intersect)
  
  return intersect
