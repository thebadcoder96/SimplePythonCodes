# Automate Instagram 

This is a tool that will allow you to like and comment on posts for given tags and also follow the accounts of the posts you have liked. It uses the instagram-private-api python package build around the Instagram API.

### How to run

- Install required package by ```pip install -r requirements.txt``` in the terminal/cmd.
- Must have an instagram account. Enter your username and password in the respective variables in [line 49-50](/AutoInsta/Insta.py#L49). Code in [Insta.py](/AutoInsta/Insta.py)
- You can enter the tags in the ```tags``` variable in [line 52](/AutoInsta/Insta.py#L52).
- Enter ```ppt``` in [line 54](/AutoInsta/Insta.py#L54). It is the number of posts that the program will *like per tag*. Default is set to ```10``` and the value can have a range of ```0-86```
-  Simply run the code on any IDE or by ```python3 Insta.py``` in the terminal/cmd.


**NOTE:** Please be careful as running the code multiple times in a short span can get your account to be flagged suspicious by Instagram. 
