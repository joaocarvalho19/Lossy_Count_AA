class ExactCounter:
    def __init__(self, tokens):
        self.counter = {}
        self.tokens = tokens
    
    def run(self):
        for word in self.tokens:
            if word not in self.counter:
                self.counter[word] = 1
            else:
                self.counter[word] += 1
        
        result = dict(sorted(self.counter.items(), key=lambda item: item[1], reverse=True))
        return result