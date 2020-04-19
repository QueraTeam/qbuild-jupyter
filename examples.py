from qbuild_jupyter import converter


# convert initial directory in path
nonquera_extract_dir_path, nonquera_extract_zip_path = converter.convert_initial_to_nonquera_in_path(
    path='/path/to/initial/dir',
    mode='dir',
    nonquera_dir='/path/to/where/you/want/dir'
)


# convert initial zip in path
nonquera_extract_dir_path, nonquera_extract_zip_path = converter.convert_initial_to_nonquera_in_path(
    path='/path/to/initial.zip',
    mode='zip',
    nonquera_dir='/path/to/where/you/want/dir'
)


# convert initial directory in temporary file
temp_file = converter.convert_initial_to_nonquera_in_temp_file(
    path='/path/to/initial/dir',
    mode='dir',
)


# convert initial zip in temporary file
temp_file = converter.convert_initial_to_nonquera_in_temp_file(
    path='/path/to/initial.zip',
    mode='zip',
)
