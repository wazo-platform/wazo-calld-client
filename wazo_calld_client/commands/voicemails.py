# -*- coding: utf-8 -*-
# Copyright 2016-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class VoicemailsCommand(CalldCommand):

    resource = 'voicemails'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_voicemail(self, voicemail_id):
        url = '{url}/{voicemail_id}'.format(
            url=self.base_url, voicemail_id=voicemail_id
        )
        return self._get(url)

    def get_voicemail_from_user(self):
        url = self._client.url('users', 'me', 'voicemails')
        return self._get(url)

    def get_voicemail_folder(self, voicemail_id, folder_id):
        url = '{url}/{voicemail_id}/folders/{folder_id}'.format(
            url=self.base_url, voicemail_id=voicemail_id, folder_id=folder_id
        )
        return self._get(url)

    def get_voicemail_folder_from_user(self, folder_id):
        url = self._client.url('users', 'me', 'voicemails', 'folders', folder_id)
        return self._get(url)

    def get_voicemail_message(self, voicemail_id, message_id):
        url = '{url}/{voicemail_id}/messages/{message_id}'.format(
            url=self.base_url, voicemail_id=voicemail_id, message_id=message_id
        )
        return self._get(url)

    def get_voicemail_message_from_user(self, message_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        return self._get(url)

    def delete_voicemail_message(self, voicemail_id, message_id):
        url = '{url}/{voicemail_id}/messages/{message_id}'.format(
            url=self.base_url, voicemail_id=voicemail_id, message_id=message_id
        )
        r = self.session.delete(url)
        if r.status_code != 204:
            self.raise_from_response(r)

    def delete_voicemail_message_from_user(self, message_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        r = self.session.delete(url)
        if r.status_code != 204:
            self.raise_from_response(r)

    def move_voicemail_message(self, voicemail_id, message_id, dest_folder_id):
        url = '{url}/{voicemail_id}/messages/{message_id}'.format(
            url=self.base_url, voicemail_id=voicemail_id, message_id=message_id
        )
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
        url = '{url}/{voicemail_id}/messages/{message_id}/recording'.format(
            url=self.base_url, voicemail_id=voicemail_id, message_id=message_id
        )
        return self._get_recording(url)

    def get_voicemail_recording_from_user(self, message_id):
        url = self._client.url(
            'users', 'me', 'voicemails', 'messages', message_id, 'recording'
        )
        return self._get_recording(url)

    def voicemail_greeting_exists(self, voicemail_id, greeting):
        url = '{url}/{voicemail_id}/greetings/{greeting}'.format(
            url=self.base_url, voicemail_id=voicemail_id, greeting=greeting
        )
        response = self.session.head(url, headers=self.headers)
        # FIXME: invalid voicemail_id return 400 instead 404
        if response.status_code in (404, 400):
            return False
        if response.status_code != 200:
            self.raise_from_response(response)
        return True

    def get_voicemail_greeting(self, voicemail_id, greeting):
        url = '{url}/{voicemail_id}/greetings/{greeting}'.format(
            url=self.base_url, voicemail_id=voicemail_id, greeting=greeting
        )
        return self._get_recording(url)

    def get_voicemail_greeting_from_user(self, greeting):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        return self._get_recording(url)

    def create_voicemail_greeting(self, voicemail_id, greeting, data):
        url = '{url}/{voicemail_id}/greetings/{greeting}'.format(
            url=self.base_url, voicemail_id=voicemail_id, greeting=greeting
        )
        self._create_recording(url, data)

    def create_voicemail_greeting_from_user(self, greeting, data):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        self._create_recording(url, data)

    def update_voicemail_greeting(self, voicemail_id, greeting, data):
        url = '{url}/{voicemail_id}/greetings/{greeting}'.format(
            url=self.base_url, voicemail_id=voicemail_id, greeting=greeting
        )
        self._put_recording(url, data)

    def update_voicemail_greeting_from_user(self, greeting, data):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        self._put_recording(url, data)

    def delete_voicemail_greeting(self, voicemail_id, greeting):
        url = '{url}/{voicemail_id}/greetings/{greeting}'.format(
            url=self.base_url, voicemail_id=voicemail_id, greeting=greeting
        )
        r = self.session.delete(url)
        if r.status_code != 204:
            self.raise_from_response(r)

    def delete_voicemail_greeting_from_user(self, greeting):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        r = self.session.delete(url)
        if r.status_code != 204:
            self.raise_from_response(r)

    def copy_voicemail_greeting(self, voicemail_id, greeting, dest_greeting):
        url = '{url}/{voicemail_id}/greetings/{greeting}/copy'.format(
            url=self.base_url, voicemail_id=voicemail_id, greeting=greeting
        )
        r = self.session.post(url, json={'dest_greeting': dest_greeting})
        if r.status_code != 204:
            self.raise_from_response(r)

    def copy_voicemail_greeting_from_user(self, greeting, dest_greeting):
        url = self._client.url(
            'users', 'me', 'voicemails', 'greetings', greeting, 'copy'
        )
        r = self.session.post(url, json={'dest_greeting': dest_greeting})
        if r.status_code != 204:
            self.raise_from_response(r)

    def _create_recording(self, url, data):
        r = self.session.post(url, headers={'Content-type': 'audio/wav'}, data=data)
        if r.status_code != 204:
            self.raise_from_response(r)

    def _put_recording(self, url, data):
        r = self.session.put(url, headers={'Content-type': 'audio/wav'}, data=data)
        if r.status_code != 204:
            self.raise_from_response(r)

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
