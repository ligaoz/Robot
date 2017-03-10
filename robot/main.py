'''
Created on 9 Mar 2017

@author: liga
'''
import argparse
from urllib import urlopen

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    arguments = parser.parse_args()
    url = arguments.input
    html = urlopen(url)
    data = html.read().decode('utf-8').split("\n")
    print(data)
   # size = int(data[0])
   # print(size)
   # data.pop(0)

if __name__ == '__main__':
    main()