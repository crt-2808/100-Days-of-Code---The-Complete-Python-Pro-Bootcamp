import requests
import os
import dotenv
import datetime

dotenv.load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
today=datetime.datetime.today()
formated_day=today.strftime("%Y%m%d")

user_params={
    "token": os.getenv("PIXELA_TOKEN"),
    "username": os.getenv("PIXELA_user"),
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

graph_config={
    "id":"graph1",
    "name":"Read",
    "unit":"pages",
    "type":"int",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":os.getenv("PIXELA_TOKEN")
}

#Crea el usuario
#response=requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

#Crea el dashboard
graph_endpoint=f"{pixela_endpoint}/{os.getenv("PIXELA_user")}/graphs"
#response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#Crea el pixel en el dashboard
graphs_online_endpoint=f"{graph_endpoint}/{os.getenv("PIXELA_ID")}"
graph_info={
    "date": formated_day,
    "quantity": "15"
}
#response=requests.post(url=graphs_online_endpoint, json=graph_info, headers=headers)
#print(response.text)

#Update el pixel en el dashboard
pixel_endpoint=f"{graphs_online_endpoint}/{formated_day}"
new_pixel={
    "quantity":"20"
}

#response=requests.put(url=pixel_endpoint,json=new_pixel,headers=headers)
#print(response.text)

#Delete el pixel en el dashboard
#response=requests.delete(pixel_endpoint, headers=headers)
#print(response.text)
