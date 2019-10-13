# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.client import BaseClient


class CalldClient(BaseClient):

    namespace = 'wazo_calld_client.commands'

    def __init__(self, host, port=9500, version='1.0', **kwargs):
        super(CalldClient, self).__init__(
            host=host, port=port, version=version, **kwargs
        )
