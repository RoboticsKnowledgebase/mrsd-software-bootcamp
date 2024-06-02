#!/bin/bash
cp ../src/Controller.cpp src/
cp ../include/Controller.h include/
# cp source/src/result.json results/result.json
rm -rf build
mkdir build
cd build


# rm -rf build
# mkdir build
# cd build
cmake ..
make
./missiledefense