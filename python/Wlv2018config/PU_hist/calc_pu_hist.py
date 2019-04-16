#!/usr/bin/python
import sys, os

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# mb_xsec = ['69200']
# mb_xsec = ['30000','40000','50000','60000','69200','70000','80000','90000','100000']
mb_xsec = ['73000','74000','75000','76000','77000','78000','79000','72500','73500','74500','75500','76500','77500','78500','79500']

if len(sys.argv)>1:
    mb_xsec = sys.argv[1].split(',')

print 'xsec List:', mb_xsec

for xsec in mb_xsec:
    print 'Using xsec ',xsec,'mb'
    os.system("pileupCalc.py -i\
      /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt\
      --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PileUp/pileup_latest.txt\
      --calcMode true\
      --minBiasXsec "+str(xsec)+"\
      --maxPileupBin 100\
      --numPileupBins 100\
      ./MyDataPileupHistogram_mbxsec_"+str(xsec)+".root")

