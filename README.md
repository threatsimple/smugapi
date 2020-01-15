# smugapi

a few smug api endpoints that may be useful

# command line

All development related tasks are managed via the `Makefile`.

Managing the app at runtime is handled via the `smugapi` command.

# running the service

```
smugapi run
```

This will run the web service and bind to localhost.


You'll want to pass api keys via either the cmd line or environment variables.

# developing

## dev environment

```
make dev
```

This creates a python virtualenv in `pyvenv` and installs the required libs, as
referenced in `reqs.pip`.

This also sets up the current source directory as the `smugapi` module in the
venv for ease of development.

## testing

```
make test
```

Assuming you've run `make dev`, you can use `make test` to run tests. This
will handle the executing the tests in the virtualenv for you, so no need to
handle that in your shell.


