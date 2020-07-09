
#install virtualenv called env and activate
virtualenv env
source env/bin/activate

#Install the dependencies needed to run the samples.

$ pip install -r requirements.txt



steps: 
1. install the required modules as mentioned above
2. run the deidentify step usage: python deid-fpe.py 
3. run the reidentify step usage: python reid-fpe.py
