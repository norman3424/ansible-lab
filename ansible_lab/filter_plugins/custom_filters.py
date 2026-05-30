#!/usr/bin/env python3

def mask_ip(ip_address):
    try:
        parts = ip_address.split('.')
        if len(parts) == 4:
            return f"{parts[0]}.{parts[1]}.{parts[2]}.*"
        return ip_address
    except Exception:
        return ip_address

class FilterModule(object):
    def filters(self):
        return {
            'mask_ip': mask_ip
        }
