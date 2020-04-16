import wget
import re
import image_gen
import json
import random
from retrying import retry
import praw
import configparser
counter = 0
config = configparser.ConfigParser()
config.read("/root/reddit_comment_reader/configuration/config.ini")
dirpath=config["general"]["home_directory"]
my_client_id=config['praw']['client_id']
my_client_secret=config['praw']['client_secret']
my_user_agent=config['praw']['user_agent']
subreddit=config['praw']['subreddit']
def main():
    reddit = praw.Reddit(user_agent=my_user_agent,
                         client_id=my_client_id,
                         client_secret=my_client_secret)
    submission = ""
    url = "";
    for submission in reddit.subreddit(subreddit).hot(limit=2):
        if(submission.stickied):
            continue
        else:
            title = submission.title
            submission = submission
            url = str(submission.url)
            div_id = "t3_" + str(submission.id)
            f = open(dirpath + "/title/title.txt", "w")
            f.write(title)
            f.close()
            image_gen.generate(url, div_id, "title", "title")
            break
    top_level_comments = list(submission.comments)
    for i in range(6):
        if(top_level_comments[i].stickied):
            continue
        else:
            print(top_level_comments[i])
            div_id = "t1_" + str(top_level_comments[i])
            text = top_level_comments[i].body
            text = re.sub("](.*)","]",text)
            f = open(dirpath + "/comments/" + str(i) + ".txt", "w")
            f.write(text)
            f.close()
            image_gen.generate(url, div_id, str(i), "images")
main()
