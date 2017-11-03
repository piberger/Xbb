all: interface/VHbbNameSpace_h.so

interface/VHbbNameSpace_h.so: interface/VHbbNameSpace.h
	 cd interface && root -b -l -q ../init.cc && cd ..	 

clean:
	 rm interface/VHbbNameSpace_h.so
	 rm interface/VHbbNameSpace_h.d

