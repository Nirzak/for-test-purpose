#!/usr/bin/env python3
import os
def check_reboot():
    """Returns True if the computer has pending reboot"""
    return os.path.exist("/run/reboot_required")

def main():
    pass

main()