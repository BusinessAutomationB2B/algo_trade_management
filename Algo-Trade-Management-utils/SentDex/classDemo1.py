class Book(object):               
  scale=(1,5)

  def __init__(self, title):        
      self.title = title
      self.ratings = []

  def rate(self,rating):
      if rating in range(self.scale[0]-1, self.scale[1]+1):
          self.ratings.append(rating)

  def __str__(self):
      return '"{0}" rates an average of {1} from {2} reviews.'.format(
         self.title, sum(self.ratings)/float(len(self.ratings)), len(self.ratings))

# test the class
mybook = Book('Zen of Python')
mybook.rate(5)
mybook.rate(3)
mybook.rate(5)
print(str(mybook))

    
