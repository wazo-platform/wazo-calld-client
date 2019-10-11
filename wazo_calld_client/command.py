# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import CalldError
from .exceptions import InvalidCalldError


class CalldCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response):
        try:
            raise CalldError(response)
        except InvalidCalldError:
            RESTCommand.raise_from_response(response)
