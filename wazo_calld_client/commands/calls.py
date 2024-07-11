# Copyright 2015-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from collections.abc import Mapping

from ..command import CalldCommand


class CallsCommand(CalldCommand):
    resource = 'calls'

    def list_calls(
        self,
        application=None,
        application_instance=None,
        recurse=None,
        tenant_uuid=None,
    ):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = self._client.url(self.resource)
        params = {}
        if application:
            params['application'] = application
        if application_instance:
            params['application_instance'] = application_instance

        r = self.session.get(url, headers=headers, params=params)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_calls_from_user(self, application=None, application_instance=None):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource)
        params = {}
        if application:
            params['application'] = application
        if application_instance:
            params['application_instance'] = application_instance

        r = self.session.get(url, headers=headers, params=params)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_call(self, call_id, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = self._client.url(self.resource, call_id)
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def make_call(self, call):
        headers = self._get_headers()
        url = self._client.url(self.resource)
        r = self.session.post(url, json=call, headers=headers)
        if r.status_code != 201:
            self.raise_from_response(r)
        return r.json()

    def make_call_from_user(
        self,
        extension,
        variables=None,
        line_id=None,
        from_mobile=False,
        all_lines=False,
        auto_answer_caller=False,
    ):
        body = {'extension': extension}
        if variables:
            body['variables'] = variables
        if line_id:
            body['line_id'] = line_id
        if from_mobile:
            body['from_mobile'] = from_mobile
        if all_lines:
            body['all_lines'] = all_lines
        if auto_answer_caller:
            body['auto_answer_caller'] = auto_answer_caller

        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource)
        r = self.session.post(url, json=body, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def hangup(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def hangup_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def connect_user(self, call_id, user_id, **kwargs):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'user', user_id)
        r = self.session.put(url, headers=headers, json=kwargs if kwargs else None)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def start_mute(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'mute', 'start')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_mute(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'mute', 'stop')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_mute_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'mute', 'start')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_mute_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'mute', 'stop')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def send_dtmf_digits(self, call_id, digits):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'dtmf')
        params = {'digits': digits}
        r = self.session.put(url, headers=headers, params=params)
        if r.status_code != 204:
            self.raise_from_response(r)

    def send_dtmf_digits_from_user(self, call_id, digits):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'dtmf')
        params = {'digits': digits}
        r = self.session.put(url, headers=headers, params=params)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_hold(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'hold', 'start')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_hold(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'hold', 'stop')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_hold_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'hold', 'start')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_hold_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'hold', 'stop')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def answer(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'answer')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def answer_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'answer')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_record(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'record', 'start')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_record_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'record', 'start')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_record(self, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'record', 'stop')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_record_from_user(self, call_id):
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'record', 'stop')
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def park(
        self,
        call_id: str,
        parking_id: str,
        preferred_slot: str | None = None,
        timeout: int | None = None,
    ) -> Mapping:
        headers = self._get_headers()
        url = self._client.url(self.resource, call_id, 'park')
        body = {
            'parking_id': parking_id,
            'preferred_slot': preferred_slot,
            'timeout': timeout,
        }
        r = self.session.put(url, headers=headers, json=body)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()

    def park_from_user(
        self,
        call_id: str,
        parking_id: str,
        preferred_slot: str | None = None,
        timeout: int | None = None,
    ) -> Mapping:
        headers = self._get_headers()
        url = self._client.url('users', 'me', self.resource, call_id, 'park')
        body = {
            'parking_id': parking_id,
            'preferred_slot': preferred_slot,
            'timeout': timeout,
        }
        r = self.session.put(url, headers=headers, json=body)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()
