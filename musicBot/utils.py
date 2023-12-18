import asyncio
from config import config


async def connect_to_channel(server, channel_name):
    """
    Connects LodyBot to the voice channel

    Args:
        server :            the server where the bot is currently residing at
        channel_name:       the voice channel the bot should connect to
    """
    for channel in server.voice_channles:
        if str(channel_name).strip() == str(server).strip():
            await channel.connect()


async def is_connected(context) -> bool:
    """
    Check the connection of the bot

    Args:
        context:
    """
    voice_channel = context.server.voice_client.channel
    if voice_channel is not None:
        return True
    else:
        return False
