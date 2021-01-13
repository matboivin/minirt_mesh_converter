# An ugly script to convert .obj files for miniRT

Convert `.obj` files to `.rt` files to render a triangle mesh effect for [miniRT](https://github.com/matboivin/miniRT) project at 42.

<p align="center">
  <img src="assets/deer.png" alt="deer" width="680" />
</p>

### Disclaimer

This project was done for **learning purposes** and is thus **not intended for production**.  
Don't copy. Learn.

## Prerequisites

* Python 3.6 or greater
* Learn more about `.obj` files formatting [here](https://en.wikipedia.org/wiki/Wavefront_.obj_file).

## Usage

Run the script:

```console
python minirt_converter.py <file.obj> <color>
```

* `file.obj`: The file to be converted
* `color`: The color of the triangles

Then, **add Resolution, Ambient Light, cameras and light points** to your [scene](https://github.com/matboivin/miniRT/blob/master/doc/scene_file.md).

The `cat.rt`, `deer.rt` and `wolf.rt` scenes can be found [here](https://github.com/matboivin/miniRT/tree/master/scenes). They have approximately 1500 triangles each and my miniRT takes 3 minutes to render it, to give you an idea of the rendering time.

<p align="center">
  <img src="assets/cat.png" alt="cat" width="680" />
  <img src="assets/wolf3d.png" alt="wolf" width="680" />
</p>

### License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
