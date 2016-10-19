bb = input("what is the y intercept?")
mm = input("what is the slope?")
how = input("How many repetitions?")
dmain = input("what is the domain?")
yy = bb + (mm * how)

print yy

while how > 0:
  how = how - dmain
  yy = bb + (mm * how)
  print yy
