#!/usr/bin/env python
# coding: utf-8

# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def scrape_all():
   # Initiate headless driver for deployment
   browser = Browser("chrome", executable_path="chromedriver", headless=True)
   news_title, news_paragraph = mars_news(browser)

# Run all scraping functions and store results in dictionary
data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
}

# Define our function
def mars_news(browser):

   # Visit the mars nasa news site
   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)
   # Optional delay for loading the page
   browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')
       # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, none

   return news_title, news_p

# Define function for Featured Image
def featured_image(browser):
    try:
        # find the relative image url
        img_url_rel = img_soup.select_one('figure.lege a img').get("src")
    except AttributeError:
        return None
return img_url

# Define function for Mars Facts
def mars_facts():
    try:
        # use 'read_html' to scrape the facts table into a DataFrame
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return: None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())