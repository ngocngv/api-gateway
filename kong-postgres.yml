version: '2'
services:     
        
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


    kong-api-gateway:
        image: haufelexware/wicked.kong:latest
        depends_on:
            - "kong-database"
        security_opt:
            - seccomp:unconfined
        expose:
            - "8000"
        environment:
            - "DATABASE=postgres"
            - "VIRTUAL_HOST=https://${PORTAL_NETWORK_APIHOST}:443"
            - "VIRTUAL_HOST_WEIGHT=100"
            - "EXCLUDE_PORTS=7946,8001,8443"
            - "EXTRA_SETTINGS=http-request set-header X-Forwarded-Port %[dst_port]"
            - "SSL_CERT=${GATEWAY_PEM}"
        command: "dockerize -timeout 30s -wait tcp://kong-database:5432 kong start"
        restart: unless-stopped




        
# 8000 – non-SSL enabled proxy layer for API requests.
# 8443 – SSL enabled proxy for API requests.
# 8001 – RESTful Admin API for configuration. You will use this port to administrate your Kong installation.
# 7946 – This is used for Kong clustering        

# 8053 - dnsmasq     
        
        
        
        
        
        
        
        
        
        
