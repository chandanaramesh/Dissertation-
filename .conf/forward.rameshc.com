;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     ns1.rameshc.com. root.ns1.rameshc.com (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns1.rameshc.com.
rameshc.com.    IN      MX      10      mail.rameshc.com.
@       IN      A       10.0.240.0
@       IN      AAAA    ::1
ns1     IN      A       10.154.0.2
a       IN      A       10.0.240.1
b       IN      A       10.0.240.2
mail    IN      A       10.154.0.3