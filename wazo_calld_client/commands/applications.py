# -*- coding: utf-8 -*-
# Copyright 2018-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class ApplicationsCommand(CalldCommand):

    resource = 'applications'

    def create_node(self, application_uuid, call_ids):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'nodes')
        body = {'calls': [{'id': call_id} for call_id in call_ids]}

        r = self.session.post(url, json=body, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete_node(self, application_uuid, node_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'nodes', node_uuid)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def get(self, application_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid)
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_nodes(self, application_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'nodes')
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_node(self, application_uuid, node_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'nodes', node_uuid)
        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def answer_call(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'answer'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def hangup_call(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'calls', call_id)
        r = self.session.delete(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def join_node(self, application_uuid, node_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls', call_id
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def list_calls(self, application_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'calls')

        r = self.session.get(url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_call(self, application_uuid, call):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'calls')
        r = self.session.post(url, json=call, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def make_call_to_node(self, application_uuid, node_uuid, call):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls'
        )
        r = self.session.post(url, json=call, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def delete_call_from_node(self, application_uuid, node_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls', call_id
        )
        r = self.session.delete(url, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def make_call_user_to_node(self, application_uuid, node_uuid, call):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls', 'user'
        )
        r = self.session.post(url, json=call, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def send_playback(self, application_uuid, call_id, playback):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'playbacks'
        )
        r = self.session.post(url, json=playback, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def delete_playback(self, application_uuid, playback_uuid):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'playbacks', playback_uuid
        )
        r = self.session.delete(url, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def snoops(self, application_uuid, call_id, snoop):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'snoops'
        )
        r = self.session.post(url, json=snoop, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def update_snoop(self, application_uuid, snoop_uuid, snoop):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'snoops', snoop_uuid)
        r = self.session.put(url, json=snoop, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def delete_snoop(self, application_uuid, snoop_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'snoops', snoop_uuid)
        r = self.session.delete(url, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def get_snoop(self, application_uuid, snoop_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'snoops', snoop_uuid)
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_snoops(self, application_uuid):
        headers = self._get_headers()
        url = self._client.url(self.resource, application_uuid, 'snoops')
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def start_progress(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'progress', 'start'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_progress(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'progress', 'stop'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_hold(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'hold', 'start'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_hold(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'hold', 'stop'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_moh(self, application_uuid, call_id, moh_uuid):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'moh', moh_uuid, 'start'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_moh(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'moh', 'stop'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def start_mute(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'mute', 'start'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_mute(self, application_uuid, call_id):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'mute', 'stop'
        )
        r = self.session.put(url, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def send_dtmf_digits(self, application_uuid, call_id, digits):
        headers = self._get_headers()
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'dtmf'
        )
        params = {'digits': digits}
        r = self.session.put(url, headers=headers, params=params)
        if r.status_code != 204:
            self.raise_from_response(r)
