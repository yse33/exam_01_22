from search_text import *

text = "The hummingbird's wings blurred while it eagerly sipped the sugar water from the feeder. He ran out of money, so he had to stop playing poker."
search_sentence = input("Enter the words you want to search for: ")
print(search_and_replace_text(search_sentence.split(' '), text))