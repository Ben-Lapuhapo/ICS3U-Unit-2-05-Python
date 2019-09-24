#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 23 2019
# This program shows how local variables work

# Global Variable
variable_X = 25


def local_variable():
    # this shows what happens with local variables

    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Local  variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X,  variable_Y, variable_Z))


def global_variable():
    # this shows what happens with goal variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Global  variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X,  variable_Y, variable_Z))


def main():
    # This function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
