# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class CtidNGError(HTTPError):

    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidCtidNGError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
        except KeyError:
            raise InvalidCtidNGError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(CtidNGError, self).__init__(exception_message, response=response)


class InvalidCtidNGError(Exception):
    pass
