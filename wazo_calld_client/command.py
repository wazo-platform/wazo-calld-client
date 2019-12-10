# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import CalldError
from .exceptions import InvalidCalldError


class CalldCommand(RESTCommand):

    ro_headers = {'Accept': 'application/json'}
    rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_headers(self, write=False, **kwargs):
        headers = dict(self.rw_headers) if write else dict(self.ro_headers)
        tenant_uuid = kwargs.get('tenant_uuid') or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        return headers

    @staticmethod
    def raise_from_response(response):
        try:
            raise CalldError(response)
        except InvalidCalldError:
            RESTCommand.raise_from_response(response)
