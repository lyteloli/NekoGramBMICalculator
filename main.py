from const import NEKO, STORAGE
import asyncio
import menus


async def main():
    await STORAGE.acquire_pool()
    NEKO.attach_router(menus.bmi.FUNCTIONS_ROUTER)
    NEKO.attach_router(menus.start.FORMATTERS_ROUTER)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    NEKO.start_polling()
