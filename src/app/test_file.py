from pattern.web import Twitter, plaintext

twitter = Twitter(language='en') 
for tweet in twitter.search('"Paul Bunyan Communications"', cached=False):
   print tweet.text.encode('utf-8')
