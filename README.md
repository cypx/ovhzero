

Reference
* OVH API https://eu.api.ovh.com/
* Python wrapper https://github.com/ovh/python-ovh


Init project
```
sudo apt install python-pip python-virtualenv
virtualenv --no-site-packages ./venv
source ./venv/bin/activate
pip install -Ur requirements.txt
```

Go to https://eu.api.ovh.com/createApp/ and create an API application.

Init access token
```
./init_api_fullaccess.py
```
Update your ovh.conf file with the returned token

Now you can use any script, like
```
./get_add_domain.py
```
