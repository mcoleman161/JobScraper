import discord
import asyncio
import subprocess
import scraper

# Replace 'your_token_here' with your actual bot token
TOKEN = 'MTE3MjAzMjg0NjY0MzM0MzQ2MQ.Gc1XDy.vg_bAvB6P0b6kmE93IHVtpo-txpnrjPrb4RumE'

client = discord.Client(intents=discord.Intents.default())
client.message_content = True


def PrintJobList(job_list):
    for job in job_list:
        print(job)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    #await client.process_commands(message)
    if message.author == client.user: #bot cannot read itself
        return

    if message.content.startswith('!NewJobs'):
        print('creating CSV...')
        scraper.create_new_csv()
        print('retrieving jobs...')
        addedJobs = scraper.return_added_jobs()
        removedJobs = scraper.return_removed_jobs()


        await message.channel.send(f'The new jobs since the last run are as followed: ')
        for added_job in addedJobs:
            # We must break the csv format back down to user friendly text
            split_job = added_job.split(',')
            await message.channel.send(f' JOB TITLE:  {split_job[0]}')
            await message.channel.send(f' JOB CRAFT:  {split_job[1]}')
            await message.channel.send(f' PRODUCT TEAM:  {split_job[2]}')
            await message.channel.send(f' OFFICE:  {split_job[3]}')
            await message.channel.send("----")

        await message.channel.send(f'The jobs removed since the last run are as followed: ')
        for removed_job in removedJobs:
            split_removed_job = removed_job.split(',')
            await message.channel.send(f' JOB TITLE:  {split_removed_job[0]}')
            await message.channel.send(f' JOB CRAFT:  {split_removed_job[1]}')
            await message.channel.send(f' PRODUCT TEAM:  {split_removed_job[2]}')
            await message.channel.send(f' OFFICE:  {split_removed_job[3]}')
            await message.channel.send('-----')
        scraper.cleanup_csvs()
client.run(TOKEN)