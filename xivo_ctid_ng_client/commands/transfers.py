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


class TransfersCommand(RESTCommand):

    resource = 'transfers'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_transfer(self, transfer_id):
        r = self.session.get('{url}/{transfer_id}'.format(url=self.base_url, transfer_id=transfer_id),
                             headers=self.headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_transfer(self, transferred, initiator, context, exten, flow='attended', variables=None):
        variables = variables or {}
        body = {
            'transferred_call': transferred,
            'initiator_call': initiator,
            'context': context,
            'exten': exten,
            'flow': flow,
            'variables': variables
        }
        r = self.session.post(self.base_url,
                              json=body,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def complete_transfer(self, transfer_id):
        self.session.put('{url}/{transfer_id}/complete'.format(url=self.base_url, transfer_id=transfer_id),
                         headers=self.headers)

    def cancel_transfer(self, transfer_id):
        self.session.delete('{url}/{transfer_id}'.format(url=self.base_url, transfer_id=transfer_id),
                            headers=self.headers)
