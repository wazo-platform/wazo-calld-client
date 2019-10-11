# -*- coding: utf-8 -*-
# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class ApplicationsCommand(RESTCommand):

    resource = 'applications'
    ro_headers = {'Accept': 'application/json'}
    rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_node(self, application_uuid, call_ids):
        url = self._client.url(self.resource, application_uuid, 'nodes')
        body = {'calls': [{'id': call_id} for call_id in call_ids]}

        r = self.session.post(url, json=body, headers=self.rw_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get(self, application_uuid):
        url = self._client.url(self.resource, application_uuid)
        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def answer_call(self, application_uuid, call_id):
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'answer'
        )
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def hangup_call(self, application_uuid, call_id):
        url = self._client.url(self.resource, application_uuid, 'calls', call_id)
        r = self.session.delete(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def join_node(self, application_uuid, node_uuid, exten, context, auto_answer=False):
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls'
        )
        body = {'exten': exten, 'context': context, 'auto_answer': auto_answer}

        r = self.session.post(url, json=body, headers=self.rw_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_calls(self, application_uuid):
        url = self._client.url(self.resource, application_uuid, 'calls')

        r = self.session.get(url, headers=self.ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_call(self, application_uuid, call):
        url = self._client.url(self.resource, application_uuid, 'calls')
        r = self.session.post(url, json=call, headers=self.rw_headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def make_call_to_node(self, application_uuid, node_uuid, call):
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls'
        )
        r = self.session.post(url, json=call, headers=self.rw_headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def make_call_user_to_node(self, application_uuid, node_uuid, call):
        url = self._client.url(
            self.resource, application_uuid, 'nodes', node_uuid, 'calls', 'user'
        )
        r = self.session.post(url, json=call, headers=self.rw_headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def send_playback(self, application_uuid, call_id, playback):
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'playbacks'
        )
        r = self.session.post(url, json=playback, headers=self.rw_headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def snoops(self, application_uuid, call_id, snoop):
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'snoops'
        )
        r = self.session.post(url, json=snoop, headers=self.rw_headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def start_progress(self, application_uuid, call_id):
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'progress', 'start'
        )
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def stop_progress(self, application_uuid, call_id):
        url = self._client.url(
            self.resource, application_uuid, 'calls', call_id, 'progress', 'stop'
        )
        r = self.session.put(url, headers=self.ro_headers)
        if r.status_code != 204:
            self.raise_from_response(r)
