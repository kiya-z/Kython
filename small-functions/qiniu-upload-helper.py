#!/usr/bin/env python
#coding:utf-8

#must install qiniu(use pip) before using.

import gtk

# get gtk.SelectionData object or None according to the given target
# how to get the target value? you can use gtk.Clipboard.wait_for_targets to get the target of current clipboard
image = gtk.clipboard_get().wait_for_contents('image/png')

if image is None:
    print 'no image in clipboard!' 
else:
    from qiniu import Auth, put_data
    # 'key_qiniu' is another file storing my keys and bucket_name, touch one by yourself
    from key_qiniu import access_key,secret_key,bucket_name
    q = Auth(access_key,secret_key)

    import time
    key = 'from_clipboard/' + time.strftime('%Y/%m/%d/%H/%M/%S', time.localtime(time.time())) 
    print key

    data = image.data
    token = q.upload_token(bucket_name)
    ret, info = put_data(token,key,data)
    print ret
    assert ret['key'] == key
    