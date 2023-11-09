from requests_html import HTMLSession
import csv
import os #needed for file rename
import discord
import asyncio
import subprocess

def create_new_csv():
    session = HTMLSession()
    r = session.get('https://www.riotgames.com/en/work-with-us/jobs#office=884&officeName=Los%20Angeles%2C%20USA')
    #print(r.html.absolute_links) # Debug: to see how to parse absolute links
    #r.html.render() not needed to pre-render for tags at this time

    new_csv_file = open('new_riot_scrape.csv', 'w', encoding='utf-8')
    csv_Input = csv.writer(new_csv_file, delimiter=',')
    csv_Input.writerow(['TITLE', 'GROUP', 'PROJECT', 'LOCATION'])

    jobListings = r.html.find('a.job-row__inner')
    for jobListing in jobListings:
        jobList = jobListing.find('a.job-row__inner', first=True).text
        #print() # Adding in an end line in the worst way possible for debugging.
        jobList = jobList.replace(' ', '_')
        jobList = jobList.replace(',', '')
        jobList = jobList.replace("\n",',')
        
        #print(jobList) #Debug print statement
        res = list(map(str.strip, jobList.split(',')))# What was I even smoking this day, splitting a string on comma then stripping it into a map and storing into a list
        csv_Input.writerow(res) # Write list to CSV. List should not go over len(3) but we just jam it in without checking (Whoops)
        
    new_csv_file.close() #Close CSV


def return_added_jobs():
    with open('riot_scrape.csv', 'r') as t1, open('new_riot_scrape.csv', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    
    diffJobs = []
    for line in filetwo:
        if line not in fileone:
            #line.replace('_', ' ')
            diffJobs.append(line)
    return diffJobs
               
def return_removed_jobs():
    with open('riot_scrape.csv', 'r') as t1, open('new_riot_scrape.csv', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    
    removedJobs = []
    for line in fileone:
        if line not in filetwo:
            #line.replace('_', ' ')
            removedJobs.append(line)
    return removedJobs

#We now have a difference CSV.

def cleanup_csvs():
    #TODO Remove previous CSV and overwrite with current? or do we just check for latest? do we want emperical data?
        #Revaluation we are going to rewrite previous with new. Goal of project is to create alerts not data analysis at this time.
    try:
        os.remove('riot_scrape.csv')
    except OSError:
        print("Failed to remove previous riot scrape file due to it not existing.")

    try:
        os.rename('new_riot_scrape.csv','riot_scrape.csv')
    except:
        print("OSError occurred, file most likely did not get deleted prior to rename.")
