# import requests
import requests
from urllib.parse import urlencode

# #got help with this tutorial : https://www.youtube.com/watch?v=ckPEY2KppHc&t=18s



# # locations = server.location ## NOT SURE IF THIS IS CORRECT WY TO DO THIS OR TO IMPORT FROM CRUD>PY? OR TO JUST QUERY ON THIS PAGE??/

# data_type = 'json'
# endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
# params = {'address' : '1600 Amphitheatre Parkway, Mountain View, CA', 'key': API_KEY}
# url_params = urlencode(params)
# # sample = 'https//maps.googleapis.com/maps/api/geocode/json?address=539+NW+13th+Ave,+Portland,+OR+97209'
# # print(url_params)

# url = f'{endpoint}?{url_params}'
# print(url)

def get_addresses_from_db_to_gmaps(address_or_postcode):
    
        
    
    data_type = 'json'
    endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
    params = {'address' : address_or_postcode, 'key': API_KEY}
    url_params = urlencode(params)
    # sample = 'https//maps.googleapis.com/maps/api/geocode/json?address=539+NW+13th+Ave,+Portland,+OR+97209'
    # print(url_params)

    url = f'{endpoint}?{url_params}'
    print(url)



def get_lat_lng(address_or_postcode, data_type = 'json'):
    

    endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
    params = {'address' : address_or_postcode, 'key': API_KEY}
    url_params = urlencode(params)
    # sample = 'https//maps.googleapis.com/maps/api/geocode/json?address=539+NW+13th+Ave,+Portland,+OR+97209'
    # print(url_params)
    url = f'{endpoint}?{url_params}'
    r = requests.get(url)
    if r.status_code not in range(200,299):
       return {}
    latlng = {}
    try: 
        latlng = r.json()['results'][0]['geometry']['location']
        print(latlng, "***********************")
    except:
        pass
    return {'lat': latlng.get('lat'), 'lng': latlng.get('lng')}





    # print(url)
    # return url
    # return r.json()['results'][0].keys()
    # return r.json()['results']['geometry']['location']







# address = DanceEvent.query.filter_by(dance_event_location=address).all()

# params = {
#     'key': API_KEY,
#     'address': address
# }

# base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
# response = requests.get(base_url, params=params).json()
# # response.json()
# response.keys()

# if response['status'] == 'OK';
#     response['results'][0].keys()
#     # geometry = response['results][0]['geometry']
#     # lat = geometry = ['location']['lat']
#     #long =geometry = ['location']['lng']

#     print (lat,lon)