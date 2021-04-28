'''
    This file contains all of the functions for the webpage. 
'''

# Function to remove the Punctuation 
def remove_Punctuation(text):
  # List of punctuation to be removed. 
  punctuation = [".", ",", "!", "?"]
  
  # List to be returned with the updated words. 
  updated_List = []

  # Loop to check for punctuation
  for word in text: 
    if word[-1] in punctuation: 
      updated_List.append(word[:-1])
    else:
      updated_List.append(word)

  return updated_List

# Function to create the Stem'd strings 
def create_Stem(text):
  # List of ends to stem out
  stem = ["ing", "ed", "n't", "'ll", "est"]

  # Updated list to return at the end of the function 
  update_Text = []

  for word in text:
    if word[-3:] in stem:
      update_Text.append(word[:-3])
    else:
      update_Text.append(word)
  
  return update_Text

  # Function to remove stop words 
def remove_Stop_Words(text):
  # Defining the stop words based on the given samples 
  stop_Words = ["the", "to", "with", "is", "for", "you", "if", "have", "any", "on", 'your', 'of', 'or']

  # Both lists that will 
  new_Text = []

  # Splitting the sting into a list so it will not return the individal letters. 
  text_List = text.split()

  # Removing the punctuation
  text_List = remove_Punctuation(text_List)

  # Stemming down the words
  text_List = create_Stem(text_List)

  # For loop to take the list of words, compares each string to the strings inside the stop_Words list and ignores 
  # if string is in the stop_Words list, if not then will be appended to the new list that will be returned. 
  # The if statement will automatically lowercase each word
  for word in text_List:
    # checking if the initial word is in the stop check
    if word.lower() in stop_Words: 
      continue
    else:
      new_Text.append(word.lower())
    
  return new_Text

# The final function to check for similarity. 
def jaccard_Similarity(text1, text2):
  # Slimming down text from junk
  text1, text2 = remove_Stop_Words(text1), remove_Stop_Words(text2)

  # Grabbing all of the text shared between the two
  shared_text = set(text1).intersection(set(text2))
  
  # Now grabbing combined count of all of the text in general
  all_text = set(text1).union(set(shared_text))

  # Getting the result, if it has more than 50% similarty
  # Function will return 1, if less than 50% return 0
  result = 100*(len(shared_text)/len(all_text))

  if result > 50:
    return 1
  else:
    return 0