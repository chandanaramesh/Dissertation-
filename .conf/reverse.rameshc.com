;
; BIND reverse data file for local loopback interface
;
$TTL    604800
@       IN      SOA     rameshc.com. root.rameshc.com. (
                              1         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns1.rameshc.com.
ns1     IN      A       10.154.0.2
2       IN      PTR     a.rameshc.com.
1       IN      PTR     b.rameshc.com.