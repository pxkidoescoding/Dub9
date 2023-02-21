<?php 
$command = escapeshellcmd("python3 /home/pxki/web/failsafe.py /home/pxki/web/boot.py $_SERVER[REQUEST_URI] $_SERVER[REMOTE_ADDR]");
$output = shell_exec($command);
echo $output;

?>
