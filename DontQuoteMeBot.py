import praw, string
import config

bot = config.bot

subreddit = bot.subreddit(config.subreddit)

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    author = comment.author
    if comment.author != config.username:
        if "dont quote me" in text.lower().translate(str.maketrans('', '', string.punctuation)):
            message = (">{}\n\n***\n~ u/{}").format(text, author)
            comment.reply(message)

