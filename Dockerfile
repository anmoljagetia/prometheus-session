FROM python:3.5.1-onbuild
WORKDIR /code
ADD . /code
#COPY prometheus-node-exporter /etc/docker/
#RUN chmod 777 /etc/docker/prometheus-node-exporter
#ENV ARGS "-collector.diskstats.ignored-devices=^(ram|loop|fd)\d+$ -collector.filesystem.ignored-mount-points=^/(sys|proc|dev|run)($|/) -collector.textfile.directory=/var/lib/prometheus/node-exporter" 
#CMD python app.py
#EXPOSE 9100
#RUN /etc/docker/prometheus-node-exporter $ARGS &
CMD python app.py

