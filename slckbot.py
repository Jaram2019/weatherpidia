import asyncio
import json

import websockets
from slacker import Slacker

# BotUserOauth = os.environ["BOT_USER_OAUTH"]
BotUserOauth = 'xoxb-392235298884-528005666023-Wx5NDEqwE2xh37nvCrzEFmmV'

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
        else:
            print(message_json)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(execute_bot())
asyncio.get_event_loop().run_forever()








def slack_notify(text=None, channel='random', username="알림봇", attachments=None):
    slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)
