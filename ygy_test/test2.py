import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):

    word_lst = sentences.split()
    answer = []
    
    for word in sentences.split():
        if nlp(word):
            answer.append('X'*len(word))
        else:
            answer.append(word)

    return ' '.join(answer)


