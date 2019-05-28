import os
import sys

from slack import WebClient

BOT_NAME = '@Yellowhaska_bot'

slack_client = WebClient(os.environ.get('813912120:AAHzZliY0ZQ1-C_VWoxNE5KN9ZBwN6yKSfA'))

if __name__ == '__main__':

    api_call = slack_client.api_call('users.list')
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print(f'Bot ID for {user["name"]} is {user.get("id")}')
    else:
        print(f'could not find bot user with the name {BOT_NAME}')
