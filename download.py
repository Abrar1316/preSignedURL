from dotenv.main import load_dotenv
load_dotenv()
import os
from boto3 import Session

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
REGION_NAME = os.environ['REGION_NAME']
BUCKET_NAME = os.environ['BUCKET_NAME']

ses = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY,
              region_name=REGION_NAME)


s3 = ses.client('s3')
url = s3.generate_presigned_url(
      ClientMethod='get_object',
      Params={
             'Bucket': BUCKET_NAME,
             'Key': "Route53.png-anaxYcCEp4",
             'ResponseContentDisposition': 'attachment'
             },
             ExpiresIn=180
      )

print(url)

