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

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

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


def negativity_censor(text, censor_list, negative_words):
  text_words = []
  for x in text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      text_words.append(word)
  for i in range(0,len(text_words)):
    if (text_words[i] in censor_list) == True:
      word_clean = text_words[i]
      censored_word = ""
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      text_words[i] = text_words[i].replace(word_clean, censored_word)
    count = 0
    for i in range(0,len(text_words)):
      if (text_words[i] in negative_words) == True:
        count += 1
        if count > 2:
          word_clean = text_words[i]
          for x in punctuation:
            word_clean = word_clean.strip(x)
          censored_word = ""
          for x in range(0,len(word_clean)):
            censored_word = censored_word + "X"
          text_words[i] = text_words[i].replace(word_clean, censored_word)
  return " ".join(text_words)


#print(negativity_censor(email_three, proprietary_terms, negative_words))

def ultimate_censor(text, censor_list):
  text_words = []
  for x in text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      text_words.append(word)
  for i in range(0, len(text_words)):
    check_word = text_words[i].lower()
    for x in punctuation:
      check_word = check_word.strip(x)
    if check_word in censor_list:

      clean_word = text_words[i]
      censored_word = ""
      for x in punctuation:
        clean_word = clean_word.strip(x)
      for x in range(0, len(clean_word)):
        censored_word += "X"
      text_words[i] = text_words[i].replace(clean_word, censored_word)
  return text_words

censor_all = proprietary_terms + negative_words

print(ultimate_censor(email_four, censor_all))
