from typing import Dict, Iterable

try:
    import yaml
except ImportError:
    _yaml_loader = None
else:
    _yaml_loader = getattr(yaml, "CLoader", yaml.Loader)


def _yaml_import_error(s: str) -> Iterable[Dict]:  # no cov
    import yaml  # noqa

    return yaml_load_all(s)


def _yaml_load_all(s: str) -> Iterable[Dict]:
    assert _yaml_loader
    yield from yaml.load_all(s, Loader=_yaml_loader)


if _yaml_loader is None:
    yaml_load_all = _yaml_import_error
else:
    yaml_load_all = _yaml_load_all
