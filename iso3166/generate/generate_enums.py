import argparse
import subprocess
from pathlib import Path
import os
from zipfile import ZipFile
from pprint import pprint

DEFAULT_PACKAGE = str(
    Path(__file__).parent / 'iso_country_code_ALL_csv.zip.gpg'
)

def exec_command(*args):
    ret = subprocess.run(args, capture_output=True)
    if ret.returncode != 0:
        raise RuntimeError(
            f'Error executing [{args}]:\n\t{ret.stderr.decode()}'
        )
    return ret.stdout


def main():

    parser = argparse.ArgumentParser(
        prog='generate_enums',
        description='Generate python iso3166 enumerations from the '
                    'ISO csv package.'
    )

    package = parser.add_mutually_exclusive_group()

    package.add_argument(
        '-e',
        '--encrypted-package',
        dest='encrypted',
        type=str,
        default=DEFAULT_PACKAGE,
        help=f'The path to an encrypted ISO 3166 standard csv zip file. '
             f'Default: {DEFAULT_PACKAGE}'
    )

    package.add_argument(
        '-p',
        '--package',
        dest='package',
        type=str,
        help='The path to an unencrypted ISO 3166 standard csv zip file.'
    )

    args = parser.parse_args()

    package = getattr(args, 'package', None)
    if args.encrypted:
        package = Path(args.encrypted)
        if args.encrypted.endswith('.gpg'):
            package = Path(args.encrypted[0:-4])
        exec_command(
            'gpg',
            '--output',
            package,
            '--decrypt',
            args.encrypted
        )

    if package is None or not os.path.isfile(package):
        raise RuntimeError(f'{package} does not exist or is not a file!')

    context = {
        'languages': [],
        'countries': [],
        'regions': []
    }

    with ZipFile(package, 'r') as csv_pkg:
        pprint(csv_pkg.namelist())

    cleanup()



def cleanup():
    exec_command(
        'rm',
        '-rf',
        f'`git ls-files --others --exclude-standard {Path(__file__).parent}`'
    )

if __name__ == '__main__':
    main()
