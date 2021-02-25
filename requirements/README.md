# pip requirements files

## Index

- [default.txt](default.txt)    Default requirements
- [test.txt](test.txt)          Requirements for running test suite

## Examples

### Installing requirements

```bash
$ pip install -U -r requirements/default.txt
```

### Running the tests

```bash
$ pip install -U -r requirements/default.txt
$ pip install -U -r requirements/test.txt
```

### Learn More
`-U` or `--upgrade`             Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy used.  
`-r` or `--requirement <file>`  Install from the given requirements file. This option can be used multiple times.  
`-h` or `--help`                Show help.

To see all help documentation, run
```bash
$ pip install -h
```