;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     brokelings.com. root.brokelings.com (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns.brokelings.com.
@       IN      A       160.153.137.14
@       IN      AAAA    ::1
ns      IN      A       160.153.137.14
mail    IN      CNAME   brokelings.wordpress.com.
