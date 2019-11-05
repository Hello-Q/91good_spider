class MeituanSpider:
    name = 'meituan'
    # start_urls = get_start_url()
    start_urls = ['https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=bf46b0704b40c039eb84.1550629537.1.0.0&userid=-1&limit=32&offset=32&cateId=20287&areaId=-1']

    def parse(self, response):
        print(response.text)
