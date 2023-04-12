# Copyright 2015-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class TransfersCommand(CalldCommand):
    resource = 'transfers'

    def list_transfers_from_user(self):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource)
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_transfer(self, transfer_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, transfer_id)
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_transfer(
        self,
        transferred,
        initiator,
        context,
        exten,
        flow='attended',
        variables=None,
        timeout=None,
    ):
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
        headers = self._get_headers()
        url = self.base_url
        r = self.session.post(url, json=body, headers=headers)

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
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource)
        r = self.session.post(url, json=body, headers=headers)
        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def complete_transfer(self, transfer_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, transfer_id, 'complete')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def complete_transfer_from_user(self, transfer_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, transfer_id, 'complete')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def cancel_transfer(self, transfer_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, transfer_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def cancel_transfer_from_user(self, transfer_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, transfer_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)
