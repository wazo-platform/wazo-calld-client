# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class TrunksCommand(CalldCommand):

    resource = 'trunks'
    ro_headers = {'Accept': 'application/json'}
    rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_trunks(self):
        url = self._client.url(self.resource)
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
