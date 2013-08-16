#!/usr/bin/python

import sys
from projects import projects

def calc(hours,day,total_days,verbose):
    day = float(day)
    hours = float(hours)
    total_days = float(total_days)
    ratio = day/total_days

    if(verbose):
        verbose_string="[ day(%2s)/total_days(%2s) == %s, ratio(%2s)*hours(%2s)==%2s ]" % (day,total_days,ratio,ratio,hours,ratio*hours)
        return [ratio*hours,verbose_string ]
    return [ratio*hours]

def generate_times(hours, verbose=False):
    total_days = 0
    for i in projects:
        total_days+=projects[i]
    for i in projects:
        result =  calc(hours,projects[i],total_days,verbose)
        if(verbose):
            try:
                import termcolor
                project_name = termcolor.colored(i, color="red", attrs=["bold"])

                hrs = termcolor.colored(result[0], color="white")
                print "%-25s: %2s %s" % ( project_name, hrs,result[1])
            except Exception as e:
                print "%-10s: %2s %s" % ( i, result[0],result[1])

        else:
            try:
                import termcolor
                project_name = termcolor.colored(i, color="red", attrs=["bold"])

                hrs = termcolor.colored(result[0], color="white")
                print "%-25s: %2s" % ( project_name, hrs)
            except Exception as e:
                print "%-10s: %2s" % ( i, result[0])

def describe():
    for p in projects:
        print "Project: %-10s, %1s days a week" % (p,projects[p])

if __name__ == '__main__':
    import argparse
    program_version = "1.0"
    parser = argparse.ArgumentParser(
        prog='PRORATE',
        description='''*note*: Program makes use of termcolor (http://pypi.python.org/pypi/termcolor) 'sudo pip install termcolor'  ''',
        epilog=     '''  '''
    )

    parser.add_argument("--version", action='version', version='%(prog)s '+program_version)
    parser.add_argument("--time",'-t', type=int, help="the amount of time to prorate")
    parser.add_argument("--verbose","-v", action="store_true", default=False,required=False, help="Show a detailed description of the formula being done")
    parser.add_argument("--describe","-d", action="store_true", help="Show the project data we are using")
    args = parser.parse_args()

    if(args.describe):
        describe()

    if(args.time):
        generate_times(args.time,args.verbose)

    else:
        if(args.describe):
            pass
        else:
            print "Need a time...."
            parser.print_help()
            sys.exit()
