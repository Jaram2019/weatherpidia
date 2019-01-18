import asyncio
import json
import os

import crawler
import websockets
from slacker import Slacker

BotUserOauth = os.environ["BOT_USER_OAUTH"]

token = BotUserOauth
slack = Slacker(token)
response = slack.rtm.start()
sock_endpoint = response.body['url']


# websocket Processing Part


async def execute_bot():
    ws = await websockets.connect(sock_endpoint)
    while True:
        message_json = json.loads(await ws.recv())
        # print(message_json['type'])
        if 'content' in message_json:
            print(message_json['content'])
            data_string = crawler.weather_crawling(message_json['text'])
            slack_notify(data_string, '#random', username="날씨봇")
        else:
            print(message_json)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(execute_bot())
asyncio.get_event_loop().run_forever()


def slack_notify(text=None, channel='random', username="알림봇", attachments=None):
    slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)
