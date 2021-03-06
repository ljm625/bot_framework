FROM tiangolo/uwsgi-nginx:python2.7
COPY nginx.conf /etc/nginx/conf.d/
COPY ./ /app
RUN pip install -r /app/requirements.txt
EXPOSE 5050
VOLUME ["/app/config"]