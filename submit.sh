#PBS -A open
#PBS -l walltime=2:00:00
#PBS -l nodes=1:ppn=1
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

module load python
python mc.py


