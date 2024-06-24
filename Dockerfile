FROM alpine

ADD plugin.sh /bin/

RUN chmod +x /bin/plugin.sh

RUN apk -Uuv add curl ca-certificates jq

ENTRYPOINT /bin/plugin.sh
