import requests

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

# response = requests.post(url=pixela_endpint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Page Read",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
