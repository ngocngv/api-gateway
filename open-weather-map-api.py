


# ADD OPEN WEATHER MAP API
# http://openweathermap.org/current


# Add your API using the RESTful API
#-------------------------------------------------------------------------------------------

curl -i -X POST \
    --url http://127.0.0.1:8001/apis/ \
    --data 'name=api.openweathermap.org' \
    --data 'upstream_url=http://api.openweathermap.org/data/2.5/' \
    --data 'request_host=api.openweathermap.org'


    
    

curl -v 'http://127.0.0.1:8000/weather?q=London&APPID=<key>' \
    --header 'Host: api.openweathermap.org'


# API key you created after registering with Open Weather Mapper.

curl -v 'http://127.0.0.1:8000/weather?q=London&APPID=5175e4224d160e3f7077182cc0a211bc' \
    --header 'Host: api.openweathermap.org' \
    --header 'apikey: 6e4a113cb70c46a489a0cdccd69fcd97'





    
    
# Forward your requests through Kong
#-------------------------------------------------------------------------------------------
# Issue the following cURL request to verify that Kong is properly forwarding requests to your API:

curl -i -X GET   \
    --url 'http://127.0.0.1:8000/weather?q=London&APPID=5175e4224d160e3f7077182cc0a211bc' \
    --header 'Host: api.openweathermap.org' \
    --header 'apikey: 6e4a113cb70c46a489a0cdccd69fcd97'






















