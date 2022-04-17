from OCC.Display.WebGl import x3dom_renderer, threejs_renderer
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Vec
from OCC.Extend.ShapeFactory import translate_shp, rotate_shp_3_axis

# determined the environment we will render in webgl
my_ren = threejs_renderer.ThreejsRenderer()

black = (0, 0, 0)
white = (1, 1, 1)
for i in range(8):
	for j in range(8):
		# we created a cube with dimensions 1 1 1
		box_shp = BRepPrimAPI_MakeBox(
			1, 1, 1
		).Shape()
		# We define the angle of rotation and the axis of rotation
		angle_x = 0
		angle_y = 0
		angle_z = 0
		# We enter the values in degrees and enter the object we want to rotate into the parameters
		rotated_box = rotate_shp_3_axis(box_shp, angle_x, angle_y, angle_z, "deg")
		tr_x = j
		tr_y = 0
		tr_z = i
		# We enter the values what we want to translate on the plane.
		trans_box = translate_shp(rotated_box, gp_Vec(tr_x, tr_y, tr_z))
		if i % 2 == 0:
			if j % 2 == 0:
				color = white
			else:
				color = black
		else:
			if j % 2 != 0:
				color = white
			else:
				color = black
		# We display the object in the plane
		my_ren.DisplayShape(
			trans_box, export_edges=True, color=color, transparency=1
		)

# render all object
my_ren.render()
