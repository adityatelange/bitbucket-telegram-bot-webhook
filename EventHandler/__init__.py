from EventHandler.issue import issue
from EventHandler.repo import repo
from bot import Bot


def event_handler(x_event_key, data_json):
    event_type = x_event_key.split(':')[0]
    event_sub_type = x_event_key.split(':')[1]

    try:
        msg = globals()[event_type](event_sub_type, data_json)
        Bot(msg)
    except KeyError as ke:
        print(ke)
