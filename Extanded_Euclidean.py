def Ex_eu(a,b) : 

  x0, x1, y0, y1 = 1, 0, 0, 1

  while b!=0 :
    n, a, b = a // b, b, a % b
    x0, x1 = x1, x0 - n * x1
    y0, y1 = y1, y0 - n * y1

  return x0, y0