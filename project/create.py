import argparse
from datetime import datetime
from pathlib import Path

from .static_config import StaticConfig


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-interactive', action='store_true', 
    			 help='Do not prompt user for parameters '
    			      '(all parameters must be provided via commandline)')
    parser.add_argument('-author', type=str, help='Author of the project (required)', default=None)
    parser.add_argument('-project', type=str, help='Name of the project (required)', default=None)
    parser.add_argument('-codename', type=str, help='Short codename for project (optional)',
                        default=None)
    parser.add_argument('-org', type=str, help='Organisation responsible for the project (optional)', 
                        default=None)
    args = parser.parse_args()
    return {
        k: v for k, v in args.__dict__.items() if v is not None
    }


def get_input_and_validate(request_str, required=True):
    valid = False
    while not valid:
        value = input(request_str)
        valid = True

        if required and not value:
            valid = False
    
    return value


def get_params_from_user(already_given_params):
    print('Provide the following information (* = required):')
    required = {
        param: get_input_and_validate(f'{param}*:', required=True)
        for param in (set(StaticConfig.REQUIRED_PARAMS) - set(already_given_params))
    }
    optional = {
        param: get_input_and_validate(f'{param}:', required=False)
        for param in (set(StaticConfig.OPTIONAL_PARAMS) - set(already_given_params))
    }
    return {**already_given_params, **required, **optional}


def extract_initials(s):
    return ''.join([
        w[0] for w in s.split()
    ])


def extract_code(s):
    if len(s.split()) == 1:
        code = s
    else:
        code = extract_initials(s)

    return ''.join([c.lower() for c in code if c.isalpha()])


def clean_params(params):

    all_needed_params = list(StaticConfig.REQUIRED_PARAMS)
    if any(param not in all_needed_params for param in params):
        missing_params = set(all_needed_params) - set(params)
        raise ValueError(f'Necessary Parameters Missing: {missing_params}')

    for param in params:
        if isinstance(params[param], str):
            params[param] = params[param].strip()

    if 'org' not in params or not params['org']:
        params['org'] = extract_code(params['author'])
    if 'codename' not in params or not params['codename']:
        params['codename'] = extract_code(params['project'])
    
    params['date'] = datetime.now().strftime('%Y-%m-%d')
    
    MAGIC_LINE_LEN = 24
    n_spaces = MAGIC_LINE_LEN - len(params['codename'])
    n_spaces = n_spaces if n_spaces > 1 else 1
    params['spaces'] = n_spaces * ' '
    
    return params


def copy_and_format(template_dir, target_dir, project_params):
    target_dir.mkdir(exist_ok=True)
    
    for temp_path in template_dir.glob('*'):
        if temp_path.name != 'module':
            name = temp_path.name
        else:
            name = project_params['codename']
        
        target_path = target_dir / temp_path.name

        if temp_path.is_dir():
            copy_and_format(temp_path, target_path, project_params)
        else:
            with temp_path.open(mode='r') as f:
            	contents = f.read()
            	try:
                    contents = contents.format(**project_params)
            	except KeyError as e:
            	    print('Failed to format', temp_path)
            	    print(contents)
            	    raise e
            	    
            project_file = target_path
            with project_file.open(mode='w') as f:
                f.write(contents)


def create_project(project_params):
    print('Creating project with the following parameters:')
    for param in project_params:
    	if param in StaticConfig.REQUIRED_PARAMS or StaticConfig.OPTIONAL_PARAMS:
            print(f'{param}: {project_params[param]}')

    
    output_path = Path(StaticConfig.OUTPUT_DIR)
    project_dir = output_path / project_params['codename']
    template_path = Path(StaticConfig.TEMPLATE_DIR)
    copy_and_format(template_path, project_dir, project_params)


def main():
    args = parse_args()
    print(args)
    if not args['no_interactive']:
        del args['no_interactive']
        print('Requesting user input for project parameters...')
        project_params = get_params_from_user(args)
    else:
        project_params = args
    
    project_params = clean_params(project_params)
    create_project(project_params)


if __name__ == '__main__':
    main()

