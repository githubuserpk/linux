def process_gcs_uri(uri:str) -> (str,str,str,str):

    '''
#Note: receives a GCS uril and breaks it down to the scheme, bucket, path and file
Parameters: 
  uri (str): GCS uri

Returns:
  scheme(str): uri scheme
  bucket(str): uri bucket
  path(str): uri path
  file(str): uri file
    '''
    print("in process gcs uri function")

    a="a"
    b="b"
    c="d"
    d="d"

    url_arr = uri.split("/")
    if "." not in url_arr[-1]:
        filename=""
    else:
        filename = url_arr.pop()
    scheme = url_arr[0]
    bucket = url_arr[2]
    path = "/".join(url_arr[3:])
    return scheme, bucket, path, filename

    #return a,b,c,d

uri = "gs://pkdeltaai-01-bucket/requirements.txt"
scheme, bucket, path, filename = process_gcs_uri(uri)
print("scheme, bucket, path, filename: ",scheme,bucket,path,filename)
