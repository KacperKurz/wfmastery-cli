#! /bin/python

import requests
import sys
import json


# TODO add more functions
# TODO error handling
def parse_arguments():
    # grab arguments from command line
    arguments = sys.argv
    arguments.pop(0)

    if len(arguments) == 0:
        # TODO call help function
        print("TODO")
    else:
        # if arguments begin with not a function then we call the default function
        if not arguments[0][0] == '-':
            function_arguments = []
            # get arguments we need to pass to default function
            for i in range(len(arguments)):
                if arguments[i][0] == '-':
                    break
                function_arguments.append(arguments[i])
                # TODO call default action
        # scan through arguments searching for functions
        for i in range(len(arguments)):
            if arguments[i][0] == '-':
                function_arguments = []
                # get arguments we need to pass to function
                for j in range(i + 1, len(arguments)):
                    if arguments[j][0] == '-':
                        break
                    function_arguments.append(arguments[j])
                # call functions
                # So apparently switches are not a thing in python so you can't judge me for what i'm about to do ¯\_(ツ)_/¯
                if arguments[i] == "-u" or arguments[i] == "--update":
                    # TODO call update function
                    print("TODO")






parse_arguments()

