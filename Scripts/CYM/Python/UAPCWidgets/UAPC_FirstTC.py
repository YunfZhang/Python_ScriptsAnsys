import os
import scade.model.a661 as UAPC


A661Layer = UAPC.LayerInstance(
    name="a661_layer",
    oid="9cd7fce4-1137-4d68-9799-a2b31205acf2",
    width=15360,
    height=15360,
)
model = UAPC.DefinitionFile(width=768, height=768, ratio=(20, 20), layers=[A661Layer])


BasicContainer_CursorOver = (
    UAPC.WidgetInstance(
        name="BasicContainer_CursorOver",
        oid="93c83da0-108b-402e-b6a0-3cdf22c418cc",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="176")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="1740")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="16920")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround_CursorOver",
                oid="042cbf04-03d8-4315-964b-dfae480746c0",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="177")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3860")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1900")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="2c1ff2f0-2fd3-4d6f-ad00-a227205ed734",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="178")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="1020")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="170")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="610")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="CursorOver"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle_Pos",
                oid="77b51ee8-0caf-4cb4-9bfe-56168507e2b5",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="179")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="9")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="CursorOver",
                oid="a3d0639c-0745-4a71-bb2c-5062c759ae12",
                type=UAPC.A661Widget(name="CursorOver"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PositionReportMode",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_REPORT_ON_TRANSITION")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="6b096cbb-1d37-4cc3-87e0-73a65fe83619",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="181")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1070")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="590")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="CursorPosOverlay"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="CursorPosOverlay",
                oid="8ca40c68-348f-4470-b487-24cde842d76c",
                type=UAPC.A661Widget(name="CursorPosOverlay"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="182")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1040")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="620")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle_Pos",
                oid="d4df383d-d447-487b-8ce8-5910620c8441",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="183")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1040")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="9")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_CursorOver)
BasicContainer_ActiveArea = (
    UAPC.WidgetInstance(
        name="BasicContainer_ActiveArea",
        oid="b186b478-7f45-44b8-92a9-eda4749bd5f7",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="184")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="5960")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="17040")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround_ActiveArea",
                oid="083e3bc2-c858-4cd0-b993-789260d8c721",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="185")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3040")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1740")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="b0d4d96f-8b9f-45ae-b1e6-0ebfc6ee67f5",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="186")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1070")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="ActiveArea"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ActiveArea",
                oid="b20fc321-0bdf-4d4d-afad-b7995e368aca",
                type=UAPC.A661Widget(name="ActiveArea"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="187")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle_Pos",
                oid="af366697-7f77-4f5d-9199-093353b6d499",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="188")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="9")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_ActiveArea)
