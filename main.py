#WRITE YOUR CODE IN THIS FILE
def hasL (w):
    for i in range (0, len (w), 1):
        if w[i] == "l":
            return True
    else :
      return False

print (hasL ("dog"))
print (hasL ("alabama"))