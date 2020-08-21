# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(text, phrase):
  censored_letter = ""
  for i in range(0,len(phrase)):
    if phrase[i] == " ":
      censored_letter += " "
    else:
      censored_letter += "X"
  return text.replace(phrase, censored_letter)

#print(censor(email_one, "learning algorithms"))




proprietary_terms = [
"she", "She", "personality matrix", "sense of self",
"self-preservation", "learning algorithm", "her", "Her", "herself", "Herself"
]

def censor_two(text, censor_list):
  for phrase in censor_list:
    censored_letter = ""
    for i in range(0,len(phrase)):
      if phrase[i] == " ":
        censored_letter += " "
      else:
        censored_letter += "X"
    text = text.replace(phrase, censored_letter)
  return text

print(censor_two(email_two, proprietary_terms))


