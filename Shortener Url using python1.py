import pyshorteners
url= input('Enter the url: ')
def shortneurl(url):
    s= pyshorteners.Shortener()
    print("Shortern URL:",s.tinyurl.short(url))

shortneurl(url)
