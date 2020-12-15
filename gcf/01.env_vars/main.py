import os
def env_vars(request):
    return os.environ.get('GCP_PROJECT', 'Specified environment variable is not set.')
