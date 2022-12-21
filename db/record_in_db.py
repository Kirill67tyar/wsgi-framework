import os
import csv


def record(data: dict):
    if not os.path.exists('db.csv'):
        with open(file='db.csv', mode='w', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            headers = ['email', 'question', ]
            writer.writerow(headers)

    with open(file='db.csv', mode='a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        body = [data['email'], data['question'], ]
        writer.writerow(body)


    return True
