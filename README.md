# Parsing libs speedtest

## Running
```shell
> python -m virtualenv .venv
> pdm install
> ./run.sh
```

## Test results
## bs4
```shell
> time ./test1.py

real    0m22.559s
user    0m22.461s
sys     0m0.023s
```
## lxml
```shell
> time ./test2.py

real    0m2.523s
user    0m2.510s
sys     0m0.004s
```
## xmltodict + jmespath
```shell
> time ./test3.py

real    0m2.757s
user    0m2.746s
sys     0m0.005s
```
