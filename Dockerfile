FROM alpine

ADD plugin.sh /bin/

RUN chmod +x /bin/plugin.sh

RUN apk -Uuv add curl ca-certificates

ENTRYPOINT /bin/plugin.sh
