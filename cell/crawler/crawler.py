class queue:
   def __init__(self, *values):

      self.list = list(values)

   def push(self, value):
      self.list.append(value)

   def pop(self):
      value = self.list.pop(0)

      return value



class link:
   def __init__(self, url):
      self.parse(url)

   def parse(url):
      pass

   def move(self, path):
      pass

      # return new link object.



class page:
   pass



class node:
   pass



class memory:
   pass



class agent:
   def __init__(self):
      self.session = session()

   def fetch(self, link):
      url = str(link)

      raw = self.session.get(url)

      return page(raw)
     


class crawler:
   def __init__(self):
      self.agent = agent()
      self.memory = memory()

   def crawl(self, link):
      pass            
