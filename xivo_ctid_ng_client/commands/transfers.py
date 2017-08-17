# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Avencall
#
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class TransfersCommand(RESTCommand):

    resource = 'transfers'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_transfers_from_user(self):
        url = self._client.url('users', 'me', self.resource)
        r = self.session.get(url,
                             headers=self.headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_transfer(self, transfer_id):
        r = self.session.get('{url}/{transfer_id}'.format(url=self.base_url, transfer_id=transfer_id),
                             headers=self.headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_transfer(self, transferred, initiator, context, exten, flow='attended', variables=None, timeout=None):
        variables = variables or {}
        body = {
            'transferred_call': transferred,
            'initiator_call': initiator,
            'context': context,
            'exten': exten,
            'flow': flow,
            'variables': variables,
            'timeout': timeout,
        }
        r = self.session.post(self.base_url,
                              json=body,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def make_transfer_from_user(self, exten, initiator, flow, timeout=None):
        body = {
            'exten': exten,
            'initiator_call': initiator,
            'flow': flow,
            'timeout': timeout,
        }
        r = self.session.post(self._client.url('users', 'me', self.resource),
                              json=body,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def complete_transfer(self, transfer_id):
        self.session.put('{url}/{transfer_id}/complete'.format(url=self.base_url, transfer_id=transfer_id),
                         headers=self.headers)

    def complete_transfer_from_user(self, transfer_id):
        url = self._client.url('users', 'me', self.resource, transfer_id, 'complete')
        self.session.put(url, headers=self.headers)

    def cancel_transfer(self, transfer_id):
        self.session.delete('{url}/{transfer_id}'.format(url=self.base_url, transfer_id=transfer_id),
                            headers=self.headers)

    def cancel_transfer_from_user(self, transfer_id):
        url = self._client.url('users', 'me', self.resource, transfer_id)
        self.session.delete(url, headers=self.headers)
