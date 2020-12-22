# Twitter Basic Bot

I created a Twitter Bot deployed on Docker, It currently has the following functionality: 

* Auto Reply - Replies to user who tweets directly at the 'host' account given pre-defined keywords are mentioned. 
* Auto Tweet - Automatically tweets URl Links gathered from the NY times API periodically. 
* Follow followers - Automatically follows back those who follow the 'host' account. 

More functionallity to be added.

## Pre-requisites: 

* A Twitter account for the bot 
* Twitter Developer Account 
* Tweepy 
* **Recommended** - Virtualenv
* Docker
 
## Getting the bot running
 
1. Create a twitter application - https://apps.twitter.com/app/new
1. Fill out the required fields
1. After completing the process successfully gather the following credentials: 

  * Consumer key
  * Consumer secret
  * Access token
  * Access secret
  
1.Enter the credentials in the 'Config.py' in the respective fields.   


That's it! You should now have a working Twitter Bot. 

*This is NOT a deployabl version....In The coming weeks I'll be making changes to refine and ensure it is closer to a deployable solution. i.e*

 * Docker Deployment 
 * Virtual Environment Setup 
 
 
 
 My hope is that by sharing my progress... I Can gather feedback and work towards a one-size fits all solution. 


**Support**
If you happen to get stuck anywhere, feel free to raise an issue here. Also, you can contact me via email. 
