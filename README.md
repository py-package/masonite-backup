<p align="center">
<img src="https://banners.beyondco.de/Masonite%20Backup.png?theme=light&packageManager=pip+install&packageName=masonite-backup&pattern=charlieBrown&style=style_2&description=Backup+solution+for+Masonite+Apps.&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

<p align="center">
  <a href="https://docs.masoniteproject.com">
    <img alt="Masonite Package" src="https://img.shields.io/static/v1?label=Masonite&message=package&labelColor=grey&color=blue&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAAA6gAwAEAAAAAQAAAA4AAAAATspU+QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAnxJREFUKBVNUl1IVEEUPjPObdd1VdxWM0rMIl3bzbVWLSofVm3th0AhMakHHyqRiNSHEAq5b2HSVvoQRUiEECQUQkkPbRslRGigG8auoon2oPSjpev+3PWeZq7eaC5nDt93vplz5txDQJYpNxX4st4JFiwj9aCqmswUFQNS/A2YskrZJPYefkECC2GhQwAqvLYybwXrwBvq8HSNOXRO92+aH7nW8vc/wS2Z9TqneYt2KHjlf9Iv+43wFJMExzO0YE5OKe60N+AOW6OmE+WJTBrg23jjzWxMBauOlfyycsV24F+cH+zAXYUOGl+DaiDxfl245/W9OnVrSY+O2eqPkyz4sVvHoKp9gOihf5KoAVv3hkQgbj/ihG9fI3RixKcUVx7lJVaEc0vnyf2FFll+ny80ZHZiGhIKowWJBCEAKr+FSuNDLt+lxybSF51lo74arqs113dOZqwsptxNs5bwi7Q3q8npSC2AWmvjTncZf1l61e5DEizNn5mtufpsqk5+CZTuq00sP1wkNPv8jeEikVVlJso+GEwRtNs3QeBt2YP2V2ZI3Tx0e+7T89zK5tNASOLEytJAryGtkLc2PcBM5byyUWYkMQpMioYcDcchC6xN220Iv36Ot8pV0454RHLEwmmD7UWfIdX0zq3GjMPG5NKBtv5qiPEPekK2U51j1451BZoc3i+1ohSQ/UzzG5uYFFn2mwVUnO4O3JblXA91T51l3pB3QweDl7sNXMyEjbguSjrPcQNmwDkNc8CbCvDd0+xCC7RFi9wFulD3mJeXqxQevB4prrqgc0TmQ85NG/K43e2UwnMVAJIEBNfWRYR3HfnvivrIzMyo4Hgy+hfscvLo53jItAAAAABJRU5ErkJggg==">
  </a>
  <img alt="GitHub Workflow Status (branch)" src="https://github.com/py-package/masonite-backup/actions/workflows/pythonapp.yml/badge.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-backup">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/py-package/masonite-backup?include_prereleases">
  <img alt="License" src="https://img.shields.io/github/license/py-package/masonite-backup">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# Masonite Backup (WIP)

Backup solution for Masonite.

### Features

- [x] Backup Database
- [x] Backup Files
- [x] Store Backup Locally in the filesystem
- [ ] Send Backup Notifications
- [ ] Email Backup
- [ ] Store Backup in other Masonite Supported Storage Drivers [s3]


### Installation

```bash
pip install masonite-backup
```

### Configuration

Add BackupProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from backup import BackupProvider

# ...
PROVIDERS = [
    # ...
    # Third Party Providers
    BackupProvider,
    # ...
]
```

Then you can publish the package resources (if needed) by doing:

```bash
python craft package:publish backup
```

### Usage

Once you publish the package resources, you can use the `backup` command to backup your database and files. Before that if you want to configure options of backup then you can do that by updating `config/backup.py` configuration file.

```python
# config/backup.py

FILENAME = "backup"
DIRECTORY = "backup"
SOURCE = {
    "root": base_path(),
    "excludes": [
        ".git",
        "storage",
        "venv",
        "node_modules",
        "__pycache__",
        # add more...
    ],
}
```

**Backup Database and Files**

```bash
python craft backup:run
```

**Backup Database Only**

```bash
python craft backup:run --only-db
```

**Backup Files Only**

```bash
python craft backup:run --only-files
```


## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## Maintainers

- [x] [Yubaraj Shrestha](https://www.github.com/py-package)

## License


Backup is open-sourced software licensed under the [MIT license](LICENSE).

