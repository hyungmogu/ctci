def word_count_engine(document):
  keywords_count = count_keywords(document)
  sort_by_count(keywords_count)
  return keywords_count # your code goes here

def count_keywords(document):
    words = document.split()
    output = []
    keywords_count = {}

    for word in words:
        new_word = strip_punctuation(word).lower()
        if (not keywords_count.get(new_word)):

            keywords_count[new_word] = 1
        else:
            keywords_count[new_word] += 1

    for key, value in keywords_count.iteritems():
        keyword_count = [key, str(value)]
        output.append(keyword_count)

    return output

def sort_by_count(keywords_count_list):
    keywords_count_list.sort(reverse = True, key = lambda keyword: keyword[1])
    return

def strip_punctuation(key):
    output = []
    letters = [ x for x in key]

    for letter in letters:
        # if specialized character exists, then omit it
        if (not letter.isalpha()):
            continue

        output.append(letter)

    return ''.join(output)