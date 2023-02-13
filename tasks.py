import numpy as np

def task_one(l1, l2):
  return [i for i in l1 if i not in l2]

def task_two(ar):
  new_ar = np.array(ar)
  ind = np.where(new_ar != 0) # indexes to filter zeros out
  return list(new_ar[ind])

def main():
  # task_one
  print("task 1: {0}".format(task_one([1,2,3,4,5,'a'],[2,3,4])))
  
  # task two
  array = [0,1,0,0,4,5,6,7,0,8,-4,0]
  print("task 2: {0}".format(task_two(array)))

if __name__ == '__main__':
  main()