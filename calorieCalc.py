api_key = "feRjDyiF1DZIMqAzMJFCwGePYZPg1RHaa8JgbjYR"
import urllib.request
import json


def search(foodName):
    """Takes in foodName as a string
    and returns the ndbno"""
    #foodName = input("What did you eat today? ")
    url = "https://api.nal.usda.gov/ndb/search/?format=json&q={}&max=50&sort=r&ds=Standard+Reference&offset=0&api_key={}".format(ndbno,api_key)
    page = urllib.request.urlopen(url)
    data_bytes = page.read()
    data_string = data_bytes.decode('utf-8')
    page.close()
    data_dict = json.loads(data_string)
    # In format: dict: ( dict: list: ( dict: value ) )
    # ["item"][0] will return first search item
    ndbno = data_dict["list"]["item"][0]["ndbno"]
    return ndbno

def calURL(ndbno):
    """Takes in ndbno as a string and 
    returns a url for a JSON list"""
    return "https://api.nal.usda.gov/ndb/V2/reports?ndbno={}&type=f&format=json&api_key={}".format(ndbno, api_key)

def calList(ndbno):
    """Takes in a food number and returns the list of foods"""
    url = calURL(ndbno)
    page = urllib.request.urlopen(url)
    data_bytes = page.read()
    data_string = data_bytes.decode('utf-8')
    page.close()
    data_dict = json.loads(data_string)
    return data_dict
    
def getCalories(foodName):
    """Takes in foodName as a string and 
    returns the calorie value"""
    data_dict = calList(search(foodName))
    # In the format of: dict: ( list ( dict: ( dict: ( list: dict:value ) ) ) )
    # ['nutrients'][1] as calories is second item in dict
    return data_dict['foods'][0]['food']['nutrients'][1]['value']