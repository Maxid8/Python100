import requests

USERNAME = "danika"
TOKEN = "f1g5drt4jk1uzfhg8ikdr1g"

pixela_endpint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpint, json=user_params)
print(response.text)

# graph_endpoint = f"{pixela_endpint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Page Read",
#     "unit": "page",
#     "type": "int",
#     "color": "sora"
# }

# headers = {
#     "X-"
# }

# requests.post()
