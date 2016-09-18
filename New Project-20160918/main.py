def crawl_web(seed,max_depth):
	tocrawl = [seed]
	crawled = [ ]
#	index = [ ]
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			
			union(tocrawl,get_all_links(content))
		
			crawled.append(page)
	return index


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
			 
def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_qoute = page.find('"', start_link)
	end_qoute = page.find('"',start_qoute+1)
	url = page[start_qoute+1:end_qoute]
	return url, end_qoute

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
    
def get_page(url):
	try:
		import urllib
		f=urllib.urlopen('http://xkcd.com/353')
		myfile = f.read()
		return myfile
	except:
		return " "
	

	
def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([keyword, [url]])
	
def lookup(index,keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return[]
	
def add_page_to_index(index,url,content):
	words = content.split()
	for word in words:
		add_to_index(index,word,url)
	

index = [ ]

print (get_all_links(get_page("http://xkcd.com/353")))
print (lookup(index,"/archive"))
print (crawl_web("http://xkcd.com/353",3))
print (lookup(index,"/"))


