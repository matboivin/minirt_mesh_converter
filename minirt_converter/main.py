"""Program's entrypoint."""

from argparse import Namespace
from pathlib import Path

import coloredlogs
from verboselogs import VerboseLogger

from .convert import convert_obj_to_rt
from .helpers import parse_args


def main(logger: VerboseLogger, filename: Path, color: str) -> None:
    """Run program.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    filename : Path
        The file to convert.
    color : str
        The color of the object in RGB format.

    """
    convert_obj_to_rt(logger, filename, color)


def entrypoint() -> None:
    """Program's entrypoint."""
    args: Namespace = parse_args()
    filename: Path = Path(args.filename)
    logger: VerboseLogger = VerboseLogger("minirt_converter")

    coloredlogs.install(
        logger=logger,
        level="DEBUG",
        fmt="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
    )

    try:
        main(logger, filename, args.color)
    except (OSError, FileNotFoundError) as err:
        logger.error(err)


if __name__ == "__main__":
    entrypoint()
