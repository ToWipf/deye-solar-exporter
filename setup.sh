#!/bin/sh
echo "START BUILD"
rm deye_cmd
git clone https://github.com/ToWipf/deye-logger-at-cmd
cd deye-logger-at-cmd
make
cp build/main ../deye_cmd
cd ..
rm -rf deye-logger-at-cmd
echo "END BUILD"
