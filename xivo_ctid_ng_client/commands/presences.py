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


class PresencesCommand(RESTCommand):

    resource = 'presences'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_presence(self, user_uuid):
        r = self.session.get(self._client.url('users', user_uuid, self.resource),
                             headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_presence_from_user(self):
        r = self.session.get(self._client.url('users', 'me', self.resource),
                             headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def update_presence(self, user_uuid, status_name):
        body = {
            'presence': status_name,
        }

        r = self.session.put(self._client.url('users', user_uuid, self.resource),
                             json=body,
                             headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def update_presence_from_user(self, status_name):
        body = {
            'presence': status_name,
        }

        r = self.session.put(self._client.url('users', 'me', self.resource),
                             json=body,
                             headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)
