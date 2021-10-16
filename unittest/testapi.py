# importing the requests library
import requests

def Postgamemove(gameid,playerid,row,col):
	# defining the api-endpoint	
	API_ENDPOINT = " http://localhost:9098/tictacserver/makeamove/"+gameid+"/"+playerid+"/"+row+"/"+col
	# data to be sent to api
	data = {}
	'''
		"playerid" : playerid,
		"row" : row,
                "col" : col
               }
	print(data)
	'''
	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)
	# extracting response text	
	print("response",r,r.json())

def Postcreate_new_game():
	# defining the api-endpoint	
	API_ENDPOINT = " http://localhost:9098/tictacserver/createnewgame"
	# data to be sent to api
	data = {}

	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)
	# extracting response text	
	print("response",r,r.json())

def Postcreate_new_player():
	# defining the api-endpoint	
	API_ENDPOINT = " http://localhost:9098/tictacserver/newplayer"
	# data to be sent to api
	data = {}
	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)
	# extracting response text	
	print("response",r,r.json())


def get_games():
	# defining the api-endpoint	
	API_ENDPOINT = " http://localhost:9098/tictacserver/getallgames"
	# data to be sent to api
	data = {}
	# sending post request and saving response as response object
	r = requests.get(url = API_ENDPOINT, data = data)
	# extracting response text	
	print("response",r,r.json())


def get_player():
	# defining the api-endpoint	
	API_ENDPOINT = " http://localhost:9098/tictacserver/getplayerinfo"
	# data to be sent to api
	data = {}
	# sending post request and saving response as response object
	r = requests.get(url = API_ENDPOINT, data = data)
	# extracting response text	
	print("response",r,r.json())

def get_gamestatus():
	# defining the api-endpoint	
	API_ENDPOINT = " http://localhost:9098/tictacserver/getallgamesstatus"
	# data to be sent to api
	data = {}
	# sending post request and saving response as response object
	r = requests.get(url = API_ENDPOINT, data = data)
	# extracting response text	
	print("response",r,r.json())


