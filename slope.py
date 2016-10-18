bb = input("what is the y intercept?")
mm = input("what is the slope?")
how = input("what is the ending x value?")
yy = mm + (bb * how)
print yy

while how > 0:
  how = how - 1
  yy = mm + (bb * how)
  print yy how
