# -*- coding: utf-8 -*-
# Copyright 2020-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class LinesCommand(CalldCommand):

    resource = 'lines'

    def list_lines(self, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = self._client.url(self.resource)

        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
