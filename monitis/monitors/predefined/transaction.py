#!/usr/bin/env python
# encoding: utf-8
"""
transaction.py

Created by Jeremiah Shirk on 2012-09-03.
Copyright (c) 2012 Monitis. All rights reserved.
"""

from monitis.api import get, post, MonitisError, validate_kwargs


def suspend_transaction_monitor(**kwargs):
    ''' Suspend transaction monitors '''
    required = {}
    optional = {'monitor_ids': 'monitorIds', 'tag': 'tag'}
    req_args = validate_kwargs(required, optional, **kwargs)
    monitor_ids = req_args.get('monitorIds', None)
    if isinstance(monitor_ids, list):
        req_args['monitorIds'] = ','.join(monitor_ids)
    return post(action='suspendTransactionMonitor', **req_args)


def activate_transaction_monitor(**kwargs):
    ''' Activate transaction monitors '''
    required = {}
    optional = {'monitor_ids': 'monitorIds', 'tag': 'tag'}
    req_args = validate_kwargs(required, optional, **kwargs)
    monitor_ids = req_args.get('monitorIds', None)
    if isinstance(monitor_ids, list):
        req_args['monitorIds'] = ','.join(monitor_ids)
    return post(action='activateTransactionMonitor', **req_args)


def transaction_tests(**kwargs):
    ''' Get a user's transaction or full page load monitors '''
    required = {}
    optional = {'type': 'type'}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionTests', **req_args)


def transaction_test_info(**kwargs):
    ''' Get info on the specified monitor '''
    required = {'monitor_id': 'monitorId'}
    optional = {}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionTestInfo', **req_args)


def transaction_test_result(**kwargs):
    ''' Get results for the specified Transaction or
    Full Page Load monitor
    '''
    required = {'monitor_id': 'monitorId', 'year': 'year',
                'month': 'month', 'day': 'day'}
    optional = {'location_ids': 'locationIds', 'timezone': 'timezone'}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionTestResult', **req_args)


def transaction_step_result(**kwargs):
    ''' Get deatailed step results for a transaction monitor check '''
    required = {'result_id': 'resultId', 'year': 'year',
                'month': 'month', 'day': 'day'}
    optional = {}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionStepResult', **req_args)


def transaction_step_capture(**kwargs):
    ''' Get capture for the specified Transaction step '''
    required = {'monitor_id': 'monitorId', 'result_id': 'resultId'}
    optional = {}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionStepCapture', **req_args)


def transaction_step_net(**kwargs):
    ''' Get net for the specified Transaction step '''
    required = {'result_id': 'resultId', 'year': 'year',
                'month': 'month', 'day': 'day'}
    optional = {}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionStepNet', **req_args)


def transaction_locations(**kwargs):
    ''' Get locations for transaction monitors '''
    required = {}
    optional = {}
    req_args = validate_kwargs(required, optional, **kwargs)
    return get(action='transactionLocations', **req_args)


def transaction_snapshot(**kwargs):
    ''' Get last results of user's Transaction monitors '''
    required = {}
    optional = {'location_ids': 'locationIds'}
    req_args = validate_kwargs(required, optional, **kwargs)
    location_ids = req_args.get('locationIds', None)
    if isinstance(location_ids, list):
        req_args['locationIds'] = ','.join(location_ids)
    return get(action='transactionSnapshot', **req_args)