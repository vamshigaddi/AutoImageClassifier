from minio import Minio
from minio.error import S3Error

# Initialize MinIO client
client = Minio(
    'objectstore.e2enetworks.net',
    access_key='',
    secret_key='',
    secure=True
)

# List all buckets
buckets = client.list_buckets()
for bucket in buckets:
    print(f"Bucket: {bucket.name}")

# # List objects in a bucket
bucket_name = 'gis-storage'
# objects = client.list_objects(bucket_name, recursive=True)
# for obj in objects:
#     print(f"Object: {obj.object_name}")

# List objects under a specific prefix (folder)
prefix = 'ipcam/'
objects = client.list_objects(bucket_name, prefix=prefix, recursive=True)
for obj in objects:
    print(f"Object in folder: {obj.object_name}")
