#!/bin/bash -e

NUM_ITER=${1:-1}

for i in $(seq 1 $NUM_ITER)
do
	fio --name TEST --eta-newline=5s --filename=fio-tempfile4read.dat --rw=randread --blocksize=4k --ioengine=libaio --iodepth=32 --direct=1 --numjobs=1 --size=100g --runtime=120
done

