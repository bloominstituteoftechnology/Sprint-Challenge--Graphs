#!/bin/sh

echo '';
echo '';
echo 'from HostA to HostD: ';
node src/routing.js HostA HostD;
echo '';
echo 'from HostA to HostH: ';
node src/routing.js HostA HostH;
echo '';
echo 'from HostA to HostA: ';
node src/routing.js HostA HostA;
echo '';
echo 'from HostE to HostB: ';
node src/routing.js HostE HostB;
echo '';
echo '';
