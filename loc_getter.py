#!/usr/bin/env python

#######################################################
# Script takes a physical address or a file containing
#   a list of addresses and returns their latitude and
#   longitude. This uses Google's Maps API.
#
#   Author: Nathan Ciobanu <nathanciobanu@gmail.com>
#######################################################

import argparse



def get_geo(addr):
    #TODO: implement this
    m_geo_data = {}
    return m_geo_data



def main(args):
    geo_data = {}
    if args.address:
        addr = args.address
        plus_address = addr.replace(' ', '+')
        geo_data = get_geo(plus_address)
        print addr + ' lat: ' + geo_data['lat'] + ' lng: '\
                           + geo_data['lng']

    if args.addr_file:
        with open(args.addr_file, 'r') as f:
            addresses = f.readlines()
            for addr in addresses:
                plus_address = addr.replace(' ', '+')
                geo_data = get_geo(plus_address)
                print addr + ' lat: ' + geo_data['lat'] + ' lng: '\
                           + geo_data['lng']


 
if __name__ == "__main__":
    aparser = argparse.ArgumentParser(
                         description="Geo location "\
                         +"retriever arg parser")
    aparser.add_argument("--address", metavar="Street address",
                         help = "Enter a physical address")
    aparser.add_argument("--addr_file", metavar="List of addresses file",
                         help = "Enter a file name with a list of "\
                         +"addresses, one per line")
    args = aparser.parse_args()
    main(args)
