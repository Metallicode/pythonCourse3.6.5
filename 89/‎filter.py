##def filterFunc(x):
##      return len(x) > 10
##
##numList = ["aaaaaa", "aaaaaaaaaa", "aaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaa", "aaaaaaaaaaaa"]
##newFilterdList = list(filter(filterFunc,numList))
##print(newFilterdList)
##
##

def has_i_in_word(word):
      return "i" in word

wordList = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"]
wordsWith_i = list(filter(has_i_in_word,wordList))
print(wordsWith_i)
