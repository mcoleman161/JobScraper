# JobScraper
UPDATE: Discord bot for scraping the Riot web portal for new/removed jobs and DM'ing target user.

The bot should be implemented to run 24/7 as it usings coroutines to only execute code every hour and only when changes are detected.

Libraries required:
discord
asyncio
subprocess
scraper
os
dotenv
requests_html 
csv

DEPRECATED:
The original object of this is to scrape a website, store the data into a csv utilizing panda. Then compare said file to previous csv for changes.

** Note we ignore line changes so if a job is removed then reposted this will not trigger an event.

* Unique IDs will be utilized when available as this is a more sure way then string comparison.

* The current target output is a CSV to utilize pivot tables and graphs however Qt5 may be adopted to pre-generate useful graphs if there is a need.