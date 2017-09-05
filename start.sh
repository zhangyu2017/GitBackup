#! /bin/bash
srcdir=src
targetdir='1.5,3.2,9'
targetdir=${targetdir//,/ } #replace with space 
taskNumber=10
cd src
echo -e "#!/bin/sh\n#$ -V \n#$ -N ampt\n\
#$ -cwd\n#$ -o job.log\n#$ -e job.err\n\
./exec" > run.sh 
cd ..
for target in $targetdir
do 
    mkdir 'a'$target
    cd 'a'$target
    cp ../src -r srcdir
    for i in {1..$taskNumber}
    do
        cp -r srcdir $i
        cd $i
        #awk 'NR==29''{$1=}' input.ampt 1<>input.ampt #line 29 corresponds to random seed 
        qsub run.sh
        cd ..
    done
    cd ..
done

