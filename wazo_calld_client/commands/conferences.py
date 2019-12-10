# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class ConferencesCommand(CalldCommand):

    resource = 'conferences'

    def list_participants(self, conference_id):
        url = self._client.url(self.resource, conference_id, 'participants')
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def user_list_participants(self, conference_id):
        url = self._client.url(
            'users', 'me', self.resource, conference_id, 'participants'
        )
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def kick_participant(self, conference_id, participant_id):
        url = self._client.url(
            self.resource, conference_id, 'participants', participant_id
        )
        r = self.session.delete(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def mute_participant(self, conference_id, participant_id):
        url = self._client.url(
            self.resource, conference_id, 'participants', participant_id, 'mute'
        )
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def unmute_participant(self, conference_id, participant_id):
        url = self._client.url(
            self.resource, conference_id, 'participants', participant_id, 'unmute'
        )
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def record(self, conference_id):
        url = self._client.url(self.resource, conference_id, 'record')
        r = self.session.post(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_record(self, conference_id):
        url = self._client.url(self.resource, conference_id, 'record')
        r = self.session.delete(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)
