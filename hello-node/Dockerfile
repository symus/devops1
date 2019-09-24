FROM node:6

MAINTAINER symus "syedmustafa.net@gmail.com"

WORKDIR /hello-node

COPY ./package*.json /hello-node

RUN npm install
#RUN npm ci --only=production

COPY . /hello-node

RUN ["chmod", "+x", "/hello-node/wait-for-it.sh"]

CMD ["bash", "/hello-node/wait-for-it.sh", "rabbitmq-server:5672", "--", "node", "app.js"]
