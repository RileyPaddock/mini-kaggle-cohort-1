b_0, b_1 = (2.5389802665309413, -0.5565010793760151)

def logistic_fit(b_0, b_1, x):
  return 8/(1+math.e**(-1*(b_0 + b_1*x))) - 2

