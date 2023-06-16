import scrapy
from docx import Document

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # Obtener el texto del XPath especificado
        xpath_expression = "/html/body/div/div[2]//text()"
        text = ' '.join(response.xpath(xpath_expression).extract())

        # Guardar el texto en un archivo .doc
        document = Document()
        document.add_paragraph(text)
        document.save("output.doc")

        self.log("Texto extraído y guardado en output.doc")
