#!/home/betafkrx/virtualenv/betacodings.com/3.7/bin/python

try:
    from pytonik import Web
except Exception as err:
    exit(err)

App = Web.App()
App.runs()
