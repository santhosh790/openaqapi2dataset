import requests

class API:
    def __init__(self):
        '''
        This belongs to the API hit and returning JSON Response

        '''
        self.base_url = "http://api.openaq.org"
        self.version = "v1"

    def create_url(self, reqResource, paramMap):
        urlFormat = "{}/{}/{}"
        url = ""
        if reqResource != "":
            url = urlFormat.format(self.base_url,self.version,reqResource)
        if len(paramMap) > 0:
            url = url +"?"
            for each in paramMap:
                url = url+each+'='+str(paramMap[each])+"&"
            url = url[:-1]
        else:
            url = url +"?limit=20&page=1"

        return url

    def getdata(self, url):

        init_result = requests.get(url)
        if init_result.status_code == 200:
            return init_result.json()
        print("Error in handling the url: %s"%url)

        return {}

    def get_next_page(self, meta_data):
        total_pages = round(meta_data['found']/meta_data['limit'])
        if meta_data['found']%meta_data['limit'] > 0:
            total_pages +=1

        #print(total_pages-meta_data['page'])

        return total_pages-meta_data['page']


    def get_next_params(self, meta):

        total_pages = round(meta['found']/meta['limit'])
        if meta['found']%meta['limit'] > 0:
            total_pages +=1
        return total_pages, meta['limit'], meta['page']+1

    def retrieve_all_data(self, api, params):

        json_data = self.getdata(self.create_url(api,params))
        all_data = []
        print(json_data)
        if json_data != {}:

            meta = json_data['meta']
            total_pages = round(meta['found']/meta['limit'])
            if meta['found']%meta['limit'] > 0:
                total_pages +=1
            all_data.extend(json_data['results'])
            while total_pages > meta['page']:
                params['limit'] = meta['limit']
                params['page'] = meta['page']+1
                iter_data = self.getdata(self.create_url(api,params))
                all_data.extend(iter_data['results'])
                meta = iter_data['meta']

        return all_data
