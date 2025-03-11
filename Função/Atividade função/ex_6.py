text = input("Digite uma frase: ")
def inve(text):
  if text == text[::-1]:
   return True
  return False

print(inve(text))
 