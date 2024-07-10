import json
from typing import Union

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NewsListConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "news"
        self.room_group_name = "update"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # Receive message from WebSocket
    async def receive_json(self, content, **kwargs):
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "list.update",
                "data": content,
            },
        )

    # Receive message from room group
    async def list_update(self, event: Union[str, dict]):
        data = event["data"]

        # msgpack cant deal with datetime.datetime
        if type(data) == str:
            data = json.loads(data)

        if data.get("wake"):
            return

        # Send message to WebSocket
        await self.send_json(data)
