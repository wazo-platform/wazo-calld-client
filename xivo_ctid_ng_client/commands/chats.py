# -*- coding: utf-8 -*-
# Copyright 2016-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class ChatsCommand(RESTCommand):

    resource = 'chats'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def send_message(self, from_, to, alias, msg, to_xivo_uuid=None):
        body = {
            'from': from_,
            'to': to,
            'alias': alias,
            'msg': msg,
        }
        if to_xivo_uuid:
            body['to_xivo_uuid'] = to_xivo_uuid
        r = self.session.post(self.base_url,
                              json=body,
                              headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def send_message_from_user(self, to, alias, msg, to_xivo_uuid=None):
        body = {
            'to': to,
            'alias': alias,
            'msg': msg,
        }
        if to_xivo_uuid:
            body['to_xivo_uuid'] = to_xivo_uuid
        r = self.session.post(self._client.url('users', 'me', self.resource),
                              json=body,
                              headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def get_history_from_user(self, participant_user_uuid=None, participant_server_uuid=None, limit=None):
        params = {}
        if participant_user_uuid:
            params['participant_user_uuid'] = participant_user_uuid
            params['participant_server_uuid'] = participant_server_uuid
        if limit:
            params['limit'] = limit

        r = self.session.get(self._client.url('users', 'me', self.resource),
                             params=params,
                             headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
