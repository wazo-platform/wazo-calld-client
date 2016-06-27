# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Avencall
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


class CallsCommand(RESTCommand):

    resource = 'calls'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_calls(self):
        url = self.base_url

        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_call(self, call_id):
        url = '{base_url}/{call_id}'.format(base_url=self.base_url,
                                            call_id=call_id)

        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_call(self, call):
        r = self.session.post(self.base_url,
                              json=call,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def make_call_from_user(self, extension, variables=None):
        body = {'extension': extension}
        if variables:
            body['variables'] = variables
        r = self.session.post(self._client.url('users', 'me', self.resource),
                              json=body,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def hangup(self, call_id):
        url = '{base_url}/{call_id}'.format(base_url=self.base_url,
                                            call_id=call_id)

        self.session.delete(url, headers=self.headers)

    def connect_user(self, call_id, user_id):
        url = '{base_url}/{call_id}/user/{user_id}'.format(base_url=self.base_url,
                                                           call_id=call_id,
                                                           user_id=user_id)

        r = self.session.put(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
