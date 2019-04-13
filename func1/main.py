import requests

# URL: https://us-central1-gcp-serverless-test-237520.cloudfunctions.net/hello

def hello(request):
    # Fire off middle cloud func
    r = requests.get('https://us-central1-gcp-serverless-test-237520.cloudfunctions.net/middle_func')

    return r.text

