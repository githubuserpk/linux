#reference url: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample

from google.cloud import storage
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('myapp-dev-bucket-raw')
# Then do other things...
#blob = bucket.get_blob('remote/path/to/file.txt')
#print(blob.download_as_string())
#blob.upload_from_string('New contents!')
blob2 = bucket.blob('storage.txt')
blob2.upload_from_filename(filename='storage.txt')
