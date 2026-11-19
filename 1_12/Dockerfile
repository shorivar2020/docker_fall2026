FROM ubuntu:24.04
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
EXPOSE 5001

CMD ["serve", "-s", "-l", "5001", "build"]
