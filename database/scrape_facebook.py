from facebook_scraper import get_posts


def get_facebook_articles() -> list:
	"""
	Scrape facebook and return articles as a list.

	Returns
	-------
	articles : list
		articles as a list
	""" 
	articles = []
	for post in get_posts('wowsdevblog', pages=3):
		articles.append(post)
	return articles
		

if __name__ == '__main__':
	print(get_facebook_articles())