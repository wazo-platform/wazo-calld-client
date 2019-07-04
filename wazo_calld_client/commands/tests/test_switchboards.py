# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import equal_to
from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..switchboards import SwitchboardsCommand


class TestSwitchboards(RESTCommandTestCase):

    Command = SwitchboardsCommand

    def test_list_queued_calls(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_queued_calls('my-switchboard')

        self.session.get.assert_called_once_with(
            self.client.url('switchboards', 'my-switchboard', 'calls', 'queued'),
            headers={'Accept': 'application/json'}
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_answer_queued_call_from_user(self):
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.answer_queued_call_from_user('my-switchboard', 'call-id')

        self.session.put.assert_called_once_with(
            self.client.url('switchboards', 'my-switchboard', 'calls', 'queued', 'call-id', 'answer'),
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_hold_call(self):
        self.session.put.return_value = self.new_response(204)

        self.command.hold_call('my-switchboard', 'call-id')

        self.session.put.assert_called_once_with(
            self.client.url('switchboards', 'my-switchboard', 'calls', 'queued', 'call-id'),
            headers={}
        )

    def test_list_held_calls(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_held_calls('my-switchboard')

        self.session.get.assert_called_once_with(
            self.client.url('switchboards', 'my-switchboard', 'calls', 'held'),
            headers={'Accept': 'application/json'}
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_answer_held_call_from_user(self):
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.answer_held_call_from_user('my-switchboard', 'call-id')

        self.session.put.assert_called_once_with(
            self.client.url('switchboards', 'my-switchboard', 'calls', 'held', 'call-id', 'answer'),
        )
        assert_that(result, equal_to({'return': 'value'}))
