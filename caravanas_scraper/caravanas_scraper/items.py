import scrapy

class CaravanasScraperItem(scrapy.Item):
    nome = scrapy.Field()
    telefone = scrapy.Field()
    email = scrapy.Field()
    localidade = scrapy.Field()
