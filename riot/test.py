#!/usr/bin/python
#matplotlib inline
import re
import io
from riotwatcher import RiotWatcher		#library for api key
from riotwatcher import EUROPE_WEST		#region library

euw = RiotWatcher('RGAPI-62c12c6d-5a21-4d8e-96b2-c3cad4aa9baa', default_region=EUROPE_WEST)

#check if we have API calls remaining, due to rate limit, 10request/10sec -> 500r/600sec
print(euw.can_make_request())

##API request
def getJSONReply(URL):
    response = urllib2.urlopen(URL);
    html = response.read();
    data = json.loads(html);
    return data;


##matchlist api request 
def getmatchId(SummonerID,Region, Key):
	#url request as the default API config
	matchList_URL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v2.2/matchlist/by-summoner/" +`SummonerID`+ "?api_key=" +Key 
	matchList_data = getJSONReply(matchList_URL)																	
	matches = matchList_data['matches']
	match_id = []
	for i in range(len(matches)):
		match_id.append(matches[i]['matchId'])
	fo = io.open('Match_List.json', 'w', encoding='utf-8')
	fo.write(unicode(json.dumps(matches, ensure_ascii=False))) ##can't save match_ID because of too many request
	#print(match_id)
	return match_id





