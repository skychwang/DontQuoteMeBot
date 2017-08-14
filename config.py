import praw, string

user_agent=''#Insert any string literal here.
client_id=''#Insert script id as received from Reddit.
client_secret=''#Insert script secret as received from Reddit.
username = ''#Insert your Reddit bot account username.
password = ''#Insert your Reddit bot account password.

subreddit = 'AskReddit'#Replace, if desired, with the subreddit you want this bot to operate on.

bot = praw.Reddit(user_agent=user_agent,
                  client_id=client_id,
                  client_secret=client_secret,
                  username=username,
                  password=password)
