# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class AdhocConferencesCommand(CalldCommand):

    resource = 'adhoc_conferences'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_from_user(self, host_call_id, *participant_call_ids):
        body = {
            'host_call_id': host_call_id,
            'participant_call_ids': participant_call_ids,
        }
        r = self.session.post(
            self._client.url('users', 'me', 'conferences', 'adhoc'),
            json=body,
            headers=self.headers,
        )

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def delete_from_user(self, adhoc_conference_id):
        r = self.session.delete(
            self._client.url(
                'users',
                'me',
                'conferences',
                'adhoc',
                adhoc_conference_id,
            ),
            headers=self.headers,
        )

        if r.status_code != 204:
            self.raise_from_response(r)

    def add_participant_from_user(self, adhoc_conference_id, call_id):
        r = self.session.put(
            self._client.url(
                'users',
                'me',
                'conferences',
                'adhoc',
                adhoc_conference_id,
                'participants',
                call_id,
            ),
            headers=self.headers,
        )

        if r.status_code != 204:
            self.raise_from_response(r)

    def remove_participant_from_user(self, adhoc_conference_id, call_id):
        r = self.session.delete(
            self._client.url(
                'users',
                'me',
                'conferences',
                'adhoc',
                adhoc_conference_id,
                'participants',
                call_id,
            ),
            headers=self.headers,
        )

        if r.status_code != 204:
            self.raise_from_response(r)
