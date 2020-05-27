# redis-chat

WIP - Experimenting with Redis to create a chat room app

## Chat protocol

To create a message:

1. serialise like above
2. `LPUSH` message on to list with key `general-history`
3. `PUBLISH` message on to topic `general-chat`

To read message history

1. `LPUSH` `general-history` `<your preferred history>`
2. de-serialise as above

To read message live as they come in:

1. `SUBSCRIBE` to topic `general-chat`
2. de-serialise as above
