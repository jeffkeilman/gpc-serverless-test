import requests

def middle_func(request):
    # Fire off final cloud func
    r = requests.get('https://us-central1-gcp-serverless-test-237520.cloudfunctions.net/do_something')

    return r.text