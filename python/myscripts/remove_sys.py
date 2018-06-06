import re
import os
from shutil import copyfile
import sys
print 'DEBUG'


path = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Zll2016Nano_V4/rundc-v3/Limits'
dirname = 'remove1'


remove_sys = ['VV','ZH_hbb']

remove_sys_dic = {
        'CMS_vhbb_puWeight':remove_sys,
        }

#some other example below
#remove_sys_dic = {
#        'CMS_vhbb_stats_bin':remove_sys,
#        'CMS_vhbb_bTagWeight':remove_sys,
#        'CMS_vhbb_scale_j_':remove_sys,
#        'CMS_vhbb_res_j_':remove_sys
#        }
#remove_sys_dic = {
#        'CMS_vhbb_res_j_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_PileUpDataMC_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_PileUpPtRef_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_PileUpPtBB_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_PileUpPtEC1_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_RelativeJEREC1_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_RelativeFSR_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_RelativeStatFSR_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_RelativeStatEC_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_RelativePtBB_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_RelativePtEC1_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_AbsoluteScale_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_AbsoluteMPFBias_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_AbsoluteStat_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_SinglePionECAL_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_SinglePionHCAL_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_Fragmentation_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_TimePtEta_13TeV':remove_sys,
#        'CMS_vhbb_scale_j_FlavorQCD_13TeV':remove_sys,
#        }



#creat folder
if not os.path.exists(path+'/'+dirname):
    os.makedirs(path+'/'+dirname)

for file in os.listdir(path):
    print 'file is', file
    if os.path.isfile(path+'/'+file) and '.root' in file and 'TH' in file:
        copyfile(path+'/'+file,path+'/'+dirname+'/'+file)
        #print 'the file to copy is', 
    elif os.path.isfile(path+'/'+file) and '.txt' in file and 'TH' in file:
        #print 'get list of files'
        input_file = open(path+'/'+file,"r")
        output_file = open(path+'/'+dirname+'/'+file,"w")
        
        def replacenth(string, sub, wanted, n):
            try: 
                where = [m.start() for m in re.finditer(sub, string)][n - 1]
                before = string[:where]
                after = string[where:]
                after = after.replace(sub, wanted,1)
                newString = before + after
                return newString
            except IndexError:
                return string
        
        found_process = False
        binList = []
        for line in input_file: 
            #check the order of the process
            #print 'line is', line
            if line.startswith('process') and not found_process:
                found_process = True 
                binList = line.split(' ')[1:]
                binList = filter(lambda a: a != '' and a != '\n', binList)


            sys_name = line.split(' ')[0] 
            #print 'sys_name is', sys_name
            found = False
            if sys_name in remove_sys_dic:
                found  = True
                #'print sysname is found'
            for key in remove_sys_dic:
                if key in sys_name:
                    found = True
                    sys_name = key
            if found:
                #print 'going to remove some bin from sys', sys_name
                position = [binList.index(c) for c in remove_sys_dic[sys_name]]
                #print 'position is', position
                #print 'line is', line
                newline = line
                n_replace = 0 
                #print 'string before replacement is', line
                position = sorted(position)
                for pos in position:
                    #print 'pos is', pos
                    #print pos+1-n_replace
                    newline = replacenth(newline, '1.0', ' - ', pos+1-n_replace)
                    n_replace+=1
                    #print 'string after replacement is', newline 
            else: 
                newline = line
            output_file.write(newline)
        
        
        output_file.close()
        
        
        
        
            
            
        
