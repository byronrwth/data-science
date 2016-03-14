import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    book = record[0]
    print "book: ", book
    
    value = record[1]
    words = value.split()
    print "words: ", words

    uniquewords = set(words)

    '''
    key:  milton-paradise.txt
    words:  [u'[', u'Paradise', u'Lost', u'by', u'John', u'Milton', u'1667', u']', u'Book', u'I', u'Of', u'Man', u"'", u's', u'first', u'disobedience', u',', u'and', u'the', u'fruit', u'Of', u'that', u'forbidden', u'tree', u'whose', u'mortal', u'taste', u'Brought', u'death', u'into', u'the', u'World', u',', u'and', u'all', u'our', u'woe', u',', u'With', u'loss', u'of', u'Eden', u',', u'till', u'one', u'greater', u'Man', u'Restore', u'us', u',', u'and', u'regain', u'the', u'blissful', u'seat', u',', u'Sing', u',', u'Heavenly', u'Muse', u',', u'that', u',', u'on', u'the', u'secret', u'top', u'Of', u'Oreb', u',', u'or', u'of', u'Sinai', u',', u'didst', u'inspire', u'That', u'shepherd', u'who', u'first', u'taught', u'the', u'chosen', u'seed', u'In', u'the', u'beginning', u'how', u'the', u'heavens', u'and', u'earth', u'Rose', u'out', u'of', u'Chaos', u':', u'or', u',', u'if', u'Sion', u'hill', u'Delight', u'thee', u'more', u',', u'and', u'Siloa', u"'", u's', u'brook', u'that', u'flowed', u'Fast', u'by', u'the', u'oracle', u'of', u'God', u',', u'I', u'thence', u'Invoke', u'thy', u'aid', u'to', u'my', u'adventurous', u'song', u',', u'That', u'with', u'no', u'middle', u'flight', u'intends', u'to', u'soar', u'Above', u'th', u"'", u'Aonian', u'mount', u',', u'while', u'it', u'pursues', u'Things', u'unattempted', u'yet', u'in', u'prose', u'or', u'rhyme', u'.']
    '''
    for w in uniquewords:
      #mr.emit_intermediate(w, 1)  # key = w, value = 1
      mr.emit_intermediate(w, book)  # key = w, value = key = document id

      '''
      def emit_intermediate(self, key, value):
          self.intermediate.setdefault(key, [])
          self.intermediate[key].append(value)
      '''

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    """
    total = []
    for v in list_of_values:
      total.append(v)
    mr.emit((key, total))
    """
    
    '''
    def emit(self, value):
        self.result.append(value) 
    '''
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  '''
  def execute(self, data, mapper, reducer):
      for line in data:
          record = json.loads(line)
          mapper(record)

      for key in self.intermediate:
          reducer(key, self.intermediate[key])

      #jenc = json.JSONEncoder(encoding='latin-1')
      jenc = json.JSONEncoder()
      for item in self.result:
          print jenc.encode(item)
  '''
