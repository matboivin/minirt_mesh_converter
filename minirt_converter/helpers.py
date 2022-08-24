"""Command line helper functions."""

from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    """Parse the program's arguments.

    Returns
    -------
    argparse.Namespace
        The program's arguments.

    """
    parser: ArgumentParser = ArgumentParser(
        prog="minirt_converter",
        description="Convert .obj files to .rt files to render a triangle mesh "
        "effect for miniRT project of School 42.",
    )

    parser.add_argument("filename", type=str, help="obj file to convert.")
    parser.add_argument(
        "color", type=str, help="the color in RGB format (e.g., 255,255,255)."
    )

    parser.add_argument_group(
        "example usage", "minirt_converter file.obj 255,204,0"
    )

    return parser.parse_args()
