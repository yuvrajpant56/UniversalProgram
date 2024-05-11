

#programing assignment 2
Dict_a={0:"    ",1:"[A1]",2:"[B1]",3:"[C1]",4:"[D1]",5:"[E1]",6:"[A2]",7:"[B2]",8:"[C2]",9:"[D2]",10:"[E2]"}
Dict_c={0:"Y",1: "X1",2:"Z1",3:"X2",4:"Z2",5:"X3",6:"Z3",7:"X4",8:"Z4",9:"X5",10:"Z5",11: "X6",12:"Z6",13:"X7",14:"Z7",15:"X8",16:"Z8"}
Dict_l={1:"A1",2:"B1",3:"C1",4:"D1",5:"E1",6:"A2",7:"B2",8:"C2",9:"D2",10:"E2"}

class universal:
  count=0

  primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

  def __init__(self,encode_program,x1,x2,k):
    self.encode_program=encode_program
    self.x1=x1
    self.x2=x2
    self.k=k
    print("\nWELCOME TO PROGRAM ASSIGNMENT 2:")

  def state(self):
    self.State=(self.primes[1]**self.x1)*(self.primes[3]**self.x2)

  def sequence(self):
    encoded_number=self.encode_program+1
    factor=[]
    for prime in self.primes:
      while encoded_number % prime == 0:
        factor.append(prime)
        encoded_number //= prime

        if encoded_number==1:
          break
    if encoded_number>113:
      factor=[]

    factor_count=[]

    if not factor:
      print(f"\nthe number {self.encode_program} cannot be decoded using the listed prime numbers.")
      return None
    else:
      for i in self.primes:
        count=factor.count(i)
        if count>0:
          factor_count.append(count)
        else:
          factor_count.append(0)
      print("factor_count:",factor_count)
      last_one_index=max(loc for loc,val in enumerate(factor_count) if val>=1)
      return factor_count[:last_one_index + 1]

  def solve(self, Godel_sequence):
        self.Godel_sequence=Godel_sequence
        solution = []
        for val in Godel_sequence:
            for a in range(0, 101):
                for z in range(0, 101):
                    if 2**a * (2*z + 1) - 1 == val:
                        for b in range(0, 101):
                            for c in range(0, 101):
                                if 2 ** b * (2 * c + 1) - 1 == z:
                                    solution.append((a, b, c))
        return solution

  def final_solution(self,pair_variable):
    print("\nDecoded Program Instruction:")
    self.pair_variable=pair_variable
    for inst in self.pair_variable:
      a=inst[0]
      b=inst[1]
      c=inst[2]
      str1=Dict_a[a]
      str2=Dict_c[c]
      if b>=3:
        str3=Dict_l[b-2]
      if (b==0):
        output=f"{str1} {str2} <- {str2}"
      elif (b==1):
        output=f"{str1} {str2} <- {str2} + 1"
      elif (b==2):
        output=f"{str1} {str2} <- {str2} - 1"
      else:
        output= f"{str1} IF {str2} != 0 GOTO {Dict_l[b-2]}"

      print(output)




  def state_variable(self):
    U=[]
    print("\nProcessing State Variable Adjustments:")
    print("\nThe length of instruction is:",len(self.Godel_sequence))
    while self.k != len(self.Godel_sequence) + 1 and self.k != 0:

        U=self.pair_variable[self.k-1][1:]
        P=self.primes[U[1]]


        if U[0]==0:
          self.k=self.k+1
          continue

        if U[0]==1:
          self.State=self.State*P
          self.k=self.k+1
          continue

        if self.State%P!=0:
          self.k=self.k+1
          continue

        if U[0]==2:
          self.State//=P
          self.k=self.k+1
          continue

        else:
          for i in range(len(self.Godel_sequence)):
            self.k=0
            if self.pair_variable[i][0]+2==U[0]:
              self.k=i+1
              break
    return self.State

  def print_factors(self):
    print('\nFinal State Value:', self.State)
    print(f'\nDecoding Each Variable in State {self.State}')
    variables = ["Y", "X1", "Z1", "X2", "Z2", "X3", "Z3", "X4", "Z4", "X5", "Z5", "X6", "Z6", "X7", "Z7", "X8", "Z8", "X9", "Z9", "X10"]
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    results = []

    for i, prime in enumerate(p):
        count = 0
        while self.State % prime == 0:
            count += 1
            self.State //= prime
        results.append(count)

    print("\nPrime Factor Decomposition Results:")
    print("--------------------------------------------------------")
    print("{:<8} | {:<15}".format("Variable", "Prime Factor Count"))
    print("--------------------------------------------------------")
    for variable, result in zip(variables, results):
        print("{:<8} | {:<15}".format(variable, result))
    print("--------------------------------------------------------")










k=int(input("enter the value for k (should be 1):"))
encode_program=int(input("enter the encoded program number:"))
x1=int(input("enter the x1 variable value:"))
x2=int(input("enter the x2 variable value:"))
parameter=universal(encode_program,x1,x2,k)
parameter.state()
Godel_sequence=parameter.sequence()
if Godel_sequence is None:
  print("\nDecoding failed. Exiting Program.")
else:
  print("godel_sequence:",Godel_sequence)
  pair_variable=parameter.solve(Godel_sequence)
  print('pair_variable',pair_variable)
  instruction=parameter.final_solution(pair_variable)
  State_output=parameter.state_variable()
  parameter.print_factors()