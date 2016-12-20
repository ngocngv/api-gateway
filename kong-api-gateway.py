



# Create the API using the administration API and port:

# Request:
curl -i -X POST \
    --url http://127.0.0.1:8001/apis/ \
    --data 'name=kong.io' \
    --data 'upstream_url=http://api.kong.io/data/1.0' \
    --data 'request_host=api.kong.io'


    
    
# Use the administration API to confirm the Weather API was added successfully:

# Request:
curl --url http://127.0.0.1:8001/apis    

curl --url http://127.0.0.1:8001/apis | jq
curl --url http://127.0.0.1:8001/apis | python -m json.tool
    
    

    
# TEST

# Request:
curl -v 'http://127.0.0.1:8000/weather?q=London&APPID=<key>' \
    --header 'Host: api.kong.io'





    
    
    
    
# INSTALL KEY AUTHENTICATION PLUGIN
#--------------------------------------------------------------------------------------
# https://getkong.org/plugins/key-authentication/

curl -X POST \
    --url http://127.0.0.1:8001/apis/ff90b448-38ac-414e-8b2e-b02d784a01a8/plugins \
    --data "name=key-auth"

    
    

# TEST AUTHENTICATION REQUIRED
#--------------------------------------------------------------------------------------
curl -v 'http://127.0.0.1:8000/weather?q=London&APPID=<key>' \
    --header 'Host: api.kong.io'

# HTTP/1.1 401 Unauthorized



# ADD A CONSUMER:
#--------------------------------------------------------------------------------------

# Create a Consumer:
curl -X POST \
    --url http://127.0.0.1:8001/consumers/ \
    --data "username=<USERNAME>" \
    --data "custom_id=<CUSTOM_ID>"

#
curl -X POST \
    --url http://127.0.0.1:8001/consumers/ \
    --data "username=test" \
    --data "custom_id=123456"



# Create an API Key:
curl -X POST \
    --url http://127.0.0.1:8001/consumers/{consumer}/key-auth -d ''

#            
curl -X POST \
    --url http://127.0.0.1:8001/consumers/test/key-auth --data ''


            
        
# Using the API Key:

curl -v 'http://127.0.0.1:8000/weather?q=London&APPID=<key>' \
    --header 'Host: api.kong.io' \
    --header 'apikey: 6e4a113cb70c46a489a0cdccd69fcd97'


    
    
    
        
        
        
        
        
        
        
        
        
        




