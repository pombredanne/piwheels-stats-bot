from twitter import twitter
from db import PiWheelsDatabase

db = PiWheelsDatabase()

downloads = db.count_downloads_yesterday()
time_saved = db.get_time_saved_yesterday()
days = str(time_saved).split(',')[0]
tweet = ('Yesterday, {:,} packages were downloaded from piwheels.org, '
         'saving users over {} of build time').format(downloads, days)

if downloads and time_saved:
    print('Tweeting: {}'.format(tweet))
    twitter.update_status(status=tweet)
else:
    print('Not tweeting: {}'.format(tweet))
