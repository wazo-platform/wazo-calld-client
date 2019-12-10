#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

setup(
    name='wazo_calld_client',
    version='0.1',
    description='a simple client library for the wazo-calld HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_calld_client.commands': [
            'applications = wazo_calld_client.commands.applications:ApplicationsCommand',
            'calls = wazo_calld_client.commands.calls:CallsCommand',
            'conferences = wazo_calld_client.commands.conferences:ConferencesCommand',
            'faxes = wazo_calld_client.commands.faxes:FaxesCommand',
            'relocates = wazo_calld_client.commands.relocates:RelocatesCommand',
            'transfers = wazo_calld_client.commands.transfers:TransfersCommand',
            'trunks = wazo_calld_client.commands.trunks:TrunksCommand',
            'switchboards = wazo_calld_client.commands.switchboards:SwitchboardsCommand',
            'voicemails = wazo_calld_client.commands.voicemails:VoicemailsCommand',
        ]
    },
)
