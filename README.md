

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

Create your ovh.conf file with the following info
```
[default]
; general configuration: default endpoint
endpoint=ovh-eu

[ovh-eu]
; configuration specific to 'ovh-eu' endpoint
application_key=<APP_KEY get from https://eu.api.ovh.com/createApp/>
application_secret=<APP_SECRET get from https://eu.api.ovh.com/createApp/>
```

Init access token
```
./init_api_fullaccess.py
```
Update your ovh.conf file with the returned token
```
echo "consumer_key=<CONSUMER_KEY get from previsous command>" >> ovh.conf
```


Now you can use any script, like
```
./get_add_domain.py
```
