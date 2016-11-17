import RiotConsts as rc

class RiotAPI(object)

	def __init__(self, api_key, region = rc.REGION[EUROPE_WEST]):
		self.api_key = api_key
		self.region = region
	
	
	def _request(self, api_url, params={})
