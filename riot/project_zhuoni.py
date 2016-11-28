#!/usr/bin/python
#matplotlib inline
import re
import io
import os
import urllib2
#import networkx as nx
#import community
import json
import glob
import numpy as np
import operator
import matplotlib.pyplot as plt
from matplotlib import pyplot
import math
import time
import os.path
#import ijson
from pymongo import MongoClient
Match_List = '/work/repos/bigwork2016/riot/Match_List/Match_List.json'

#================================= end of includes ==================================================================

##API request
def getJSONReply(URL):
    response = urllib2.urlopen(URL);
    html = response.read();
    data = json.loads(html);
    return data;

##std input, RitoMongo.conf - source from internet
def getUserInput():
    FileExists=os.path.isfile('RitoMongo.conf') ;
    res=[];
    if (FileExists):
        with open('RitoMongo.conf') as f:
            for line in f:
                res.append(line.rstrip('\n'));
                print line.rstrip('\n');
    elif (not FileExists):
        SummonerName= raw_input('Enter your Summoner name: ');
        Region  = (raw_input('Enter your region: ')).upper();
        Key = raw_input('Enter your API Key which you retrieved from Riot website: ');
        f = open('RitoMongo.conf','w');
        f.write(SummonerName+'\n'+Region+'\n'+Key);
        f.close();
    return res;

##request game api, arg = summonerID, return recent game table
def getRecentHistory(SummonerID):
        rURL= "https://" +Region.lower()+ ".api.pvp.net/api/lol/" + Region.lower()+ "/v1.3/game/by-summoner/" + `SummonerID`+ "/recent?api_key=" + Key;
        r_data=getJSONReply(rURL);
        r_data['_id']=r_data['summonerId'];
        r_data.pop('summonerId');
        #with io.open('RecentHistory/%s.txt' % str(SummonerID), 'w', encoding='utf-8') as f:
        #    f.write(unicode(json.dumps(r_data, ensure_ascii=False)))
        return r_data;

##request summoner API, return summoner table, arg = (summonerName, Region, Key), return summonerName, summoner byname table
def ReformatJSON(SummonerName,Region,Key):
    idURL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v1.4/summoner/by-name/" + SummonerName+ "?api_key=" + Key;
    id_data = getJSONReply(idURL);
    idRes=id_data[SummonerName.lower()];
    idRes['_id'] = idRes['id'];
    idRes.pop('id');
    #print idRes;
    return idRes,id_data;

##request summoner API, return summoner table, arg = (summonerID, Region, key) , summonerID, summoner table
def ReformatJSONbyid(SummonerID,Region,Key):
    idURL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v1.4/summoner/" +SummonerID+ "?api_key=" +Key
    id_data = getJSONReply(idURL);
    idRes=id_data[SummonerID];
    idRes['_id'] = idRes['id'];
    idRes.pop('id');
    with io.open('Summoner/%s.txt' % str(SummonerID), 'w', encoding='utf-8') as f:
          f.write(unicode(json.dumps(idRes, ensure_ascii=False)))
    return idRes,id_data;		

##matchlist api request 
def getmatchId(SummonerID,Region, Key):
	#url request as the default API config
	matchList_URL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v2.2/matchlist/by-summoner/" +`SummonerID`+ "?api_key=" +Key 
	matchList_data = getJSONReply(matchList_URL)																	
	matches = matchList_data['matches']
	match_id = []
	#match_id = {}, try loop with dict
	for i in range(len(matches)):
		match_id.append(matches[i]['matchId'])
	
	#with io.open('Match_List/%s.json' % str(match_id), 'w', encoding='utf-8') as fo:
	#	fo.write(unicode(json.dumps(matches, ensure_ascii=False)))
	#	fo.close()

	fo = io.open('Match_List.json', 'w', encoding='utf-8')
	fo.write(unicode(json.dumps(matches, ensure_ascii=False))) ##can't save match_ID because of too many request
	#print(match_id)
	return match_id


	
def getmatch(matchID, Region ,key):
	match_URL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v2.2/match/" +`matchID`+ "?api_key=" +Key 
	match_data = getJSONReply(match_URL)
	match = match_data['participants']
	print(match)
	#playerID = []
	#for i in range(len(match)):
	#	match[j]['player']
		#for j in range(len(match[j]['player'])):
			#playerID.append()
			#print(match[j]['player'])
	#for i in range(len(match))
	#	return playersID
	

    
#================================= Main =============================================================================
_InputFields= getUserInput();
SummonerName=_InputFields[0];
Region=_InputFields[1];
Key=_InputFields[2];

print "----------------------------------------------------------------------";
print "If you've inputted wrong data, please delete or modify RitoMongo.conf" ;
print "----------------------------------------------------------------------";
# Retrieving the SummonerID;
idURL,id_data=ReformatJSON(SummonerName,Region,Key);
SummonerID = id_data[SummonerName.lower()]["_id"];
rdata=getRecentHistory(SummonerID);
# Connecting to mongoDB database
#client = MongoClient();
#db = client['RitoMongoDB'];
#SummonerID_Collection = db["SummonerID"];
#RecentHistory_Collection = db["RecentHistory"];
#entryID = SummonerID_Collection.insert_one({str(SummonerID):idURL}).inserted_id;
#entryID = RecentHistory_Collection.insert_one({str(SummonerID):rdata}).inserted_id;
#client.close();

idlist = [SummonerID]
for i in range(len(rdata["games"])):
    for j in range(len(rdata["games"][i]["fellowPlayers"])):
        idlist.append(rdata["games"][i]["fellowPlayers"][j]["summonerId"])
len(set(idlist))

##matchlist, contain the match_list of matches by summonerID
match_list = getmatchId(SummonerID, Region, Key)
#print(match_list)
#playersID = getmatch(match_list, Region, Key)



#print(sorted(set(idlist)))

#for gamer in idlist:
#    idURL,id_data=ReformatJSONbyid(str(gamer),Region,Key)
#    time.sleep(1)
#    rdata=getRecentHistory(gamer)
#    time.sleep(1)
