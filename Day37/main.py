import requests
import time

# Create your own user and token. I outsourced this to a file called <Account.txt>. The first line of the file is the username and the second line is the token.
file = open("Account.txt","r")
content = file.readlines()

USERNAME = content[0].strip("\n") 
TOKEN = content[1]

file.close()

pixela_endpint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_endpint, json=user_params)
# print(response.text)

# --- Create the graph ---

graph_config = {
    "id": "graph1",
    "name": "Page Read",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

# graph_endpoint = f"{pixela_endpint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --- Daily update to the graph ---

time_tuple = time.localtime() # get struct_time
time_string = time.strftime("%Y%m%d", time_tuple)

graph_endpoint = f"{pixela_endpint}/{USERNAME}/graphs/{graph_config['id']}"

graph_update = {
    "date": time_string,
    "quantity": "20"
}

# response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
# print(response.text)

# --- overwrite pixel ---

ow_time = "20240125"
ow_graph_endpoint = f"{pixela_endpint}/{USERNAME}/graphs/{graph_config['id']}/{ow_time}"
ow_graph_update = {
    "quantity": "12"
}

response = requests.put(url=ow_graph_endpoint, json=ow_graph_update, headers=headers)
print(response.text)
