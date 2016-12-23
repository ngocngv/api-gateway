

# https://docs.gelato.io/guides/advanced-kong-integration



# Step 1: Create the "loop-back" API

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
curl -i -X GET http://127.0.0.1:8000/api-test -d "Host: api.test.io" 




  
  
  
