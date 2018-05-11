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
parser.add_argument('--user', default = None, help='insert lxplus username, if lxplus user does not match tier3 username. Only is used when --server is not set.')
parser.add_argument('--eos', dest='webservice', action='store_const', default = False, const='eos', help='use default path with eos webserver')
parser.add_argument('--afs', dest='webservice', action='store_const', default = False, const='afs/cern.ch', help='use default path with afs webserver')
parser.add_argument('--name', default = None, help='Give a name to the new dir')

parser.add_argument('--fext', default = 'png,pdf,root', help='only copy specified file extensions. Default: "png,pdf,root". Use "all" for no restriction')
parser.add_argument('--folders', default = "region", help='how to make subfolders: <none>, <region> (default), <variable>')
parser.add_argument('--tar', default = False, action='store_const', const=True,  help='use tar compression')
parser.add_argument('--no', dest='do_outp', action='store_const',
                   const=False, default=True,  help='no copying')
parser.add_argument('--ni', dest='do_inp', action='store_const',
                   const=False, default=True,  help='no preparation of folders for each Region')
parser.add_argument('--nh', dest='ht', action='store_const',
                   const=False, default=True,  help='no htaccess file is created')

#Move all plots in corresponding subfolders

def MakeSubFolders(_input, current_):

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
        if not os.path.isfile(current_+'/.htaccess'):
            print current_+'/.htaccess'
            raise Exception("HTaccessFileNotFound")
        print 'command is','cp -r '+current_+'/.htaccess ' + _plotfolder + '/'
        subprocess.call('cp -r '+current_+'/.htaccess ' + _plotfolder + '/', shell = True)
        subprocess.call('cp -r ' + current_ + '/.htaccess ' + _plotfolder + '/config/', shell = True)
    if not os.path.isfile(current_+'/index.php'):
        print current_+'/index.php'
        raise Exception("IndexFileNotFound")
    subprocess.call('cp -r '+current_+'/index.php ' + _plotfolder + '/', shell = True)
    subprocess.call('cp -r ' + current_ + '/index.php ' + _plotfolder + '/config/', shell = True)

    #Files, file extension
    FILE = os.listdir('.')
    fext = args.fext.split(',')

    print "File extensions to copy: " + ', '.join(fext)
    
    for file in FILE:
        if not os.path.isfile(file):
            continue
        filename, ext = os.path.splitext(file)   
        if  not 'all' in fext and ext.split(".")[1] not in fext:
            continue
        #skip folders in listdir

        folder = None
        if args.folders == 'region':
            folder = filename.split("__")[0]
            folder = folder.replace("comp_","")
        elif args.folders == 'variable':
            folder = filename.split("__")[1]
   
        if folder is None:
            folder2 = _plotfolder
        else:
            folder2 = os.path.join(_plotfolder,folder)

        print file + ' --> ' + folder2
        if folder2:
            if not os.path.isdir(folder2):
                os.mkdir(folder2)
                #subprocess.call('cp -r ../config '+ folder2 + '/', shell = True)
                if args.ht:
                    if not os.path.isfile(current_+'/.htaccess'):
                        raise Exception("HTaccessFileNotFound")
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

def MoveSubFolders(_input, _output, server=None, user=None):
    if server is None:
        if user is None: 
            # try to use Tier3 username for LxPlus server
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
    
    if args.tar:
        tarfile = _plotfolder + '.tar'
        zipcommand = 'tar -cf ' + tarfile + ' ' + _plotfolder
        print zipcommand
        subprocess.call(zipcommand, shell = True)
        copyCommand = 'ssh '+ server +' "cd '+ _output + ' && tar -xvv" < ' + tarfile
        print copyCommand
        subprocess.call(copyCommand, shell = True)
        remTarCmd = 'rm ' + tarfile
        print remTarCmd
        subprocess.call(remTarCmd, shell = True)
    
    else:
        print 'gonna lunch the command'
        copyCommand = 'scp -r ' + _plotfolder + ' ' + server + ':' + _output
        print copyCommand
        subprocess.call(copyCommand, shell = True)


args = parser.parse_args()

_input = os.path.abspath(args._input[0])

if len(args._input) > 1:
    _output = args._input[1]

else:
    _output = "/"

print 'Input folder is', _input
print 'Output folder is', _output

_current = '/'.join(os.path.realpath(__file__).split('/')[:-1])
os.chdir(_input)

if args.do_inp:
    MakeSubFolders(_input,_current)

if args.do_outp:
    MoveSubFolders(_input, _output, server=args.server, user=args.user )

