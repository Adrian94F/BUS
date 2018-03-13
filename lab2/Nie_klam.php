<?php
$aadmin = base64_decode(urldecode('VxudCsIeS5e0MLhUIVh3C%2Bl3%2FvQKcTTGP49fRXSFRcA%3D'));
$aadmin = substr($aadmin, 16);
$aadmin = urlencode(base64_encode($aadmin));
print($aadmin);