import os

from slacker import Slacker

OAuth = os.environ["SLACK_OAUTH"]
BotUserOauth = os.environ["BOT_USER_OAUTH"]


def slack_notify(text=None, channel='random', username="알림봇", attachments=None):
    token = BotUserOauth
    slack = Slacker(token)
    slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)
