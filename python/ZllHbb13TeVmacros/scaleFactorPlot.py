import ROOT
import numpy
import sys
sys.path.insert(0,'/mnt/t3nfs01/data01/shome/gaperrin/VHbb/CMSSW_7_4_3/src/Xbb/python/myutils')
from StackMaker import StackMaker
import ConfigParser

def conversion_x(x):
    u = (x-ROOT.gPad.GetX1())/(ROOT.gPad.GetX2()-ROOT.gPad.GetX1())
    return u;

def getSF(channel,labels, config):
    SF = []
    for label in labels:
        if config.has_option(channel,label): SF.append(eval(config.get(channel,label)))
        else: SF.append([-99, 0])#dummy value, such that SF is out of plot range

    return SF


def getGraph(channel,labels,shift, config):#,v_b,input_sigma,x_position,y_position,nuisances):
    SF = getSF(channel, labels, config)
    sf_v = []
    sf_e = []
    for sf in SF:
        sf_v.append(sf[0])
        sf_e.append(sf[1])

    p = range(0,len(sf_v))
    zero = [0]*len(sf_v)

    #sf = get_scale_factors(channel,labels,shift,v_b,input_sigma,nuisances)[0]
    #sf_e = get_scale_factors(channel,labels,shift,v_b,input_sigma,nuisances)[1]
    #d = numpy.array(sf) # store scale factors in array
    #e = numpy.array(sf_e) # store scale factors errors in array
    #p = numpy.array(y_position)
    #zero = numpy.array(x_position)

#    for i in range(len(labels)):
#        print 'CMSSW_vhbb_'+labels[i]+'_Zll_SF_8TeV '+ str(d[i]) + ' +/- ' + str(e[i])

    markerStyle = 20
    if ('Zee' in channel ):
        markerStyle = 20
    if ('Znn' in channel):
        markerStyle = 21
    if ('Wln' in channel):
        markerStyle = 22

    for i in range(len(sf_v)): p[i] = p[i]+shift
    print 'POSITIONS: '
    #print n,d,p,e,zero
    #g = ROOT.TGraphErrors(n,d,p,e,zero)
    g = ROOT.TGraphErrors(len(sf_v),numpy.array(sf_v),numpy.array(p),numpy.array(sf_e),numpy.array(zero))
    #g = ROOT.TGraphErrors(1,numpy.array([1.2]),numpy.array([1.+shift]),numpy.array([0.1]),numpy.array([0.1]))
    print "X"
    g.SetFillColor(0)
    print "X"
    g.SetLineColor(2)
    print "X"
    g.SetLineWidth(3)
    print "X"
    g.SetMarkerStyle(markerStyle)
    print "X"
    print 'Ok'
    print "X"
    return g

_file_sf = 'ZHbb_SF.ini'
config = ConfigParser.ConfigParser()
config.read(_file_sf)

#Choose what channels will be displayed on the plot
ch={'Zll':1.,'Zll low Pt':0.,'Zll high Pt':0.,'Wln':1.,'Wln low Pt':0.,'Wln high Pt':0.,'Znn':1.,'Znn low Pt':0.,'Znn high Pt':0.,'Znn med Pt':0.,'Zee':0.,'Zmm':0.}
#list of the y-axis labels
labels = ['TT','Wj1b','Wj2b','Zj0b','Zj1b','Zj2b','mjet']

label_dictionary = {"TT":"t#bar{t}","Wj0b":"W+0b","Wj1b":"W+b","Wj2b":"W+b#bar{b}","Zj0b":"Z+0b","Zj1b":"Z+b","Zj2b":"Z+b#bar{b}","s_Top":"t","mjet":"multijet"}
c = ROOT.TCanvas("c","c",600,600)

# calculate the shift on the y position
shift=0.
for channel,active in ch.iteritems(): shift+=active;
shift=1./(shift+1)

#input_sigma = getInputSigma(options)
#print 'Input sigma'
#print input_sigma

