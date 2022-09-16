import time

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   # TODO 1: adjacents
   # Your code goes here
   return adj_set

def generate_path(current, explored):
   list = [current]
   count = 0
   while explored[current] != "s":       #assume the parent of root is "s"
      list.append(explored[current])
      current = explored[current]
      count += 1
   return (list[::-1], count+1)

def BFS(start, end, word_dict):
   ''' you can modify this method '''
   explored = {start:"s"}
   return (["No solution"], 0)

def recur(start, end, word_dict, explored, limit):
   ''' your code goes here '''
   return None
 
def DLS(start, end, word_dict, limit):
   explored = {start:"s"}
   return recur(start, end, word_dict, explored, limit-1)

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))

   # Test BFS
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   path_and_steps = (BFS(initial, goal, word_dict))
   if path_and_steps != None:
      print ("Path:", path_and_steps[0])
      print ("The number steps: {}".format(path_and_steps[1]))
   else:
      print ("Solution not found in {} steps".format(limit))
 
   # Test DLS
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   limit = int(input("Type the limit: "))
   path_and_steps = (DLS(initial, goal, word_dict, limit))
   if path_and_steps != None:
      print ("Path:", path_and_steps[0])
      print ("steps within {} limit:".format(limit), path_and_steps[1])
   else:
      print ("Solution not found in {} steps".format(limit))
   
   # Now, start iterative deepening
   '''Your code goes here'''
   
   # Print out the shortest path and length of the path (number of steps)
   

if __name__ == '__main__':
   main()
