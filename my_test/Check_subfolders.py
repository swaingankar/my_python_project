import os

def fcount(path, map = {}):
  count = 0
  for f in os.listdir(path):
    child = os.path.join(path, f)
    if os.path.isdir(child):
      child_count = fcount(child, map)
      count += child_count + 1 # unless include self
  map[path] = count
  print(map)
  return count

path = "c:/users/Sachin/Desktop/"
map = {}
print(fcount(path, map))