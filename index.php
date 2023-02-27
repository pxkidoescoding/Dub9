<?php 
if (!isset($_COOKIE["args"])) {
    $args = '';
} else {
    $args = $_COOKIE["args"];
}
if (!isset($_COOKIE["usr"])) {
    $cookiemaker = '';
} else {
    $cookiemaker = $_COOKIE["usr"];
}
//echo $args;
$command = escapeshellcmd("python3 /home/pxki/web/failsafe.py /home/pxki/web/boot.py $_SERVER[REQUEST_URI] $_SERVER[REMOTE_ADDR] $cookiemaker $args");
$output = shell_exec($command);
echo $output;

?>
