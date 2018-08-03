from scrapy import Spider
from operate.items import OperateItem
import re
import math
from scrapy.http import Request

class OperateSpider(Spider):
    name = "operate_spider"
    allowed_urls = ['http://www.airlinequality.com/']
    airline = 'american-airlines'
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
        		Textchunk = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Recommended')
        		Recommended = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		Recommended = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Aircraft')
        		Aircraft = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		Aircraft = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Type Of Traveller')
        		TypeOfTraveller = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		TypeOfTraveller = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Cabin Flown')
        		CabinFlown = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		CabinFlown = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Route')
        		Route = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		Route = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Date Flown')
        		DateFlown = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr[' + str(row_no+1)  + ']/td/text()').extract()[1]
        	except (ValueError, IndexError):
        		DateFlown = 'nan'
        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Seat Comfort')
        		SeatComfort = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		SeatComfort = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Cabin Staff Service')
        		CabinStaffService = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		CabinStaffService = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Food & Beverages')
        		FoodAndBeverages = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		FoodAndBeverages = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Inflight Entertainment')
        		InflightEntertainment = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		InflightEntertainment = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Ground Service')
        		GroundService = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		GroundService = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Wifi & Connectivity')
        		WifiAndConnectivity = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		WifiAndConnectivity = 'nan'

        	try:
        		row_no = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr/td[1]/text()').extract().index('Value For Money')
        		ValueForMoney = response.xpath('//*[@id="anchor' + i + '"]/div/div[2]/table//tr['+ str(row_no+1) +']/td/span[@class="star fill"]/text()').extract()[-1]
        	except (ValueError, IndexError):
        		ValueForMoney = 'nan'

        	item = OperateItem()
        	item['Textchunk'] = Textchunk
        	item['Recommended'] = Recommended
        	item['Aircraft'] = Aircraft
        	item['TypeOfTraveller'] = TypeOfTraveller
        	item['CabinFlown'] = CabinFlown
        	item['Route'] = Route
        	item['DateFlown'] = DateFlown
        	item['SeatComfort'] = float(SeatComfort)
        	item['CabinStaffService'] = float(CabinStaffService)
        	item['FoodAndBeverages'] = float(FoodAndBeverages)
        	item['InflightEntertainment'] = float(InflightEntertainment)
        	item['GroundService'] = float(GroundService)
        	item['WifiAndConnectivity'] = float(WifiAndConnectivity)
        	item['ValueForMoney'] = float(ValueForMoney)

        	yield item