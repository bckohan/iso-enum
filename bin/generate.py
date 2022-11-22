import argparse
import subprocess
from pathlib import Path
import os
from zipfile import ZipFile
from pprint import pprint
import csv
from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape
)
from copy import copy

python_templates = Path(__file__).parent / 'templates' / 'python'
python_src = Path(__file__).parent.parent / 'iso_enum'
python_test = python_src / 'tests'

# TODO
# java_src = Path(__file__).parent.parent
# cpp_src = Path(__file__).parent.parent
# js_src = Path(__file__).parent.parent
# c_src = Path(__file__).parent.parent

standards = Path(__file__).parent.parent / 'standards'

DEFAULT_ISO3166 = str(
    standards / 'iso_country_code_ALL_csv.zip.gpg'
)
DEFAULT_ISO639 = str(
    standards / 'iso639-1.csv'
)
DEFAULT_ISO4217 = str(
    standards / 'iso4217.csv'
)

ISO639_PYTHON_TEMPLATES = [
    {
        'tmpl': 'iso639/ISOLanguage.py.jinja2',
        'dest': python_src / 'iso639' / 'ISOLanguage.py',
        'test': 'iso639/tests/ISOLanguage.py.jinja2',
        'test_dest': python_test / 'iso639' / 'ISOLanguage.py',
        'extra_ctx': {}
    }
]


def exec_command(*args):
    ret = subprocess.run(args, capture_output=True)
    if ret.returncode != 0:
        raise RuntimeError(
            f'Error executing [{args}]:\n\t{ret.stderr.decode()}'
        )
    return ret.stdout


python_context = {
    'quote_char': "'"
}
python_environment = Environment(
    loader=FileSystemLoader(python_templates),
    autoescape=select_autoescape(['python'])
)


def to_list(lst):
    return f"[{', '.join([python_context['quote_char']+str(itm)+python_context['quote_char'] for itm in lst])}, ]"


def quote(to_quote):
    if not isinstance(to_quote, str):
        to_quote = str(to_quote)
    return f'{python_context["quote_char"]}{to_quote}{python_context["quote_char"]}'


python_environment.filters["to_list"] = to_list
python_environment.filters["quote"] = quote


def main():

    parser = argparse.ArgumentParser(
        prog='generate_enums',
        description='Generate python iso3166 enumerations from the '
                    'ISO csv package.'
    )

    parser.add_argument(
        '--iso3166',
        dest='iso3166',
        type=str,
        default=DEFAULT_ISO3166,
        help=f'The path to an encrypted ISO 3166 standard csv zip file. '
             f'Default: {DEFAULT_ISO3166}'
    )
    
    parser.add_argument(
        '--iso639',
        dest='iso639',
        type=str,
        default=DEFAULT_ISO639,
        help=f'The path to an unencrypted ISO 639 standard csv zip file. '
             f'Default: {DEFAULT_ISO639}'
    )
    
    parser.add_argument(
        '--iso4217',
        dest='iso4217',
        type=str,
        default=DEFAULT_ISO4217,
        help=f'The path to an unencrypted ISO 4217 standard csv zip file.'
             f'Default: {DEFAULT_ISO4217}'
    )

    args = parser.parse_args()

    iso639 = getattr(args, 'iso639', None)
    iso4217 = getattr(args, 'iso4217', None)
    iso3166 = getattr(args, 'iso3166', None)

    if iso3166 is None or not os.path.isfile(iso3166):
        raise RuntimeError(f'{iso3166} does not exist or is not a file!')

    generate_iso639(iso639)
    generate_iso4217(iso4217)
    #generate_iso3166(iso3166)

    cleanup()


def generate_iso639(file_path):
    iso639_context = {
        'languages': []
    }
    with open(file_path, 'r') as iso_f:
        csv_reader = csv.DictReader(iso_f)
        for row in csv_reader:
            iso639_context['languages'].append({
                'identifier': row['Identifier'],
                'english':  [
                    eng.strip() for eng in row['English Name'].split(';')
                ],
                'french':  [
                    fr.strip() for fr in row['French Name'].split(';')
                ],
                'indigenous': [
                    ind.strip() for ind in row['Indigenous Name'].split(';')
                ]
            })

    from pprint import pprint
    pprint(iso639_context['languages'])

    for template in ISO639_PYTHON_TEMPLATES:
        tmpl = python_environment.get_template(template['tmpl'])
        context = copy(python_context)
        context.update(template['extra_ctx'])
        context.update(iso639_context)
        output_dir = Path(template['dest']).parent
        os.makedirs(output_dir, exist_ok=True)
        print(f'Writing {template["dest"]}...')
        with open(template['dest'], 'w') as output:
            output.write(tmpl.render(context))

        if 'test' in template:
            print(f'Writing {template["test_dest"]}...')
            tmpl = python_environment.get_template(template['test'])
            with open(template['test_dest'], 'w') as output:
                output.write(tmpl.render(context))


def generate_iso3166(file_path):
    if file_path.endswith('.gpg'):
        iso3166_encrypted = str(Path(file_path))
        file_path = Path(iso3166_encrypted[0:-4])
        exec_command(
            'gpg',
            '--output',
            file_path,
            '--decrypt',
            iso3166_encrypted
        )

    with ZipFile(file_path, 'r') as csv_pkg:
        pass
        #pprint(csv_pkg.namelist())


def generate_iso4217(file_path):
    pass


def cleanup():
    files = exec_command(
        'git',
        'ls-files',
        '--others',
        '--exclude-standard',
        Path(__file__).parent
    ).decode().split()
    print('Deleting:')
    pprint(files, indent=4)
    exec_command(
        'rm',
        '-rf',
        *files
    )


if __name__ == '__main__':
    main()
