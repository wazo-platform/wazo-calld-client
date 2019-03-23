#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import (
    setup,
    find_packages,
)

setup(
    name='xivo_ctid_ng_client',
    version='0.1',

    description='a simple client library for the xivo-ctid-ng HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'ctid_ng_client.commands': [
            'applications = xivo_ctid_ng_client.commands.applications:ApplicationsCommand',
            'calls = xivo_ctid_ng_client.commands.calls:CallsCommand',
            'conferences = xivo_ctid_ng_client.commands.conferences:ConferencesCommand',
            'faxes = xivo_ctid_ng_client.commands.faxes:FaxesCommand',
            'relocates = xivo_ctid_ng_client.commands.relocates:RelocatesCommand',
            'transfers = xivo_ctid_ng_client.commands.transfers:TransfersCommand',
            'switchboards = xivo_ctid_ng_client.commands.switchboards:SwitchboardsCommand',
            'voicemails = xivo_ctid_ng_client.commands.voicemails:VoicemailsCommand',
        ],
    }
)
