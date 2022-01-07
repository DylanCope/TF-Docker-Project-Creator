class StaticConfig:
    REQUIRED_PARAMS = {
            'author': 'Author Name',
            'project': 'Project Name',
    }
    OPTIONAL_PARAMS = {
            'org': 'Organisation',
            'codename': 'Project Codename',
    }
    TEMPLATE_DIR = './template'
    OUTPUT_DIR = '../' # folder in which to create project folder
