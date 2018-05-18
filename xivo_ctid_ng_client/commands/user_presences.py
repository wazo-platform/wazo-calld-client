# -*- coding: utf-8 -*-
# Copyright (C) 2016 Avencall
# Copyright (C) 2016 Proformatique, Inc.
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class UserPresencesCommand(RESTCommand):

    resource = 'presences'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_presence(self, user_uuid, xivo_uuid=None):
        kwargs = {'headers': self.headers}
        if xivo_uuid:
            params = {'xivo_uuid': xivo_uuid}
            kwargs['params'] = params

        r = self.session.get(self._client.url('users', user_uuid, self.resource), **kwargs)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_presence_from_user(self):
        r = self.session.get(self._client.url('users', 'me', self.resource),
                             headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def update_presence(self, user_uuid, presence):
        body = {
            'presence': presence,
        }

        r = self.session.put(self._client.url('users', user_uuid, self.resource),
                             json=body,
                             headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def update_presence_from_user(self, presence):
        body = {
            'presence': presence,
        }

        r = self.session.put(self._client.url('users', 'me', self.resource),
                             json=body,
                             headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)
