# JobScraper
Python code for scraping mediocre job boards and putting them into easy to use CSV with email updates.

The object of this is to scrape a website, store the data into a csv utilizing panda. Then compare said file to previous csv for changes.

** Note we ignore line changes so if a job is removed then reposted this will not trigger an event.

* Unique IDs will be utilized when available as this is a more sure way then string comparison.

* The current target output is a CSV to utilize pivot tables and graphs however Qt5 may be adopted to pre-generate useful graphs if there is a need.