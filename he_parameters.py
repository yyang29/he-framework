import math


class HeParameters:
  # Class members
  N = None
  L = None
  log_P = None
  dnum = None
  log_q_i = None
  alpha = None
  beta = None

  def __init__(self, N, L, log_P, dnum, log_q_i):
    self.N = N
    self.L = L
    self.log_P = log_P
    self.dnum = dnum
    self.log_q_i = log_q_i

    # Derived parameters
    self.alpha = math.ceil((L + 1) / dnum)
    self.beta = dnum
    self.k = math.ceil(self.log_P / self.log_q_i)

  def display_parameters(self):
    print("HE parameters are: ")
    print(f"N: {self.N}")
    print(f"L: {self.L}")
    print(f"log_P: {self.log_P}")
    print(f"dnum: {self.dnum}")
    print(f"log_q_i: {self.log_q_i}")
    print(f"alpha: {self.alpha}")
    print(f"beta: {self.beta}")
    print(f"k: {self.k}\n")
