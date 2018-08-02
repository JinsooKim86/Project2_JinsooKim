from scrapy import Spider
from operate.items import OperateItem
import re
import math
from scrapy.http import Request

class OperateSpider(Spider):
    name = "operate_spider"
    allowed_urls = ['http://www.airlinequality.com/']
    airline = 'delta-air-lines'
    start_urls = ['http://www.airlinequality.com/airline-reviews/' + airline]

    def parse(self, response):
    	number_of_pages = math.ceil(int(re.findall('\d+', response.xpath('//*[@id="main"]/section[3]/div[1]/div/article/div/text()').extract_first())[-1])/10)
    	result_urls = ['http://www.airlinequality.com/airline-reviews/' + self.airline + '/page/' + str(i) for i in range(1,number_of_pages + 1)]
    	for url in result_urls:
    		yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):
        anchor_numbers = re.findall('\d+',str(response.xpath('//*[@id="main"]/section[3]/div[1]/article/article//@id').extract()))
        for i in anchor_numbers:

        	try:
        		Textchunk = response.xpath('//*[@id="anchor' + i + '"]/div/div[1]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		Textchunk = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Recommended')
        		Recommended = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		Recommended = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Aircraft')
        		Aircraft = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		Aircraft = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Type Of Traveller')
        		TypeOfTraveller = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		TypeOfTraveller = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Cabin Flown')
        		CabinFlown = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		CabinFlown = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Route')
        		Route = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		Route = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Date Flown')
        		DateFlown = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		DateFlown = float('nan')
        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Seat Comfort')
        		SeatComfort = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		SeatComfort = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Cabin Staff Service')
        		CabinStaffService = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		CabinStaffService = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Food & Beverages')
        		FoodAndBeverages = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		FoodAndBeverages = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Inflight Entertainment')
        		InflightEntertainment = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		InflightEntertainment = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Ground Service')
        		GroundService = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		GroundService = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Wifi & Connectivity')
        		WifiAndConnectivity = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		WifiAndConnectivity = float('nan')

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Value For Money')
        		ValueForMoney = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		ValueForMoney = float('nan')

        	item = OperateItem()
        	item['Textchunk'] = Textchunk
        	item['Recommended'] = Recommended
        	item['Aircraft'] = Aircraft
        	item['TypeOfTraveller'] = TypeOfTraveller
        	item['CabinFlown'] = CabinFlown
        	item['Route'] = Route
        	item['DateFlown'] = DateFlown
        	item['SeatComfort'] = SeatComfort
        	item['CabinStaffService'] = CabinStaffService
        	item['FoodAndBeverages'] = FoodAndBeverages
        	item['InflightEntertainment'] = InflightEntertainment
        	item['GroundService'] = GroundService
        	item['WifiAndConnectivity'] = WifiAndConnectivity
        	item['ValueForMoney'] = ValueForMoney

        	yield item