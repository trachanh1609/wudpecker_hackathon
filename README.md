# wudpecker_hackathon

## 1. Elasticsearch
You need Elasticsearch ready and an index created. Elasticsearch can be in local machine or in the cloud.
The name of the index should match INDEX_NAME in .env file

Follow /elasticsearch/README.md to install on Docker
Here is the sample of the .env file and Elasticsearch is running on Localhost port 9200
```
ES_USERNAME=elastic
ES_PASSWORD=mylocalhost

INDEX_NAME=search-calls
```


## 2. Python virtual venv and FastAPI
Create venv
```
# For WINDOWS
\wudpecker_hackathon>python -m virtualenv -p="C:\Users\anh_v\AppData\Local\Programs\Python\Python39\python.exe" venv

# For MAC
sudo pip3 install virtualenv
$virtualenv --python=python3.9 venv
```

Activate venv
```
# For WINDOWS
\wudpecker_hackathon>.\venv\Scripts\activate

# For MAC
$source venv/bin/activate
```

Install requirements
```
\wudpecker_hackathon>pip install -U -r requirements.txt
```


Run FastAPI server
```
$uvicorn main:app --reload 
```

