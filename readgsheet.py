import pygsheets
# from pprint import pprint

client = pygsheets.authorize(service_account_file='service_account_file.json')

sh = client.open('Notifications')
wks = sh.sheet1


async def get_notifications():
    # print(sh.updated)
    google_sheet_records = wks.get_values('A2', 'F10')
    unsent_notifications = []
    wks.unlink()
    for i, record in enumerate(google_sheet_records, start=2):
        if record[5] != 'done':
            unsent_notifications.append(
                {
                    'tg_id': record[0],
                    'text': record[1],
                    'created_at': f'{record[2]} {record[3]}',
                    'answer_time': record[4]
                }
            )
        wks.update_value(f'F{i}', 'done')
    wks.link()

    return unsent_notifications

# pprint(get_notifications())
