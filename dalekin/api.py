# -*- coding: utf-8 -*-
import aiohttp

from .config import TELEGRAM_BASE_URL


def api_url(method):
    return TELEGRAM_BASE_URL.format(method=method)


async def telegram_request(method, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url(method), params=params) as resp:
            if resp.status != 200:
                pass  # TODO: log error
            return resp
