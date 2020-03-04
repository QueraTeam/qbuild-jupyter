*qbuild-jupyter* is a convert system for our jupyter challenges.

# Installation

For installing or updating qbuild, run the following commands:

```bash
$ git clone this repository
$ cd qbuild-jupyter
$ sudo pip3 install . 
```

---

# [Examples]('example.py'):

### Convert initial directory:

```python
from qbuild_jupyter import converter

nonquera_extract_dir_path, nonquera_extract_zip_path = converter.convert_initial_to_nonquera(
    path='/path/to/initial/dir',
    mode='dir',
    nonquera_dir='/path/to/where/you/want/dir'
)

```

### Convert initial zip

```python
from qbuild_jupyter import converter

nonquera_extract_dir_path, nonquera_extract_zip_path = converter.convert_initial_to_nonquera(
    path='/path/to/initial.zip',
    mode='zip',
    nonquera_dir='/path/to/where/you/want/dir'
)

```


