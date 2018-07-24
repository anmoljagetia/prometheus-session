# prometheus-session
A short demo on how to use docker-compose and docker to create a Web Service connected to a load balancer and a Redis Database. The following is monitored using Prometheus, Alertmanager and the visualizations are drawn in Grafana.


# Install
The instructions assume that you have already installed [Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/).

In order to get started be sure to clone this project onto your machine. Please note that the demo webservices will inherit the name from the directory you create. If you create a folder named test. Then the services will all be named test-web, test-redis, test-lb. Also, when you scale your services it will then tack on a number to the end of the service you scale.

```
git clone https://github.com/anmoljagetia/prometheus-session.git
```

# How to get up and running

Once you've cloned the project to your host we can now start our demo project. Navigate to the directory in which you have cloned the project and run :

```
docker-compose up -d
```

The  docker-compose command will build a few images, pull the remaining images from Docker Hub and then link them together based on the information inside the docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. After the command completes, we thestatus can now be viewed by running :

```
docker-compose ps
```

# Scaling
Now comes the fun part of compose which is scaling. Let's scale our web service from 1 instance to 3 instances. This will now scale our web service container. We now should run an update on our stack so the Loadbalancer is informed about the new web service containers. you can see that the instances are automatically registered for monitoring on prometheus. When we similarly downscale, the instances are automatically removed.

```
docker-compose scale web=3
```

# Alerting
We can test alerting, by gettinga ny of the sample alerts to fire. We are presently monitoring all the components, so we can kill the redis container, and see that the webservice is broken. We can then investigate, and see that the alert was fired because the backend redis had failed.

Similarly, we can test for fullness by sending requests to the webservice. This will be then trigger the **TooManyRequests Alert**.
