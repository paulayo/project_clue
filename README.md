## E-commerce development with Django Oscar.
## Oscar is an e-commerce  framework  for building domain-driven applicatioins.


## Features of the application:
1.  Any product type can be handled including downloadable products,
     subscriptions (e.g., a T-shirt in different sizes and colours).

2.  Customisable products, such as T-shirts with personalised messages.

3. Large catalogue support - Oscar is used in production by sites 
        with more than 20 million products.



Featuring:

docker-machine version 0.14.0
docker-compose version 1.20.1
docker-py version: 3.1.4
CPython version: 3.6.4


### OS X Instructions

1. Start new machine - `docker-machine create -d virtualbox dev;`
1. Configure your shell to use the new machine environment - `eval $(docker-machine env dev)`
1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Grab IP - `docker-machine ip dev` - and view in your browser
