from scraper.scraping import *

# As I can't easily get Selenium working on my separate Linux division, I'll skip this for now and will grab the data collected by a colleague

# scrape.accept_cookie()
# test = scrape.get_urls_from_page(1, 'huis')
# print(test)

# Get all links
all_links = get_all_links()

# Create an empty dataframe
immo_df = create_df()

# Get all info
df = get_df(immo_df, all_links.head(5))

print(df)
