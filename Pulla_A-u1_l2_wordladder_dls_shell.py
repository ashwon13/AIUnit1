from argparse import BooleanOptionalAction
import time



def isAdjacent(current, word):
   count=0
   for i in range(len(current)):
        
      if((current[i]!=word[i]) and count>=1):
         return False
      elif(current[i]!=word[i]):
         count+=1
   return True





def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   for word in words_set:
      if isAdjacent(current, word):
         adj_set.add(word)
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
   q=[start]
   
   count=0
   if start==end:
      return generate_path(start,explored)
   while True:
      if len(q)==0:
         return None
      current = q.pop(0)
      
      if current == end:
         return generate_path(current,explored)
      
      children = generate_adjacents(current,word_dict)
      for child in children:
         if child not in explored:
            q.append(child)
            explored[child] = current
   
   return None
   



   

def recur(start, end, word_dict, explored, limit):
   ''' your code goes here '''
  
   if start==end:
      return explored
   elif limit<=0:
      return None
   else:
      if limit<=0:
         return None
      for child in generate_adjacents(start,word_dict):
         result=recur(child,end,word_dict,explored,limit-1)
         if result is not None:
            return result
   return None
   
 
def DLS(start, end, word_dict, limit):
   explored={start:'s'}
   
   return recur(start, end, word_dict, explored, limit-1)
    
   
   

def main():
   filename = input("Type the word file: ")
   words_dict = set()
   
   file = open(filename, "r")
   for word in file.readlines():
      words_dict.add(word.rstrip('\n'))
   
   # Test BFS
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   
   path_and_steps = BFS(initial, goal, words_dict)
   if path_and_steps != None:
      print ("Path:", path_and_steps[0])
      print ("The number steps: {}".format(path_and_steps[1]))
   else:
      print ("Solution not found")
 
   # Test DLS
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   limit = int(input("Type the limit: "))
   path_and_steps = DLS(initial, goal, words_dict,limit)
   if path_and_steps != None:
      print ("Path:", path_and_steps[0])
      print ("The number steps: {}".format(path_and_steps[1]))
   else:
      print ("Solution not found in {} steps".format(limit))
   
   # Now, start iterative deepening
   '''Your code goes here'''
   
   # Print out the shortest path and length of the path (number of steps)
   

if __name__ == '__main__':
   main()