from qbuild_jupyter import converter


# convert initial directory
nonquera_extract_dir_path, nonquera_extract_zip_path = converter.convert_initial_to_nonquera(
    path='/path/to/initial/dir',
    mode='dir',
    nonquera_dir='/path/to/where/you/want/dir'
)


# convert initial zip
nonquera_extract_dir_path, nonquera_extract_zip_path = converter.convert_initial_to_nonquera(
    path='/path/to/initial.zip',
    mode='zip',
    nonquera_dir='/path/to/where/you/want/dir'
)
