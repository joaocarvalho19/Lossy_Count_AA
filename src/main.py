import time
import sys
import re
from exact_counter import ExactCounter
from lossy_counter import LossyCounter


def tokenizer():
    tokens = []
    file = open(file_path, "r")
    file = file.read()

    tokens_line = re.sub("[^0-9a-zA-Z]+"," ",file).lower().split(" ")
    tokens_line = [token for token in tokens_line if len(token)>3]
    tokens.extend(tokens_line)

    print("Tokens length: ", len(tokens))
    return tokens

if __name__ == "__main__":
    file_path = None

    try:
        file_path = sys.argv[1]
    except Exception as err:
        print("Usage: python3 src/main.py texts/<file>")
        sys.exit()
    
    begin = time.time()

    tokens = tokenizer()
    # Exact Counter
    exact_count = ExactCounter(tokens).run()
    #print(exact_count)

    # Lossy Counter
    lossy_count = LossyCounter(tokens, 5e-3).run()
    #print(lossy_count)

    for word in lossy_count:
        exact_value = exact_count[word]
        lossy_value = lossy_count[word]
        acc = round(lossy_value / exact_value * 100, 2)
        print("{:<20} -- Exact: {:<5} | Lossy: {:<5} -- Acc: {:<4}".format(word, exact_value, lossy_value, acc))