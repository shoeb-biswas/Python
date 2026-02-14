# number of line in the string
# number of words in the string
# number of characters in the string
# And save it to the counter_of_string.txt file

from functools import reduce
with open("./sample_data/test.txt","r") as file:

  #Number of lines
  string = file.readlines()
  line = len(string)

  #Number of word
  words = list(map(lambda x: len(x.split()),string))
  words = reduce(lambda x,y: x+y,words)

  #Number of character
  string = list(map(str.strip,string))
  string = list(map(lambda x: x.replace(" ",""),string))

  character = list(map(lambda x: len(x),string))
  character = reduce(lambda x,y: x+y, character)

  with open("./sample_data/counter_of_string.txt","w") as file:
    file.write(f"Total number of lines: {line}\nTotal number of words: {words}\nTotal number of character: {character}")
