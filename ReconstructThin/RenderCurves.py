from bpy import context, data, ops

# Create a bezier circle and enter edit mode.
ops.curve.primitive_bezier_circle_add(radius=1.0,
                                      location=(0.0, 0.0, 0.0),
                                      enter_editmode=True)

# Subdivide the curve by a number of cuts, giving the
# random vertex function more points to work with.
ops.curve.subdivide(number_cuts=16)

# Randomize the vertices of the bezier circle.
# offset [-inf .. inf], uniform [0.0 .. 1.0],
# normal [0.0 .. 1.0], RNG seed [0 .. 10000].
ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=0.0, seed=0)

# Scale the curve while in edit mode.
ops.transform.resize(value=(2.0, 2.0, 3.0))

# Return to object mode.
ops.object.mode_set(mode='OBJECT')

# Store a shortcut to the curve object's data.
obj_data = context.active_object.data

# Which parts of the curve to extrude ['HALF', 'FRONT', 'BACK', 'FULL'].
obj_data.fill_mode = 'FULL'

# Breadth of extrusion.
obj_data.extrude = 0

# Smoothness of the segments on the curve.
obj_data.resolution_u = 20
obj_data.render_resolution_u = 32

ops.curve.primitive_bezier_circle_add(radius=0.05, enter_editmode=True)
ops.curve.subdivide(number_cuts=4)
bevel_control = context.active_object
bevel_control.data.name = bevel_control.name = 'Bevel Control'

obj_data.bevel_object = bevel_control
ops.object.mode_set(mode='OBJECT')
