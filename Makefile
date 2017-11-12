all: interface/VHbbNameSpace_h.so python/setcwd.sh

interface/VHbbNameSpace_h.so: interface/VHbbNameSpace.h
	 cd interface && root -b -l -q ../init.cc && cd ..	 

python/setcwd.sh:
	 echo -e "#!/bin/bash\ncd $(PWD)" > python/setcwd.sh

clean:
	 rm interface/VHbbNameSpace_h.so
	 rm interface/VHbbNameSpace_h.d
	 rm interface/VHbbNameSpace_h_ACLiC_dict_rdict.pcm
	 rm python/setcwd.sh

