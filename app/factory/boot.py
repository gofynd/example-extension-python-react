from .redis import RedisManager

async def startup(app, loop):
    pass
  

async def shutdown(app, loop):
    await RedisManager.close()