<p align="center" style="font-size: 53px; font-weight:bold; color: transparent; -webkit-background-clip: text; background-clip: text; background-image: linear-gradient(90deg, red, orange, fuchsia);">
    User controller
</p>


-----


## Setup:
> ```shell
> # SSH
> git clone git@github.com:xristxgod/USER-CONTROLLER.git
> # HTTPS
> git clone https://github.com/xristxgod/USER-CONTROLLER.git
> ```


-----


## Settings in .prod.env file:
> `TOKEN_DADATA` - Token from the DADATA service
> 
> `DATABASE_URI` - Database url
> 
> `CACHE_DATABASE_NAME` - Database name for cache
> 
> `CACHE_DATABASE_COLLECTION` - Collection name
> 
> `CACHE_DATABASE_URI` - Database url for cache


-----


## How to run:
> ```shell
> # Run
> docker-compose -f docker-compose.yml up --build
> # Stop
> docker-compose -f docker-compose.yml stop
> ```
