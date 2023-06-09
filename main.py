import requests
import datetime


USERNAME = "kirill1984"
TOKEN = "secret_my"
pixela_endpoint = "https://pixe.la/v1/users"

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


pixela_headers = {
    "X-USER-TOKEN":TOKEN
}
graph_params = {
    "id": "pullups1",
    "name": "pullups",
    "unit": "counts",
    "type": "int",
    "color": "sora",
    "timezone" : "Europe/Moscow",
}

pixela_get_graph_url= f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}.html"
# pixela_response = requests.post(url=pixela_endpoint, json=user_params)
# pixela_graph_create_response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=pixela_headers)
# print(pixela_graph_create_response.text)
pixela_get_graph = requests.get(url=pixela_get_graph_url)
print(pixela_get_graph.url)

def put_pixel(yyyymmdd: str, count: str, option=None):

    pixel_params = {
        'date': yyyymmdd,
        'quantity': count,
        'optionalData': option,
    }
    put_pixel_response = requests.post(url=f"{pixela_graph_endpoint}/{graph_params['id']}", headers=pixela_headers,
                                       json=pixel_params)

    print(pixel_params)
    return put_pixel_response
def get_today_date():
    now = datetime.datetime.now()
    now_date = now.strftime("%Y%m%d")
    return now_date

if __name__ == '__main__':
    answer = put_pixel(get_today_date(), '0')
    print(answer.text)
