import argparse
from .bot import Bot, settings


def main():
    desc = 'A simple chat bot for Slack'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-t', '--token',
                        required=True,
                        help='Slack API token')

    parser.add_argument('-p', '--plugins',
                        nargs='*',
                        default=['slackbot.plugins'],
                        metavar='PLUGIN',
                        help='Slackbot plugins')

    parser.add_argument('-e', '--errorsto',
                        required=True,
                        help='The destination of the error message')

    args = parser.parse_args()

    settings.API_TOKEN = args.token
    settings.PLUGINS = args.plugins
    settings.ERRORS_TO = args.errorsto

    global bot
    bot = Bot()

    print('Start slackbot')

    bot.run()
