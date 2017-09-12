#!/usr/bin/env python
from __future__ import print_function

from myutils.Hash import Hash


def test_hash1():
    if Hash(sample='DYJetsToLL_Pt-100To250', debug=True).get() != '0891756277e0f6853d30cf270150687981915c16dbda154daf499747': raise('TEST FAILED')
    if Hash(sample='DYJetsToLL_Pt-100To250', minCut='(phi>0)||eta>0&&phi>1||pt>0', debug=True).get() != 'd823f1d7fad7cd25cf6e35b8d6f9b7c41fd797f09c48dd70a6c37bc5': raise('TEST FAILED')
    if Hash(sample='DYJetsToLL_Pt-100To250', minCut='(phi>0)||eta>0&&phi>1||pt>0', mergeCachingSize=10, debug=True).get() != '073d993b13a25fbb070c4a7e65c49c687e82fd903ddae35124c48a10': raise('TEST FAILED')
    if Hash(sample='DYJetsToLL_Pt-100To250', minCut='(phi>0)||eta>0&&phi>1||pt>0', subCut='rho>1', debug=True).get() != '5f02972ec6106002c91f09c3546f4e0c53182e02761ba463c61edd0d': raise('TEST FAILED')
    if Hash(sample='DYJetsToLL_Pt-100To250', minCut='(phi>0)||eta>0&&phi>1||pt>0', subCut='rho>1', mergeCachingSize=10, debug=True).get() != '13a847ddb473ee058d13e3010988bb55ffecfbe4d118f5bc6041c7d5': raise('TEST FAILED')
    if Hash(sample='DYJetsToLL_Pt-100To250', minCut='(phi>0)||eta>0&&phi>1||pt>0', subCut='rho>1', mergeCachingSize=10, branches=['phi','eta','rho'], debug=True).get() != '5afffe6310cf0af3522cf93a3890d968fce698ece01ea03caff76b8d': raise('TEST FAILED')

test_hash1()