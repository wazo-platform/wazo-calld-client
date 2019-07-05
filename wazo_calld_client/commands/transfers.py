# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class TransfersCommand(CalldCommand):

    resource = 'transfers'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_transfers_from_user(self):
        url = self._client.url('users', 'me', self.resource)
        r = self.session.get(url, headers=self.headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_transfer(self, transfer_id):
        r = self.session.get(
            '{url}/{transfer_id}'.format(url=self.base_url, transfer_id=transfer_id),
            headers=self.headers,
        )
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
        r = self.session.post(self.base_url, json=body, headers=self.headers)

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
        r = self.session.post(
            self._client.url('users', 'me', self.resource),
            json=body,
            headers=self.headers,
        )

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def complete_transfer(self, transfer_id):
        r = self.session.put(
            '{url}/{transfer_id}/complete'.format(
                url=self.base_url, transfer_id=transfer_id
            ),
            headers=self.headers,
        )
        if r.status_code != 204:
            self.raise_from_response(r)

    def complete_transfer_from_user(self, transfer_id):
        url = self._client.url('users', 'me', self.resource, transfer_id, 'complete')
        r = self.session.put(url, headers=self.headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def cancel_transfer(self, transfer_id):
        r = self.session.delete(
            '{url}/{transfer_id}'.format(url=self.base_url, transfer_id=transfer_id),
            headers=self.headers,
        )
        if r.status_code != 204:
            self.raise_from_response(r)

    def cancel_transfer_from_user(self, transfer_id):
        url = self._client.url('users', 'me', self.resource, transfer_id)
        r = self.session.delete(url, headers=self.headers)
        if r.status_code != 204:
            self.raise_from_response(r)
