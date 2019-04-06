import requests
import json

API_ENDPOINT = ("https://api.iot.dspmc.org/api/v2")
API_KEY      = ("05f52e096a743ca57d3b5f3f0d81d1c4c24de540")
proxies      = {"https":"https://sean.pribadi:66623457@cache.itb.ac.id:8080"}

def update_item(mall,ID,count,time): #update count and time sebuah camera

    #API Url for update item
    url = API_ENDPOINT + "/nodes" + "/item"

    #body
    payload = {
            "name": mall,
            "id" : ID,
            "value" : {
                "count" : count,
                "time" : time
                }
    }
    #headers
    headers = {'content-type': 'application/json',
               'IOT-API-KEY' : API_KEY}

    #put request
    r = requests.put(url, data=json.dumps(payload), headers=headers, proxies=proxies)

def get_item(mall): # dapatkan semua informasi camera pada sebuah mall

    #API Url for get item
    url = API_ENDPOINT + "/nodes" + "/retrieve_item"

    #body
    payload = {
            "name": mall 
    }

    #headers
    headers = {'content-type': 'application/json',
               'IOT-API-KEY' :API_KEY}
    
    #request post 
    r = requests.post(url, data=json.dumps(payload), headers=headers, proxies=proxies)
    
    #print data 
    print(r.text)

def new_item(mall,lokasi,lantai): #new camera

    #API Url for get item
    url = API_ENDPOINT + "/nodes" + "/item"

    #body
    payload = {    
        "name": mall,
        "value": {
            "lokasi" : lokasi, 
            "lantai" : lantai
        }
    }
    #headers
    headers = {'content-type': 'application/json',
               'IOT-API-KEY' :API_KEY}

    #request post 
    r = requests.post(url, data=json.dumps(payload), headers=headers, proxies=proxies)
    data = json.loads(r.text)
    
    keyid = data['data']['insertedId']
    print ( "Id : ", keyid)
    return keyid

def new_mall(mall) :
    #API Url for get item
    url = API_ENDPOINT + "/nodes" 

    #body
    payload = {    
        "name": mall
    }
    
    #headers
    headers = {'content-type': 'application/json',
               'IOT-API-KEY' :API_KEY}

    #request post 
    r = requests.post(url, data=json.dumps(payload), headers=headers, proxies=proxies)
    print(r.text)

def list_semua_mall():
    #API Url for get item
    url = API_ENDPOINT + "/nodes" 
    
    #headers
    headers = {'content-type': 'application/json',
               'IOT-API-KEY' :API_KEY}
    
    r = requests.get(url , headers=headers,proxies=proxies)
    print(r.text)

def delete_mall(mall):
    #API Url for get item
    url = API_ENDPOINT + "/nodes"
    
    #params
    params = {'name': mall }
    
    #headers
    headers = {'content-type': 'application/json',
               'IOT-API-KEY' :API_KEY}
    
    r = requests.delete(url ,params = params, headers=headers,proxies=proxies)
    print(r.text)
    
#mall = "MALL"
#ID = "5c9209e01ca0eb778b740c06"
#count = 2000
#time = "23:25"

#delete_mall(mall)
update_item("BIP","5c9b28261ca0eb3cc740ac88",5,"23:25")





