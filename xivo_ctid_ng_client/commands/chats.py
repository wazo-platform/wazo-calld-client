# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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
