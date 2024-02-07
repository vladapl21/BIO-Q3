# question 3a
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
available = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
score_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
def wordgame(word):
  score = 0
  for x in word:
    print(x)
    score += int((alphabet.index(x))+1)
  print(score)

  for i in range(12):
    total = 0
    j = 0
    while total != score:  
      if available[0] in alphabet:
        score_list[i] += available[0]
      else: 
        score_list[i] += available[1]

      time.sleep(0.5)

      total += int(alphabet.index(score_list[i][j])) + 1
      print(total)
      available[alphabet.index(score_list[i][j])] = ""
      #available.remove(score_list[i][j])
      j += 1


  print(score_list)

wordgame("BAB")