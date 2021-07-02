#PBS -A open
#PBS -l walltime=24:00:00 
#PBS -l nodes=1:ppn=2
#PBS -l feature=rhel7 
#PBS -j oe
#PBS -m abe
#PBS -N JP10

cd $PBS_O_WORKDIR

echo " "
echo " "
echo "Job started on"'hostname'
echo " at "
date

$ADFBIN/reaxff


