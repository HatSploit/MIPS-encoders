#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.encoder import Encoder

from pex.string import String
from pex.assembler import Assembler


class HatSploitEncoder(Encoder, String, Assembler):
    details = {
        'Name': "mipsbe XOR Encoder",
        'Encoder': "mipsbe/xor",
        'Authors': [
            'Ivan Nikolsky (enty8080) - encoder developer'
        ],
        'Description': "Simple XOR encoder for mipsbe.",
        'Architecture': "mipsbe"
    }

    options = {
        'KEY': {
            'Description': "4-byte key to encode.",
            'Value': "abcd",
            'Type': None,
            'Required': True
        }
    }

    def run(self):
        key = self.parse_options(self.options)
        passes = len(self.payload) / 5

        reg_10 = (passes + 1) ^ 0xffff
        reg_5 = len(self.payload) ^ 0xffff

        decoder = self.assemble(
            self.details['Architecture'],
            """
            start:
                
            """
        )

        
