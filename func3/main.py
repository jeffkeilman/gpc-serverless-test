import random, requests, time
from google.cloud import datastore

# URL: https://us-central1-gcp-serverless-test-237520.cloudfunctions.net/do_something

def do_something(request):
    # Wait a while and save something random to a database
    time.sleep(3)

    # Get a random int
    rand_int = random.randint(1, 100)
    
    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = 'Number'
    # The name/ID for the new entity
    name = 'rand_num' + str(rand_int)
    # The Cloud Datastore key for the new entity
    rand_key = datastore_client.key(kind, name)

    # Prepares the new entity
    rand = datastore.Entity(key=rand_key)
    rand['num'] = rand_int

    # Saves the entity
    try:
        datastore_client.put(rand)
    except:
        return 'Failure!'

    return 'Success!'