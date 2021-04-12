<?php

$getData = json_decode(file_get_contents(__DIR__.'/data.txt'), true);

echo "<br>";
echo "Current Power: ".$getData['acw']." W<br>";
echo "DC Voltage: ".$getData['dcv']." V<br>";
echo "DC Current: ".$getData['dci']." A<br>";
echo "AC Voltage: ".$getData['acv']." V<br>";
echo "AC Current: ".$getData['aci']." A<br>";
echo "AC Frequency: ".$getData['acf']." Hz<br>";
echo "Temperature: ".$getData['temp']." C<br>";
echo "Generated all time: ".$getData['alltime']." kWh<br>";
echo "Generated today: ".$getData['today']." kWh<br>";

echo "<br>Last updated: ".date("H:i:s d-m-Y", filemtime(__DIR__.'/data.txt'));