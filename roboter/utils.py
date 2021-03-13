import csv

def suggest_robo():
    with open('restaurant.csv', 'r') as read_csv:
        reader = csv.DictReader(read_csv)
        for row in reader:
            suggest = row['Name']
            print('私のオススメのレストランは、{}です。'.format(suggest))
            yn = input('このレストランは好きですか？ [Yes/No]\n')
            if yn == '':
                print('もう一度入力してください')


def talk_roboter():
    while True:
        name = input('こんにちは！私はRobokoです。あなたの名前は何ですか？\n')
        if name == '':
           print('もう一度入力してください。')
        else:
            suggest_robo()
            restaurant = input('{}さん。どこのレストランが好きですか？\n'.format(name))
            if restaurant == '':
                print('もう一度入力してください。')
            else:
                with open('restaurant.csv', 'a+') as csv_file:
                    fieldnames = ['Name', 'Count']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    if csv_file.tell() == 0:
                        writer.writeheader()
                    else:
                        reader = csv.DictReader(csv_file)
                        for row in reader:
                            if restaurant == row['Name']:
                                add_count = int(row['Count']) + 1
                        if add_count >= 2:
                            writer.writerow({'Count':add_count})
                        else:
                            writer.writerow({'Name': restaurant, 'Count': 1})
            print('{}さん。ありがとうございました。\n良い一日を！さようなら。'.format(name))
            break
