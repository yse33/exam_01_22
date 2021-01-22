def search_and_replace_text(search_sentence, text):
    if len(search_sentence) < 2:
        return "You have to enter 2 or more words in order to search!" 
    elif " ".join(search_sentence) not in text:
        return "The words you have put in are not found anywhere in the text!"
    else:
        search_sentence = " ".join(search_sentence)
        text = text.replace(search_sentence, "")
        text += search_sentence
        return text