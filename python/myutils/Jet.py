import ROOT
class Jet(object):
    def __init__(self, pt, eta, phi, mass, btag=0.0, index=0, pt_reg=0.0, mass_reg=0.0):
        self.pt = pt
        self.eta = eta
        self.phi = phi
        self.mass = mass
        self.btag = btag
        self.index = index
        self.pt_reg = pt_reg
        self.mass_reg = mass_reg

    @staticmethod
    def deltaR(jet1, jet2):
        deltaPhi = ROOT.TVector2.Phi_mpi_pi(jet1.phi-jet2.phi)
        deltaEta = jet1.eta-jet2.eta
        return ROOT.TMath.Sqrt(deltaEta*deltaEta + deltaPhi*deltaPhi)

    @staticmethod
    def get(tree):
        jets = []
        for i in range(tree.nJet):
            if tree.Jet_lepFilter[i] > 0 and (tree.Jet_puId[i] > 6 or tree.Jet_Pt[i] > 50.0) and tree.Jet_jetId[i] > 2:
                jets.append(Jet(pt=tree.Jet_Pt[i], eta=tree.Jet_eta[i], phi=tree.Jet_phi[i], mass=tree.Jet_mass_nom[i], btag=tree.Jet_btagDeepB[i], index=i, pt_reg=tree.Jet_PtReg[i], mass_reg=tree.Jet_PtReg[i]/tree.Jet_Pt[i]*tree.Jet_mass_nom[i]))
        return jets
