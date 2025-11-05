# Copyright 2016-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class VoicemailsCommand(CalldCommand):
    resource = 'voicemails'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_voicemail(self, voicemail_id):
        url = self._client.url(self.resource, voicemail_id)
        return self._get(url)

    def get_voicemail_from_user(self):
        url = self._client.url('users', 'me', 'voicemails')
        return self._get(url)

    def get_voicemail_folder(self, voicemail_id, folder_id):
        url = self._client.url(self.resource, voicemail_id, 'folders', folder_id)
        return self._get(url)

    def get_voicemail_folder_from_user(self, folder_id):
        url = self._client.url('users', 'me', 'voicemails', 'folders', folder_id)
        return self._get(url)

    def get_voicemail_message(self, voicemail_id, message_id):
        url = self._client.url(self.resource, voicemail_id, 'messages', message_id)
        return self._get(url)

    def get_voicemail_message_from_user(self, message_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        return self._get(url)

    def get_all_voicemail_messages_from_user(self, voicemail_type='all', **params):
        url = self._client.url('users', 'me', 'voicemails', 'messages')
        return self._get(url, params | {"voicemail_type": voicemail_type})

    def delete_voicemail_message(self, voicemail_id, message_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, voicemail_id, 'messages', message_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def delete_voicemail_message_from_user(self, message_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def move_voicemail_message(self, voicemail_id, message_id, dest_folder_id):
        url = self._client.url(self.resource, voicemail_id, 'messages', message_id)
        return self._move_message(url, dest_folder_id)

    def move_voicemail_message_from_user(self, message_id, dest_folder_id):
        url = self._client.url('users', 'me', 'voicemails', 'messages', message_id)
        return self._move_message(url, dest_folder_id)

    def _move_message(self, url, dest_folder_id):
        headers = self._get_headers()
        body = {'folder_id': dest_folder_id}
        r = self.session.put(url, json=body, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def get_voicemail_recording(self, voicemail_id, message_id):
        url = self._client.url(
            self.resource,
            voicemail_id,
            'messages',
            message_id,
            'recording',
        )
        return self._get_recording(url)

    def get_voicemail_recording_from_user(self, message_id):
        url = self._client.url(
            'users', 'me', 'voicemails', 'messages', message_id, 'recording'
        )
        return self._get_recording(url)

    def voicemail_greeting_exists(self, voicemail_id, greeting):
        headers = self._get_headers()
        url = self._client.url(self.resource, voicemail_id, 'greetings', greeting)
        response = self.session.head(url, headers=headers)
        # FIXME: invalid voicemail_id return 400 instead 404
        if response.status_code in (404, 400):
            return False
        if response.status_code != 200:
            self.raise_from_response(response)
        return True

    def get_voicemail_greeting(self, voicemail_id, greeting):
        url = self._client.url(self.resource, voicemail_id, 'greetings', greeting)
        return self._get_recording(url)

    def voicemail_greeting_from_user_exists(self, greeting):
        headers = self._get_headers()
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        response = self.session.head(url, headers=headers)
        if response.status_code == 404:
            return False
        if response.status_code != 200:
            self.raise_from_response(response)
        return True

    def get_voicemail_greeting_from_user(self, greeting):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        return self._get_recording(url)

    def create_voicemail_greeting(self, voicemail_id, greeting, data):
        url = self._client.url(self.resource, voicemail_id, 'greetings', greeting)
        self._create_recording(url, data)

    def create_voicemail_greeting_from_user(self, greeting, data):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        self._create_recording(url, data)

    def update_voicemail_greeting(self, voicemail_id, greeting, data):
        url = self._client.url(self.resource, voicemail_id, 'greetings', greeting)
        self._put_recording(url, data)

    def update_voicemail_greeting_from_user(self, greeting, data):
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        self._put_recording(url, data)

    def delete_voicemail_greeting(self, voicemail_id, greeting):
        headers = self._get_headers()
        url = self._client.url(self.resource, voicemail_id, 'greetings', greeting)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def delete_voicemail_greeting_from_user(self, greeting):
        headers = self._get_headers()
        url = self._client.url('users', 'me', 'voicemails', 'greetings', greeting)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def copy_voicemail_greeting(self, voicemail_id, greeting, dest_greeting):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, voicemail_id, 'greetings', greeting, 'copy'
        )
        body = {'dest_greeting': dest_greeting}
        r = self.session.post(url, json=body, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def copy_voicemail_greeting_from_user(self, greeting, dest_greeting):
        headers = self._get_headers()
        url = self._client.url(
            'users', 'me', 'voicemails', 'greetings', greeting, 'copy'
        )
        body = {'dest_greeting': dest_greeting}
        r = self.session.post(url, json=body, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def _create_recording(self, url, data):
        headers = self._get_headers()
        headers['Content-type'] = 'audio/wav'
        r = self.session.post(url, headers=headers, data=data)
        if r.status_code != 204:
            self.raise_from_response(r)

    def _put_recording(self, url, data):
        headers = self._get_headers()
        headers['Content-type'] = 'audio/wav'
        r = self.session.put(url, headers=headers, data=data)
        if r.status_code != 204:
            self.raise_from_response(r)

    def _get_recording(self, url):
        headers = self._get_headers()
        headers['Accept'] = 'audio/wav'
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.content

    def _get(self, url, params: dict | None = None):
        headers = self._get_headers()
        r = self.session.get(url, headers=headers, params=params)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()
