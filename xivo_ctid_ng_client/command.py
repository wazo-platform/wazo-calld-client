# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.command import RESTCommand

from .exceptions import CtidNGError
from .exceptions import InvalidCtidNGError


class CtidNGCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        try:
            raise CtidNGError(response)
        except InvalidCtidNGError:
            RESTCommand.raise_from_response(response)
