import time

def find_shortest_string_recursive(list):

    if len(list) == 1:
        return list[0]
    
    result = find_shortest_string_recursive(list[1:])

    return list[0] if len(list[0]) <= len(result) else result

def find_shortest_string(list):
  
    return min(list, key = len)

def benchmark(callback):
   
    start_time = time.time()

    for i in range(1000):
        callback()

    return (time.time() - start_time) / 1000

print("Iterative: " + str(benchmark(lambda : find_shortest_string(['cat', 'dogs', '', 'bats', 'flags']))))
print("Recursive: " + str(benchmark(lambda : find_shortest_string_recursive(['cat', 'dogs', '', 'bats', 'flags']))))