# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Avencall
#
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class CallsCommand(RESTCommand):

    resource = 'calls'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_calls(self):
        url = self.base_url

        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_calls_from_user(self, application=None, application_instance=None):
        url = self._client.url('users', 'me', self.resource)
        params = {}
        if application:
            params['application'] = application
        if application_instance:
            params['application_instance'] = application_instance

        r = self.session.get(url, headers=self.headers, params=params)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_call(self, call_id):
        url = '{base_url}/{call_id}'.format(base_url=self.base_url,
                                            call_id=call_id)

        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def make_call(self, call):
        r = self.session.post(self.base_url,
                              json=call,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def make_call_from_user(self, extension, variables=None, line_id=None, from_mobile=False):
        body = {'extension': extension}
        if variables:
            body['variables'] = variables
        if line_id:
            body['line_id'] = line_id
        if from_mobile:
            body['from_mobile'] = from_mobile
        r = self.session.post(self._client.url('users', 'me', self.resource),
                              json=body,
                              headers=self.headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def hangup(self, call_id):
        url = '{base_url}/{call_id}'.format(base_url=self.base_url,
                                            call_id=call_id)

        self.session.delete(url, headers=self.headers)

    def hangup_from_user(self, call_id):
        url = self._client.url('users', 'me', self.resource, call_id)

        self.session.delete(url)

    def connect_user(self, call_id, user_id):
        url = '{base_url}/{call_id}/user/{user_id}'.format(base_url=self.base_url,
                                                           call_id=call_id,
                                                           user_id=user_id)

        r = self.session.put(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
