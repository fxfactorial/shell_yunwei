import scrapy

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = [dmoz.org]
	start_urls = [
	"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
	"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

def parse(self, reponse):
	filename = reponse.url.split("/")[-2]
    with open(filename, 'wb') as f:
		f.write(response.body)
