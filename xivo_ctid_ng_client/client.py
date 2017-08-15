# -*- coding: utf-8 -*-
# Copyright (C) 2015 Avencall
#
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.client import BaseClient


class CtidNGClient(BaseClient):

    namespace = 'ctid_ng_client.commands'

    def __init__(self,
                 host,
                 port=9500,
                 version='1.0',
                 **kwargs):
        super(CtidNGClient, self).__init__(
            host=host,
            port=port,
            version=version,
            **kwargs)
