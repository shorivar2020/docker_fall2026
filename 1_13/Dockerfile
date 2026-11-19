FROM golang:1.27.4
WORKDIR /usr/src/app
COPY . .
RUN go build
RUN go test ./...
EXPOSE 8080

CMD ["./server"]
