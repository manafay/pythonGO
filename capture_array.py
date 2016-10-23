def print_list_to_file(file_in, file_out):
    op = map(lambda x: '\'' + x + '\'' + ',' + '\n', file_in.read().split())
    return open(file_out, 'w').writelines(['['] + op + [']'])


def generate_list(input_f, output_f):
    with open(input_f) as inf:
        return print_list_to_file(inf, output_f)

print(generate_list('html_attributes', 'output_html_attributes'))