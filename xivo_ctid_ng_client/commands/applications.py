# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class ApplicationsCommand(RESTCommand):

    resource = 'applications'
    ro_headers = {'Accept': 'application/json'}
    rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_node(self, application_uuid, *call_ids):
        url = self._client.url(self.resource, application_uuid, 'nodes')
        body = {
            'calls': [{'id': call_id} for call_id in call_ids],
        }

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

    def join_node(self, application_uuid, node_uuid, exten, context, auto_answer=False):
        url = self._client.url(self.resource, application_uuid, 'nodes', node_uuid, 'calls')
        body = {
            'exten': exten,
            'context': context,
            'auto_answer': auto_answer,
        }

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
