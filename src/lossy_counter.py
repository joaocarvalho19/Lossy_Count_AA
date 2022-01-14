from collections import defaultdict

class LossyCounter:
    'Implemendation of Lossy Counting'

    def __init__(self, tokens, epsilon):
        self.tokens = tokens
        self.n = len(tokens)
        self.count = defaultdict(int)
        self.bucket_id = {}
        self.epsilon = epsilon
        self.current_bucket_id = 1

    def run(self):
        for word in self.tokens:
            self.addCount(word)

        result = {}
        for item, count in sorted(self.getIter(10), key=lambda x: x[1], reverse=True): #, self.getBucketId(item))
            result[item] = count

        return result


    def getCount(self, item):
        'Return the number of the item'
        return self.count[item]

    def getBucketId(self, item):
        'Return the bucket id corresponding to the item'
        return self.bucket_id[item]

    def addCount(self, item):
        'Add item for counting'
        #self.n += 1
        if item not in self.count:
            self.bucket_id[item] = self.current_bucket_id - 1

        self.count[item] += 1

        if self.n % int(1 / self.epsilon) == 0:
            self.trim()
            self.current_bucket_id += 1

    def getIter_with_threshold_rate(self, threshold_rate):
        return self.getIter(threshold_rate * self.n)

    def trim(self):
        'trim data which does not fit the criteria'
        for item, total in list(self.count.items()):
            if total <= self.current_bucket_id - self.bucket_id[item]:
                del self.count[item]
                del self.bucket_id[item]

    def getIter(self, threshold_count):
        #assert threshold_count > self.epsilon * self.n, "too small threshold"

        self.trim()
        for item, total in self.count.items():
            if total >= threshold_count - self.epsilon * self.n:
                yield (item, total)
            else:
                raise StopIteration