BasicContainer_MapHorz_MapVert_ItemList = (
    UAPC.WidgetInstance(
        name="BasicContainer_MapHorz_MapVert_ItemList",
        oid="2cdcb8c6-f042-49b1-9e84-910b3d4ca82c",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="189")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="6700")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="6220")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround_MapHorz_MapVert_ItemList",
                oid="63fd43af-b464-4820-891f-ca1483eb4970",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="190")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="10260")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="5060")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="4f28d970-1de0-413e-ba31-f0948bc3f118",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="191")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="1140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="4390")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="MapHorz_ItemList"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="b467767e-7d13-487e-be17-247cfd08e66d",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="192")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="6240")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="4230")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="MapVert_ItemList"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="f5f303d2-ec9f-4043-b968-af629268903c",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="193")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="4000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="MapHorz",
                oid="df1f6bbd-14ba-431b-9cca-ca2260d93d4e",
                type=UAPC.A661Widget(name="MapHorz"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="194")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="4000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ScreenReferencePointX", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ScreenReferencePointY", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Range", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ScreenRange", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ProjectionType", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=[
                    UAPC.WidgetInstance(
                        name="MapHorz_Source",
                        oid="753f837b-559f-4563-b18c-65c9a1e22780",
                        type=UAPC.A661Widget(name="MapHorz_Source"),
                        props=[
                            UAPC.DefinitionAttribute(
                                name="WidgetIdent", value=UAPC.IntPropValue(value="195")
                            ),
                            UAPC.DefinitionAttribute(
                                name="Enable",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="Visible",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="MapDataFormat",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_MDF_DIST_DIST")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="EventFlag",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_VALIDATION")
                                ),
                            ),
                        ],
                        runtime_messages=None,
                        events=None,
                        children=[
                            UAPC.WidgetInstance(
                                name="MapHorz_ItemList_Basic01",
                                oid="29b84bbb-6c6a-4846-bcd8-355a2b73df63",
                                type=UAPC.A661Widget(name="MapHorz_ItemList"),
                                props=[
                                    UAPC.DefinitionAttribute(
                                        name="WidgetIdent",
                                        value=UAPC.IntPropValue(value="196"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Enable",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Visible",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="MaxNumberOfItem",
                                        value=UAPC.IntPropValue(value="25"),
                                    ),
                                ],
                                runtime_messages=None,
                                events=None,
                                children=None,
                            )
                        ],
                    )
                ],
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="8f39dfda-aadf-42a3-a664-0e9375edc65a",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="197")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="5200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="4000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="MapVert",
                oid="011d81b7-0dc7-41ad-8644-4087fa3779ca",
                type=UAPC.A661Widget(name="MapVert"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="198")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="5200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="4000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RangeX", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RangeY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RefPosX", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RefPosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RefGeoPosX", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RefGeoPosY", value=UAPC.IntPropValue(value="100")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=[
                    UAPC.WidgetInstance(
                        name="MapVert_Source",
                        oid="6c954ff7-3668-4d32-a049-3f692e388cc1",
                        type=UAPC.A661Widget(name="MapVert_Source"),
                        props=[
                            UAPC.DefinitionAttribute(
                                name="WidgetIdent", value=UAPC.IntPropValue(value="199")
                            ),
                            UAPC.DefinitionAttribute(
                                name="Enable",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="Visible",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="MapDataFormatX",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_MDF_ABSOLUTE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="MapDataFormatY",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_MDF_ABSOLUTE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="EventFlag",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                        ],
                        runtime_messages=None,
                        events=None,
                        children=[
                            UAPC.WidgetInstance(
                                name="MapVert_ItemList_Basic01",
                                oid="f07c063f-6848-41e1-b54c-5c26725d2b74",
                                type=UAPC.A661Widget(name="MapVert_ItemList"),
                                props=[
                                    UAPC.DefinitionAttribute(
                                        name="WidgetIdent",
                                        value=UAPC.IntPropValue(value="200"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Enable",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Visible",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="MaxNumberOfItem",
                                        value=UAPC.IntPropValue(value="25"),
                                    ),
                                ],
                                runtime_messages=None,
                                events=None,
                                children=None,
                            )
                        ],
                    )
                ],
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_MapHorz_MapVert_ItemList)
BasicContainer_Buttons = (
    UAPC.WidgetInstance(
        name="BasicContainer_Buttons",
        oid="60ef796f-dfd1-4d52-ad85-ff8dac424f85",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="201")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="10040")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="14733")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround_Buttons",
                oid="f2b4ffb4-6d61-4ec5-8669-9763bb1af070",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="202")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-2340")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="7300")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="6447")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="PushButton_Basic01",
                oid="d73aeaee-1a5b-49d1-86da-70042b3ec5c2",
                type=UAPC.A661Widget(name="PushButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="203")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="3480")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1840")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3440")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="PushButton"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="PicturePushButton_Basic01",
                oid="6b3e1d85-2509-44f8-b84e-4cf6e01ad782",
                type=UAPC.A661Widget(name="PicturePushButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="204")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="820")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5400")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="112")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="PicturePushButton"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ToggleButton",
                oid="72325d0c-618e-467a-92fd-ba6de1b0a269",
                type=UAPC.A661Widget(name="ToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="205")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1827")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3260")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="ToggleButton"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="LabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="SymbolPushButton_Basic01",
                oid="a2afdb9c-b830-4c2f-9bef-1cd251cd75d6",
                type=UAPC.A661Widget(name="SymbolPushButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="206")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="135")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolPosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="SymbolPushButton"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="SymbolToggleButton",
                oid="0223fdec-edf8-4bd1-8cca-4b6aaef589f5",
                type=UAPC.A661Widget(name="SymbolToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="207")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-1180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateSymbolReference",
                        value=UAPC.IntPropValue(value="1"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolPosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="SymbolToggleButton"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="PictureToggleButton",
                oid="925c1c5b-5f9e-44f6-94bf-d8ade6b71feb",
                type=UAPC.A661Widget(name="PictureToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="208")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-2173")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5520")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternatePictureReference",
                        value=UAPC.IntPropValue(value="1"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="PictureToggleButton"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="e0333de6-ee73-45c3-99cd-370bb527daf4",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="209")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="2927")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3480")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="CheckButton"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_Buttons)
BasicContainer_Symbol = (
    UAPC.WidgetInstance(
        name="BasicContainer_Symbol",
        oid="6c7c39fe-47e3-4298-bee4-187058e5a796",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="210")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="1760")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="14260")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround_Symbol",
                oid="f58cb541-51e0-4f17-a6a3-52b4b8cd1f89",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="211")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="60")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3740")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="798c91db-09af-4159-ba03-2c63d7a6daf9",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="212")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1560")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="SymbolAnimated"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="7f21fb4b-701d-46aa-aec0-43ce6818a435",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="213")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1020")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="Symbol")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Symbol",
                oid="5a301ca4-211b-4aa7-9c08-2a69bd60b6c1",
                type=UAPC.A661Widget(name="Symbol"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="214")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="1640")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Symbol",
                oid="eda168ab-dfc7-4d09-83a9-fbea83760bce",
                type=UAPC.A661Widget(name="Symbol"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="215")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="2520")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="740")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolReference", value=UAPC.IntPropValue(value="2")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Symbol",
                oid="4bdffb1e-5c90-494e-95fa-73de3bbd484a",
                type=UAPC.A661Widget(name="Symbol"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="216")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="3360")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="740")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="2")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolReference", value=UAPC.IntPropValue(value="2")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="SymbolAnimated",
                oid="2c42e906-f3c3-4573-826f-af614301aecd",
                type=UAPC.A661Widget(name="SymbolAnimated"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="217")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="720")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="660")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LoopType",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LOOP_FORWARD_AND_RESET")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfSymbols", value=UAPC.IntPropValue(value="3")
                    ),
                    UAPC.DefinitionAttribute(
                        name="IndexOfFrequency", value=UAPC.IntPropValue(value="10")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AnimationType",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RUN")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="1"),
                                UAPC.IntPropValue(value="2"),
                                UAPC.IntPropValue(value="3"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="OrientationArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MovementXArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MovementYArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_Symbol)
BasicContainer_EditBox = (
    UAPC.WidgetInstance(
        name="BasicContainer_EditBox",
        oid="0fd17093-86e2-40f0-857b-4e8f73b15fcd",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="218")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="5660")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="13940")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround_EditBox",
                oid="723656ab-6d7b-409a-ab3a-6528ff1104c3",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="219")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-2580")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="5580")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="EditBoxText",
                oid="1179d9c9-fbfa-40f0-b3d6-aa478295d6a4",
                type=UAPC.A661Widget(name="EditBoxText"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="2100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartCursorPos", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ReportAllChanges",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_EDB_CHANGE_CONFIRMED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="EditBoxText"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="4bbe84fc-ac2c-466f-8866-ce133f936746",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="221")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="EditBoxNumeric"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="EditBoxNumeric",
                oid="a2f0fabe-c6c0-45f3-9632-fc2afbd455a0",
                type=UAPC.A661Widget(name="EditBoxNumeric"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="222")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="720")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Value", value=UAPC.FloatPropValue(value="0.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="TicsCoarse", value=UAPC.FloatPropValue(value="10.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="TicsFine", value=UAPC.FloatPropValue(value="0.1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MinValue", value=UAPC.FloatPropValue(value="0.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxValue", value=UAPC.FloatPropValue(value="100.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendAreaSizeX", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartCursorPosByte", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxFormatStringLength",
                        value=UAPC.IntPropValue(value="16"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxLegendStringLength",
                        value=UAPC.IntPropValue(value="16"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendPosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ReportAllChanges",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_EDB_CHANGE_CONFIRMED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendRemoved",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumericKeyFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="CyclicFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FormatString", value=UAPC.StringPropValue(value="+___.##")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendString", value=UAPC.StringPropValue(value="LD")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="EditBoxMasked",
                oid="fa77d874-02bd-4324-a554-d1e17065013a",
                type=UAPC.A661Widget(name="EditBoxMasked"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="223")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3320")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlphaMask", value=UAPC.IntPropValue(value="4294967295")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumericMask", value=UAPC.IntPropValue(value="4294967295")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartCursorPos", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ReportAllChanges",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_EDB_CHANGE_CONFIRMED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="EditBoxMasked"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="EditBoxMultiLine",
                oid="c9bea751-aaed-4329-96d5-0ad9df15d638",
                type=UAPC.A661Widget(name="EditBoxMultiLine"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="224")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-1160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartCursorPos", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ReportAllChanges",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_EDB_CHANGE_CONFIRMED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="VerticalScroll",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="EditBoxMultiLine"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="7b41eb19-1386-419e-9ae0-e3e8414652cb",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="225")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-1800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="EditBoxNumericBCD"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="EditBoxNumericBCD",
                oid="fd4d9d0d-11e8-40aa-8771-052db2ca3bfd",
                type=UAPC.A661Widget(name="EditBoxNumericBCD"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="226")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-2500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="5000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendAreaSizeX", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Value",
                        value=UAPC.ArrayPropValue(
                            [UAPC.IntPropValue(value="0"), UAPC.IntPropValue(value="0")]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MinValue",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="4051261785"),
                                UAPC.IntPropValue(value="2576941056"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxValue",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="293601280"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MinFieldsValues",
                        value=UAPC.ArrayPropValue(
                            [UAPC.IntPropValue(value="0"), UAPC.IntPropValue(value="0")]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxFieldsValues",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="25188697"),
                                UAPC.IntPropValue(value="2576941056"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="TicsCoarse",
                        value=UAPC.ArrayPropValue(
                            [UAPC.IntPropValue(value="1"), UAPC.IntPropValue(value="0")]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="TicsFine",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="5242880"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfFields", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendPosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendRemoved",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxFormatStringLength",
                        value=UAPC.IntPropValue(value="32"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxLegendStringLength",
                        value=UAPC.IntPropValue(value="16"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PositiveStringLength", value=UAPC.IntPropValue(value="16")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NegativeStringLength", value=UAPC.IntPropValue(value="16")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ReportAllChanges",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_EDB_CHANGE_CONFIRMED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumericKeyFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="CyclicFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeOfFields",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="3"),
                                UAPC.IntPropValue(value="2"),
                                UAPC.IntPropValue(value="2"),
                                UAPC.IntPropValue(value="4"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FormatString",
                        value=UAPC.StringPropValue(value="###d##&apos;##.####&quot;+"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LegendString", value=UAPC.StringPropValue(value="LD")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PositiveString", value=UAPC.StringPropValue(value="E")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NegativeString", value=UAPC.StringPropValue(value="W")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_EditBox)
BasicContainer_Combo = (
    UAPC.WidgetInstance(
        name="BasicContainer_Combo",
        oid="ab39ae1a-9cf8-4a41-8ed7-f21a25e7e614",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="227")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="1720")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="11980")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="1014f093-8061-4115-a465-8df3546aa01c",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="228")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3860")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1900")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ComboBox",
                oid="b2660136-f895-49d7-a56a-9f7ddacf8d4f",
                type=UAPC.A661Widget(name="ComboBox"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="229")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="520")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectingAreaWidth", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectingAreaHeight",
                        value=UAPC.IntPropValue(value="4900"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxNumberOfEntries", value=UAPC.IntPropValue(value="16")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfEntries", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectedEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningMode",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_OPEN_DOWN")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="EntryList",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.StringPropValue(value="ComboBox1"),
                                UAPC.StringPropValue(value="ComboBox2"),
                                UAPC.StringPropValue(value="ComboBox3"),
                                UAPC.StringPropValue(value="ComboBox4"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ComboBoxEdit",
                oid="fc34a48d-28ea-4539-b3b5-122bea3e3ae6",
                type=UAPC.A661Widget(name="ComboBoxEdit"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="230")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="60")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="740")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectingAreaWidth", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectingAreaHeight",
                        value=UAPC.IntPropValue(value="4900"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxNumberOfEntries", value=UAPC.IntPropValue(value="16")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfEntries", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectedEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningMode",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_OPEN_DOWN")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartCursorPos", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ReportAllChanges",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_EDB_CHANGE_CONFIRMED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="EntryList",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.StringPropValue(value="ComboBoxEdit1"),
                                UAPC.StringPropValue(value="ComboBoxEdit2"),
                                UAPC.StringPropValue(value="ComboBoxEdit3"),
                                UAPC.StringPropValue(value="ComboBoxEdit4"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_Combo)
BasicContainer_Gp = (
    UAPC.WidgetInstance(
        name="BasicContainer_Gp",
        oid="d0e2b4f8-cdd1-48bf-b211-8c57f2306590",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="231")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="1780")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="5220")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="53233a88-2d8e-4ec6-bb07-23a16466597a",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="232")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="4820")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="5980")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpArcCircle",
                oid="0bcbe217-ae84-47e5-99ae-c58165ef1702",
                type=UAPC.A661Widget(name="GpArcCircle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="233")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="2760")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="3920")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="EndAngle", value=UAPC.IntPropValue(value="1073741824")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Radius", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpArcEllipse",
                oid="d7a1a1c0-740a-4179-b96d-7ac27a4e2b7d",
                type=UAPC.A661Widget(name="GpArcEllipse"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="234")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="5020")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="EndAngle", value=UAPC.IntPropValue(value="1073741824")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpCrown",
                oid="f27fb7c8-1198-43fd-ac2a-5430463c0017",
                type=UAPC.A661Widget(name="GpCrown"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="235")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="3180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="EndAngle", value=UAPC.IntPropValue(value="1073741824")
                    ),
                    UAPC.DefinitionAttribute(
                        name="InnerRadius", value=UAPC.IntPropValue(value="1500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OuterRadius", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpLine",
                oid="684273f0-23d4-4eb1-8388-c3ea4e71b269",
                type=UAPC.A661Widget(name="GpLine"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="236")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosXStart", value=UAPC.IntPropValue(value="3140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosYStart", value=UAPC.IntPropValue(value="2660")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosXEnd", value=UAPC.IntPropValue(value="4140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosYEnd", value=UAPC.IntPropValue(value="3660")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpLinePolar",
                oid="c59f1889-218e-4876-a970-835f58c62906",
                type=UAPC.A661Widget(name="GpLinePolar"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="237")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosXStart", value=UAPC.IntPropValue(value="140")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosYStart", value=UAPC.IntPropValue(value="2780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="312962560")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LineLength", value=UAPC.IntPropValue(value="1806")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpTriangle",
                oid="31654147-2509-4727-9929-b5b3379950af",
                type=UAPC.A661Widget(name="GpTriangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="238")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="3500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX2", value=UAPC.IntPropValue(value="4100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY2", value=UAPC.IntPropValue(value="2800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX3", value=UAPC.IntPropValue(value="4700")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY3", value=UAPC.IntPropValue(value="1800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="2931fc31-f708-4150-93f3-1d4ced4150da",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="239")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1640")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="LabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="LabelComplex",
                oid="c6516cda-82ef-4c32-8a24-172ec3db5163",
                type=UAPC.A661Widget(name="LabelComplex"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="240")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="180")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1060")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="DefaultStyleText",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="LabelComplex"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Picture",
                oid="7f5e208e-d78b-4486-9f7e-3a865dba204b",
                type=UAPC.A661Widget(name="Picture"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="241")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="3680")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="260")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureReference", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="PictureAnimated",
                oid="cf17fd4e-adfc-4f47-ab28-485b9ac31b5a",
                type=UAPC.A661Widget(name="PictureAnimated"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="242")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="2460")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfPictures", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="IndexOfFrequency", value=UAPC.IntPropValue(value="10")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LoopFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AnimationFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="11"),
                                UAPC.IntPropValue(value="12"),
                                UAPC.IntPropValue(value="13"),
                                UAPC.IntPropValue(value="14"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_Gp)
BasicContainer_MapGrid = (
    UAPC.WidgetInstance(
        name="BasicContainer_MapGrid",
        oid="c2b01d80-1768-4a82-8289-0d3a3247a17b",
        type=UAPC.A661Widget(name="BasicContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="243")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="11380")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="16080")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="Label",
                oid="359d184d-aa43-4111-991d-247383e0c050",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="244")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="1020")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="2120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="1880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="640")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="MapGrid")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="9e9de41d-015b-4d92-948d-26e04ac4f98b",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="245")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="60")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="MapHorz",
                oid="ccbb2b22-bb67-414f-af21-b8e757bbb887",
                type=UAPC.A661Widget(name="MapHorz"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="246")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="60")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ScreenReferencePointX",
                        value=UAPC.IntPropValue(value="400"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ScreenReferencePointY",
                        value=UAPC.IntPropValue(value="400"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Range", value=UAPC.IntPropValue(value="6553600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ScreenRange", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ProjectionType", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=[
                    UAPC.WidgetInstance(
                        name="MapHorz_Source",
                        oid="d33b83db-9d47-4b98-a38c-758722f92327",
                        type=UAPC.A661Widget(name="MapHorz_Source"),
                        props=[
                            UAPC.DefinitionAttribute(
                                name="WidgetIdent", value=UAPC.IntPropValue(value="247")
                            ),
                            UAPC.DefinitionAttribute(
                                name="Enable",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="Visible",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="MapDataFormat",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_MDF_DIST_DIST")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="EventFlag",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_VALIDATION")
                                ),
                            ),
                        ],
                        runtime_messages=None,
                        events=None,
                        children=[
                            UAPC.WidgetInstance(
                                name="MapGrid_Basic01",
                                oid="4cb46d60-54d2-43cf-a16c-c1928000186e",
                                type=UAPC.A661Widget(name="MapGrid"),
                                props=[
                                    UAPC.DefinitionAttribute(
                                        name="WidgetIdent",
                                        value=UAPC.IntPropValue(value="248"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Visible",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="OffsetX",
                                        value=UAPC.FloatPropValue(value="0.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="OffsetY",
                                        value=UAPC.FloatPropValue(value="0.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="IncrementX",
                                        value=UAPC.FloatPropValue(value="100.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="IncrementY",
                                        value=UAPC.FloatPropValue(value="100.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="CountX",
                                        value=UAPC.IntPropValue(value="64"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="CountY",
                                        value=UAPC.IntPropValue(value="64"),
                                    ),
                                ],
                                runtime_messages=None,
                                events=None,
                                children=None,
                            ),
                            UAPC.WidgetInstance(
                                name="MapGrid_Basic02",
                                oid="95df8238-a72b-416b-a926-e08feac29c07",
                                type=UAPC.A661Widget(name="MapGrid"),
                                props=[
                                    UAPC.DefinitionAttribute(
                                        name="WidgetIdent",
                                        value=UAPC.IntPropValue(value="249"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Visible",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="OffsetX",
                                        value=UAPC.FloatPropValue(value="0.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="OffsetY",
                                        value=UAPC.FloatPropValue(value="0.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="IncrementX",
                                        value=UAPC.FloatPropValue(value="100.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="IncrementY",
                                        value=UAPC.FloatPropValue(value="100.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="CountX",
                                        value=UAPC.IntPropValue(value="64"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="CountY",
                                        value=UAPC.IntPropValue(value="64"),
                                    ),
                                ],
                                runtime_messages=None,
                                events=None,
                                children=None,
                            ),
                            UAPC.WidgetInstance(
                                name="MapGrid_Basic03",
                                oid="57bdead4-4c86-4e9e-817c-7736574d29e9",
                                type=UAPC.A661Widget(name="MapGrid"),
                                props=[
                                    UAPC.DefinitionAttribute(
                                        name="WidgetIdent",
                                        value=UAPC.IntPropValue(value="250"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="Visible",
                                        value=UAPC.EnumPropValue(
                                            value=UAPC.A661Constant(name="A661_TRUE")
                                        ),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="OffsetX",
                                        value=UAPC.FloatPropValue(value="0.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="OffsetY",
                                        value=UAPC.FloatPropValue(value="0.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="IncrementX",
                                        value=UAPC.FloatPropValue(value="100.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="IncrementY",
                                        value=UAPC.FloatPropValue(value="100.0"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="CountX",
                                        value=UAPC.IntPropValue(value="64"),
                                    ),
                                    UAPC.DefinitionAttribute(
                                        name="CountY",
                                        value=UAPC.IntPropValue(value="64"),
                                    ),
                                ],
                                runtime_messages=None,
                                events=None,
                                children=None,
                            ),
                        ],
                    )
                ],
            ),
        ],
    ),
)
A661Layer.children.append(BasicContainer_MapGrid)
BlinkingContainer = (
    UAPC.WidgetInstance(
        name="BlinkingContainer",
        oid="9ae4b7e6-97f4-4359-acd6-0ff1c5abb815",
        type=UAPC.A661Widget(name="BlinkingContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="251")
            ),
            UAPC.DefinitionAttribute(
                name="BlinkingType", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="f60e096a-d45e-4d8c-a244-e08a656ddf85",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="252")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="2040")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="16580")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="4380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="78c2b069-998c-4161-bd57-fe6c131fc2fa",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="253")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="2160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="18040")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="BlinkingContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Symbol",
                oid="ab2334ed-8a54-4913-a098-53493c970d87",
                type=UAPC.A661Widget(name="Symbol"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="254")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="4500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="17220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SymbolReference", value=UAPC.IntPropValue(value="10")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(BlinkingContainer)
RotationContainer = (
    UAPC.WidgetInstance(
        name="RotationContainer",
        oid="179b2e6a-aa21-417b-9fdd-c670c8c85bba",
        type=UAPC.A661Widget(name="RotationContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="255")
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="CenterX", value=UAPC.IntPropValue(value="6400")
            ),
            UAPC.DefinitionAttribute(
                name="CenterY", value=UAPC.IntPropValue(value="3640")
            ),
            UAPC.DefinitionAttribute(
                name="RotationAngle", value=UAPC.IntPropValue(value="0")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="4103d86d-e6e5-44c6-b92b-dae249f7bf5a",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="256")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="6720")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="16500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="4380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="096aa232-b2a5-403b-b210-f9a62a476df3",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="257")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="6840")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="17960")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="RotationContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpCrown",
                oid="c255374a-36b8-4ca7-b27f-face6b4a532c",
                type=UAPC.A661Widget(name="GpCrown"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="258")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="10120")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="17220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="EndAngle", value=UAPC.IntPropValue(value="1119270656")
                    ),
                    UAPC.DefinitionAttribute(
                        name="InnerRadius", value=UAPC.IntPropValue(value="490")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OuterRadius", value=UAPC.IntPropValue(value="880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(RotationContainer)
TranslationContainer = (
    UAPC.WidgetInstance(
        name="TranslationContainer",
        oid="5b270ad8-f7bd-43f5-8389-8bf3ded687da",
        type=UAPC.A661Widget(name="TranslationContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="259")
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="TranslationX", value=UAPC.IntPropValue(value="1980")
            ),
            UAPC.DefinitionAttribute(
                name="TranslationY", value=UAPC.IntPropValue(value="13940")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="0f50f294-3bd5-4f9d-938a-34835162a0ab",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="260")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="4380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="fae93a2c-b442-4e07-8aa8-10a8d18d8959",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="261")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="4200")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="560")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="TranslationContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="38384baf-aba9-4ec2-814f-719629a1cdef",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="262")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="1600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="660")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(TranslationContainer)
MaskContainer = (
    UAPC.WidgetInstance(
        name="MaskContainer",
        oid="563e0709-f7ee-4afe-8583-4540a9688ce8",
        type=UAPC.A661Widget(name="MaskContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="263")
            ),
            UAPC.DefinitionAttribute(
                name="MaskEnabled",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="7100")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="14140")
            ),
            UAPC.DefinitionAttribute(
                name="MaskReference", value=UAPC.IntPropValue(value="1")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="9d3a9305-bd91-4f40-a6e2-0e21e1ba5f29",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="264")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2940")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1840")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="3b4d7e81-1f37-4320-9440-34efb918ac40",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="265")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1060")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="560")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="MaskContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="6429c210-16a5-4458-af6b-803a9a21af3f",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="266")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(MaskContainer)
MutuallyExclusiveContainer = (
    UAPC.WidgetInstance(
        name="MutuallyExclusiveContainer",
        oid="78e1b8d9-2c80-4356-ba6b-de8fbf12e566",
        type=UAPC.A661Widget(name="MutuallyExclusiveContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="267")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="11040")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="14900")
            ),
            UAPC.DefinitionAttribute(
                name="VisibleChild", value=UAPC.IntPropValue(value="268")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="ToggleButton",
                oid="018cdfbb-2846-4ffd-9783-7f38376404c6",
                type=UAPC.A661Widget(name="ToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="268")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-940")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="6460")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="760")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="MutuallyExclusiveContainer"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ToggleButton",
                oid="cc0ea133-2858-45a5-8d87-f16fe97752e3",
                type=UAPC.A661Widget(name="ToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="269")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="MutuallyExclusive2"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ToggleButton",
                oid="e6d2709b-b543-4d9e-a9ba-5efc20ba375d",
                type=UAPC.A661Widget(name="ToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="270")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="MutuallyExclusive3"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(MutuallyExclusiveContainer)
Panel = (
    UAPC.WidgetInstance(
        name="Panel",
        oid="a2b2d35f-e5f3-4662-9824-c2ba7b985573",
        type=UAPC.A661Widget(name="Panel"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="271")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="1960")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="10780")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="100")
            ),
            UAPC.DefinitionAttribute(
                name="MotionAllowed",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="30441863-317d-41df-b242-dde2986d800a",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="272")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2580")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="cbe7d814-62b2-4d67-80b2-0327d4c1f4de",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="273")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="1960")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="640")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="Panel")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="d325e296-54b6-404d-a880-821d6083aa64",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="274")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="820")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(Panel)
PopUpPanel = (
    UAPC.WidgetInstance(
        name="PopUpPanel",
        oid="d1fd986d-ae7d-4b96-9f61-1410ad1b8302",
        type=UAPC.A661Widget(name="PopUpPanel"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="275")
            ),
            UAPC.DefinitionAttribute(
                name="UAPositionFlag",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="AutomaticClosure",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_FALSE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="5420")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="10800")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="21")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="68cd4147-5fe5-4e06-8624-9bcb43a8810f",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="276")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="500")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2580")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="1880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="76aec9f8-c918-495e-b1ea-6e36e78136a1",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="277")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1560")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="1960")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="640")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="PopUpPanel"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpRectangle",
                oid="f61eba7c-594e-4b57-bd83-f5504d2ef9d5",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="278")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="780")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="600")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(PopUpPanel)
PopUpPanelButton = (
    UAPC.WidgetInstance(
        name="PopUpPanelButton",
        oid="5723a1a6-57bc-4e13-b2bd-2178fc35befe",
        type=UAPC.A661Widget(name="PopUpPanelButton"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="279")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="9320")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="12620")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="5620")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="1580")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="110")
            ),
            UAPC.DefinitionAttribute(
                name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="PopupPosX", value=UAPC.IntPropValue(value="9320")
            ),
            UAPC.DefinitionAttribute(
                name="PopupPosY", value=UAPC.IntPropValue(value="13320")
            ),
            UAPC.DefinitionAttribute(
                name="PopupSizeX", value=UAPC.IntPropValue(value="5400")
            ),
            UAPC.DefinitionAttribute(
                name="PopupSizeY", value=UAPC.IntPropValue(value="2640")
            ),
            UAPC.DefinitionAttribute(
                name="MaxStringLength", value=UAPC.IntPropValue(value="32")
            ),
            UAPC.DefinitionAttribute(
                name="PictureReference", value=UAPC.IntPropValue(value="1")
            ),
            UAPC.DefinitionAttribute(
                name="PicturePosition",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_RIGHT")),
            ),
            UAPC.DefinitionAttribute(
                name="Alignment",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_LEFT")),
            ),
            UAPC.DefinitionAttribute(
                name="UAPositionFlag",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="AutomaticClosure",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_FALSE")),
            ),
            UAPC.DefinitionAttribute(
                name="LabelString", value=UAPC.StringPropValue(value="PopUpPanelButton")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="BackGround",
                oid="0c4ce70f-d9d0-4d68-a6ce-7ded900d1c3d",
                type=UAPC.A661Widget(name="GpRectangle"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="280")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-320")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="4380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="2160")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="21")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="621dee5a-316f-4afb-9a00-c9c8431c0a9a",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="281")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="860")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3540")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="630")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="34")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="PopUpPanelButton"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="GpCrown",
                oid="c3d95f0b-2d8e-438a-8356-151ea1ec8434",
                type=UAPC.A661Widget(name="GpCrown"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="282")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="2380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StartAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="EndAngle", value=UAPC.IntPropValue(value="1119270656")
                    ),
                    UAPC.DefinitionAttribute(
                        name="InnerRadius", value=UAPC.IntPropValue(value="490")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OuterRadius", value=UAPC.IntPropValue(value="880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Filled",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FillIndex", value=UAPC.IntPropValue(value="74")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Halo",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(PopUpPanelButton)
ScrollPanel = (
    UAPC.WidgetInstance(
        name="ScrollPanel",
        oid="76e1ec6e-4a83-4375-8562-f3abcca760c3",
        type=UAPC.A661Widget(name="ScrollPanel"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="283")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="1820")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="3620")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="5080")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="6860")
            ),
            UAPC.DefinitionAttribute(
                name="LineDeltaX", value=UAPC.IntPropValue(value="100")
            ),
            UAPC.DefinitionAttribute(
                name="LineDeltaY", value=UAPC.IntPropValue(value="100")
            ),
            UAPC.DefinitionAttribute(
                name="PageDeltaX", value=UAPC.IntPropValue(value="500")
            ),
            UAPC.DefinitionAttribute(
                name="PageDeltaY", value=UAPC.IntPropValue(value="500")
            ),
            UAPC.DefinitionAttribute(name="HomeX", value=UAPC.IntPropValue(value="0")),
            UAPC.DefinitionAttribute(name="HomeY", value=UAPC.IntPropValue(value="0")),
            UAPC.DefinitionAttribute(
                name="FrameX", value=UAPC.IntPropValue(value="200")
            ),
            UAPC.DefinitionAttribute(
                name="FrameY", value=UAPC.IntPropValue(value="200")
            ),
            UAPC.DefinitionAttribute(
                name="SizeXsheet", value=UAPC.IntPropValue(value="10000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeYsheet", value=UAPC.IntPropValue(value="10000")
            ),
            UAPC.DefinitionAttribute(name="BoundX", value=UAPC.IntPropValue(value="0")),
            UAPC.DefinitionAttribute(name="BoundY", value=UAPC.IntPropValue(value="0")),
            UAPC.DefinitionAttribute(
                name="SizeXbound", value=UAPC.IntPropValue(value="10000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeYbound", value=UAPC.IntPropValue(value="10000")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="110")
            ),
            UAPC.DefinitionAttribute(
                name="HorizontalScroll",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TOP")),
            ),
            UAPC.DefinitionAttribute(
                name="VerticalScroll",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_RIGHT")),
            ),
            UAPC.DefinitionAttribute(
                name="FlagReportFramePos",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_FALSE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="Slider",
                oid="82f3a66e-e1bd-4625-aabb-a245cf6b9317",
                type=UAPC.A661Widget(name="Slider"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="284")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="4920")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MinValue", value=UAPC.FloatPropValue(value="0.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxValue", value=UAPC.FloatPropValue(value="100.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Value", value=UAPC.FloatPropValue(value="0.0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MajorTickInterval",
                        value=UAPC.FloatPropValue(value="20.0"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="ShowMajorLabels",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Orientation",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT_TO_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LsbMultiple", value=UAPC.IntPropValue(value="5")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MinorTickMultiple", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MajorTickReference",
                        value=UAPC.FloatPropValue(value="0.0"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="SelectionListButton",
                oid="23652d53-69bb-4683-95e9-c6823f226826",
                type=UAPC.A661Widget(name="SelectionListButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="285")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="580")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="3460")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectingAreaWidth", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectingAreaHeight",
                        value=UAPC.IntPropValue(value="4900"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxNumberOfEntries", value=UAPC.IntPropValue(value="16")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfEntries", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectedEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningMode",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_OPEN_DOWN")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="Selection"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="EntryList",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.StringPropValue(value="Entry1"),
                                UAPC.StringPropValue(value="Entry2"),
                                UAPC.StringPropValue(value="Entry3"),
                                UAPC.StringPropValue(value="Entry4"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ScrollList",
                oid="859641c5-8c0d-439a-a31f-ef167e0cfd97",
                type=UAPC.A661Widget(name="ScrollList"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="286")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="440")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="-40")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="4900")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxNumberOfEntries", value=UAPC.IntPropValue(value="16")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfEntries", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SelectedEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="FirstAccessibleEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="FirstVisibleEntry", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="VerticalScroll",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="FlagReportVisibleEntry",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="DefaultStyleText",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="EnableArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelStringArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.StringPropValue(value="Entry1"),
                                UAPC.StringPropValue(value="Entry2"),
                                UAPC.StringPropValue(value="Entry3"),
                                UAPC.StringPropValue(value="Entry4"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(ScrollPanel)
BufferFormat = (
    UAPC.WidgetInstance(
        name="BufferFormat",
        oid="c2c68e91-00fe-4bf4-a4f9-9a438a31458c",
        type=UAPC.A661Widget(name="BufferFormat"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="287")
            ),
            UAPC.DefinitionAttribute(
                name="NumberOfFields", value=UAPC.IntPropValue(value="1")
            ),
            UAPC.DefinitionAttribute(
                name="BufferStructure",
                value=UAPC.ArrayPropValue(
                    [
                        UAPC.StructPropValue(
                            [
                                UAPC.DefinitionAttribute(
                                    name="WidgetIdent",
                                    value=UAPC.IntPropValue(value="283"),
                                ),
                                UAPC.DefinitionAttribute(
                                    name="ParameterIdent",
                                    value=UAPC.EnumPropValue(
                                        value=UAPC.A661Constant(name="A661_ENABLE")
                                    ),
                                ),
                            ]
                        )
                    ]
                ),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(BufferFormat)
Connector = (
    UAPC.WidgetInstance(
        name="Connector",
        oid="f59673c4-7734-4d98-929b-13374c650c5a",
        type=UAPC.A661Widget(name="Connector"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="288")
            ),
            UAPC.DefinitionAttribute(
                name="ConnectorReference", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(Connector)
CursorRef = (
    UAPC.WidgetInstance(
        name="CursorRef",
        oid="eae294d5-b7b6-48eb-b193-4a1f7f0a7eba",
        type=UAPC.A661Widget(name="CursorRef"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="289")
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="11440")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="8660")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(CursorRef)
ExternalSource = (
    UAPC.WidgetInstance(
        name="ExternalSource",
        oid="20883142-5de6-4895-a2b7-c7b208902822",
        type=UAPC.A661Widget(name="ExternalSource"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="290")
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="5440")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="12660")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="800")
            ),
            UAPC.DefinitionAttribute(
                name="SourceReference", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="SourceX", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="SourceY", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="SourceDX", value=UAPC.IntPropValue(value="500")
            ),
            UAPC.DefinitionAttribute(
                name="SourceDY", value=UAPC.IntPropValue(value="300")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="1")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(ExternalSource)
FocusIn = (
    UAPC.WidgetInstance(
        name="FocusIn",
        oid="2e3b1618-4934-44c0-bb8b-14f90c1db5d1",
        type=UAPC.A661Widget(name="FocusIn"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="291")
            ),
            UAPC.DefinitionAttribute(
                name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(FocusIn)
FocusOut = (
    UAPC.WidgetInstance(
        name="FocusOut",
        oid="05539369-7d68-42ef-831f-c057cc4650d5",
        type=UAPC.A661Widget(name="FocusOut"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="292")
            ),
            UAPC.DefinitionAttribute(
                name="NextFocusInAppId", value=UAPC.IntPropValue(value="1")
            ),
            UAPC.DefinitionAttribute(
                name="NextFocusInLayerId", value=UAPC.IntPropValue(value="1")
            ),
            UAPC.DefinitionAttribute(
                name="NextFocusInId", value=UAPC.IntPropValue(value="0")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(FocusOut)
ProxyButton = (
    UAPC.WidgetInstance(
        name="ProxyButton",
        oid="f5941ecc-e3f2-48f9-afc1-6c9361a13617",
        type=UAPC.A661Widget(name="ProxyButton"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="293")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="DedicatedKeyIdent", value=UAPC.IntPropValue(value="8")
            ),
            UAPC.DefinitionAttribute(
                name="TargetWidgetIdent", value=UAPC.IntPropValue(value="283")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=None,
    ),
)
A661Layer.children.append(ProxyButton)
RadioBox = (
    UAPC.WidgetInstance(
        name="RadioBox",
        oid="508d7ee5-7b15-4e72-b4ea-973820270043",
        type=UAPC.A661Widget(name="RadioBox"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="294")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="a2043315-671a-4e7a-a72b-aac5b93ca331",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="295")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="11880")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="11380")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="RadioBox")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="44bd2909-a0ca-4761-9a60-1e133d15f738",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="296")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="11900")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="10720")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="RadioBox")
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(RadioBox)
WatchdogContainer = (
    UAPC.WidgetInstance(
        name="WatchdogContainer",
        oid="1c02afcd-a9f3-4022-8a10-3b0813e306fd",
        type=UAPC.A661Widget(name="WatchdogContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="297")
            ),
            UAPC.DefinitionAttribute(
                name="TimePeriod", value=UAPC.IntPropValue(value="10")
            ),
            UAPC.DefinitionAttribute(
                name="ValidCountLimit", value=UAPC.IntPropValue(value="100")
            ),
            UAPC.DefinitionAttribute(
                name="FailCountLimit", value=UAPC.IntPropValue(value="80")
            ),
            UAPC.DefinitionAttribute(
                name="Refresh", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="ShowIfFailIdent", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="ShowFail",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_FALSE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="PopUpMenu",
                oid="13fb9252-3c3d-4298-84da-20426dedca2c",
                type=UAPC.A661Widget(name="PopUpMenu"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="298")
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningMode",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_OPEN_UP")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfEntries", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="7060")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="7700")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="4900")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PopUpIdentArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="EnableArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StringArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.StringPropValue(value="Entry1"),
                                UAPC.StringPropValue(value="Entry2"),
                                UAPC.StringPropValue(value="Entry3"),
                                UAPC.StringPropValue(value="Entry4"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="PopUpMenuButton",
                oid="f6bbef09-649b-488f-9a51-e227bd436b57",
                type=UAPC.A661Widget(name="PopUpMenuButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="299")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="9720")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="8520")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3680")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="740")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PopupPosX", value=UAPC.IntPropValue(value="9720")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PopupPosY", value=UAPC.IntPropValue(value="9220")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PopupSizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PopupSizeY", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLengthPopUp", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NumberOfEntries", value=UAPC.IntPropValue(value="4")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_RIGHT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="OpeningMode",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_OPEN_UP")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="PopUpMenuButton"),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PopUpIdentArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                                UAPC.IntPropValue(value="0"),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="EnableArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                                UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ]
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StringArray",
                        value=UAPC.ArrayPropValue(
                            [
                                UAPC.StringPropValue(value="Entry1"),
                                UAPC.StringPropValue(value="Entry2"),
                                UAPC.StringPropValue(value="Entry3"),
                                UAPC.StringPropValue(value="Entry4"),
                            ]
                        ),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="Label",
                oid="2e99b3e4-3ae6-41b5-a69e-c3c72566db26",
                type=UAPC.A661Widget(name="Label"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="300")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Anonymous",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="8080")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="10480")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="RotationAngle", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MotionAllowed",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Font", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ColorIndex", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="WatchdogContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(WatchdogContainer)
MenuBar = (
    UAPC.WidgetInstance(
        name="MenuBar",
        oid="ff39cc40-fcc6-4143-9b51-e721b0bf9654",
        type=UAPC.A661Widget(name="MenuBar"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="301")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Horizontal",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="8160")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="6920")
            ),
            UAPC.DefinitionAttribute(
                name="ButtonPos", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="ButtonSize", value=UAPC.IntPropValue(value="800")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="ToggleButton",
                oid="bdb86b9e-3e6e-41c1-acf1-41823d8f42ae",
                type=UAPC.A661Widget(name="ToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="302")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="360")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="2060")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="660")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="MenuBar")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="ToggleButton",
                oid="37d1041e-2d6f-4151-82bd-c12b978931be",
                type=UAPC.A661Widget(name="ToggleButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="303")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="1980")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="60")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="1960")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="820")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="110")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="ToggleState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateFlag",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString", value=UAPC.StringPropValue(value="MenuBar")
                    ),
                    UAPC.DefinitionAttribute(
                        name="AlternateLabelString",
                        value=UAPC.StringPropValue(value="AlternateLabelString"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(MenuBar)
SizeToFitContainer = (
    UAPC.WidgetInstance(
        name="SizeToFitContainer",
        oid="283ba5e7-fa5c-4031-8c46-9a04f7b3acea",
        type=UAPC.A661Widget(name="SizeToFitContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="304")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="7340")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="5320")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="3540")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="1160")
            ),
            UAPC.DefinitionAttribute(
                name="NumberOfVisibleChildren", value=UAPC.IntPropValue(value="3")
            ),
            UAPC.DefinitionAttribute(
                name="SizeToFitMode",
                value=UAPC.EnumPropValue(
                    value=UAPC.A661Constant(name="A661_SIZE_TOP_DOWN")
                ),
            ),
            UAPC.DefinitionAttribute(
                name="ItemSpacing", value=UAPC.IntPropValue(value="100")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="670b1a87-5ed7-4aef-8444-589bd15f9c34",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="305")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="SizeToFitContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="d563c815-ddb1-4826-afe5-c1ca7a965f76",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="306")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="-20")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="80")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="SizeToFitContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(SizeToFitContainer)
ShuffleToFitContainer = (
    UAPC.WidgetInstance(
        name="ShuffleToFitContainer",
        oid="14ca3213-b727-4333-96df-46b928e7be80",
        type=UAPC.A661Widget(name="ShuffleToFitContainer"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="307")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="13420")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="7520")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="800")
            ),
            UAPC.DefinitionAttribute(
                name="NumberOfVisibleChildren", value=UAPC.IntPropValue(value="3")
            ),
            UAPC.DefinitionAttribute(
                name="ShuffleToFitMode",
                value=UAPC.EnumPropValue(
                    value=UAPC.A661Constant(name="A661_SHUFFLE_UP")
                ),
            ),
            UAPC.DefinitionAttribute(
                name="ItemSpacing", value=UAPC.IntPropValue(value="100")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="1")
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="cc28fcd0-5669-4fa1-81fa-c20f5a6576f3",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="308")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="10800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1460")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="ShuffleToFitContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
            UAPC.WidgetInstance(
                name="CheckButton",
                oid="a6787ba6-2dda-4819-805d-486ab595f7fc",
                type=UAPC.A661Widget(name="CheckButton"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="309")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosX", value=UAPC.IntPropValue(value="10800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PosY", value=UAPC.IntPropValue(value="1460")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeX", value=UAPC.IntPropValue(value="3000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="SizeY", value=UAPC.IntPropValue(value="800")
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="50")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="CheckButtonState",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_UNSELECTED")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="ShuffleToFitContainer"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=None,
            ),
        ],
    ),
)
A661Layer.children.append(ShuffleToFitContainer)
TabbedPanelGroup = (
    UAPC.WidgetInstance(
        name="TabbedPanelGroup",
        oid="436dce2f-2303-4b00-8937-f5ff81e06a7b",
        type=UAPC.A661Widget(name="TabbedPanelGroup"),
        props=[
            UAPC.DefinitionAttribute(
                name="WidgetIdent", value=UAPC.IntPropValue(value="310")
            ),
            UAPC.DefinitionAttribute(
                name="Enable",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="Visible",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
            UAPC.DefinitionAttribute(
                name="PosX", value=UAPC.IntPropValue(value="11420")
            ),
            UAPC.DefinitionAttribute(
                name="PosY", value=UAPC.IntPropValue(value="2740")
            ),
            UAPC.DefinitionAttribute(
                name="SizeX", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="SizeY", value=UAPC.IntPropValue(value="3000")
            ),
            UAPC.DefinitionAttribute(
                name="StyleSet", value=UAPC.IntPropValue(value="0")
            ),
            UAPC.DefinitionAttribute(
                name="ActiveTabbedPanelID", value=UAPC.IntPropValue(value="311")
            ),
            UAPC.DefinitionAttribute(
                name="TabPosition",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TOP")),
            ),
            UAPC.DefinitionAttribute(
                name="AutomaticInsetSizeFlag",
                value=UAPC.EnumPropValue(value=UAPC.A661Constant(name="A661_TRUE")),
            ),
        ],
        runtime_messages=None,
        events=None,
        children=[
            UAPC.WidgetInstance(
                name="TabbedPanel",
                oid="ae83f51f-7b6f-4f48-8a4c-36de6349afbb",
                type=UAPC.A661Widget(name="TabbedPanel"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="311")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_CENTER")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="InsetSize", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="TabbedPanel"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=[
                    UAPC.WidgetInstance(
                        name="Symbol",
                        oid="2002da69-e3ea-402a-bda4-cf3aa42b8ff7",
                        type=UAPC.A661Widget(name="Symbol"),
                        props=[
                            UAPC.DefinitionAttribute(
                                name="WidgetIdent", value=UAPC.IntPropValue(value="312")
                            ),
                            UAPC.DefinitionAttribute(
                                name="MotionAllowed",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="Visible",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="PosX", value=UAPC.IntPropValue(value="600")
                            ),
                            UAPC.DefinitionAttribute(
                                name="PosY", value=UAPC.IntPropValue(value="1000")
                            ),
                            UAPC.DefinitionAttribute(
                                name="RotationAngle", value=UAPC.IntPropValue(value="0")
                            ),
                            UAPC.DefinitionAttribute(
                                name="StyleSet", value=UAPC.IntPropValue(value="1")
                            ),
                            UAPC.DefinitionAttribute(
                                name="SymbolReference",
                                value=UAPC.IntPropValue(value="1"),
                            ),
                            UAPC.DefinitionAttribute(
                                name="ColorIndex", value=UAPC.IntPropValue(value="1")
                            ),
                        ],
                        runtime_messages=None,
                        events=None,
                        children=None,
                    )
                ],
            ),
            UAPC.WidgetInstance(
                name="TabbedPanel",
                oid="2f05eafb-49ff-41ec-9122-d83d7de484db",
                type=UAPC.A661Widget(name="TabbedPanel"),
                props=[
                    UAPC.DefinitionAttribute(
                        name="WidgetIdent", value=UAPC.IntPropValue(value="313")
                    ),
                    UAPC.DefinitionAttribute(
                        name="Enable",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Visible",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_TRUE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="StyleSet", value=UAPC.IntPropValue(value="100")
                    ),
                    UAPC.DefinitionAttribute(
                        name="NextFocusedWidget", value=UAPC.IntPropValue(value="0")
                    ),
                    UAPC.DefinitionAttribute(
                        name="MaxStringLength", value=UAPC.IntPropValue(value="32")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PictureReference", value=UAPC.IntPropValue(value="1")
                    ),
                    UAPC.DefinitionAttribute(
                        name="PicturePosition",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_CENTER")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="AutomaticFocusMotion",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_FALSE")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="Alignment",
                        value=UAPC.EnumPropValue(
                            value=UAPC.A661Constant(name="A661_LEFT")
                        ),
                    ),
                    UAPC.DefinitionAttribute(
                        name="InsetSize", value=UAPC.IntPropValue(value="1000")
                    ),
                    UAPC.DefinitionAttribute(
                        name="LabelString",
                        value=UAPC.StringPropValue(value="TabbedPanel"),
                    ),
                ],
                runtime_messages=None,
                events=None,
                children=[
                    UAPC.WidgetInstance(
                        name="Symbol",
                        oid="41734906-887f-4e99-b4c3-451fabcb0809",
                        type=UAPC.A661Widget(name="Symbol"),
                        props=[
                            UAPC.DefinitionAttribute(
                                name="WidgetIdent", value=UAPC.IntPropValue(value="314")
                            ),
                            UAPC.DefinitionAttribute(
                                name="MotionAllowed",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="Visible",
                                value=UAPC.EnumPropValue(
                                    value=UAPC.A661Constant(name="A661_TRUE")
                                ),
                            ),
                            UAPC.DefinitionAttribute(
                                name="PosX", value=UAPC.IntPropValue(value="600")
                            ),
                            UAPC.DefinitionAttribute(
                                name="PosY", value=UAPC.IntPropValue(value="1200")
                            ),
                            UAPC.DefinitionAttribute(
                                name="RotationAngle", value=UAPC.IntPropValue(value="0")
                            ),
                            UAPC.DefinitionAttribute(
                                name="StyleSet", value=UAPC.IntPropValue(value="1")
                            ),
                            UAPC.DefinitionAttribute(
                                name="SymbolReference",
                                value=UAPC.IntPropValue(value="1"),
                            ),
                            UAPC.DefinitionAttribute(
                                name="ColorIndex", value=UAPC.IntPropValue(value="1")
                            ),
                        ],
                        runtime_messages=None,
                        events=None,
                        children=None,
                    )
                ],
            ),
        ],
    ),
)
A661Layer.children.append(TabbedPanelGroup)
output_path = "Outputs/out_uapc_1.sgfx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
UAPC.save_sgfx(model, output_path)
