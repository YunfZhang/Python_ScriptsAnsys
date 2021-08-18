import os
import sys


#load test environment
try:
    import ENVIRONMENT as ENV
except Exception as e:
    print ("Test Environment not set in 'ENVIRONMENT.py'.")
    print("You can use template 'ENVIRONMENT_Template.py' to do so!")
    raise

#Get the installation path and initial directory of API
api_dir = os.path.join(ENV.SCADE_DIR, "SCADE/APIs/Python/lib")

# NOTE: to get coverage, run "copy_api.py" prior to running the tests
sys.path.append(api_dir)

import scade.model.display as SDY

scalar_type_list = ['int', 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64','wchar','bool','char','real','float32','float64']

defs = SDY.GlobalDefinitions(
    [
        SDY.TypeDefinition(
            name="Test_Array_Float32",
            definition=SDY.ArrayType(
                SDY.PredefType(SDY.SimpleType.FLOAT32), SDY.LiteralExpr("334")
            ),
        ),
        SDY.TypeDefinition(
            name="Test_Struct_Float32",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="Label1", ty=SDY.PredefType(SDY.SimpleType.FLOAT32)
                    ),
                    SDY.StructFieldType(
                        name="Label2", ty=SDY.PredefType(SDY.SimpleType.FLOAT32)
                    ),
                ]
            ),
        ),
    ]
)
for scalar_type in scalar_type_list:
    #define the variable type
    upper_type = f"{scalar_type.upper()}"
    var1 = getattr(SDY.SimpleType,'%s' % upper_type)
    #added array types
    defs.definitions.append(
        SDY.TypeDefinition(
            name=f"T_Array_{scalar_type.capitalize()}",
            definition=SDY.ArrayType(
                SDY.PredefType(var1), SDY.LiteralExpr("334"))
                )
        )
    #added structure types
    # defs.definitions.append(
    #     SDY.TypeDefinition(
    #         name=f"T_Struct_{scalar_type.capitalize()}",
    #         definition=SDY.StructType([
    #             SDY.StructFieldType(
    #                 name="newlabel",
    #                 ty=SDY.PredefType(SDY.SimpleType.FLOAT32)
    #             )

    #         ])
    #     )
    # )
    # definition_struct.fields.append()
    definition_struct = SDY.StructType([])
    for i in range(1,335):
        definition_struct.fields.append(
            SDY.StructFieldType(
                name=f"Label{i}",
                ty=SDY.PredefType(var1)
            )
    )
    defs.definitions.append(
        SDY.TypeDefinition(
            name=f"T_Struct_{scalar_type.capitalize()}",
            definition=definition_struct
        )
    )




output_path = "test2/Perf_dgfx.dgfx"
SDY.save_dgfx(defs, output_path)