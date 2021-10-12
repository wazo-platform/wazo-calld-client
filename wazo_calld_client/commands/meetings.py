# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class MeetingsCommand(CalldCommand):

    resource = 'meetings'

    def list_participants(self, meeting_uuid):
        headers = self.get_headers()
        url = self._client.url(self.resource, meeting_uuid, 'participants')
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def user_list_participants(self, meeting_uuid):
        headers = self.get_headers()
        url = self._client.url(
            'users', 'me', self.resource, meeting_uuid, 'participants'
        )
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