graphs={}
latex={}
j=1
for channel,active in ch.iteritems():
    print channel
    print active
    if active > 0.:
        graphs[channel] = getGraph(channel,labels,j*shift, config)#,j*shift,v_b,input_sigma,x_position,y_position,nuisances) # create the graph with the scale factors
        #sf = get_scale_factors(channel,labels,shift,v_b,input_sigma,nuisances)[0]
        #sf_e = get_scale_factors(channel,labels,shift,v_b,input_sigma,nuisances)[1]
        #for i in range(0,len(sf)):
        #    latex[labels[i]] = [labels[i],sf[i],sf_e[i],y_position[i]+0.35*shift]
        #    print "%s %s pm %s" %(labels[i],sf[i],sf_e[i])
        j+=1

#print graphs

xmin = 0.25
xmax = 2.5
xmin = 0.
xmax = 2.
#labels = removeDouble(labels)
n = len(labels)
h2 = ROOT.TH2F("h2","",1,xmin,xmax,n,0,n) # x min - max values.
h2.GetXaxis().SetTitle("Scale factor")

for i in range(n):
    h2.GetYaxis().SetBinLabel(i+1,label_dictionary[labels[i]])


drawSys=False
#if(drawSys):
#    #for the moment just random systematics
#    sys_e = numpy.array(sys)
#    #!! Create the graph for the systematics, if any. It will show only error brackets, no points
#    g2 = ROOT.TGraphErrors(n,d,p,sys_e,zero)
#    g2.SetFillColor(0)
#    g2.SetLineWidth(3);

h2.Draw(); ROOT.gStyle.SetOptStat(0);
h2.GetXaxis().SetTitleSize(0.04);
h2.GetXaxis().SetLabelSize(0.04);
h2.GetYaxis().SetLabelSize(0.06);
#h2.SetFillStyle(4000)
c.SetFillStyle(4000)

globalFitBand = ROOT.TBox(1.0, 0., 1.5, n);
globalFitBand.SetFillStyle(3013);
globalFitBand.SetFillColor(65);
globalFitBand.SetLineStyle(0);
#globalFitBand.Draw("same");
globalFitLine = ROOT.TLine(1.0, 0., 1.0, n);
globalFitLine.SetLineWidth(2);
globalFitLine.SetLineColor(214);#214
globalFitLine.Draw("same");

#!! Legend
#l2 = ROOT.TLegend(0.68, 0.70,0.8,0.9)
l2 = ROOT.TLegend(0.28, 0.70,0.4,0.9)
l2.SetLineWidth(2)
l2.SetBorderSize(0)
l2.SetFillColor(0)
l2.SetFillStyle(4000)
l2.SetTextFont(62)
for channel,g in graphs.iteritems():
    print channel
    if channel == 'Zll':
        l2.AddEntry(g,'ZH, Z#rightarrowl^{+}l^{-}',"pl")
    elif channel == 'Znn':
        l2.AddEntry(g,'ZH, Z#rightarrow#nu#nu',"pl")
    elif channel == 'Wln':
        l2.AddEntry(g,'WH, W#rightarrowln',"pl")
    #l2.AddEntry(g,channel,"pl")
l2.AddEntry(g,"Stat.","l")
#if(drawSys) : l2.AddEntry(g2,"Syst.","l")
l2.SetTextSize(0.035)
#l2.SetNColumns(3)
l2.Draw("same")
for channel,g in graphs.iteritems():
    print channel
    g.Draw("P same")
    #for label in labels:
        #StackMaker.myText("%.2f #pm %.2f" %(latex[label][1],latex[label][2]),conversion_x(xmin)-0.02,conversion_y(latex[label][3])-0.005,0.5)
if(drawSys) : g2.Draw("[] same")
StackMaker.myText("CMS Preliminary",conversion_x(xmin)+0.1,0.95,0.6)
StackMaker.myText("#sqrt{s} =  13TeV, L = 2.3 fb^{-1}",conversion_x(xmin)+0.1,0.92,0.6)
#
ROOT.gPad.SetLeftMargin(0.2)
ROOT.gPad.Update()
c.Print("histo.pdf")
c.Print("histo.png")
c.Print("histo.root")




