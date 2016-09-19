import os
import json

# A class to apply SF's tabulated in json files
class LeptonSF:
    def __init__(self, lep_json, lep_name, lep_binning, extrapolateFromClosestBin=True) :
        if not os.path.isfile(lep_json):
            self.valid = False
            if lep_json!="":
                print "[LeptonSF]: Warning: ", lep_json, " is not a valid file. Return."
            else:
                print "[LeptonSF]: No file has been specified. Return."
        else:
            self.init(lep_json, lep_name, lep_binning, extrapolateFromClosestBin)

    def init(self, lep_json, lep_name, lep_binning, extrapolateFromClosestBin) :
        f = open(lep_json, 'r')             
        print '[LeptonSF]: Initialize with the following parameters:'
        print '\tfile:',lep_json
        print '\titem:', lep_name
        print '\tbinning:', lep_binning
        results = json.load(f)
        if lep_name not in results.keys():
            self.valid = False
            print "[LeptonSF]: Warning: ", lep_name , " is not a valid item. Return."
            return False
        self.res = results[lep_name]
        self.lep_name = lep_name
        self.lep_binning = lep_binning
        self.valid = True
        self.extrapolateFromClosestBin = extrapolateFromClosestBin
        f.close()

    def get_1D(self, pt):
        if not self.valid:
            return [1.0, 0.0]

        stripForEta = 5
        if self.lep_binning not in self.res.keys():
            return [1.0, 0.0]

        # if no bin is found, search for closest one, and double the uncertainty
        closestPtBin = ""
        closestPt = 9999.

        ptFound = False

        for ptKey, result in sorted(self.res[self.lep_binning].iteritems()) :
            #print 'ptKey is', ptKey
            ptL = float(((ptKey[7:]).rstrip(']').split(',')[0]))
            ptH = float(((ptKey[7:]).rstrip(']').split(',')[1]))

            #print 'ptL is', ptL
            #print 'ptH is', ptH

            if abs(ptL-pt)<closestPt or abs(ptH-pt)<closestPt and not ptFound:
                closestPt = min(abs(ptL-pt), abs(ptH-pt))
                closestPtBin = ptKey

                if (pt>ptL and pt<ptH):

                    closestPtBin = ptKey
                    ptFound = True

                if ptFound:
                    return [result["value"], result["error"]]

        if self.extrapolateFromClosestBin and not (closestPtBin==""):
            return [self.res[self.lep_binning][closestPtBin]["value"],2*self.res[self.lep_binning][closestPtBin]["error"]]
        else:
            return [1.0, 0.0]
                    

    def get_2D(self, pt, eta):
        if not self.valid:
            return [1.0, 0.0]        

        stripForPt= 4

        stripForEta = 5
        if self.lep_binning not in self.res.keys():
            return [1.0, 0.0]

        if "abseta" in self.lep_binning:
            eta = abs(eta)
            stripForEta = 8

        if "pt_eta_ratio" in self.lep_binning:
            stripForEta = 4
            stripForPt= 5

        # if no bin is found, search for closest one, and double the uncertainty
        closestEtaBin = ""
        closestPtBin = ""
        closestEta = 9999.
        closestPt = 9999.

        etaFound = False
        for etaKey, values in sorted(self.res[self.lep_binning].iteritems()) :
            etaL = float(((etaKey[stripForEta:]).rstrip(']').split(',')[0]))
            etaH = float(((etaKey[stripForEta:]).rstrip(']').split(',')[1]))

            ptFound = False

            if abs(etaL-eta)<closestEta or abs(etaH-eta)<closestEta and not etaFound:
                closestEta = min(abs(etaL-eta), abs(etaH-eta))
                closestEtaBin = etaKey

            if (eta>etaL and eta<etaH):
                closestEtaBin = etaKey
                etaFound = True                

            for ptKey, result in sorted(values.iteritems()) :
                ptL = float(((ptKey[stripForPt:]).rstrip(']').split(',')[0]))
                ptH = float(((ptKey[stripForPt:]).rstrip(']').split(',')[1]))                

                if abs(ptL-pt)<closestPt or abs(ptH-pt)<closestPt and not ptFound:
                    closestPt = min(abs(ptL-pt), abs(ptH-pt))
                    closestPtBin = ptKey

                if (pt>ptL and pt<ptH):
                    closestPtBin = ptKey
                    ptFound = True

                if etaFound and ptFound:
                    return [result["value"], result["error"]]

        if self.extrapolateFromClosestBin and not (closestPtBin=="" or closestEtaBin==""):
            return [self.res[self.lep_binning][closestEtaBin][closestPtBin]["value"], 
                    2*self.res[self.lep_binning][closestEtaBin][closestPtBin]["error"]] 
        else:
            return [1.0, 0.0]


##################################################################################################
# EXAMPLE 
#

if __name__ == "__main__":

    jsonpath = os.environ['CMSSW_BASE']+"/src/Xbb"
    jsons = {    
        jsonpath+'/python/json/EfficienciesAndSF_ISO.json' : ['MC_NUM_LooseRelIso_DEN_LooseID_PAR_pt_spliteta_bin1', 'abseta_pt_ratio'],
        jsonpath+'/python/json/ScaleFactor_egammaEff_WP80.json' : ['ScaleFactor_egammaEff_WP80', 'pt_eta_ratio'],
        jsonpath+'/python/json/eff_Ele27_WPLoose_Eta2p1_RunBtoF.json' : ['Trigger_Eff', 'eta_pt_ratio'],
        jsonpath+'/python/json/egammaEffi_tracker.json' : ['egammaEffi_tracker', 'eta_pt_ratio'],
        jsonpath+'/python/json/SingleMuonTrigger_LooseMuons_beforeL2fix_Z_RunBCD_prompt80X_7p65.json' : ['MuonTrigger_data_all_IsoMu22_OR_IsoTkMu22_pteta_Run2016B_beforeL2Fix', 'abseta_pt_MC'],
        jsonpath+'/python/json/SingleMuonTrigger_LooseMuons_afterL2fix_Z_RunBCD_prompt80X_7p65.json' : ['MuonTrigger_data_all_IsoMu22_OR_IsoTkMu22_pteta_Run2016B_afterL2Fix', 'abseta_pt_MC']
        }

    for j, name in jsons.iteritems():
        lepCorr = LeptonSF(j , name[0], name[1])
        if not 'ScaleFactor_egammaEff_WP80' in j:
            weight = lepCorr.get_2D( 65 , -1.5)
        else: 
            weight = lepCorr.get_2D( -1.5, 65)
        val = weight[0]
        err = weight[1]
        print 'SF: ',  val, ' +/- ', err
    
    
