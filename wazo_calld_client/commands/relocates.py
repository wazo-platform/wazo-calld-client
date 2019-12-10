# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class RelocatesCommand(CalldCommand):

    resource = 'relocates'

    def list_from_user(self):
        url = self._client.url('users', 'me', self.resource)
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_from_user(self, relocate_uuid):
        url = self._client.url('users', 'me', self.resource, relocate_uuid)
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def create_from_user(
        self, initiator, destination, location=None, completions=None, timeout=None
    ):
        body = {'initiator_call': initiator, 'destination': destination}
        if location:
            body['location'] = location
        if completions:
            body['completions'] = completions
        if timeout:
            body['timeout'] = timeout

        r = self.session.post(
            self._client.url('users', 'me', self.resource),
            json=body,
            headers=self.rw_headers,
        )

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def complete_from_user(self, relocate_uuid):
        url = self._client.url('users', 'me', self.resource, relocate_uuid, 'complete')
        r = self.session.put(url, headers=self.rw_headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def cancel_from_user(self, relocate_uuid):
        url = self._client.url('users', 'me', self.resource, relocate_uuid, 'cancel')
        r = self.session.put(url, headers=self.rw_headers)

        if r.status_code != 204:
            self.raise_from_response(r)
