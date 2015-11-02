# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
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

    def make_call(self, token=None, **kwargs):
        url = '{base_url}/calls'.format(base_url=self.base_url)

        headers = {'X-Auth-Token': token}
        r = self.session.post(url,
                              headers=self.headers,
                              params=kwargs
                             )

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()['data']

    def get_call(self, call_id=None, token=None):
        url = '{base_url}/calls/{call_id}'.format(base_url=self.base_url,
                                                  call_id=call_id
                                                 )

        headers = {'X-Auth-Token': token}
        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()['data']

    def hangup(self, call_id=None, token=None):
        url = '{base_url}/calls/{call_id}'.format(base_url=self.base_url,
                                                  call_id=call_id)

        headers = {'X-Auth-Token': token}
        self.session.get(url, headers=self.headers)
