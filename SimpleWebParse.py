'''
Created on Mar 1, 2016

@author: drewc
'''
from html.parser import HTMLParser
from bs4 import BeautifulSoup


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print( "Encountered a start tag:", tag )
    def handle_endtag(self, tag):
        print( "Encountered an end tag :", tag )
    def handle_data(self, data):
        print( "Encountered some data  :", data )
        
if __name__ == '__main__':
    print( "Simple Parse" )
    parser = MyHTMLParser()
    parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1><ul/></body></html>')
    
    html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>
        
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <ul><li>one<\li><li>two<\li><li>three<\li></ul>
        <ul></ul>
        <p class="story">...</p>
        """
    soup = BeautifulSoup( html_doc, 'html.parser' )
    
    print( soup.prettify() )
    
    for link in soup.find_all('a'):
        print(link.get('href'))    
    
    for Ulist in soup.find_all('ul'):
        #print( "Ulist = ", Ulist, " len Ulist = ", len( Ulist ))
        items = Ulist.find_all('li')
        itemCount = len( items )
        if itemCount  > 0:
            print( "items = ", items )
        else:
            print( "No List Items")
            
            
