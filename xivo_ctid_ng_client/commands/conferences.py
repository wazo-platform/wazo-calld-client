# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from ..command import CtidNGCommand


class ConferencesCommand(CtidNGCommand):

    resource = 'conferences'
    ro_headers = {'Accept': 'application/json'}
    rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_participants(self, conference_id):
        url = self._client.url(self.resource, conference_id, 'participants')
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def kick_participant(self, conference_id, participant_id):
        url = self._client.url(self.resource, conference_id, 'participants', participant_id)
        r = self.session.delete(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def mute_participant(self, conference_id, participant_id):
        url = self._client.url(self.resource, conference_id, 'participants', participant_id, 'mute')
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def unmute_participant(self, conference_id, participant_id):
        url = self._client.url(self.resource, conference_id, 'participants', participant_id, 'unmute')
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)
