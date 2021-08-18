import os
import scade.model.display as SDY


layer = SDY.Layer(
    name="symbology_layer1",
    oid="bb42e795-6c6b-4123-b242-ceaecf2ed120",
    ratio=(1.0, 1.0),
    origin=(0.0, 0.0),
)
model = SDY.Specification(width=768, height=768, layers=[layer])


inputs = layer.declaration.input
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_VISIBILITY",
        oid="b490dd2a-c86d-48fb-86d3-7f588b7421af",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_CENTER",
        oid="f31c51b0-77ac-4f65-a091-886f9dae373a",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-276.0,329.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_RADIUS",
        oid="fe5d4675-b6f9-4187-9790-e4ce20686853",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("30.819"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_START_ANGLE",
        oid="c1c709dd-3f96-46c3-a00d-781b7e52971f",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_END_ANGLE",
        oid="c8a11a3c-4f5e-4dcb-a398-2b47a703ab0f",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("377.985992"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_HALOING",
        oid="de5bfe9f-642a-48c8-86ba-c4c9df2502ae",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_OUTLINE_COLOR",
        oid="ce0544bf-091f-40f0-8d6b-70b86f4778c2",
        representation=SDY.Representation.COLOR,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("16"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_LINE_WIDTH",
        oid="f4067baa-349b-47ef-801f-645916019da9",
        representation=SDY.Representation.LINE_WIDTH,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_LINE_STIPPLE",
        oid="454d9117-478f-47eb-955a-0e42d09fe610",
        representation=SDY.Representation.LINE_STIPPLE,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_OUTLINE_OPACITY",
        oid="05cc8396-6f5d-4016-805e-1407b046ebb0",
        representation=SDY.Representation.OPACITY,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("255"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_FILLED_COLOR",
        oid="e990085a-7b68-4c9b-8098-31c0bad6b802",
        representation=SDY.Representation.COLOR,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("6"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_FILLED_OPACITY",
        oid="9aee0db6-1931-4d53-b962-ff8fcd84366b",
        representation=SDY.Representation.OPACITY,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("255"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_POLYGON_SMOOTH",
        oid="ff6bfd86-6336-4951-9e86-11dcb59b4719",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_LINE_CAP",
        oid="72eeb9a2-3a08-460d-8611-65d4153fc592",
        representation=SDY.Representation.LINE_CAP,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_TEXTURE_ID",
        oid="1f20107d-b2f3-4e71-af2e-45aed45bfedd",
        representation=SDY.Representation.TEXTURE,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_VISIBILITY",
        oid="a6f4f9a7-1fbb-4fad-b4d9-48f6e4c4d67f",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_CENTER",
        oid="0b9758e4-a7e0-4645-a6da-dd3037156808",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-273.268005,258.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_RAIDUS",
        oid="f6796152-251d-478a-9798-a896e01df943",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("29.732"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_HALOING",
        oid="694ee7ff-b0b3-4300-b5b6-bfcfadaae32a",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_OUTLINE_COLOR",
        oid="fdaefcd0-fcd1-45ae-b608-adf7c0d1519f",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("16"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_LINE_WIDTH",
        oid="6bb3ea4d-826d-4ad1-9c90-ad960b0b80ae",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_LINE_STIPPLE",
        oid="2f7e6f84-1e9b-4030-b910-427284d1305c",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_OUTLINE_OPACITY",
        oid="257dd63c-32e4-4b6b-b054-6b2184728158",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("255"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_FILLED_COLOR",
        oid="f3217ae5-1caa-4326-ac44-34a3b48aa2d4",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("6"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_FILLED_OPACITY",
        oid="99fb64fd-666c-4d4c-8bb4-59bc27f644e0",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("255"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_POLYGON_SMOOTH",
        oid="a203a5a5-1945-4ad9-b434-0afc2b79fb07",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_TEXTURE_ID",
        oid="1f20107d-b2f3-4e71-af2e-45aed45bfedd",
        representation=SDY.Representation.TEXTURE,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CROWN_VISIBILITY",
        oid="439f3cba-8e8a-4f54-9222-531209080fed",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CROWN_CENTER",
        oid="2b99c4ca-9db9-4a10-b8f3-c3ffc86372e7",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-275.243988,176.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CROWN_RADIUS",
        oid="a6aaac7a-3157-4bb2-b429-0708d99a081c",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("32.757"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CROWN_START_ANGLE",
        oid="9d4ab284-dd9d-44d7-b72d-8652d9accef7",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("102.338997"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CROWN_END_ANGLE",
        oid="3c8d3b3a-a3fa-4a8e-b958-a77eecd6bf4d",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("388.071991"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CROWN_THICHNESS",
        oid="6816134f-0e2d-4b32-ad70-617b34f2b4ec",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("13.127"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_RECTANLGE_FIRST_POINT",
        oid="32578ed5-dfb8-42bf-ad60-31664b3ed0e4",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-300.0,117.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_RECTANLGE_SECOND_POINT",
        oid="9934bede-5a5e-465f-a927-ba8d2b8bf7d6",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-248.0,79.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_SHAPE_X",
        oid="91ab28be-38f9-40b9-9cde-2555df2c1771",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("-260.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_SHAPE_Y",
        oid="2da8a6cd-614d-4ba3-9835-ba406c8d4333",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("21.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_LINE_PONIT",
        oid="eae23e40-cb5c-421e-90df-8e7bf8e8a874",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-291.0,-98.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_LINE_LINE_STIPPLE",
        oid="9c52562a-3c60-4b06-8545-970cb0d3bdd8",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TEXT_VISIBILITY",
        oid="d1c474ca-7ad2-4b54-b136-ed4d6d877cdc",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TEXT_TEXT",
        oid="a3eacabf-470c-46d4-9169-e742e20093b0",
        representation=SDY.Representation.AS_STRING,
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.CHAR), SDY.LiteralExpr("255")),
        init=SDY.parse_expr("[84,69,83,84,50,0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TEXT_HALOING",
        oid="d647bccf-9cc1-43d5-8067-7ef023deaa55",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TEXT_OUTLINE_COLOR",
        oid="40b78942-dcf7-474f-8239-e915e93b567b",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("17"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TEXT_FONT_LINE_WIDTH",
        oid="5822dcc8-30e4-4e20-90ae-b22e03ff6114",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_BIFONT_VALUE",
        oid="556b6150-d0a9-4763-831e-57bc1766bb43",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("12.12"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_BIFONT_FONT_LINE_WIDTH",
        oid="028d7ef7-08ae-413c-9a79-bb5745c73ed9",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_BIFONT_SMALL",
        oid="9f529eb3-f00c-47d2-a22e-533ff85dd195",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_BITMAP_VISIBLITY",
        oid="06f636b6-05bf-4944-8344-9d10e3ec594a",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_ELLIPSE_VISIBILITY",
        oid="b490dd2a-c86d-48fb-86d3-7f588b7421af",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_ELLIPSE_CENTER",
        oid="f31c51b0-77ac-4f65-a091-886f9dae373a",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-276.0,329.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_ELLIPSE_HORIZONTAL_RADIUS",
        oid="2d310581-ae33-4381-b30a-cb2172fff077",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_ELLIPSE_VERTICAL_RADIUS",
        oid="2fbee22a-2a76-4666-9eb2-3090fc6a7088",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_ELLIPSE_START_ANGLE",
        oid="c1c709dd-3f96-46c3-a00d-781b7e52971f",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("76.759003"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_ELLIPSE_END_ANGLE",
        oid="c8a11a3c-4f5e-4dcb-a398-2b47a703ab0f",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("377.985992"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ELLIPSE_VISIBILITY",
        oid="a6f4f9a7-1fbb-4fad-b4d9-48f6e4c4d67f",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ELLIPSE_CENTER",
        oid="0b9758e4-a7e0-4645-a6da-dd3037156808",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-273.268005,258.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ELLIPSE_HORIZONTAL_RAIDUS",
        oid="f6796152-251d-478a-9798-a896e01df943",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("29.732"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ELLIPSE_VERTICAL_RAIDUS",
        oid="f6796152-251d-478a-9798-a896e01df943",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("20.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_GROUP_ANGLE",
        oid="ba914d10-05e5-4053-b4e5-2a2b7b2cda1b",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_VISIBLITY",
        oid="4b2f53a9-b65e-4b24-8b8f-6df72b39b59d",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("true"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_INDEX",
        oid="3de2c577-12b4-45e9-9849-5ccc3e84e488",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("1"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_X",
        oid="9a786fe3-5233-45c0-9da8-7777e64e98ab",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("102.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_Y",
        oid="c32d3dcc-48aa-45e8-9b6b-fcff2316cdfe",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("33.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_SCALEX",
        oid="5ebfb71c-5df0-4363-bf52-8b2c66fef7e8",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("1.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_SCALEY",
        oid="1b8b5504-fb8b-44d5-964d-59c536f87b87",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("1.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_COND_ANGLE",
        oid="d0227c68-ef7f-49e8-82b2-792a590c2997",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRANSLATE_FUNCTIONAL",
        oid="fe9846cb-fa73-496e-902b-51b95e4d736a",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("77.338997"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FUNCTIONAL",
        oid="427344c3-3037-448d-bcb1-cd44763b293f",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("178.253006"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRAN_FILTER_FIRST",
        oid="2cfe29cc-8048-4ff3-a037-03c389ad73d5",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRAN_FILTER_SECOND",
        oid="7aadb91f-c287-4de9-9f20-f4332e87045f",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRAN_FILTER_FIRST2",
        oid="fad14579-2e9a-4a81-a6eb-ac27b4553c95",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[171.0,-149.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRAN_FILTER_SECOND2",
        oid="180229af-93b7-4422-8173-8da839afa9df",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[340.0,-168.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRAN_FILTER_X",
        oid="8a1093ed-88f0-4148-b11d-97a45cdaa029",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("102.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_TRAN_FILTER_Y",
        oid="528f24a6-d7cf-4624-9679-b8b1fdd752fa",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("33.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FILTER_S",
        oid="12f4a9a4-c367-4374-aa20-4efb9d2edce4",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("96.071999"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FILTER_E",
        oid="99c35dfb-4346-4d34-a902-251ab010e760",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("403.089996"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FILTER_S1",
        oid="cd43a400-1753-4c31-a2d6-30ad6a2ab1d1",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("96.071999"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FILTER_E1",
        oid="1322459d-6e31-40b3-8184-e3c04ae716bc",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("403.089996"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FILTER_X",
        oid="4538dc23-a621-4c1a-974d-884c91e11a0d",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("102.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ROTATE_FILTER_Y",
        oid="7a5ba75b-8635-4002-ab8b-ebdce9c94221",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("33.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="TextArea_Value",
        oid="067aaaf0-4859-4bf8-a009-27cc314c4a1b",
        representation=SDY.Representation.AS_STRING,
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.CHAR), SDY.LiteralExpr("255")),
        init=SDY.parse_expr("[0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="CursorPosRequest",
        oid="6900d2f7-c80b-4397-b14b-c54b58e521c9",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ImportCode_Input_a",
        oid="70ea03ae-ace6-4c09-b30a-b1c2dd767854",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ImportCode_Input_b",
        oid="bd29f38a-db56-47ea-8394-d80f804b5773",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ImportCode_Input_c",
        oid="866c36f8-f1c0-4ae5-bca4-13ffcb409422",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ImportCode_Input_d",
        oid="b32ee924-17da-45db-be18-36617d2fdffe",
        representation=SDY.Representation.AS_INT_ARRAY,
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.CHAR), SDY.LiteralExpr("255")),
        init=SDY.parse_expr("[0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_Assignment_Input",
        oid="29d2ca5b-13c8-4c3c-8b1d-0d0ecf7a06a6",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_ARC_GRADIENT_ID",
        oid="d1a66336-a1ea-4226-b697-b5fa93e0a1a8",
        representation=SDY.Representation.GRADIENT,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_CIRCLE_GRADIENT_ID",
        oid="fb83cedc-4dd5-4f15-b15f-ca0b6c04d460",
        representation=SDY.Representation.GRADIENT,
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("2"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_VISIBILITY",
        oid="38ec0005-a725-486a-a7ef-cf2de83c269c",
        type=SDY.PredefType(SDY.SimpleType.BOOL),
        init=SDY.LiteralExpr("false"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_POINT0",
        oid="de3aaa0e-bc5c-4089-b3ca-3005e00d3009",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[-6.0,-280.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_POINT1",
        oid="d2bd777d-f2eb-49c8-8fdd-b15de1dd4283",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[0.0,-326.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_POINT2",
        oid="f7c6f381-1d11-4850-ab6a-8ae9bfc046ab",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[48.0,-315.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_POINT2_CC1",
        oid="8185f42c-0fc4-4a8e-99f2-f66333580b06",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[11.0,-277.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_POINT2_CC2",
        oid="f20e55f6-4ddc-4031-9dfb-99167929bdc7",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[20.0,-306.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="LAYER1_PATH_POINT3",
        oid="102d7aa0-1fc6-4b63-b3fe-3a9406e9a0ae",
        type=SDY.ArrayType(SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")),
        init=SDY.parse_expr("[42.0,-286.0]"),
    )
)
inputs.append(
    SDY.Variable(
        name="Center",
        oid="aaa2fb23-02fa-4cba-9fdf-c8400680a292",
        type=SDY.NamedType("t_global_real_2"),
        init=SDY.parse_expr("c_t_global_real_2"),
    )
)
inputs.append(
    SDY.Variable(
        name="DGFX_Visiable",
        oid="3e4446cb-a548-41cf-b483-87c80261231e",
        type=SDY.NamedType("t_global_bool"),
        init=SDY.parse_expr("c_t_global_bool"),
    )
)
inputs.append(
    SDY.Variable(
        name="DGFX_LineWidth",
        oid="780acde4-6462-41bc-b980-f60d40475b8d",
        type=SDY.NamedType("t_global_int"),
        init=SDY.parse_expr("c_t_global_int"),
    )
)


outputs = layer.declaration.output
outputs.append(
    SDY.MemVariable(
        name="LAYER1_ImportCode_Output_A",
        memory=SDY.MemVariable("true"),
        oid="88d79873-3caf-4f9c-bd24-755c20326019",
        type=SDY.PredefType(SDY.SimpleType.INT),
        init=SDY.LiteralExpr("0"),
    )
)
outputs.append(
    SDY.MemVariable(
        name="LAYER1_Assignment_Output",
        memory=SDY.MemVariable("true"),
        oid="6607c17f-c066-40f3-a659-b72dc89b88a8",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)


locals = layer.declaration.local
locals.append(
    SDY.MemVariable(
        name="Local_StartAngle",
        memory=SDY.MemVariable("true"),
        oid="fcebca1b-dd96-4854-bd0f-5eec917520ad",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("50.0"),
    )
)


localConstants = layer.declaration.local_constant
localConstants.append(
    SDY.Variable(
        name="Local_EndAngle",
        oid="d50358b7-4855-4f86-8835-017fe10e5b14",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("180.0"),
    )
)


probes = layer.declaration.probe
probes.append(
    SDY.Variable(
        name="obs_radius",
        oid="e6a324f3-4dc1-4e46-a877-81b6be6f13b2",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
probes.append(
    SDY.Variable(
        name="obs_x",
        oid="97c69f19-074a-4704-9296-3303ff9ba743",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)
probes.append(
    SDY.Variable(
        name="obs_y",
        oid="3b2fe12a-4ed3-4aca-9e72-19973d7089f9",
        type=SDY.PredefType(SDY.SimpleType.REAL),
        init=SDY.LiteralExpr("0.0"),
    )
)


group_Primitives = SDY.Container(
    name="group_Primitives",
    oid="37735914-921d-402f-9550-ab8c4f74866c",
    origin=(-278.0, 83.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_Primitives)
arc = SDY.Arc(
    name="arc",
    oid="5bb24283-a332-45b4-8ecd-951d0f7cb1b1",
    center=(-53.411999, 261.0),
    radius=31.321005,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
    start_angle=73.30101,
    end_angle=345.378998,
    clockwise=False,
)
group_Primitives.children.append(arc)
arc = SDY.Arc(
    name="arc",
    oid="3bf8fef3-687c-4bb3-941e-8bf315fc53bd",
    center=(13.0, 265.0),
    radius=30.81901,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
    start_angle=76.759003,
    end_angle=17.986023,
    clockwise=False,
)
group_Primitives.children.append(arc)
circle = SDY.Circle(
    name="circle",
    oid="f68841fe-786b-43c6-905a-1714ddd35c4f",
    center=(-55.0, 184.0),
    radius=29.732002,
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group_Primitives.children.append(circle)
circle = SDY.Circle(
    name="circle",
    oid="30cb3be0-1316-4134-98c9-da135040d5b7",
    center=(15.732, 194.0),
    radius=29.732,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
)
group_Primitives.children.append(circle)
crown = SDY.Crown(
    name="crown",
    oid="d6a75d64-0248-41e4-a693-d3a960326b59",
    center=(-55.715, 107.0),
    radius=29.017002,
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
    start_angle=1.975006,
    end_angle=298.178986,
    clockwise=False,
    thickness=11.441,
)
group_Primitives.children.append(crown)
crown = SDY.Crown(
    name="crown",
    oid="f6705018-bb51-4bfb-815c-c5b4c20502c3",
    center=(13.756001, 112.0),
    radius=32.757011,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
    start_angle=102.338997,
    end_angle=28.071991,
    clockwise=False,
    thickness=13.127,
)
group_Primitives.children.append(crown)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="07bd7e31-9783-447b-bd69-fad280a7199f",
    first_point=(-75.0, 49.0),
    third_point=(-27.0, 12.0),
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group_Primitives.children.append(rectangle)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="e366f5cf-9aec-424b-b6b3-9a2ff37e8f80",
    first_point=(-11.0, 53.0),
    third_point=(41.0, 15.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
)
group_Primitives.children.append(rectangle)
shape = SDY.Shape(
    name="shape",
    oid="9201a821-577e-426a-bfd5-a34715d193f7",
    points=[
        (-63.0, -36.0),
        (-62.0, -72.0),
        (-48.0, -37.0),
        (-3.0, -14.0),
        (-57.0, -18.0),
        (-87.0, -4.0),
    ],
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group_Primitives.children.append(shape)
shape = SDY.Shape(
    name="shape",
    oid="95d9f316-9128-48bb-b7ce-0b01e87dbcb6",
    points=[
        (29.0, -43.0),
        (38.0, -78.0),
        (54.0, -44.0),
        (85.0, -21.0),
        (41.0, -30.0),
        (11.0, -13.0),
    ],
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=17,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
)
group_Primitives.children.append(shape)
line = SDY.Line(
    name="line",
    oid="ab035636-3c6f-400d-aef0-3911214076bf",
    points=[
        (-82.0, -176.0),
        (-74.0, -87.0),
        (-61.0, -155.0),
        (-44.0, -90.0),
        (-39.0, -182.0),
    ],
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
)
group_Primitives.children.append(line)
line = SDY.Line(
    name="line",
    oid="a2594b77-6f74-4499-9f38-6e667a127418",
    points=[
        (-2.0, -162.0),
        (21.0, -97.0),
        (24.0, -161.0),
        (47.0, -106.0),
        (87.0, -87.0),
        (96.0, -149.0),
    ],
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=17,
    outline_opacity=255,
)
group_Primitives.children.append(line)
text = SDY.Text(
    name="text",
    oid="3871c062-095a-4992-8579-c367e7c66f59",
    position=(-70.0, -221.0),
    value=[84, 69, 83, 84, 49, 0],
    haloing=[84, 69, 83, 84, 49, 0],
    halo_color=-1,
    outline_color=14,
    line_width=2,
    font=0,
    horiz_align=SDY.HorizAlignEnum.LEFT,
    vert_align=SDY.VertAlignEnum.BOTTOM,
)
group_Primitives.children.append(text)
text = SDY.Text(
    name="text",
    oid="1b5d7d04-f2ce-4327-ae61-6231ae08d3aa",
    position=(-11.0, -214.0),
    value=[84, 69, 83, 84, 50, 0],
    haloing=[84, 69, 83, 84, 50, 0],
    halo_color=-1,
    outline_color=17,
    line_width=2,
    font=0,
    horiz_align=SDY.HorizAlignEnum.LEFT,
    vert_align=SDY.VertAlignEnum.BOTTOM,
)
group_Primitives.children.append(text)
bifont = SDY.BiFont(
    name="bifont",
    oid="259003df-0b58-41c4-b68c-0fb379ca6b61",
    position=(-72.0, -256.0),
    value=12.12,
    haloing=12.12,
    outline_color=14,
    halo_color=-1,
    first_line_width=2,
    first_font=0,
    second_line_width=2,
    second_font=0,
    horiz_align=SDY.HorizAlignEnum.LEFT,
    vert_align=SDY.VertAlignEnum.BOTTOM,
)
group_Primitives.children.append(bifont)
bifont = SDY.BiFont(
    name="bifont",
    oid="652f66d4-fa47-4497-b2eb-6832d5ff154f",
    position=(-11.0, -248.0),
    value=12.12,
    haloing=12.12,
    outline_color=17,
    halo_color=-1,
    first_line_width=2,
    first_font=0,
    second_line_width=2,
    second_font=0,
    horiz_align=SDY.HorizAlignEnum.LEFT,
    vert_align=SDY.VertAlignEnum.BOTTOM,
)
group_Primitives.children.append(bifont)
bitmap = SDY.Bitmap(
    name="bitmap",
    oid="7c4b65d3-62d8-46b5-b326-d796bf801033",
    position=(-104.0, -434.0),
    texture_id=0,
)
group_Primitives.children.append(bitmap)
textarea = SDY.TextArea(
    name="text area",
    oid="a1621876-bc36-4967-ad6b-00ab3ae1c7fc",
    first_point=(176.0, 195.0),
    third_point=(63.0, 234.0),
    value=[69, 83, 84, 69, 82, 69, 76, 32, 84, 69, 67, 72, 78, 79, 76, 79, 71, 89, 0],
    haloing=[69, 83, 84, 69, 82, 69, 76, 32, 84, 69, 67, 72, 78, 79, 76, 79, 71, 89, 0],
    halo_color=-1,
    outline_color=16,
    line_width=2,
    font=0,
    horiz_align=SDY.HorizAlignEnum.LEFT,
    vert_align=SDY.VertAlignEnum.BOTTOM,
)
group_Primitives.children.append(textarea)
textarea = SDY.TextArea(
    name="text area",
    oid="78f79eac-8618-49ef-9147-a5e1a0d964fa",
    first_point=(180.0, 250.0),
    third_point=(67.0, 289.0),
    value=[69, 83, 84, 69, 82, 69, 76, 32, 84, 69, 67, 72, 78, 79, 76, 79, 71, 89, 0],
    haloing=[69, 83, 84, 69, 82, 69, 76, 32, 84, 69, 67, 72, 78, 79, 76, 79, 71, 89, 0],
    halo_color=-1,
    outline_color=16,
    line_width=2,
    font=0,
    horiz_align=SDY.HorizAlignEnum.LEFT,
    vert_align=SDY.VertAlignEnum.BOTTOM,
)
group_Primitives.children.append(textarea)
arcellipse = SDY.ArcEllipse(
    name="arc ellipse",
    oid="5bb24283-a332-45b4-8ecd-951d0f7cb1b1",
    center=(73.0, 150.0),
    radius=(30.0, 20.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
    start_angle=73.300842,
    end_angle=345.379791,
    clockwise=False,
)
group_Primitives.children.append(arcellipse)
arcellipse = SDY.ArcEllipse(
    name="arc ellipse",
    oid="3bf8fef3-687c-4bb3-941e-8bf315fc53bd",
    center=(132.0, 147.0),
    radius=(30.0, 20.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
    start_angle=76.758926,
    end_angle=35.706688,
    clockwise=False,
)
group_Primitives.children.append(arcellipse)
ellipse = SDY.Ellipse(
    name="ellipse",
    oid="f68841fe-786b-43c6-905a-1714ddd35c4f",
    center=(73.0, 71.0),
    radius=(30.0, 20.0),
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group_Primitives.children.append(ellipse)
ellipse = SDY.Ellipse(
    name="ellipse",
    oid="30cb3be0-1316-4134-98c9-da135040d5b7",
    center=(140.0, 68.0),
    radius=(30.0, 20.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
)
group_Primitives.children.append(ellipse)
path = SDY.Path(
    name="path",
    oid="7ae1bb48-1c84-4c12-a34b-8957a4c49e9b",
    commands=[
        SDY.MoveTo(start_point=(-80.0, -279.0)),
        SDY.LineTo(end_point=(-74.0, -324.0)),
        SDY.CurveTo(
            first_control_point=(-73.0, -299.0),
            second_control_point=(-54.0, -289.0),
            end_point=(-26.0, -314.0),
        ),
        SDY.LineTo(end_point=(-32.0, -285.0)),
    ],
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=33,
    fill_opacity=255,
)
group_Primitives.children.append(path)
path = SDY.Path(
    name="path",
    oid="44bc7bf5-9152-45ad-ad2c-80c8d8e254d8",
    commands=[
        SDY.MoveTo(start_point=(-6.0, -280.0)),
        SDY.LineTo(end_point=(0.0, -326.0)),
        SDY.CurveTo(
            first_control_point=(11.0, -277.0),
            second_control_point=(20.0, -306.0),
            end_point=(48.0, -315.0),
        ),
        SDY.LineTo(end_point=(42.0, -286.0)),
    ],
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=56,
    fill_opacity=255,
)
group_Primitives.children.append(path)
group_Containers = SDY.Container(
    name="group_Containers",
    oid="c009626e-015d-4f84-bd11-b52e19d72eec",
    origin=(228.0, 161.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_Containers)
panelgroup = SDY.PanelContainer(
    name="panel group",
    oid="f2349d99-149f-4411-87e6-5fe013dbe9c2",
    origin=(-331.0, -40.0),
    width=124.0,
    height=42.0,
)
group_Containers.children.append(panelgroup)
circle = SDY.Circle(
    name="circle",
    oid="5d30fd93-1526-4df3-80df-dbc0fbc9e781",
    center=(30.0, -9.0),
    radius=79.649002,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=16,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
)
panelgroup.children.append(circle)
group = SDY.Container(
    name="group",
    oid="1e286aa6-cbfc-40ce-805b-61e77d88ac7a",
    origin=(45.0, 212.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
group_Containers.children.append(group)
arc = SDY.Arc(
    name="arc",
    oid="1b474f9c-5a6e-4ef7-83c3-c9197b1d2c3b",
    center=(-3.0, 1.0),
    radius=40.497005,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=27,
    outline_opacity=196,
    fill_color=46,
    fill_opacity=196,
    start_angle=212.904999,
    end_angle=320.792999,
    clockwise=False,
)
group.children.append(arc)
conditionalgroup = SDY.CondContainer(
    name="conditional group",
    oid="e0b47764-7253-4839-bb05-44e0f923669f",
    origin=(-139.0, 157.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
group_Containers.children.append(conditionalgroup)
circle = SDY.Circle(
    name="circle",
    oid="ab2b9ab4-6e73-4812-8942-43f5e53faf92",
    center=(-35.0, 2.0),
    radius=31.000002,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=27,
    outline_opacity=196,
    fill_color=46,
    fill_opacity=196,
)
conditionalgroup.children.append(circle)
crown = SDY.Crown(
    name="crown",
    oid="fe3cbce2-ffad-4bad-b222-c67aa1f38d4e",
    center=(33.0, 1.0),
    radius=34.0,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=46,
    outline_opacity=196,
    fill_color=27,
    fill_opacity=196,
    start_angle=331.928009,
    end_angle=284.036011,
    clockwise=False,
    thickness=14.235,
)
conditionalgroup.children.append(crown)
translategroup = SDY.TranslationContainer(
    name="translate group",
    oid="dd08c13e-78f6-4e2a-99b4-37fdca8e63da",
    origin=(-55.0, 108.0),
    ref_point=(181.076996, 111.0),
    start_point=(-52.0, 111.0),
    end_point=(117.0, 111.0),
)
group_Containers.children.append(translategroup)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="b7370943-9227-4e02-b93d-f6287624aeec",
    first_point=(2.0, 12.0),
    third_point=(198.0, -3.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=46,
    outline_opacity=196,
    fill_color=27,
    fill_opacity=196,
)
translategroup.children.append(rectangle)
ellipse = SDY.Ellipse(
    name="ellipse",
    oid="845697a8-94f9-4e24-942b-a113fcd333f0",
    center=(67.0, 35.0),
    radius=(67.0, 20.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=27,
    outline_opacity=196,
    fill_color=46,
    fill_opacity=196,
)
translategroup.children.append(ellipse)
rotategroup = SDY.RotationContainer(
    name="rotate group",
    oid="a4531670-d537-4b41-b948-183bcb67175c",
    origin=(75.0, 6.0),
    ref_angle=25.201,
    start_angle=355.020996,
    end_angle=11.952,
    clockwise=False,
)
group_Containers.children.append(rotategroup)
crown = SDY.Crown(
    name="crown",
    oid="6a09482c-21e7-4000-ac2a-772cdc0a931a",
    center=(-3.0, -1.0),
    radius=83.648003,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=46,
    outline_opacity=196,
    fill_color=27,
    fill_opacity=196,
    start_angle=27.790005,
    end_angle=234.462006,
    clockwise=False,
    thickness=12.971,
)
rotategroup.children.append(crown)
shape = SDY.Shape(
    name="shape",
    oid="0702eb5c-ee55-4538-8b4b-729289cb6ac3",
    points=[(-3.0, 3.0), (-45.0, -49.0), (3.0, -1.0)],
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=46,
    outline_opacity=196,
    fill_color=27,
    fill_opacity=196,
)
rotategroup.children.append(shape)
translationfilter = SDY.FilterTranslationContainer(
    name="translation filter",
    oid="0eedb88a-9bda-4d0c-9ecb-b046406e74d8",
    origin=(-105.0, 57.0),
    start_point=(-182.0, 54.0),
    end_point=(-33.0, 53.0),
)
group_Containers.children.append(translationfilter)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="6510197a-a69d-472b-9571-875a854d7782",
    first_point=(-84.0, 25.0),
    third_point=(85.0, 6.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=46,
    outline_opacity=196,
    fill_color=27,
    fill_opacity=196,
)
translationfilter.children.append(rectangle)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="8b7aac74-72ac-4ee3-ad9c-6a53971f88de",
    first_point=(-84.0, -3.0),
    third_point=(85.0, -22.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=26,
    outline_opacity=196,
    fill_color=46,
    fill_opacity=196,
)
translationfilter.children.append(rectangle)
rotationfilter = SDY.FilterRotationContainer(
    name="rotation filter",
    oid="be064be3-e67b-47e9-9073-cc39c8abd51a",
    origin=(-113.0, -33.0),
    start_angle=351.558014,
    end_angle=324.571991,
    clockwise=False,
)
group_Containers.children.append(rotationfilter)
arc = SDY.Arc(
    name="arc",
    oid="7d29f8d7-a9a2-4873-add2-c61e0987b2fd",
    center=(-52.0, 2.0),
    radius=47.264996,
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=17,
    outline_opacity=255,
    fill_color=6,
    fill_opacity=255,
    start_angle=96.071999,
    end_angle=43.089996,
    clockwise=False,
)
rotationfilter.children.append(arc)
arcellipse = SDY.ArcEllipse(
    name="arc ellipse",
    oid="fe4da9e5-8598-427f-90ba-9a24fa09ce8d",
    center=(49.0, -6.0),
    radius=(28.0, 63.0),
    line_width=2,
    line_stipple=0,
    haloing=0,
    halo_color=-1,
    outline_color=17,
    outline_opacity=255,
    fill_color=26,
    fill_opacity=255,
    start_angle=100.490898,
    end_angle=41.634064,
    clockwise=False,
)
rotationfilter.children.append(arcellipse)
group_Masks = SDY.Container(
    name="group_Masks",
    oid="56f60563-ca61-4f17-bd59-a6d0df3b1cf7",
    origin=(89.0, -189.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_Masks)
group = SDY.Container(
    name="group",
    oid="ae77a42e-e206-44c9-8252-d17c14990b4f",
    origin=(-37.0, 48.0),
    scale=(0.5, 0.5),
    angle=0.0,
    clockwise=False,
)
group_Masks.children.append(group)
clipplane = SDY.ClipPlane(
    name="clip plane",
    oid="947e4abb-b9f6-4a47-92b1-8d442c22ebee",
    start_point=(1.0, 28.0),
    angle=309.401001,
    clockwise=False,
)
group.children.append(clipplane)
circle = SDY.Circle(
    name="circle",
    oid="ff99d044-7f8b-4aae-bf54-d3182e016c83",
    center=(-1.0, 2.0),
    radius=49.193001,
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group.children.append(circle)
group = SDY.Container(
    name="group",
    oid="0491f6e5-84bf-4f35-a456-f5059e76c884",
    origin=(76.0, 75.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
group_Masks.children.append(group)
clipbox = SDY.ClipBox(
    name="clip box",
    oid="71c2e3ac-6d35-4e84-8d91-d64a88cfb7d5",
    clip_inside=True,
    first_point=(-69.0, 45.0),
    third_point=(74.0, -40.0),
)
group.children.append(clipbox)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="66c5530c-add5-4506-9e1c-32a4c66c579b",
    first_point=(-105.0, 6.0),
    third_point=(19.0, -61.0),
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group.children.append(rectangle)
group = SDY.Container(
    name="group",
    oid="21ae42f1-2f75-465b-acc9-cb133b0536ee",
    origin=(-50.0, -16.0),
    scale=(0.5, 0.5),
    angle=0.0,
    clockwise=False,
)
group_Masks.children.append(group)
clipbox = SDY.ClipBox(
    name="clip box",
    oid="df7c26d9-d743-486d-80dd-df799f8c5358",
    clip_inside=True,
    first_point=(-91.0, 55.0),
    third_point=(15.0, -38.0),
)
group.children.append(clipbox)
shape = SDY.Shape(
    name="shape",
    oid="0f782d3c-ff36-4f1e-ae0c-85ff5b5937f2",
    points=[
        (-106.0, -51.0),
        (-47.0, 14.0),
        (-25.0, -81.0),
        (6.0, 34.0),
        (61.0, -60.0),
        (94.0, 31.0),
        (34.0, 78.0),
    ],
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group.children.append(shape)
group = SDY.Container(
    name="group",
    oid="676b9bec-98d1-45dd-8fe0-1c63869d1429",
    origin=(60.0, 5.0),
    scale=(0.5, 0.8),
    angle=0.0,
    clockwise=False,
)
group_Masks.children.append(group)
stencil = SDY.Stencil(
    name="stencil",
    oid="f405be23-de67-4d9a-9331-e56a0835dc1f",
    points=[
        (-70.0, 20.0),
        (-49.0, 66.0),
        (51.0, 20.0),
        (50.0, 137.0),
        (97.0, -7.0),
        (108.0, -34.0),
        (75.0, -64.0),
        (-20.0, -51.0),
        (49.0, -18.0),
        (-34.0, -29.0),
        (-173.0, -51.0),
        (-101.0, -3.0),
        (-141.0, 29.0),
    ],
)
group.children.append(stencil)
rectangle = SDY.Rectangle(
    name="rectangle",
    oid="7d6e88a4-16d7-4a31-a684-8029f75903e2",
    first_point=(-178.0, -11.0),
    third_point=(127.0, -63.0),
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group.children.append(rectangle)
group = SDY.Container(
    name="group",
    oid="373386de-1d35-4c65-821c-e2d8d7bf457e",
    origin=(113.0, -23.000004),
    scale=(0.5, 0.8),
    angle=0.0,
    clockwise=False,
)
group_Masks.children.append(group)
maskcontainer = SDY.MaskContainer(
    name="mask container",
    oid="b458a87a-ff60-474c-ac3a-1859682e50e7",
    origin=(0.0, -2.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
group.children.append(maskcontainer)
shape = SDY.Shape(
    name="shape",
    oid="22b1b887-5057-4373-a856-0558a8686f50",
    points=[(2.0, 68.0), (-120.0, 17.0), (-26.0, -79.0), (56.0, -4.0)],
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
maskcontainer.children.append(shape)
circle = SDY.Circle(
    name="circle",
    oid="59690ee3-c7eb-4c13-8344-7370951a8dae",
    center=(-6.0, 6.0),
    radius=70.5762,
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group.children.append(circle)
group = SDY.Container(
    name="group",
    oid="783659da-7798-4acd-9d1e-562dcacc8cbc",
    origin=(38.0, -81.999985),
    scale=(0.5, 0.8),
    angle=0.0,
    clockwise=False,
)
group_Masks.children.append(group)
maskcontainer = SDY.MaskContainer(
    name="mask container",
    oid="53f48498-db05-4613-97b0-15c5dd964aa7",
    origin=(-32.0, -9.25),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
group.children.append(maskcontainer)
shape = SDY.Shape(
    name="shape",
    oid="8c9cc0d6-f389-46c0-a5c0-0eb31987dbe0",
    points=[(-57.0, 51.0), (-33.0, -61.0), (18.0, -40.0), (50.0, 25.0)],
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
maskcontainer.children.append(shape)
circle = SDY.Circle(
    name="circle",
    oid="95bd7f63-c779-4800-abc9-88fa484bbbca",
    center=(-12.0, 5.0),
    radius=48.166378,
    line_width=2,
    line_stipple=2,
    haloing=2,
    halo_color=-1,
    outline_color=14,
    outline_opacity=196,
    fill_color=33,
    fill_opacity=196,
)
group.children.append(circle)
group_Interactors = SDY.Container(
    name="group_Interactors",
    oid="cc5d66fa-1640-4f27-89f9-56c9c6d621d6",
    origin=(230.0, -14.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_Interactors)
rectanglearea = SDY.RectangleArea(
    name="rectangle area",
    oid="fcfd4ed5-eaaa-407d-a1c5-f7a491f2ce9d",
    pointer_id=-1,
    first_point=(-24.0, 17.0),
    third_point=(-60.0, 63.0),
)
group_Interactors.children.append(rectanglearea)
circlearea = SDY.CircleArea(
    name="circle area",
    oid="daaa6a39-5000-4e64-a362-f38ce8917ac2",
    pointer_id=-1,
    center=(0.0, 26.0),
    radius=26.419998,
)
group_Interactors.children.append(circlearea)
shapearea = SDY.ShapeArea(
    name="shape area",
    oid="c91b36d4-7922-4035-bea6-620dec1b684a",
    pointer_id=-1,
    points=[(68.0, 8.0), (60.0, 54.0), (112.0, 52.0), (139.0, 30.0), (106.0, 16.0)],
)
group_Interactors.children.append(shapearea)
keyboardeventlistener = SDY.KeyboardEventListener(
    name="keyboard event listener", oid="607d8e68-6a8f-409e-bab3-0cfa35d7279d", id=0
)
group_Interactors.children.append(keyboardeventlistener)
pointereventlistener = SDY.PointerEventListener(
    name="pointer event listener", oid="5d0a1f9d-e5b0-4b4f-b753-a5df27278590", id=0
)
group_Interactors.children.append(pointereventlistener)
cursorposrequest = SDY.CursorPosRequest(
    name="cursor pos request",
    oid="9e21defe-e1b4-4262-b340-9e92438ec887",
    id=0,
    position=(50.0, 18.0),
)
group_Interactors.children.append(cursorposrequest)
group_References = SDY.Container(
    name="group_References",
    oid="88ee1d90-cefd-4a15-97d8-7382eee4bb14",
    origin=(16.0, -61.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_References)
hook = SDY.Hook(name="hook", oid="8a788f82-3194-43ea-8570-4276ae11dce0", index=-1)
group_References.children.append(hook)
assignment1 = SDY.Assignment(
    name="assignment1", oid="61208e3a-0b63-41ad-86c7-c7e117a5b5fc", input=0.0
)
group_References.children.append(assignment1)
assignment2 = SDY.Assignment(
    name="assignment2", oid="1535c982-6f83-4bef-a03e-daccbd88a360", input=0.0
)
group_References.children.append(assignment2)
group_OtherVariableScope = SDY.Container(
    name="group_OtherVariableScope",
    oid="1f0ea537-616d-4e78-b602-bd3f7a1a808b",
    origin=(-4.0, 193.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_OtherVariableScope)
crown = SDY.Crown(
    name="crown",
    oid="0a6ab3b0-2f52-4c93-acf8-80556e6124b9",
    center=(0.0, 6.0),
    radius=46.861498,
    line_width=4,
    line_stipple=2,
    haloing=2,
    halo_color=76,
    outline_color=36,
    outline_opacity=255,
    fill_color=13,
    fill_opacity=255,
    start_angle=50.194429,
    end_angle=346.551385,
    clockwise=False,
    thickness=13.246025,
)
group_OtherVariableScope.children.append(crown)
group_DGFXVariableUsage = SDY.Container(
    name="group_DGFXVariableUsage",
    oid="cffee8f3-165f-48e8-925c-5c793f7c83ee",
    origin=(6.0, 37.0),
    scale=(1.0, 1.0),
    angle=0.0,
    clockwise=False,
)
layer.children.append(group_DGFXVariableUsage)
circle = SDY.Circle(
    name="circle",
    oid="694c7b09-922b-4780-9aea-ecc80585a7db",
    center=(50.0, 10.0),
    radius=70.384657,
    line_width=0,
    line_stipple=0,
    haloing=0,
    halo_color=76,
    outline_color=14,
    outline_opacity=255,
    fill_color=45,
    fill_opacity=255,
)
group_DGFXVariableUsage.children.append(circle)
output_path = "Outputs/out_specification_1.sgfx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
SDY.save_sgfx(model, output_path)
