sudo apt update
sudo apt install python3 python3-dev python3-venv python3-setuptools build-essential -y
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
python3 --version
pip3 --version
# setup virtual environment venv for isolation
# python3 -m venv venv
# source venv/bin/activate
# pip3 install --upgrade pip
# python3 -m pip install --upgrade setuptools
