"""Setup miniRT mesh converter package."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="minirt_converter",
                 version="1.0.0",
                 author="mboivin",
                 author_email="mboivin@student.42.fr",
                 description="Convert .obj files to .rt files to render a "
                 "triangle mesh effect for miniRT project at 42.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/matboivin/minirt_mesh_converter",
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                 ],
                 python_requires=">=3.9",
                 entry_points={
                     "console_scripts":
                     ["minirt_converter=minirt_converter.main:entrypoint"]
                 })
