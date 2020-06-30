###############################################
# program: follow_account_followers.py
# author: Gilton Bosco
# version: 1.1
# date: 29 June 2020
###############################################

#importing os and dotenv packages so as to manage the environmental variables such as username and password
#importing smart_run so as to terminate smartly

import os
from dotenv import load_dotenv
from instapy import InstaPy
from instapy.util import smart_run

#loading the .env file from the root directory
load_dotenv()

#getting the username and password from the .env file
user_name = os.getenv('user_name')
user_password = os.getenv('user_password')

#A list of accounts that we need to follow their followers
accounts_to_follow_followers = ['enockgraphics','beka_graphics','saydgraphy','shine_graphics','mr_swahili']


session = InstaPy(username=user_name, password=user_password,want_check_browser=True) 


with smart_run(session, threaded=True):
	session.follow_user_followers(accounts_to_follow_followers, amount=20,
	                                  randomize=True, interact=False)
	session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)
	
	session.set_skip_users(skip_private=True,
	                       skip_no_profile_pic=True,
			               skip_business=True,
			               business_percentage=100)
	session.unfollow_users(amount=10, nonFollowers=True, style="FIFO", unfollow_after=60, sleep_delay=655)
	photo_comments = ["Nice!", "Sweet!", "Beautiful :heart_eyes:"]
	session.set_do_follow(enabled=True, percentage=100, times=2)
	session.set_do_comment(enabled=True, percentage=100)
	session.set_comments(photo_comments,media = 'Photo')