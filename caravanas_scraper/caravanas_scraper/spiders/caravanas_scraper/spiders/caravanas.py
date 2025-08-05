import scrapy
import json

class CaravanasSpider(scrapy.Spider):
    name = "caravanas"
    start_urls = ['https://beautyfair.com.br/caravanas/']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'caravanas.csv',
    }

    def parse(self, response):
        for card in response.css('.shadow-caravan'):
            nome = card.css('p.font-display-bold::text').get()
            telefone = card.css('i.fa-mobile-notch + p::text').get()
            email = card.css('i.fa-envelope-open + p::text').get()
            local = card.css('i.fa-location-dot + p::text').get()
            
            yield {
                'nome': nome,
                'telefone': telefone,
                'email': email,
                'localidade': local
            }

        # ⏭ Clicando nos botões da paginação via simulação (pois URL não muda)
        next_button = response.xpath("//button/div[contains(text(), 'Próximo') or contains(text(), '›')]")
        if next_button:
            yield scrapy.FormRequest(
                url=self.start_urls[0],
                method='GET',
                callback=self.parse
            )
