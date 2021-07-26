import praw
import time

# Authentication
def authenticate():
    print("Logining in...")
    reddit = praw.Reddit("Bbot",
                        user_agent = "Catwoman's comment replies v.01")
    print("Login successfull as " + str(reddit.user.me()))
    return reddit


# Main working
def replybot(reddit, comments_list, message):
    print("Getting new comments...")
   
    for comment in reddit.subreddit("batman").stream.comments(skip_existing=True):
        if ("catwoman" in comment.body.lower() or "cat woman" in comment.body.lower()) and (comment.id not in comments_list) and (comment.author != reddit.user.me()):
            print("Comment found: " + comment.body)
            comment.reply(message)
            print("Successfully replied!:) ")
            
            try:
                comments_list.append(comment.id)
            except Exception as e: print(e)
                
            #saving comment.id
            with open("files/commentsreplylist.txt","a") as f:
                f.write(comment.id + '\n')
            
            print("Sleeping for 3 seconds...\n")        
            time.sleep(3)


# Main function
def main():
    message = ("Batman [don't do that!!]"
    "(https://media3.giphy.com/media/yyhJaoPDhCbBu/giphy.gif?cid=ecf05e47jdk9fabggr6zdmk52c61vfao2u3huw9jrfnwlhjl&rid=giphy.gif&ct=g) "
    "Do you even know where that kitty has been?\n --- \n"
    "^beep ^boop! ^I ^am ^a ^bot ^that ^replies ^to ^the ^word ^***Catwoman***!  ^Find ^out ^more [^about ^me ^here](https://www.reddit.com/r/u_batman_bot)^!")  
    
    with open("files/commentsreplylist.txt","r") as f:
        comments_list= f.read().split('\n')
        comments_list= list(filter(None, comments_list))
        
    
    reddit = authenticate()
    replybot(reddit, comments_list, message)
    
if __name__ == '__main__': main()