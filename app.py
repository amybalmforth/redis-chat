import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
p = r.pubsub()


def send_message():
    r.set('mytestkey', 'mytestvalue')


def retrieve_message():
    amy = r.get('amytestkey')
    print(amy)


def get_message_history():
    list = r.lrange('general-history', 0, 5)
    print(list)


def subscribe_messages():
    p.subscribe('general-chat')


def get_a_message():
    x = p.get_message()
    print(x['data'])


get_message_history()
subscribe_messages()
get_a_message()
