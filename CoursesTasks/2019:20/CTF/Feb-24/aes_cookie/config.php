<?php 

$host = "mysqldb";
$username = "user1";
$password = "123456789";
$database = "db";

define('FLAG', getenv('FLAG'));
define('AES_KEY', getenv('AES_KEY'));
define('AES_IV', getenv('AES_IV'));
//define('FLAG', 'FLAG{}');
//define('AES_KEY', 'efc6b9e96b9142a7b0b371b5adec6e5e');
//define('AES_IV', '821d8e8e1a9fae50d23797dffd4df47b');


$db = new PDO("mysql:host=$host; dbname=$database", $username, $password);  
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, username VARCHAR(200) UNIQUE , password VARCHAR(200), email VARCHAR(200))");

include_once('auth.lib.php');
session_start();

function compress($arr) {
    return implode('÷', array_map(function ($v, $k) { return $k.'¡'.$v; }, $arr, array_keys($arr) ));
}
 
function decompress($cookie) {
    if(preg_match('/[^\x00-\x7F]+\ *(?:[^\x00-\x7F]| )*/im',$cookie, $m) == 0) {
        echo('Decryption error (1).');
        return false;
    }

    $t = explode("÷", $cookie);

    $arr = [];
    foreach($t as $el) { 
        $el = explode("¡", $el); 
        $arr[$el[0]] = $el[1];
    } 

    if(!isset($arr['checksum'])) {
        echo('Decryption error (2).');
        return false;
    }

    $checksum = intval($arr['checksum']);
    unset($arr['checksum']);
    $cookie = compress($arr);
    if($checksum != crc32($cookie)) {
        echo('Decryption error (3).');
        return false;
    } 

    return $arr;
}

function encryptCookie($arr) {
    $cookie = compress($arr);
    $arr['checksum'] = crc32($cookie); 
    return encrypt(compress($arr), AES_KEY, AES_IV);
}

function decryptCookie($cypher) { 
    return decompress(decrypt($cypher, AES_KEY, AES_IV));
}

function encrypt($plaintext, $key, $iv) {
    $length     = strlen($plaintext);
    $ciphertext = openssl_encrypt($plaintext, 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $iv);
    return base64_encode($ciphertext) . sprintf('%06d', $length);
}

function decrypt($ciphertext, $key, $iv) {
    $length     = intval(substr($ciphertext, -6, 6));
    $ciphertext = substr($ciphertext, 0,-6);
    $output     = openssl_decrypt(base64_decode($ciphertext), 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $iv);
    if($output == FALSE) {
        echo('Decryption error (0).');
        die();
    }
    return substr($output, 0, $length);
}

