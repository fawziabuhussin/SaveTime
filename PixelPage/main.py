import requests
from datetime import datetime
# fill with your preference to get your own pix, *Token must be from 8-128 characters.
USER_NAME = "fawziabu"
TOKEN = "asuhasdiu23498qujasd"
GRAPHID = "graph1"
today = datetime.now()


pix_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pix_endpoint}/{USER_NAME}/graphs"
pixel_endpoint = f"{pix_endpoint}/{USER_NAME}/graphs/{GRAPHID}"
update_pixel = f"{pix_endpoint}/{USER_NAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
delete_pixel = f"{pix_endpoint}/{USER_NAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"




params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

""" You can use your own graph, for reading or cycling, 
pick your own choice and change the name, unit, type for float 
if you are cycling or running. """

graph_config = {
     "id": GRAPHID,
     "name": "Reading Graph",
     "unit": "Pages",
     "type": "int",
     "color": "shibafu",
}
pixel_config = {
     "date": today.strftime("%Y%m%d"),
     "quantity": "25", # Pick the number of pages.
}

new_pixel_data = {
     "quantity": "20", # Pick the number of pages.
}


headers = {
    "X-USER-TOKEN" : TOKEN,
}


""" Uncomment to create your own profile! """
# response_account = requests.post(url=pix_endpoint, json = params)
# print(f"Creating account status : {response_account.text}")

""" Uncomment to create your own graph! """

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(f"Creating graph status : {response_graph.text}")

""" Uncomment to create a pixel for the day you pick! """

# response_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers= headers)
# print(response_pixel.text)


""" Uncomment to update the pixels in a specific day! """

# response_update_pixel = requests.put(url=update_pixel, json=new_pixel_data, headers= headers)
# print(response_update_pixel.text)


""" Uncomment to delete the pixels in a specific day! """

# response_delete_pixel = requests.delete(url=delete_pixel, headers= headers)
# print(response_delete_pixel.text)