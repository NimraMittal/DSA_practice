def reversing_a_string(str):
     if len(str)==0:
          return ""
     else: 
          first = str[0]
          rest = str[1:]
          return reversing_a_string(rest)+first
     
str = "nimra"
print(reversing_a_string(str))