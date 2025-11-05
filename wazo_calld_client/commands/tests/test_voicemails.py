# Copyright 2016-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from unittest.mock import ANY

from hamcrest import assert_that, equal_to
from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..voicemails import VoicemailsCommand


class TestVoicemails(RESTCommandTestCase):
    Command = VoicemailsCommand

    def test_get_voicemail(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail(42)

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params=None,
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_from_user()

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params=None,
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_folder(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_folder(42, 1)

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params=None,
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_folder_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_folder_from_user(1)

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params=None,
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_message(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_message(42, '123')

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params=None,
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_message_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_message_from_user('123')

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params=None,
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_all_voicemail_messages_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_all_voicemail_messages_from_user(voicemail_type="all")

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
            params={'voicemail_type': 'all'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_delete_voicemail_message(self):
        self.session.delete.return_value = self.new_response(204)
        self.command.delete_voicemail_message(42, '123')

        self.session.delete.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
        )

    def test_delete_voicemail_message_from_user(self):
        self.session.delete.return_value = self.new_response(204)
        self.command.delete_voicemail_message_from_user('123')

        self.session.delete.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json'},
        )

    def test_move_voicemail_message(self):
        self.session.put.return_value = self.new_response(204)

        self.command.move_voicemail_message(42, '123', 1337)

        self.session.put.assert_called_once_with(
            ANY,
            json={'folder_id': 1337},
            headers={'Accept': 'application/json'},
        )

    def test_move_voicemail_message_from_user(self):
        self.session.put.return_value = self.new_response(204)

        self.command.move_voicemail_message_from_user('123', 1337)

        self.session.put.assert_called_once_with(
            ANY,
            json={'folder_id': 1337},
            headers={'Accept': 'application/json'},
        )

    def test_get_voicemail_recording(self):
        self.session.get.return_value = self.new_response(200, body='blob')

        result = self.command.get_voicemail_recording(42, '123')

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'audio/wav'},
        )
        assert_that(result, equal_to('blob'))

    def test_get_voicemail_recording_from_user(self):
        self.session.get.return_value = self.new_response(200, body='blob')

        result = self.command.get_voicemail_recording_from_user('123')

        self.session.get.assert_called_once_with(ANY, headers={'Accept': 'audio/wav'})
        assert_that(result, equal_to('blob'))
