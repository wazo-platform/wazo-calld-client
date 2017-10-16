# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_ctid_ng_client.command import CtidNGCommand


class RelocatesCommand(CtidNGCommand):

    resource = 'relocates'
    rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_from_user(self, initiator, destination, location=None):
        body = {
            'initiator_call': initiator,
            'destination': destination,
        }
        if location:
            body['location'] = location

        r = self.session.post(self._client.url('users', 'me', self.resource),
                              json=body,
                              headers=self.rw_headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()
