import wikipedia

def scrape(name="Microsoft", length=1):
    res = wikipedia.summary(name, sentences=length)
    return res
print(scrape("France", 3))