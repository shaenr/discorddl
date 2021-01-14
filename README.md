# discorddl

Takes csv files from discord and dumps downloads of all urls.

Just **SETUP** and follow instructions for **WINDOWS** or **LINUX**. 

Check the `ouput/` directory that was created when you're done
## Setup

### Prepare CSV Files From Discord
Your csv files from discord should be in `csv/` directory; you can have any number such as `csv/example1.csv` and `csv/example2.csv`.

They should all look something like this, with exactly 4 commas between `ID,Timestamp,Contents,Attachments`. Items to download listed below...


```
ID,Timestamp,Contents,Attachments
73224332,2020-12-31 05:24:32.491000+00:00,look at this 1,discordurl.com/pic1.png
73224332,2020-12-31 05:24:32.491000+00:00,look at this 2,discordurl.com/pic2.png
72232432,2020-12-31 05:24:32.491000+00:00,look at this 3,discordurl.com/pic3.png
...
```

## Windows
Just click `install_win.bat` and it will install and run for the first time. If you would like to run it again just use `run.bat`

## Linux
`bash install_linux.sh` should work. If for some reason you can't get it to install, try `touch executeonce.txt` to make sure this file exists.
`python3 script.py` will do it after that.