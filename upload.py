from dotenv.main import load_dotenv
load_dotenv()
import os
import string
import random
import requests
from boto3 import Session

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
REGION_NAME = os.environ['REGION_NAME']
BUCKET_NAME = os.environ['BUCKET_NAME']

# Upload file
OBJECT_NAME_TO_UPLOAD = "Route53.png"


ses = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY,
              region_name=REGION_NAME)

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
s3 = ses.client('s3')
response = s3.generate_presigned_post(
    Bucket=BUCKET_NAME, 
    Key= OBJECT_NAME_TO_UPLOAD+"-"+key , 
    ExpiresIn=600
    )

print(response)

files = {'file': open(OBJECT_NAME_TO_UPLOAD,'rb')}
r = requests.post(response['url'], data=response['fields'], files=files)
print(r.status_code)