import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 78, "name": "Joe", "views": "100000"},
#     {"likes": 8000, "name": "How to make restAPI", "views": 8000},
#     {"likes": 35, "name": "Pedro", "views": 2000}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# response = requests.get(BASE + "video/6")
# print(response.json())

# response = requests.delete(BASE + "video/1")
# print(response)

response = requests.patch(BASE + 'video/2', {'views':99, 'likes': 991})
print(response.json())