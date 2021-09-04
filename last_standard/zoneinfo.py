import sys

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

    sys.modules["zoneinfo"] = zoneinfo
