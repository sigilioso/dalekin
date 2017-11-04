#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


sys.path.append(os.path.abspath('./dalekin'))


if __name__ == '__main__':
    from dalekin import bot, config
    bot.app.go_fast(host=config.HOST, port=config.PORT)
