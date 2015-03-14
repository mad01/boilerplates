#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


def http_get(host, **kwargs):
    """ http REST api get call with headers and option to add params
    :params api: the api to be called
    :params headers: any header data have to be json
    :params urlparams: added as a url parameter have to be json"""
    url = 'http://' + host + '/'
    if "api" in kwargs:
        url += kwargs["api"]

    headers = {}
    if "headers" in kwargs:
        headers.update(kwargs["headers"])

    params = {}
    if "urlparams" in kwargs:
        if type(kwargs["urlparams"]) == dict:
            params = kwargs["urlparams"]

    req = requests.get(url, headers=headers, params=params)
    print url
    print req.text
    print req.status_code
    return req.status_code, req.text


def http_post(host, **kwargs):
    """ http REST api post call with headers and option to add params and payload
    :params api: the api to be called
    :params headers: any header data
    :params urlparams: added as a url parameter have to be json
    :params payload: payload data parameter have to be json"""
    url = 'http://' + host + '/'
    if "api" in kwargs:
        url += kwargs["api"]

    headers = {}
    if "headers" in kwargs:
        headers.update(kwargs["headers"])

    params = {}
    if "urlparams" in kwargs:
        if type(kwargs["urlparams"]) == dict:
            params = kwargs["urlparams"]

    payload = {}
    if "payload" in kwargs:
        if type(kwargs["payload"]) == dict:
            payload = kwargs["payload"]

    req = requests.post(
        url,
        headers=headers,
        params=params,
        data=json.dumps(payload)
    )
    print url
    print req.text
    print req.status_code
    return req.status_code, req.text
