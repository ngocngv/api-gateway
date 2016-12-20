

# https://github.com/Mashape/mockbin/blob/master/docs/install.md




docker run \
    -d \
    --name mockbin-redis \
    -p 6379:6379 \
    redis

 

#
# Requirements:

# Node.js (v0.10.x or higher)
# Redis
# npm modules listed in package.json


# Install from source
git clone https://github.com/Mashape/mockbin.git ./mockbin
cd mockbin


# Dockerfile
#-----------------------------------------------------------------------------------------------------




# Building the docker image
docker build -t mockbin .


    
#
docker run \
    -d \
    -p 8080:8080 \
    --name mockbin-ui \
    --link mockbin-redis:redis \
    --link kong-api-gateway:kong \
    mockbin
    
    
    
    
    
