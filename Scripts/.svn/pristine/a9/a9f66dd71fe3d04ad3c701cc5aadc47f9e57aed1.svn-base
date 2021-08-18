# Copyright (c) 2018  ESTEREL TECHNOLOGIES SAS.  ALL RIGHTS RESERVED
# This source file may be used and distributed without restriction provided
# that this copyright statement is not removed from the file and that any
# derivative work contains this copyright notice.
#
# Warranty
# ESTEREL TECHNOLOGIES SAS makes no warranty of any kind with regard to the
# use of this Software, either expressed or implied, including, but not
# limited to the fitness for a particular purpose.

"""
This example illustrates the use of the Display API by creating a Specification from scratch, and saving it to an SGFX file.
The created model is inspired by the 'OneCounter' example that is distributed with SCADE Display.
"""

import os
import scade.model.display as SDY



if __name__ == "__main__":
    # create the new Specification
    layer = SDY.Layer(name="symbology_layer")
    model = SDY.Specification(width=768, height=768, layers=[layer])

    # create the variable dictionary
    inputs = layer.declaration.input
    inputs.append(
        SDY.Variable(
            name="COLOR",
            representation=SDY.Representation.COLOR,
            type=SDY.PredefType(SDY.SimpleType.INT),
            init=SDY.LiteralExpr("39"),
        )
    )
    inputs.append(
        SDY.Variable(
            name="NEEDLE_VALUE",
            type=SDY.PredefType(SDY.SimpleType.REAL),
            init=SDY.LiteralExpr("180.0"),
        )
    )
    inputs.append(
        SDY.Variable(
            name="UNIT_VALUE",
            type=SDY.PredefType(SDY.SimpleType.REAL),
            init=SDY.LiteralExpr("180.0"),
        )
    )
    inputs.append(
        SDY.Variable(
            name="UNIT",
            representation=SDY.Representation.AS_STRING,
            type=SDY.ArrayType(
                SDY.PredefType(SDY.SimpleType.CHAR), SDY.LiteralExpr("255")
            ),
            init=SDY.parse_expr("[85, 78, 73, 84, 0]"),
        )
    )
    inputs.append(
        SDY.Variable(
            name="INDEX",
            representation=SDY.Representation.INDEX,
            type=SDY.PredefType(SDY.SimpleType.INT),
            init=SDY.LiteralExpr("2"),
        )
    )

    # create the 'counter' group
    counter = SDY.Container(name="counter")
    layer.children.append(counter)

    # create sub-groups and their contents
    green_crown = SDY.Crown(
        radius=196.18, start_angle=170.0, end_angle=270.0, thickness=49.0, fill_color=14
    )
    orange_crown = SDY.Crown(
        radius=196.18, start_angle=90.0, end_angle=170.0, thickness=49.0, fill_color=31
    )
    red_crown = SDY.Crown(
        radius=196.18, start_angle=50.0, end_angle=90.0, thickness=49.0, fill_color=37
    )
    border = SDY.Container(
        name="border", children=[green_crown, orange_crown, red_crown]
    )
    counter.children.append(border)

    needle = SDY.Container(name="needle")
    counter.children.append(needle)

    rotate_group = SDY.RotationContainer(
        name="rotate group",
        ref_angle=90.0,
        start_angle=270.0,
        end_angle=50.0,
        clockwise=True,
    )
    rotate_group.start_rotation_value = SDY.RealProp(0.0)
    rotate_group.end_rotation_value = SDY.RealProp(220.0)
    rotate_group.start_rotation_locked = SDY.BooleanProp(True)
    rotate_group.end_rotation_locked = SDY.BooleanProp(True)
    rotate_group.functional_rotation_value = SDY.RealProp(0.0)
    rotate_group.functional_rotation_value.expr = SDY.IdentifierExpr("NEEDLE_VALUE")
    needle.children.append(rotate_group)

    needle_shape = SDY.Shape(
        points=[
            (-9.801, 0.0),
            (9.801, 0.0),
            (24.503, 137.326),
            (0.0, 186.371),
            (-24.503, 137.326),
        ],
        line_width=2,
        outline_color=41,
        fill_color=39,
    )
    needle_shape.fill_color.expr = SDY.IdentifierExpr("COLOR")
    needle_shape.polygon_smooth = SDY.BooleanProp(True)
    rotate_group.children.append(needle_shape)

    needle.children.append(SDY.Circle(radius=26.0, outline_color=41, fill_color=39))

    # create the 'unit' frame
    unit = SDY.Container(name="unit", origin=(39.0, -28.0))
    counter.children.append(unit)

    frame = SDY.Rectangle(
        first_point=(25.8, -19.0),
        third_point=(91.0, -58.0),
        line_width=2,
        outline_color=41,
        fill_color=39,
    )
    frame.second_arc = SDY.ArcSegmentProp(angle=145.5, clockwise=True)
    frame.fourth_arc = SDY.ArcSegmentProp(angle=187.4, clockwise=True)
    unit.children.append(frame)

    indicator = SDY.BiFont(
        position=(55.4, -48.3),
        value=180.0,
        first_line_width=4,
        first_font=4,
        second_line_width=4,
        second_font=4,
        outline_color=41,
    )
    indicator.value.expr = SDY.IdentifierExpr("UNIT_VALUE")
    indicator.format = SDY.FormatProp(nb_before_sign=0, nb_after_sign=3)
    indicator.format.display_sign.init = SDY.DisplaySignEnum.NEVER
    unit.children.append(indicator)

    unit.children.append(
        SDY.Text(
            position=(55.4, -78.7), value=[85, 78, 73, 84, 0], font=11, outline_color=41
        )
    )

    # create the indicator frame
    lines = [
        [(0.0, 196.2), (0.0, 176.0)],
        [(-64.0, 184.4), (-58.7, 161.3)],
        [(-126.0, 150.3), (-110.3, 131.5)],
        [(-169.8, 98.1), (-148.5, 85.8)],
        [(-193., 34.1), (-168.9, 29.8)],
        [(-193., -34.1), (-168.9, -29.8)],
        [(-169.8, -98.1), (-148.5, -85.8)],
        [(-126., -150.3), (-110.3, -131.5)],
        [(-67., -184.4), (-58.7, -161.3)],
        [(0.0, -196.2), (0.0, -171.7)],
        [(67., 184.4), (58.7, 161.3)],
        [(126., 150.3), (110.3, 131.5)],
    ]
    counter.children.append(
        SDY.Container(
            name="graduation",
            children=[
                SDY.Line(points=l, line_width=5, outline_color=41) for l in lines
            ],
        )
    )

    indicator_group = SDY.Container(name="indicator", origin=(0.0, -22.0))
    counter.children.append(indicator_group)

    indicator_frame = SDY.Rectangle(
        first_point=(-72.0, 302.0),
        third_point=(57.5, 234.0),
        line_width=4,
        outline_color=41,
    )
    indicator_frame.second_arc = SDY.ArcSegmentProp(angle=180.0, clockwise=True)
    indicator_frame.fourth_arc = SDY.ArcSegmentProp(angle=180.0, clockwise=True)
    indicator_group.children.append(indicator_frame)

    green_circle = SDY.Circle(center=(-70.0, 268.0), radius=26.0, fill_color=13)
    orange_circle = SDY.Circle(center=(-8.0, 268.0), radius=26.0, fill_color=33)
    red_circle = SDY.Circle(center=(54.0, 268.0), radius=26.0, fill_color=37)
    conditional_group = SDY.CondContainer(
        children=[green_circle, orange_circle, red_circle]
    )
    conditional_group.index.init = conditional_group.indexes.default = SDY.LiteralExpr(
        "2"
    )
    conditional_group.index.expr = SDY.IdentifierExpr("INDEX")
    indicator_group.children.append(conditional_group)

    # save the Specification to a given location
    output_path = "Outputs/OneCounter.sgfx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    SDY.save_sgfx(model, output_path)
