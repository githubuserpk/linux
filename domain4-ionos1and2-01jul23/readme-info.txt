Problem Statement: 
I was using ilearngcp.xyz domain until end of jun 2023.  This domain is registered in India so the google support is not 
willing to support as domain is in India.  Hence, I had to create another domain in uk.

Why do I need google support:
I need google support because I am running dataplex dq task.  When I execute the task i get the error max vcpu reached for 
this region europe-west2.  The max being 8 and the serverless dataproc that runs the dq task needs 12 vcpu
I want to increase the quota from 8 to 12, only then the dq task will execute.  Thats why i need google support.

Another use case where i need to increase quota is - while running a vertex ai job - video from shane robinson from google 

ionos1 and ionos2:
==================
ionos1: 
I created a domain in ionos learngcp.online and tried to register with cloud identity.  It keeps giving me the error: 
"This domain name is already in use.  If you own this domain and would like to use Google Workspace, please follow these steps <link>"
I tried to change the registered domain from google to the domain email ie gcpadmin@learngcp.online email and tried to
register again but got same error.  

ionos2:  date: 01-jul-2023
============================
In this case, 
I first went to google cloud identity and selected the option "I need a new domain".  
It then asked me to enter the domain you want.  I entered learngcp.uk.  It showed me that it is available and costs £10 / year
I accepted it and went to next step.  
Next screen, it then asked me to enter which email id you will be using text box and hard coded @learngcp.uk populated by google. 
I entered wsadmin, so it looks like this on screen: wsadmin@learngcp.uk 
 
Next screen, it asked me to verify the domain.

Now, the interesting bit.  I went to ionos again and then registered second domain in minutes! 
It gave me option to select the domain name i want, I selected learngcp.uk.  It gave me mesg that "This domain is available"
I proceeded and took the 5 user option and created the domain successfully.  
Checked the dns propogation and saw the green ticks on different regions in the world.
Now, logged in back to google cloud identity and logged in to wsadmin@learngcp.uk 
It was waiting on "verify domain learngcp.uk".

I clicked on verify and clicked next, it automatically identified the registerer as 1and1 (ie ionos old company name)
and successfully verified.

I went ahead and created another user
gcpadmin@learngcp.uk

USed the gcpadmin user to login to gcp console

Now, only thing pending is to enable the billing




