# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(email, phrase):
  censored_letter = ""
  for x in range(0,len(phrase)):
    if phrase[x] == " ":
      censored_letter += " "
    else:
      censored_letter += "X"
  return email.replace(phrase, censored_letter)

#print(censor(email_one, "learning algorithms"))




proprietary_terms = [
"she", "personality matrix", "sense of self",
"self-preservation", "learning algorithm", "her", "herself"
]




#print(replacer(email_two, proprietary_terms))


