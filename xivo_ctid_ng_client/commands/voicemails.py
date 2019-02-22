# -*- coding: utf-8 -*-
# Copyright 2016-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class VoicemailsCommand(RESTCommand):

    resource = 'voicemails'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_voicemail(self, voicemail_id):
        url = '{url}/{voicemail_id}'.format(url=self.base_url, voicemail_id=voicemail_id)
        return self._get(url)

    def get_voicemail_from_user(self):
        url = self._client.url('users', 'me', 'voicemails')
        return self._get(url)

    def get_voicemail_folder(self, voicemail_id, folder_id):
        url = '{url}/{voicemail_id}/folders/{folder_id}'.format(url=self.base_url, voicemail_id=voicemail_id, folder_id=folder_id)
        return self._get(url)

    def get_voicemail_folder_from_user(self, folder_id):
        url = self._client.url('users', 'me', 'voicemails', 'folders', folder_id)
        return self._get(url)

    def get_voicemail_message(self, voicemail_id, message_id):
        url = '{url}/{voicemail_id}/messages/{message_id}'.format(url=self.base_url, voicemail_id=voicemail_id, message_id=message_id)
        return self._get(url)

    def get_voicemail_message_from_user(self, message_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        return self._get(url)

    def delete_voicemail_message(self, voicemail_id, message_id):
        url = '{url}/{voicemail_id}/messages/{message_id}'.format(url=self.base_url, voicemail_id=voicemail_id, message_id=message_id)
        self.session.delete(url)

    def delete_voicemail_message_from_user(self, message_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        self.session.delete(url)

    def move_voicemail_message(self, voicemail_id, message_id, dest_folder_id):
        url = '{url}/{voicemail_id}/messages/{message_id}'.format(url=self.base_url, voicemail_id=voicemail_id, message_id=message_id)
        return self._move_message(url, dest_folder_id)

    def move_voicemail_message_from_user(self, message_id, dest_folder_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        return self._move_message(url, dest_folder_id)

    def _move_message(self, url, dest_folder_id):
        body = {'folder_id': dest_folder_id}
        r = self.session.put(url, json=body, headers=self.headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def get_voicemail_recording(self, voicemail_id, message_id):
        url = '{url}/{voicemail_id}/messages/{message_id}/recording'.format(url=self.base_url, voicemail_id=voicemail_id, message_id=message_id)
        return self._get_recording(url)

    def get_voicemail_recording_from_user(self, message_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id, 'recording')
        return self._get_recording(url)

    def _get_recording(self, url):
        r = self.session.get(url, headers={'Accept': 'audio/wav'})
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.content

    def _get(self, url):
        r = self.session.get(url, headers=self.headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
