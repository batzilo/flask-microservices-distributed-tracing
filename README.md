Flask microservices distributed tracing
=======================================

This is a simple example to demonstrate how to trace the logs
of a single request, while it traverses multiple microservices
within an [microservices pattern application](https://microservices.io/patterns/microservices.html).

This concept is called [Distributed tracing](https://microservices.io/patterns/observability/distributed-tracing.html).

To see it in action, you will need `docker` and `docker-compose`.

```
# Start all the microservices
docker-compose up --build

# Fire a request, and get the `Request_ID` from the HTTP response headers
curl -v -X POST http://localhost:9000/foo
...
< Request_ID: 0mgcu76i7fcwl3o82c0zi7u6zzf5uwxd
...
{"data": ... }


# Get the logs from all microservices belonging to your request
docker-compose logs --no-color --timestamps | grep 0mgcu76i7fcwl3o82c0zi7u6zzf5uwxd | sed -e 's/^.*[|]\s//' | sort
```
