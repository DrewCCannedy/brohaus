# Brohaus - A House Website
## Development Usage - Windows
1. Clone the Repo
2. Make sure you have `python3` installed
3. Navigate to the folder `cd %path-to-brohaus%/brohaus`
4. run `py -m venv brohaus-env` to create a python virtual environment
5. run `.\brohaus-env\Scripts\activate` to activate the environent
6. run `pip install -r requirements.txt` to download the needed dependencies
7. connect to the gcloud sql database instance
   1. save [this](https://dl.google.com/cloudsql/cloud_sql_proxy_x64.exe) as `cloud_sql_proxy` somewhere you will remember
   2. navigate to where you saved `cloud_sql_proxy` in a new terminal
   3. run `cloud_sql_proxy -instances="brohaus:us-central1:brohaus-db"=tcp:3306`
8. run `python manage.py runserver` to start the development server
## TODO
 - Add personal pages
 - Optimizing for mobile
## CHANGELOG
#### VERSION 1.1
 - Google Cloud Deployment
 - Added functionality to deploy to google cloud
#### VERSION 1.0
 - Initial deployment
 - Added home and gecko point pages
 - Added ability to login