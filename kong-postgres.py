


# https://getkong.org/install/docker/




docker run \
    -d \
    --name kong-database \
    -p 9042:9042 \
    cassandra:2.2
        
        
kongdb-data:
    image: postgres:9.4
    volumes:
        - "/var/lib/postgresql/data"
    command: "/bin/true"
        

        
kong-database:
    image: postgres:9.4
    volumes_from:
        - "kongdb-data"
    environment:
        - "POSTGRES_USER=kong"
        - "POSTGRES_PASSWORD=kong"
    restart: unless-stopped







        
docker run \
    -d \
    --name kong-api-gateway \
    --link kong-database:kong-database \
    -e "KONG_DATABASE=cassandra" \
    -e "KONG_CASSANDRA_CONTACT_POINTS=kong-database" \
    -e "KONG_PG_HOST=kong-database" \
    -p 8000:8000 \
    -p 8443:8443 \
    -p 8001:8001 \
    -p 7946:7946 \
    -p 7946:7946/udp \
    kong
        

        
# 8000 – non-SSL enabled proxy layer for API requests.
# 8443 – SSL enabled proxy for API requests.
# 8001 – RESTful Admin API for configuration. You will use this port to administrate your Kong installation.
# 7946 – This is used for Kong clustering        

# 8053 - dnsmasq     
        
        
        
        
# Kong is running:
curl http://127.0.0.1:8001       
        
        
        
        
        
        
        
        
        
