

# https://docs.gelato.io/guides/advanced-kong-integration



# Step 1: Create the "loop-back" API
#-----------------------------------------------------------------------------------------------------

curl -X POST http://127.0.0.1:8001/apis \
    -d "name=admin-loop-back" \
    -d "request_path=/admin-loop-back" \
    -d "upstream_url=http://localhost:8001" \
    -d "strip_request_path=true"


#   
curl -i -X POST \
    --url http://127.0.0.1:8001/apis/ \
    --data "name=test.io" \
    --data "request_host=api.test.io" \
    --data "request_path=/api-test" \
    --data "upstream_url=http://mockbin.org/request"
    
    



# test
curl -i -X GET http://127.0.0.1:8000/api-test -H "Host: api.test.io" 



# Step 2: Add API Key Authentication
#-----------------------------------------------------------------------------------------------------

curl -X POST http://localhost:8001/apis/admin-loop-back/plugins \
    -d "name=key-auth"

    
#
curl -i -X POST \
    --url http://127.0.0.1:8001/apis/test.io/plugins \
    --data "name=key-auth" \
    --data "config.key_names=X-AUTH"




# Step 3: Create a Consumer
#-----------------------------------------------------------------------------------------------------

curl -X POST http://localhost:8001/consumers \
    -d "username=loop-back-consumer"


#
curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/ \
    --data "username=<USERNAME>" \
    --data "custom_id=<CUSTOM_ID>"


curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/ \
    --data "username=testio" \
    --data "custom_id=123456"


    

# Step 4: Create an API Key for our Consumer
#-----------------------------------------------------------------------------------------------------

curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/testio/key-auth \
    --data "key=testkey"
    
    
curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/testio/key-auth \
    --data "key=testkey01"
    
    
    
    
# test
curl -X GET http://127.0.0.1:8001/consumers/testio/key-auth

curl -i -X GET http://127.0.0.1:8000/api-test -H "host: api.test.io" -H "x-auth: testkey"

        
curl -i -X GET -H "host: api.test.io" -H "x-auth: testkey" http://127.0.0.1:8000/api-test
  







