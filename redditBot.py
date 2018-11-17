#IMPORTS----------------------------------------------------------------------------------------------------------------
import praw                                                                                          #REDDIT API WRAPPER
import csv                                                                               #ALLOWS ME TO WRITE TO CSV FILE
import pandas as pd                                                                          #ALLOWS ME TO READ CSV FILE
import time

#MISC. VARIABLES--------------------------------------------------------------------------------------------------------
col_names_post = ['postids']
col_names_comm = ['commids']
col_names_help = ['helpids']
years = ["11" , "12", "13","14", "15", "16", "17", "18", "19",]                     #THIS IS NO LONGER USED IN THE SCRIPT
theTime = 0

#COMMENT VARIABLES------------------------------------------------------------------------------------------------------
ifDumb = ("^^This ^^bot ^^is ^^run ^^by ^^/u/XXXXXXXXXXX ^^If ^^I'm ^^doing ^^something ^^stupid ^^please ^^message ^^him. ^^^^Sorry")
#-----------------------------------------------------------------------------------------------------------------------
newST = (
"""Welcome to the community! Congratulations on your ST! 

Here are some other cool places to learn more about your car:

* [FocusST.org](https://www.focusst.org/)

* [Ford Subreddit](https://www.reddit.com/r/Ford/)

Have fun, and drive safe!

""" + ifDumb)
#-----------------------------------------------------------------------------------------------------------------------
focusOil = (
"""**Ford Focus ST**

* Oil : 5w-30

* Filter : Motorcraft Oil Filter-FL-400S [($7)](https://www.mountuneusa.com/Motorcraft-Oil-Filter-FL-400-S-p/fl-400s.htm)

* Suggested changed every 5,000 miles.


""" + ifDumb)
#-----------------------------------------------------------------------------------------------------------------------
focuspsi = ('')

howCanIHelp = (
"""Hi, I can help if your comment includes the following (add an '!' in front of the word !example)

* oil""")

#REDDIT AUTH------------------------------------------------------------------------------------------------------------
reddit = praw.Reddit(client_id = 'XXXXXXXXXXXXXXXXXX',                                      #BASIC AUTHENTICATION TO USE 
                     client_secret='XXXXXXXXXXXXXXXX',                                      #AS A CERTAIN REDDIT ACCOUNT
                     username='XXXXXXXXXXXXXXXXXXXXX',
                     password='XXXXXXXXXXXXXXXXXXXXX',
                     user_agent='XXXXXXXXXXXXXXXXXXX')

subreddit = reddit.subreddit('FocusST')                                             #PICKS THE SUBREDDIT I'D LIKE TO SEE
#.selftext                                                                                         #RETURNS TEXT IN POST
#.title                                                                                       #RETURNS TEXT OF THE TITLE
submissions = reddit.subreddit('FocusST').new(limit=10)                             #RETURNS 10 MOST RECENT POSTS IN SUB

#ACTIONS----------------------------------------------------------------------------------------------------------------
def postHunt():                                                                         #SEARCHES THROUGH 10 MOST RECENT 
    print('Starting new scan')                                                    #SUBREDDIT'S POSTS FOR CERTAIN TRIGGER
    dataPost = pd.read_csv('postid.csv', names=col_names_post)                        #WORDS TO TRIGGER CERTAIN RESPONSE
    dataPost = dataPost.set_index('postids')
    for joined in submissions:
        if 'joined' in joined.title.lower() or 'new to me' in joined.title.lower():
            if str(joined.id) in dataPost.index:
                pass

            else:
                try:
                    print('Found someone new!')
                    print(str(joined.id) +' - ' + str(joined.title))
                    with open('postid.csv', 'a') as postCheck:
                        writer = csv.writer(postCheck)
                        writer.writerow([str(joined.id)])
                    for year in years:
                        if year in joined.title:
                            joined.reply(newST)
                            print('Replied - Sleeping 10 minutes.')
                            time.sleep(600)
                        else:
                            joined.reply(newST)
                            print('Replied - Sleeping 10 minutes.')
                            time.sleep(600)
                except:
                    print('Too Frequent to welcome - OK ERROR')

def helpYou():                                                                        
    loopsKill = 0
    for helpComment in subreddit.stream.comments():
        dataHelp = pd.read_csv('helpid.csv', names=col_names_help)
        dataHelp = dataHelp.set_index('helpids')
        loopsKill +=1
        if '/u/XXXXXXX' in helpComment.body:
            if helpComment.id in dataHelp.index:
                pass
            else:
                try:
                    helpComment.reply(howCanIHelp)
                    print(str(helpComment.id))
                    print('Helping ST Owner!')
                    with open('helpid.csv','a') as helpCheck:
                        writer1 = csv.writer(helpCheck)
                        writer1.writerow([str(helpComment.id)])
                except:
                    print('Too Frequent to help - OK ERROR')
        if loopsKill ==100:
            break

def oilComms():                                                                                #SEARCHES SUBREDDIT'S MOST
    loopKill = 0                                                                              #RECENT COMMENTS FOR '!OIL'
    for oilcomment in subreddit.stream.comments():                                            #AND REPLIES WITH OIL SPECS
        dataComm = pd.read_csv('commid.csv', names=col_names_comm)                                 #FOR THE FORD FOCUS ST
        dataComm = dataComm.set_index('commids')
        loopKill +=1
        if '!oil' in oilcomment.body:
            if oilcomment.id in dataComm.index:
                pass
            else:
                try:
                    oilcomment.reply(focusOil)
                    print(str(oilcomment.id))
                    print('Oil request printed')
                    with open('commid.csv', 'a') as oilCheck:
                        writer = csv.writer(oilCheck)
                        writer.writerow([str(oilcomment.id)])
                except:
                    print('Too Frequent to define - OK ERROR')
        if loopKill == 100:
            break
#PERMA LOOP-------------------------------------------------------------------------------------------------------------
while True:
    postHunt()
    oilComms()
    helpYou()
    if theTime % 60 == 0:
        print('Searched for : ' + str(theTime / 60) + ' min.')
    theTime +=15
    time.sleep(15)
