"""Program's entrypoint."""

import os
from argparse import Namespace

from .helpers import parse_args
from .convert import convert_obj_to_rt


def main(filename: str, color: str) -> None:
    """Run program.

    Parameters
    ----------
    filename : str
        The file to convert.
    color : str
        The color of the object in RGB format.

    """
    convert_obj_to_rt(filename, color)


def entrypoint() -> None:
    """Program's entrypoint."""
    args: Namespace = parse_args()
    filename: str = os.path.join(args.filename)

    print("==> Start conversion ...")
    main(filename, args.color)


if __name__ == "__main__":
    entrypoint()
