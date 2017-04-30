# Ashley Otero - Homework 10
# conda install flask (should be v0.12)
from flask import Flask, request

app = Flask("step2")

# define a method to respond when the root page / is requested
@app.route("/") #@ is a decorator
def main_page():
    # return the HTML code that the browser will process when / is requested:
    return """
      <html>
        <body>
          <h1>RSS Reader</h1>
          <form action="/result/" method="get">    <!-- /result/ is the URL to go to on submit -->
             Enter a search term: 
            <input  type="text" name="search_term"
                    value="" 
                    size="40">
            <input type="submit" value="Submit">
          </form>             
        </body>
      </html>
    """      

@app.route('/result/', methods=["GET"])
def result_page():        
    # request.args is a dict with the name and the value of the select and 
    print(request.args["search_term"])  # value for name = "search_term"  in input part of form
    
    import urllib.parse 
    import feedparser    # must make sure the library is installed beforehand: conda install feedparser
    from pprint import pprint # pretty print
    
    #search_term = "Penny Arcade" # testing the search_term before giving it a user input
    #search_term = input("Search term? ")  # user input
    quoted_search_term = urllib.parse.quote(request.args["search_term"]) # make it ULR safe: space => %20, " => %22, etc.
    print("Searching for:", quoted_search_term)
    
    rss_feed_URL = 'http://search.live.com/results.aspx?q={:s}&format=rss'.format(quoted_search_term) # using Bing 
    #print("RSS feed URLS is", rss_feed_URL)
    
    # web-read the feed from URL
    f = feedparser.parse(rss_feed_URL)
    
    # pretty print the entire parsed feed
    #pprint(f) 
    
    print ("This feed has", len(f.entries), "items")
    
    # title, decription, date and link for all items
    def get_desc(e):
        for e in f.entries:
            print(e.title, "<br>")
            print(e.description, "<br>")
            print(e.published, "<br>")
            print(e.link, "<br>")
            print()   
     
    html = """
        <html>
          <body>
            You searched for:  """ + request.args["search_term"] + """ <br>
            This feed has: """ + len(f.entries) + """ items. <br>
            """  """
          </body>
        </html>"""
    return html
    

if __name__ == "__main__":
    app.run(debug=False, port=8080) 
    # Don't use Debug=True in Wing, is seems to not release the socket and you'll get a bind error when you run it next!
    print("done")


