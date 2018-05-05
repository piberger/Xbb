import os
import sys
import shutil
import subprocess
import argparse

#Read input arguments



parser = argparse.ArgumentParser(description='Move plots to public webpage')
parser.add_argument('_input', nargs='*', metavar='I', help='first argument: input folder, second argument (optional) output folder. You can use --eos or --afs option to use the default path as output folder. If output folder and --eos or --afs option is set, the output folder will be appended to the default path.')
#parser.add_argument('-r', dest='region', action='store_const',
#                   const=False, default=True,  help='use automatic region list insead of default')
parser.add_argument('--server', default = None, help='other server than lxplus')
parser.add_argument('--eos', dest='webservice', action='store_const', default = False, const='eos', help='use default path with eos webserver')
parser.add_argument('--afs', dest='webservice', action='store_const', default = False, const='afs/cern.ch', help='use default path with afs webserver')
parser.add_argument('--name', default = None, help='Give a name to the new dir')

parser.add_argument('--folders', default = "region", help='how to make subfolders: <none>, <region> (default), <variable>')
parser.add_argument('--no', dest='do_outp', action='store_const',
                   const=False, default=True,  help='no copying')
parser.add_argument('--ni', dest='do_inp', action='store_const',
                   const=False, default=True,  help='no preparation of folders for each Region')
parser.add_argument('--nh', dest='ht', action='store_const',
                   const=False, default=True,  help='no htaccess file is created')

args = parser.parse_args()
#args = sys.argv[1:]
#if len(args) == 2:
#    _input = args[0]
#    _output = args[1]
#else:
#    print 'Error, need two agruments. You have provided', len(args)
#    sys.exit(1)


_input = args._input[0]
if len(args._input) > 1:
    _output = args._input[1]

else:
    _output = "/"

args.region = False
print 'Input folder is', _input
print 'Output folder is', _output

#Move all plots in corresponding subfolders

def MakeSubFolders(_input, RegionList=None):

    #I am in macro location
    #I am in Plots
    if args.name is None:
        _plotfolder = _input.split('/')[-2]
    else:
        _plotfolder = args.name
    
    if not os.path.isdir(_plotfolder):
        os.mkdir(_plotfolder)

    print 'command is','cp -r ../config ' + _plotfolder + '/'
    subprocess.call('cp -r ../config ' + _plotfolder + '/', shell = True)
    
    if args.ht:
        print 'command is','cp -r '+current_+'/.htaccess ' + _plotfolder + '/'
        subprocess.call('cp -r '+current_+'/.htaccess ' + _plotfolder + '/', shell = True)
        subprocess.call('cp -r ' + current_ + '/.htaccess ' + _plotfolder + '/config/', shell = True)
    subprocess.call('cp -r '+current_+'/index.php ' + _plotfolder + '/', shell = True)
    subprocess.call('cp -r ' + current_ + '/index.php ' + _plotfolder + '/config/', shell = True)
    FILE = os.listdir('.')

    #subprocess.call('cp -r ../config .', shell = True)
    
    #make default RegionList
    if RegionList is None:
        RegionList = []
    if not args.folders == 'none':
        for file in FILE:
               
                #skip folders in listdir
                if not os.path.isfile(file):
                    continue
                if args.folders == 'region':
                    region = file.split("__")[0]
                    region = region.replace("comp_","")
                elif args.folders == 'variable':
                    region = file.split("__")[1]
                    region = region.split(".")[0]
                if region not in RegionList:
                    RegionList.append((region,region)) 
        #print RegionList
   
    for file in FILE:
        #if not 'comp' in file: continue #Skip shape plots
        print 'file is', file
        
        #skip folders in listdir
        if not os.path.isfile(file):
            continue
        
        folder2 = None
        for name, folder in RegionList:
            if not name in file: continue
            folder2 = os.path.join(_plotfolder,folder)
            break
        if not folder2:
            if not '.pdf' in file and not '.png' in file and not '.root' in file: continue
            else:
                folder2 = _plotfolder
                #If file is not in RegionList, create folder using file prefix
            #    folder = file.split('__')[0]
            #    folder2 = os.path.join(_plotfolder,folder)

        print 'folder2 is', folder2
        if folder2:
            if not os.path.isdir(folder2):
                os.mkdir(folder2)
                #subprocess.call('cp -r ../config '+ folder2 + '/', shell = True)
                if args.ht:
                    subprocess.call('cp -r '+current_+'/.htaccess ' + folder2 + '/', shell = True)
                subprocess.call('cp -r '+current_+'/index.php ' + folder2 + '/', shell = True)
            if os.path.isfile(file):
                shutil.copy(file,folder2)
            if os.path.isfile('pdf/'+file.replace('png','pdf')):
                shutil.copy('pdf/'+file.replace('png','pdf'), folder2)
            else:
                pass
                #print 'pdf/'+file.replace('png','pdf'), 'doesn\'t exist'
            if os.path.isfile('root/'+file.replace('png','C')) :
                shutil.copy('root/'+file.replace('png','C'), folder2)
                #print 'root is here'
            else:
                pass
                #print 'root/'+file.replace('png','C'), 'doesn\'t exist'

def MoveSubFolders(_input, _output, server=None):
    if server is None:
        # TODO: username on T3 and lxplus can be different!! => as workaround give server path explicitly for now
        process = os.popen('echo $USER')
        user = process.read().strip()
        process.close()
        server = user + '@lxplus.cern.ch'
    else:
        user = server.split('@')[0]
    
    if args.name is None:
        _plotfolder = _input.split('/')[-2]
    else:
        _plotfolder = args.name

    if args.webservice:
        _output = '/' + args.webservice+ '/user/' + user[0] + "/" + user + "/www/" + _output
    print 'gonna lunch the command'
    copyCommand = 'scp -r ' + _plotfolder + ' ' + server + ':' + _output
    print copyCommand
    subprocess.call(copyCommand, shell = True)

current_ = os.getcwd()
os.chdir(_input)
if args.do_inp:
    if args.region:
        MakeSubFolders(_input, RegionList)
    else:
        MakeSubFolders(_input)

if args.do_outp:
    MoveSubFolders(_input, _output, args.server)

