from optparse import OptionParser
import os
import sys
import subprocess
import ROOT

parser = OptionParser()

parser.add_option("-T", "--tag", dest="tag", default="8TeV",
                      help="Tag to run the analysis with, example '8TeV' uses config8TeV and pathConfig8TeV to run the analysis")
parser.add_option("-D", "--datacard", dest="dc_folder", default="",
                      help="Path to the datacards to be ploted")
parser.add_option("-P", "--postfit", dest="postfit", default=True,
                  help="bool. Do you want to plot postfit or not (prefit) ?")
parser.add_option("-L", "--log", dest="log", default=True,
                  help="bool. Do you want to plot in log scale ?")

(opts, args) = parser.parse_args(sys.argv)

print 'Config suffix is', opts.tag
print 'Datacards folder is', opts.dc_folder
opts.tag = opts.tag+'config'

DC = os.listdir(opts.dc_folder)

#List of strings needed to launch the various pre/postfit

#mlfit_ = None
#mlfit_ = True
command_dics = []

for file in DC:
    if 'mlfit.root' in file:
        mlfit_ = opts.dc_folder+'/'+file
    if '.root' in file: continue
    if 'M125' in file: continue
    print 'The file name is', file
    command_dic = {}

    dc_file_ = opts.dc_folder+'/'+file
    mlfit_= opts.dc_folder+'/'+'mlfit.root'
    dc_bin_ = file.replace('vhbb_DC_TH_','').replace('.txt','')
    if 'BDT' in dc_bin_:
        var_ = 'BDT'
    elif 'CR' in dc_bin_:
        var_ = 'HjCSV1_CSV'
    else:
        print '@ERROR: neither CR not SR. Aborting'
        sys.exit()

    blind = 'False'
    if 'BDT' in file:
        blind = 'True'


    command_dic['blind'] = blind
    command_dic['dc_file'] = dc_file_
    command_dic['dc_bin'] =  dc_bin_
    command_dic['var'] =  var_
    command_dic['mlfit'] =  mlfit_
    command_dics.append(command_dic)

if not mlfit_:
    print '@ERROR: mlfit.root not found. Aborting'
    sys.exit()

#Launching all the commands
for command_dic in command_dics:
    #suffix = ' -C %s/general.ini -C %s/configPlot_vars  -C %s/datacard.ini -C %s/plots.ini -C %s/paths.ini -C %s/datacards.ini  -C %s/vhbbPlotDef.ini -P %s -L %s' %(opts.tag, opts.tag,opts.tag,opts.tag,opts.tag,opts.tag,opts.tag,opts.postfit, opts.log)
    suffix = ' -C %s/general.ini -C %s/configPlot_vars  -C %s/datacard.ini -C %s/plots.ini -C %s/paths.ini -C %s/datacards.ini  -C %s/vhbbPlotDef.ini' %(opts.tag, opts.tag,opts.tag,opts.tag,opts.tag,opts.tag,opts.tag)

    ##prefit
    #command = 'python stack_from_dcv2.py -D %s -B %s -F b -V %s' %( command_dic['dc_file'], command_dic['dc_bin'], command_dic['var'])
    #command += suffix
    ##print 'Prefit command is', command
    #subprocess.call([command], shell=True)
    #postfit
    #command = 'python stack_from_dcv2.py -D %s -B %s -M %s -F b -V %s -A %s' %( command_dic['dc_file'], command_dic['dc_bin'], command_dic['mlfit'], command_dic['var'], command_dic['blind'])
    command = 'python stack_from_dc_improved.py -D %s -B %s -M %s -F b -V %s -A %s' %( command_dic['dc_file'], command_dic['dc_bin'], command_dic['mlfit'], command_dic['var'], command_dic['blind'])
    command += suffix
    print 'command is', command
    subprocess.call([command], shell=True)
    #print 'Postfit command is', command



