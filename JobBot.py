import discord
import asyncio
import subprocess
import scraper
import os
from dotenv import load_dotenv
import time # we need time for logging

# Replace 'your_token_here' with your actual bot token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())
client.message_content = True

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    user = await client.fetch_user(126111364476305409)
    seconds = 3600
    try:
        await user.send('Hello! I have started.')
    except:
        print("USER NOT FOUND")
    print(user)
    await send_jobs(user)    
    while user:     
        await timer(user, seconds)

async def send_jobs(user):
    #await client.process_commands(message)S

    print('creating CSV...')
    scraper.create_new_csv()
    print('retrieving jobs...')
    added_jobs = scraper.return_added_jobs()
    removed_jobs = scraper.return_removed_jobs()

    if added_jobs != []:
        await user.send(f'The new jobs since the last run are as followed: ')
        for added_job in added_jobs:
            # We must break the csv format back down to user friendly text
            split_job = added_job.split(',')
            await user.send(f' JOB TITLE:  {split_job[0]}\nJOB CRAFT:  {split_job[1]}\nPRODUCT TEAM:  {split_job[2]}\nOFFICE:  {split_job[3]}\n-------')
    elif removed_jobs != []:
        user.send(f'The jobs removed since the last run are as followed: ')
        for removed_job in removed_jobs:
            split_removed_job = removed_job.split(',')
            await user.send(f' JOB TITLE:  {split_removed_job[0]}\nJOB CRAFT:  {split_removed_job[1]}\nPRODUCT TEAM:  {split_removed_job[2]}\nOFFICE:  {split_removed_job[3]}\n-------')
    else:
        print("No changes were found this run")
    scraper.cleanup_csvs()

async def timer(user, seconds):
    #Every hour call send_jobs
    await asyncio.sleep(seconds)
    await send_jobs(user)


client.run(TOKEN)