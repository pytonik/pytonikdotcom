# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/27/20.
from pytonik.Model import Model

class Doc(Model):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def importantnav(self, status, limit):
        query = self.table('tablecontent').where('status_tablecontent', status).limit(int(limit)).select().get()
        return query.rowCount, query.result
