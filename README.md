# t-mobile_s8_updates

## Description
Got tired of checking my wife's phone every night for software updates, so I wrote this to do it for me. 

The last software update the T-Mobile S8 got was back on June 17, 2018. This will check the T-Mobile software update page for the section that references that date, as it is (currently) a single (ginormous) string containing all the updates. When a new update arrives, I **assume** that they'll update that section in a timely manner.  

The `config.py` contains that section, which hasn't changed since June. `s8_update.py` will pull that section from the live site, compare it against the June block, and if there's a change, it'll send an email. If not, then it'll just check again the next time it runs. If using **cron**, I recommend the following, hourly check:  

`0 * * * * /path/to/t-mobile_s8_updates/s8_updates.py`  


## How To
The 'config.py' file has, among other things that don't need to be changed, the following:  
```
smtp_srv    = 'CHANGEME_SMTP-SERVER'
passwd      = 'CHANGEME_APPLICATION-SPECIFICPASSWORD'
from_name   = 'CHANGEME_YOUR-NAME'
from_email  = 'CHANGEME_YOUR-EMAIL-ADDRESS'
to_email    = 'CHANGEME_RECIPIENT-EMAIL-ADDRESS'
subject     = 'CHANGEME_SUBJECT'
body        = 'CHANGEME_BODY'
...
```

Go ahead ahd change everything as necessary. Below are some common servers and instructions.

---  
### DO NOT USE YOUR ACTUAL PASSWORD!!!  
### GENERATE AN APPLICATION SPECIFIC PASSWORD!!!
---  

**SMTP Servers:**  
Gmail     : smtp.gmail.com  
Apple     : smtp.mail.me.com  
Microsoft : smtp-mail.outlook.com  
Yahoo     : smtp.mail.yahoo.com  

**Application Specific Passwords:**  
Gmail     : https://security.google.com/settings/security/apppasswords  
Apple     : https://support.apple.com/en-us/HT204397  
Microsoft : https://support.microsoft.com/en-us/help/12409/microsoft-account-app-passwords-two-step-verification  
Yahoo     : https://help.yahoo.com/kb/SLN15241.html (or switch to one of the above mail providers instead) =P  

## Questions?
Feel free to contact me if you have questions. This was obviously done just for fun because I'm lazy, so I won't be putting that much more work into this than what I've already done. But if there's something obvious that needs to be addressed, I'll _possibly_ look into it.  

And yes, I'm sure there are better ways to do this. Feel free to do it those ways if you want. =P 
