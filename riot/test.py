#!/usr/bin/python
from riotwatcher import RiotWatcher		#library for api key
from riotwatcher import EUROPE_WEST		#region library
import json

euw = RiotWatcher('RGAPI-62c12c6d-5a21-4d8e-96b2-c3cad4aa9baa', default_region=EUROPE_WEST)

#check if we have API calls remaining, due to rate limit, 10request/10sec -> 500r/600sec
print(euw.can_make_request())

#save a summoner name as variable
me = euw.get_summoner(name='Manismyforte')
jme = json.dumps(me)

#output to a file save the data sets
#with open ('data.json', 'w') as fo:
#	fo.write(jme)
#	fo.close()
#print(me)

#get match statstic
match = euw.get_match('2932150137')
jmatch = json.dumps(match)
#with open ('data.json', 'w') as fo:
#	fo.write(jmatch )
#	fo.close()
print(match)
#get ranked statstics
my_ranked_stats = euw.get_ranked_stats(me['id'])
#print(my_ranked_stats)
#my_ranked_stats_last_season = euw.get_ranked_stats(me['id'], season=6)
#print(my_ranked_stats_last_season)
