from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def finish_crawl_udn_nba(task):
    def send_ws_msg(channel_name: str, type: str, data: dict):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            channel_name,
            {
                "type": type,
                **data,
            },
        )

    if task.result:
        send_ws_msg("update", "list.update", {"updated": 1})
