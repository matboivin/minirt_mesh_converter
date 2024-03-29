"""Convert .obj file to .rt file."""

from pathlib import Path
from typing import Dict, List

from verboselogs import VerboseLogger


def get_triangles_from_face(
    face: str,
    vertices_coords: Dict[str, Dict[str, str]],
    color: str,
    triangles: List[str],
) -> None:
    """Get triangles from face element coordinates.

    Parameters
    ----------
    face : str
        A Polygonal face element line.
    vertices_coords : dict of dict
        Vertices coordinates parsed from .obj file.
    color : str
        The color of the object in RGB format.
    triangles : list of str
        The list to which append new triangles.

    """
    tmp: List[str] = face.split(" ")
    matching_coords: List[str] = [
        tmp[i].split("/")[0] for i in range(1, len(tmp))
    ]

    vertex1: str = ",".join(
        (
            vertices_coords[matching_coords[0]]["x"],
            vertices_coords[matching_coords[0]]["y"],
            vertices_coords[matching_coords[0]]["z"],
        )
    )

    vertex2: str = ",".join(
        (
            vertices_coords[matching_coords[1]]["x"],
            vertices_coords[matching_coords[1]]["y"],
            vertices_coords[matching_coords[1]]["z"],
        )
    )

    vertex3: str = ",".join(
        (
            vertices_coords[matching_coords[2]]["x"],
            vertices_coords[matching_coords[2]]["y"],
            vertices_coords[matching_coords[2]]["z"],
        )
    )

    triangles.append(f"tr {vertex1} {vertex2} {vertex3} {color}")

    # if a face line has more than 5 params then its a quad not a tris therefore
    # we transform the quad into a tris.. still have to implement other polyons.
    # 4-------3
    # |      /|
    # |    /  |
    # |  /    |
    # |/      |
    # 1-------2
    # 1 2 3 4 into 1 2 3 and 1 3 4
    if len(tmp) > 5:
        vertex4: str = ",".join(
            (
                vertices_coords[matching_coords[3]]["x"],
                vertices_coords[matching_coords[3]]["y"],
                vertices_coords[matching_coords[3]]["z"],
            )
        )
        triangles.append(f"tr {vertex1} {vertex3} {vertex4} {color}")


def parse_vertices_coords(obj_data: List[str]) -> Dict[str, Dict[str, str]]:
    """Parse vertices coordinates (x, y, z).

    Parameters
    ----------
    obj_data : list of str
        List obj elements.

    Returns
    -------
    dict of dict
        All vertices coordinates.

    """
    vertices_coords: Dict[str, Dict[str, str]] = {}
    vertices_count: int = 1

    for element in obj_data:
        if element[:2] == "v ":  # Geometric vertex (v x y z [w])
            vertex_coords: List[str] = element.split(" ")

            vertices_coords[str(vertices_count)] = {
                "x": vertex_coords[1],
                "y": vertex_coords[2],
                "z": vertex_coords[3][:-1],
            }
            vertices_count += 1

    return vertices_coords


def save_polygons_to_file(
    filename: Path, obj_data: List[str], color: str
) -> None:
    """Parse vertices coordinates (x, y, z).

    Parameters
    ----------
    filename : Path
        The output filename.
    obj_data : list of str
        List obj elements.
    color : str
        The color of the object in RGB format.

    """
    vertices_coords: Dict[str, Dict[str, str]] = parse_vertices_coords(
        obj_data
    )

    triangles: List[str] = []

    for element in obj_data:
        if element[:2] == "f ":  # Polygonal face element (f 1 2 3)
            get_triangles_from_face(element, vertices_coords, color, triangles)

    filename.write_text("\n".join(triangles) + "\n")


def convert_obj_to_rt(
    logger: VerboseLogger, filename: Path, color: str
) -> None:
    """Convert .obj file to .rt format.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    filename : Path
        The file to convert.
    color : str
        The color of the object in RGB format.

    """
    outfile: Path = filename.with_suffix(".rt")

    with filename.open(mode="r", encoding="utf-8") as file_handle:
        obj_data: List[str] = file_handle.readlines()

    logger.info("Start conversion.")

    save_polygons_to_file(outfile, obj_data, color)

    logger.info(f"Result saved in: '{str(outfile)}'.")
