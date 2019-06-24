import pyshark

cap = pyshark.FileCapture('unencrypt.pcap')
def conversation_header(pkt):
    try:
        protocol = pkt.transport_layer
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        print('%s %s:%s ---> %s:%s'% (protocol, src_addr, src_port, dst_addr, dst_port))
    except AttributeError as e:
        pass

#cap.apply_on_packets(conversation_header, timeout=100)

def dns_info(pkt):
    try:
        dns = pkt.dns
        if dns.flags == '0x00008180':
            print('%s, %s' %(dns.resp_name, dns.time))
        #print(dns.resp_ttl, dns.resp_z, dns.resp_name, dns.resp_len)

    except AttributeError as e:
        pass
cap.apply_on_packets(dns_info, timeout=100)
#resp_z is the flag no error

'''
['a', 'count_add_rr', 'count_answers', 'count_auth_rr', 'count_labels', 'count_queries', 'field_names', 'flags', 'flags_authenticated', 'flags_authoritative', 'flags_checkdisable', 'flags_opcode', 'flags_rcode', 'flags_recavail', 'flags_recdesired', 'flags_response', 'flags_truncated', 'flags_z', 'get', 'get_field', 'get_field_by_showname', 'get_field_value', 'id', 'layer_name', 'pretty_print', 'qry_class', 'qry_name', 'qry_name_len', 'qry_type', 'raw_mode', 'resp_class', 'resp_edns0_version', 'resp_ext_rcode', 'resp_len', 'resp_name', 'resp_ttl', 'resp_type', 'resp_z', 'resp_z_do', 'resp_z_reserved', 'rr_udp_payload_size', 'unsolicited']

'''
