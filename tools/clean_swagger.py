"""
Applies some updates to the swagger spec in the root of this repository that are required due to this bug: 
https://github.com/Azure/autorest.python/issues/84
"""
import os
import argparse

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='The swagger spec json to update')
    args = parser.parse_args()
    
    with open(args.file, 'r') as infile:
        content = infile.read()
        content = content.replace('\\\\N', '\\\\\\\\N').replace('\\\\U', '\\\\\\\\U')
        
    with open(args.file, 'w') as outfile:
        outfile.write(content)