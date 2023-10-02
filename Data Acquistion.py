# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 02:42:10 2022

@author: Shubham
"""


# Importing libraries
from pytube import Search, YouTube
import os
# import moviepy.editor as mp
import re
import apafy as pafy


# Reading the songs list from text file
my_file = open(r"D:\UoR\fall2022\datamining\final_project\musicoutfitters.txt", 'r', encoding='utf8')
data = my_file.read()
data_into_list = data.replace('\n', ' ').split(",")


# Adding the keyword "song" for full songs and "song #shorts" for shorts
songs_list = [x + " song" for x in data_into_list]
short_songs_list = [x + " #shorts" for x in songs_list]


# Initializing lists and variables
full_song_title = []
full_song_url = []
short_songs_title = []
short_songs_url = []

count = 0
half_accept = 0
iter_var = 0

# Defining path for download
download_path = r'D:\UoR\fall2022\datamining\final_project\downloaded_songs\only_shorts_folder'
download_path1 = r'D:\UoR\fall2022\datamining\final_project\downloaded_songs\music-outfitters\shorts'
download_path_full = r'D:\UoR\fall2022\datamining\final_project\downloaded_songs\full_songs' 
download_path_full1 = r'D:\UoR\fall2022\datamining\final_project\downloaded_songs\music-outfitters\full-songs' 

full_song_path_list = []
short_song_path_list = []


# Running the loop for short songs list

for i in range(len(short_songs_list)):
    
    # Getting the search list for each song
    s = Search(short_songs_list[i])
    s_full = Search(songs_list[i])
    iter_var += 1
    
    #print("song number : ", iter_var)
    
    # initializing max_rating to -1 since there is a possibility of 0 rating everywhere and current_vid_index to 0
    max_rating = -1
    current_vid_index = 0
    # flag_first_download = 1
    
    
    # Iterating through the search results
    for i in range(len(s.results)):
        try:
            
            # For entire song
            full_vid = s_full.results[0]
            full_vid_url = full_vid.watch_url
            yt_full = YouTube(full_vid_url)
            
            # For shorts 
            current_vid = s.results[i]
            current_vid_url = current_vid.watch_url
            yt = YouTube(current_vid_url)
            
            
            # creating a pafy instance for the searched video song
            current_vid_pafy = pafy.new(current_vid_url)
            
            hashtag_present = False
            
            vid_desc = yt.description
            vid_length = yt.length
            vid_title = yt.title
            vid_rating = yt.rating
            
            # Only consider the short if it has the hashtag in it
            if ("#Shorts" in vid_desc or "#shorts" in vid_desc):
                #print("#shorts present in name")
                hashtag_present = True
            else:
                hashtag_present = False
                

            # The short length must be less than 60 seconds and more than 25 seconds
            if((vid_length<61 and hashtag_present==True and vid_length>25) or  (i == len(s.results) - 1)):
                
                
                if (vid_length<61 and hashtag_present==True and vid_length>25):
                    #print("Rating: ", vid_rating)
                    if vid_rating > max_rating:
                        
                        max_rating = vid_rating
                        current_vid_index = i
                    
                    count = count + 1
                    #print("count: ",count)
                

                
                if count%3 == 0 or i == len(s.results) - 1:
                    # For shorts 
                    if count%3!=0:
                        count = (count//3 + 1)*3
                    current_vid = s.results[current_vid_index]
                    current_vid_url = current_vid.watch_url
                    yt = YouTube(current_vid_url)
                    
                    vid_desc = yt.description
                    vid_length = yt.length
                    vid_title = yt.title
              
                    
                    # Applying regex to get a suitable file name
                    yt_full_new_title = re.sub(r'[!"#$%&()*+,./;<=>?@[\]^`{|}~\']', '', yt_full.title.split('.mp4')[0]) + '.mp4'
                    
               
                    file_name_shorts = download_path1 + '\\' + yt_full_new_title + " - shorts.mp4"
                    file_name = download_path_full1 + '\\' + yt_full_new_title + " -  song.mp4"
                    
                    short_song_path_list.append(file_name_shorts)
                    full_song_path_list.append(file_name)
                    
                    
                    # Removing duplicates
                    if(os.path.exists(file_name)):
                        os.remove(file_name)
                    
                    if(os.path.exists(file_name_shorts)):
                        os.remove(file_name_shorts)
                    
                    # Downloading the full song
                    yt_full_file = yt_full.streams.filter(only_audio=True).first().download(download_path_full1)
                    
                    
                    if(os.path.exists(yt_full_file)):
                        print("Full song exists")
                    
                    # Renaming the full song file
                    os.rename(yt_full_file, file_name)
                    
                    
                    print("Full song downloaded")
                    
                    # Downloading the short song
                    yt_shorts_file = yt.streams.filter(only_audio=True).first().download(download_path1)
                    if(os.path.exists(yt_shorts_file)):
                        print("Short exists")
                        
                    # Renaming the short song file
                    os.rename(yt_shorts_file, file_name_shorts)
                    print("Short downloaded")
                    
                    
                    print("---------------------------------------")
                    print("The short is downloaded with the name : ", yt.title)
                    print("The full song is downloaded with the name : ", yt_full.title)
                    print("---------------------------------------")
                
                
                    break
        except:
            #print("Except statement")
            continue

    
# Removing duplicates and creating final folder with correct names

for i in range(len(full_song_path_list)):
    
    if(os.path.exists(full_song_path_list[i])):
        # print(full_song_path_list[i])
        print(os.path.exists(short_song_path_list[i]))
        if (os.path.exists(short_song_path_list[i]) == False):
            print(full_song_path_list[i])
            os.remove(full_song_path_list[i])
            
    if(os.path.exists(short_song_path_list[i])):
        # print(short_song_path_list[i])
        if (os.path.exists(full_song_path_list[i]) == False):
            print(short_song_path_list[i])
            os.remove(short_song_path_list[i])
    
    
    
    
print("Number of songs downloaded are ", count//3)
print("Number of half_accept songs are ", half_accept)
print("Total number of songs are ", len(songs_list))



