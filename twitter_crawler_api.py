#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import packages for crawler
import tweepy
import requests
import shutil
import os


# In[5]:


def get_img(api,username):
    # Iterate through the first 200 statuses in the friends timeline
    tweets =  tweepy.Cursor(api.home_timeline).items(200)



    #download all media files to current working dir.
    #fix 2: download to twitter_images dir.
    media_files = []
    tweet_id = []
    for status in tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.append(media[0]['media_url'])
            tweet_id.append(status.id)


    path = os.path.dirname(os.path.realpath("twitter_crawler_api"))
    path = os.path.join(path, "twitter_images")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)        

    for media_file in media_files:
        if (media_file.split('.')[-1].lower() == 'jpg') or (media_file.split('.')[-1].lower() == 'png'):
            res = requests.get(media_file)
            imagefile = open(os.path.join('twitter_images', os.path.basename(media_file)), 'wb')
            for chunk in res.iter_content(100000):
                imagefile.write(chunk)
            imagefile.close()
    return tweet_id


# In[6]:


def get_cats(is_cat,tweet_id,api):
    path = os.path.dirname(os.path.realpath("twitter_crawler_api"))
    path = os.path.join(path, "cat_images")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)    
    tweet_id_out = tweet_id.copy()
    for i,cat in enumerate(is_cat):
        if cat != 1:
            tweet_id_out.remove(tweet_id[i])
    tweets = api.statuses_lookup(tweet_id_out)
    media_files = []
    for status in tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.append(media[0]['media_url'])
            
    for media_file in media_files:
        if (media_file.split('.')[-1].lower() == 'jpg') or (media_file.split('.')[-1].lower() == 'png'):
            res = requests.get(media_file)
            imagefile = open(os.path.join('cat_images', os.path.basename(media_file)), 'wb')
            for chunk in res.iter_content(100000):
                imagefile.write(chunk)
            imagefile.close()


# In[7]:


if __name__ == "__main__": 
    get_img()
    get_cats()

