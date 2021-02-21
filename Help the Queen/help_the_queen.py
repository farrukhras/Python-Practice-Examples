import sys

num_test_cases = 0
tests = []

with open(sys.argv[1], 'r') as f:
  num_test_cases = int(f.readline())

  # print("Num test cases = {}".format(num_test_cases))

  for test_case in range(num_test_cases):
    tribe_names = []
    this_test_people = []

    num_men = int(f.readline())

    for i in range(num_men):
      person_desc = f.readline().split()
      obj = {}

      person_tribe = person_desc[0]
      tribe_names.append(person_tribe)

      person_name = ''
      
      for j in range(1, len(person_desc)):
        person_name += person_desc[j].lower()
      
      obj[person_tribe] = person_name
      this_test_people.append(obj)
    
    tribe_names = list(set(tribe_names))

    t_objs = {}
    for t in tribe_names:
      t_objs[t] = []
    
    for p in this_test_people:
      key = list(p.keys())[0]

      if key in list(t_objs.keys()):
        t_objs[key].append(p[key])

    tests.append(t_objs)
  
# print(tests)

def count_men(tests):
  res = []
  for test in tests:
    obj = {}
    for tribe in test:
      count = len(list(set(test[tribe])))
      obj[tribe] = count 
    
    res.append(obj)     

  for i, case in enumerate(res):
    print("Case: {}".format(i))
    for j in sorted(case):
      print(j, case[j])
    
    print("")

count_men(tests)