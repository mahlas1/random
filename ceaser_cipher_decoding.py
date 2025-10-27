alphabet = ["A","B","C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def f(x):         # algorithm for decoding Caesar cryptographic for all iterations
  mylist = []
  j = 1
  while j <26:
    i = 0
    while i < len(x):
      if alphabet.index(x[i]) + j < 26:
        mylist.append(alphabet[alphabet.index(x[i]) + j])
        i = i + 1
      else:
        k =  (alphabet.index(x[i]) + j) % 26
        mylist.append(alphabet[k])
        i = i + 1
    j = j + 1
    print("".join(mylist))
    mylist.clear()
  print(x)

# example f("BGUTBMBGZTFHNLXMKTIPBMAVAXXLXTEPTRLEXTOXKHHFYHKMAXFHNLX")  f("PRJJBOYXIZLKVIBFPROBXIMEX")
