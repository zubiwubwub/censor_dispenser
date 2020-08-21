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

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_list(text, censor_list):
  for phrase in censor_list: #went through the proprietary_terms list
    censored_letter = ""
    for i in range(0,len(phrase)): #got index of the phrase in the list
      if phrase[i] == " ":
        censored_letter += " "
      else:
        censored_letter += "X"
    text = text.replace(phrase, censored_letter) #  replaced term with censored_letter
  return text

#print(censor_list(email_two, proprietary_terms))


def negativity_censor(text, censor_list,  negative_words):
  text_words = []
  for i in text.split(" "):
    list_i = i.split("\n") #split into a list at the new_line
    for word in list_i:
      text_words.append(word) # appended words into a text_words list
  return text_words


print(negativity_censor(email_three, proprietary_terms, negative_words))
