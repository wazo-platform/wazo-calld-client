# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class SwitchboardsCommand(RESTCommand):

    resource = 'switchboards'
    headers = {'Accept': 'application/json'}

    def list_queued_calls(self, switchboard_uuid):
        url = self._client.url(self.resource, switchboard_uuid, 'calls', 'queued')
        r = self.session.get(url, headers=self.headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def answer_queued_call_from_user(self, switchboard_uuid, call_id):
        url = self._client.url(self.resource, switchboard_uuid, 'calls', 'queued', call_id, 'answer')
        r = self.session.put(url)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
