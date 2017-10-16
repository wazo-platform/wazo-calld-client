#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015-2017 The Wazo Authors  (see the AUTHORS file)
#
# SPDX-License-Identifier: GPL-3.0+

from setuptools import setup
from setuptools import find_packages

setup(
    name='xivo_ctid_ng_client',
    version='0.1',

    description='a simple client library for the xivo-ctid-ng HTTP interface',

    author='Wazo Authors',
    author_email='dev.wazo@gmail.com',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'ctid_ng_client.commands': [
            'calls = xivo_ctid_ng_client.commands.calls:CallsCommand',
            'chats = xivo_ctid_ng_client.commands.chats:ChatsCommand',
            'user_presences = xivo_ctid_ng_client.commands.user_presences:UserPresencesCommand',
            'line_presences = xivo_ctid_ng_client.commands.line_presences:LinePresencesCommand',
            'relocates = xivo_ctid_ng_client.commands.relocates:RelocatesCommand',
            'transfers = xivo_ctid_ng_client.commands.transfers:TransfersCommand',
            'switchboards = xivo_ctid_ng_client.commands.switchboards:SwitchboardsCommand',
            'voicemails = xivo_ctid_ng_client.commands.voicemails:VoicemailsCommand',
        ],
    }
)
