<?php

if (isset($_POST)) {
    if ($_SERVER['REMOTE_ADDR'] != 'IPHERE') die('No access...');
    if (!is_numeric($_POST['acw'])) die('Incomplete data received...');
    if (!is_numeric($_POST['dcv'])) die('Incomplete data received...');
    if (!is_numeric($_POST['dci'])) die('Incomplete data received...');
    if (!is_numeric($_POST['acv'])) die('Incomplete data received...');
    if (!is_numeric($_POST['aci'])) die('Incomplete data received...');
    if (!is_numeric($_POST['acf'])) die('Incomplete data received...');
    if (!is_numeric($_POST['temp'])) die('Incomplete data received...');
    if (!is_numeric($_POST['alltime'])) die('Incomplete data received...');
    if (!is_numeric($_POST['today'])) die('Incomplete data received...');
    file_put_contents(__DIR__.'/data.txt', json_encode($_POST, JSON_PRETTY_PRINT));
    echo 'OK!';
}