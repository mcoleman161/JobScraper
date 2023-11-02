from requests_html import HTMLSession
import csv
session = HTMLSession()
r = session.get('https://www.riotgames.com/en/work-with-us/jobs#office=884&officeName=Los%20Angeles%2C%20USA')
print(r.html.absolute_links) # Debug: to see how to parse absolute links
#r.html.render() not needed to pre-render for tags at this time

csv_file = open('riot_scape.csv', 'w', encoding='utf-8')
csv_Input = csv.writer(csv_file, delimiter=',')
csv_Input.writerow(['TITLE', 'GROUP', 'PROJECT', 'LOCATION'])

jobListings = r.html.find('a.job-row__inner')
for jobListing in jobListings:
    jobList = jobListing.find('a.job-row__inner', first=True).text
    print()
    jobList = jobList.replace(' ', '_')
    jobList = jobList.replace(',', '')
    jobList = jobList.replace("\n",',')
    
    print(jobList)
    res = list(map(str.strip, jobList.split(',')))# What was I even smoking this day, splitting a string on comma then stripping it into a map and storing into a list
    csv_Input.writerow(res) # Write list to CSV. List should not go over len(3) but we just jam it in without checking (Whoops)
    
csv_file.close() #Close CSV


#TODO Create CSV Comparison Function, Possibly Utilizing Sets as nothing should double

#TODO Create email section if Comparison Function returns None then an email should still be sent that no changes occurred.

#TODO Remove previous CSV and overwrite with current? or do we just check for latest? do we want emperical data?
    #Revaluation we are going to rewrite previous with new. Goal of project is to create alerts not data analysis at this time.

