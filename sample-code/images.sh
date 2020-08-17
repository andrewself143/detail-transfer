#!/bin/bash

echo "Generate Images"

#!/bin/bash
infile='lists/doors.txt'
outfile='temp.txt'
rm $outfile
tr -d '\r' < $infile > $outfile

selected_models=() #get list of selected models
while read p; do
	echo $p
	selected_models+=($p)
done <lists/doors.txt #text file

#iterate through selected models
cd 2dRenderFolder
for chair_names in "${selected_models[@]}";
do
		echo 'inside'
		echo ${chair_names}

		#generate images
		python render_mesh.py --path="../models/doors" --mesh=${chair_names} --ni=4 --dist=2 --outf=../images --oc .10 .80 .61

done
