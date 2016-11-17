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
from pymongo import MongoClient;

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

##request game api, arg = summonerID
def getRecentHistory(SummonerID):
        rURL= "https://" +Region.lower()+ ".api.pvp.net/api/lol/" + Region.lower()+ "/v1.3/game/by-summoner/" + `SummonerID`+ "/recent?api_key=" + Key;
        #print rURL;
        r_data=getJSONReply(rURL);
        #print r_data;
        r_data['_id']=r_data['summonerId'];
        r_data.pop('summonerId');
        with io.open('RecentHistory/%s.txt' % str(SummonerID), 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps(r_data, ensure_ascii=False)))
        return r_data;

##request summoner API, return summoner table, arg = (summonerName, Region, Key) 
def ReformatJSON(SummonerName,Region,Key):
    idURL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v1.4/summoner/by-name/" + SummonerName+ "?api_key=" + Key;
    id_data = getJSONReply(idURL);
    idRes=id_data[SummonerName.lower()];
    idRes['_id'] = idRes['id'];
    idRes.pop('id');
    #print idRes;
    return idRes,id_data;

##request summoner API, return summoner table, arg = (summonerID, Region, key)
def ReformatJSONbyid(SummonerID,Region,Key):
    idURL = "https://" +Region.lower()+ ".api.pvp.net/api/lol/" +Region.lower()+ "/v1.4/summoner/" +SummonerID+ "?api_key=" +Key
    id_data = getJSONReply(idURL);
    idRes=id_data[SummonerID];
    idRes['_id'] = idRes['id'];
    idRes.pop('id');
    with io.open('Summoner/%s.txt' % str(SummonerID), 'w', encoding='utf-8') as f:
          f.write(unicode(json.dumps(idRes, ensure_ascii=False)))
    return idRes,id_data;

def recFellow(ID_List):
	getRecentHistory()
    
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



#print(sorted(set(idlist)))

#for gamer in idlist:
#    idURL,id_data=ReformatJSONbyid(str(gamer),Region,Key)
#    time.sleep(1)
#    rdata=getRecentHistory(gamer)
#    time.sleep(1)