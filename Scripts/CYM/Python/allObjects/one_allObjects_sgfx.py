import os
import scade.model.display as SDY

# create the new Specification
layer = SDY.Layer(name="symbology_layer1", ratio=(1.0, 1.0), origin=(0.0, 0.0))
model = SDY.Specification(width=768, height=768, layers=[layer])

# Create types
array_2 = SDY.ArrayType(SDY.SimpleType.REAL, SDY.LiteralExpr("2"))
t_global_real_2 = SDY.TypeDefinition(name="t_global_real_2", definition=array_2)
c_t_global_real_2 = SDY.ConstantDefinition(name="t_global_real_2", type=SDY.NamedType("t_global_real_2"), definition=SDY.parse_expr("[-276.0,329.0]"))



# create the variable dictionary
inputs = layer.declaration.input
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_VISIBILITY",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_CENTER",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-276.0,329.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_RADIUS",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("30.819"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_LINE_CAP",
        representation=SDY.Representation.LINE_CAP,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="COLOR",
        type=SDY.NamedType("t_global_real_2"),
        init=SDY.parse_expr("c_t_global_real_2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TEXT_TEXT",
        representation=SDY.Representation.AS_STRING,
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.CHAR), SDY.LiteralExpr("255^2")),
        init=SDY.parse_expr("[84,69,83,84,50,0]"),
    )
)
# inputs.append(SDY.Variable(name = 'Center', type = SDY.Type(SDY.GlobalType(???)), init = SDY.LiteralExpr('c_t_global_real_2')))
# inputs.append(SDY.Variable(name = 'DGFX_Visiable', type = SDY.Type(SDY.GlobalType(???)), init = SDY.LiteralExpr('c_t_global_bool')))
# inputs.append(SDY.Variable(name = 'DGFX_LineWidth', type = SDY.Type(SDY.GlobalType(???)), init = SDY.LiteralExpr('c_t_global_int')))

constants = layer.declaration.constant
constants.append(
    SDY.Variable(
        name="test_constant",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)

outputs = layer.declaration.output
outputs.append(
    SDY.MemVariable(
        name="test_output",
        memory=True,
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)  # memory = SDY.MemVariable('true'),


# save the Specification to a given location
output_path = "Outputs/allObjects.sgfx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
SDY.save_sgfx(model, output_path)
