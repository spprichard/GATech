from pattern.web import Twitter, plaintext

twitter = Twitter(language='en') 
for tweet in twitter.search('"Apple"', cached=False):
   print tweet.text.encode('utf-8')
