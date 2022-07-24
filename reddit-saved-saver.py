import praw, os, config
from praw.models import Submission, Comment
from datetime import datetime

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent='Reddit Saved Saver by /u/tobiasvl')

print("Fetching...")

try:
    saved = reddit.user.me().saved(limit=1000)
except:
    sys.exit("Failed to find your saved posts, did you add your credentials to config.ini?")

top_dir = 'reddit/'

if not os.path.exists(top_dir):
    os.mkdir(top_dir)

for submission in saved:
    sub_dir = top_dir + submission.subreddit.display_name + '/'
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
    with open(sub_dir + submission.id + '.md', 'w', encoding="utf-8") as f:
        f.write('---\n')
        #f.write('id: ' + submission.id + '\n')
        f.write('subreddit: /r/' + submission.subreddit.display_name + '\n')
        f.write('timestamp: ' + str(datetime.utcfromtimestamp(submission.created_utc)) + '\n')
        try:
            f.write('author: /u/' + submission.author.name + '\n')
        except:
            f.write('author: [deleted]\n')
        f.write('tags: [reddit, ' + submission.subreddit.display_name + ']\n')
        #f.write('permalink: https://reddit.com' + submission.permalink + '\n')
        f.write('---\n\n')
        f.write('Permalink: https://reddit.com' + submission.permalink + '\n')
        if isinstance(submission, Submission):
            f.write('# ' + submission.title + '\n\n')
            if submission.is_self:
                f.write(submission.selftext)
            else:
                f.write(submission.url)
        elif isinstance(submission, Comment):
            f.write(submission.body)
        f.write('\n\n')
        f.write('#reddit #' + submission.subreddit.display_name)
