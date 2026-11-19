FROM ubuntu:24.04
EXPOSE 5001
WORKDIR /usr/src/app

COPY public ./public
COPY src ./src
COPY package* .

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash
RUN apt install -y nodejs
RUN npm install
RUN npm run build
RUN npm install -g serve

CMD ["serve", "-s", "--listen", "5001", "build"]
