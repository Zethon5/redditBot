# redditBot
THIS IS MY FIRST REDDIT BOT

This bot is a fully functional reddit bot. The bot in this folder is associated with the account
/u/XXXXXX (Censored for privacy reasons.

This bot is capable of going through the comments in the r/FocusST subreddit and welcoming users 
if it believes they posted about recently picking up a Focus ST. This bot is also capable of running 
through any comment post in the subreddit and:
	/u/XXXXXX   -    Bot, will reply to comment and list commands the redditors can use the bot will reply to. 
	!oil        -    Bot will respond with type of oil, a filter to use, and how frequently to change oil. 

I have tried to implement fail safes for the bot, so that it can persist through error without crashing. 
Some of these methods include:
	- try/except statements.
	- time.sleep() 

To keep the bot from recommenting on comments it has already commented on:
	Bot finds comment with command word
	Bot checks if comment's id exists in a csv file, 
	If id isn't present, Bot responds and adds the comment's id to the csv
	If id is present, bot ignores ID
  SAME GOES FOR POSTS.

This subreddit is very low traffic so it was easy to practice on and allow me to have 
a good amount of control with what my bot was doing, and very unlikely anyone would care.
Mods were messaged letting them know I was going to be botting the subreddit, but they didn't respond.

To Keep this program running, I could likely use Pythonanywhere.com (PA). However, the code is pretty inieffecient
and would likely eat up PA cpu time too fast. 
