import os
import glob
import schedule
import time
import psycopg2

DATABASE_URL='postgresql://djangoadmin:adminPassword@db:5432/django'

def delete_data():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM post_filename;")
    conn.commit()
    cur.close()
    conn.close()

def delete_img():
    for file in glob.glob('./media/*.jpeg'):
        os.remove(file)

    for file in glob.glob('./media/*.jpg'):
        os.remove(file)

    for file in glob.glob('./media/*.txt'):
        os.remove(file)

    for file in glob.glob('./media/*.png'):
        os.remove(file)


schedule.every().wednesday.at("15:00").do(delete_img)
schedule.every().wednesday.at("15:00").do(delete_data)

while True:
    schedule.run_pending()
    time.sleep(1)