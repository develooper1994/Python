import argparse,sys


def main():
    '''
        C:\\Users\selcu\Desktop\proje\intermadiate python>python cli.py a=5 b=3 --hesaplama="-"
        usage: cli.py [-h] [-a A] [-b B] [--hesaplama HESAPLAMA]
        cli.py: error: unrecognized arguments: a=5 b=3
        C:\\Users\selcu\Desktop\proje\intermadiate python>python cli.py -a=5 -b=3 --hesaplama="-"
        2.0
        C:\\Users\selcu\Desktop\proje\intermadiate python>python cli.py -a=5 -b=3 --hesaplama="*"
        C:\\Users\selcu\Desktop\proje\intermadiate python>python cli.py --a=5 --b=3 --hesaplama="/"
        1.6666666666666667
        15.0
        C:\\Users\selcu\Desktop\proje\intermadiate python>python cli.py-h
        python: can't open file 'cli.py-h': [Errno 2] No such file or directory

        C:\\Users\selcu\Desktop\proje\intermadiate python>python cli.py -h
        usage: cli.py [-h] [-a A] [-b B] [--hesaplama HESAPLAMA]

        optional arguments:
          -h, --help            show this help message and exit
          -a A, --a A           ilk sayı?
          -b B, --b B           ikinci sayı?
          --hesaplama HESAPLAMA
                                hangi islem?(+,-,*,/)
    '''


    parser=argparse.ArgumentParser()
    parser.add_argument('-a','--a',type=float,default=1.0,help='ilk sayı?')
    parser.add_argument('-b','--b',type=float,default=1.0,help='ikinci sayı?')
    parser.add_argument('--hesaplama',type=str,default='+',help='hangi islem?(+,-,*,/)')
    args=parser.parse_args()
    sys.stdout.write(str(hesap(args)))

def hesap(args):
    if args.hesaplama == '+':
        return args.a + args.b
    elif args.hesaplama == '-':
        return args.a - args.b
    elif args.hesaplama == '*':
        return args.a * args.b
    elif args.hesaplama == '/':
        return args.a / args.b

if __name__ == '__main__':
    main()












