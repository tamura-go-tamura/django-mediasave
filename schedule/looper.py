import requests
import json
import schedule
import time

def job():
    #POSTするURL設定
    post_url = "https://app.takopanman.work/post/"

    #POSTするファイルの読込
    files = { "image_file": open('./reset_data.jpeg', 'rb') }

    #POST送信
    response = requests.post(
        post_url,
        files = files,)

    print(json.loads(response.text))

print("Success")
schedule.every().monday.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)