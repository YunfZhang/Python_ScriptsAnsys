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


defs = SDY.GlobalDefinitions(
    [
        SDY.TypeDefinition(
            name="U_Basic_Uint32",
            oid="82666019-6eff-44a6-8832-e3d00b4b4af4",
            definition=SDY.PredefType(SDY.SimpleType.UINT32),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Uint16",
            oid="a1eb7d7f-fb77-47bd-b266-a2053b9dd5a7",
            definition=SDY.PredefType(SDY.SimpleType.UINT16),
        ),
        SDY.TypeDefinition(
            name="t_global_int",
            oid="f2bc3ce1-714e-4786-9812-046898b0774d",
            definition=SDY.PredefType(SDY.SimpleType.INT),
        ),
        SDY.TypeDefinition(
            name="Enum_1",
            oid="b66949ad-0a75-4982-ad23-81af811acab2",
            definition=SDY.EnumType(
                enums=[
                    SDY.EnumValue(name="E1_1: 1"),
                    SDY.EnumValue(name="E1_2: 2"),
                    SDY.EnumValue(name="E1_3: 3"),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Bool",
            oid="a59be367-2cc4-4284-aecd-5def0a47e4cc",
            definition=SDY.PredefType(SDY.SimpleType.BOOL),
        ),
        SDY.TypeDefinition(
            name="Array_1",
            oid="aea6d886-164e-48e3-8390-36d9bcb436df",
            definition=SDY.ArrayType(
                SDY.PredefType(SDY.SimpleType.FLOAT32), SDY.LiteralExpr("2^3")
            ),
        ),
        SDY.TypeDefinition(
            name="Struct_1",
            oid="fa65ec6c-158c-403c-b1c2-1663430453e5",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="S1", ty=SDY.PredefType(SDY.SimpleType.INT)
                    ),
                    SDY.StructFieldType(
                        name="S2", ty=SDY.PredefType(SDY.SimpleType.INT8)
                    ),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Int64",
            oid="b5dc6415-ac16-4358-a105-244b67454300",
            definition=SDY.PredefType(SDY.SimpleType.INT64),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Int8",
            oid="35d08ab1-8466-4c34-b454-d8380eba7bec",
            definition=SDY.PredefType(SDY.SimpleType.INT8),
        ),
        SDY.TypeDefinition(
            name="t_global_bool",
            oid="7c133fc6-1998-4270-bbb2-58d158078aaa",
            definition=SDY.PredefType(SDY.SimpleType.BOOL),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Uint64",
            oid="52af53ee-e22a-44be-ae1a-9b4d0ea48062",
            definition=SDY.PredefType(SDY.SimpleType.UINT64),
        ),
        SDY.TypeDefinition(
            name="NewType_3",
            oid="aa4c9d65-9441-474e-a68a-373cd9fc0088",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="label", ty=SDY.PredefType(SDY.SimpleType.BOOL)
                    )
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="NewType_4",
            oid="89782ae3-345f-4cc0-b7d2-128f4c440ad7",
            definition=SDY.EnumType(enums=[SDY.EnumValue(name="value_3")]),
        ),
        SDY.TypeDefinition(
            name="t_global_real_2",
            oid="0c57466d-e720-4366-a7eb-91da17d0dbfa",
            definition=SDY.ArrayType(
                SDY.PredefType(SDY.SimpleType.REAL), SDY.LiteralExpr("2")
            ),
        ),
        SDY.TypeDefinition(
            name="NewType_1",
            oid="862e15d9-9d20-4847-9bdd-37c316ff54d9",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="label", ty=SDY.PredefType(SDY.SimpleType.BOOL)
                    ),
                    SDY.StructFieldType(
                        name="label_1", ty=SDY.PredefType(SDY.SimpleType.BOOL)
                    ),
                    SDY.StructFieldType(
                        name="label_2", ty=SDY.NamedType("t_global_real_2")
                    ),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Char",
            oid="bcb206c5-a9c8-46a2-81b9-f568f32af00b",
            definition=SDY.PredefType(SDY.SimpleType.CHAR),
        ),
        SDY.TypeDefinition(
            name="Basic_1",
            oid="ba6c394c-9ee5-47b2-8386-d97cd4e8afe1",
            definition=SDY.PredefType(SDY.SimpleType.INT64),
        ),
        SDY.TypeDefinition(
            name="NewType_2",
            oid="229383d0-b9f4-46fe-8e0d-098d26195ac5",
            definition=SDY.ImportedType(name="MyImportedType_int"),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Real",
            oid="484e5e69-1567-4f1a-8c45-746917be272b",
            definition=SDY.PredefType(SDY.SimpleType.REAL),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Float32",
            oid="8905006a-bb4a-47c7-a1e4-dff5ad6ab580",
            definition=SDY.PredefType(SDY.SimpleType.FLOAT32),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Int",
            oid="6ecc0a9e-7911-482a-93c9-fe841a8eee4d",
            definition=SDY.PredefType(SDY.SimpleType.INT),
        ),
        SDY.TypeDefinition(
            name="T_Combination_1",
            oid="8e4c34cc-d7e0-44f2-b5c9-b0b38cc51c8a",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="CS_1", ty=SDY.PredefType(SDY.SimpleType.BOOL)
                    ),
                    SDY.StructFieldType(name="CS_2", ty=SDY.NamedType("Basic_1")),
                    SDY.StructFieldType(name="CS_3", ty=SDY.NamedType("Array_1")),
                    SDY.StructFieldType(name="CS_4", ty=SDY.NamedType("Enum_1")),
                    SDY.StructFieldType(name="CS_6", ty=SDY.NamedType("Struct_1")),
                    SDY.StructFieldType(
                        name="CS_7",
                        ty=SDY.ArrayType(
                            SDY.PredefType(SDY.SimpleType.INT),
                            SDY.LiteralExpr("S_Int_9^2"),
                        ),
                    ),
                    SDY.StructFieldType(
                        name="CS_8",
                        ty=SDY.StructType(
                            [
                                SDY.StructFieldType(
                                    name="AS_8_1",
                                    ty=SDY.PredefType(SDY.SimpleType.REAL),
                                )
                            ]
                        ),
                    ),
                    SDY.StructFieldType(
                        name="AS_8_2",
                        ty=SDY.ArrayType(
                            SDY.PredefType(SDY.SimpleType.UINT8), SDY.LiteralExpr("3")
                        ),
                    ),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="NewType_test",
            oid="db6fcfdd-46f3-460b-b248-e7e5fd57756f",
            definition=SDY.EnumType(
                enums=[
                    SDY.EnumValue(name="value"),
                    SDY.EnumValue(name="value_1"),
                    SDY.EnumValue(name="value_2"),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Float64",
            oid="0ed40a89-22ae-44c0-90fe-254e956eaa1e",
            definition=SDY.PredefType(SDY.SimpleType.FLOAT64),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Uint8",
            oid="c7b43f91-34c9-4a02-9c92-09257e95ff34",
            definition=SDY.PredefType(SDY.SimpleType.UINT8),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Int16",
            oid="cfbcdc21-4b85-4ac3-a266-e9828ced41b3",
            definition=SDY.PredefType(SDY.SimpleType.INT16),
        ),
        SDY.TypeDefinition(
            name="NewType_1_1",
            oid="e88490ca-2c76-43f2-aec8-b02224768fd6",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="label", ty=SDY.PredefType(SDY.SimpleType.INT)
                    ),
                    SDY.StructFieldType(
                        name="label_1", ty=SDY.PredefType(SDY.SimpleType.REAL)
                    ),
                    SDY.StructFieldType(
                        name="label_2",
                        ty=SDY.ArrayType(
                            SDY.PredefType(SDY.SimpleType.INT), SDY.LiteralExpr("2")
                        ),
                    ),
                    SDY.StructFieldType(
                        name="label_3",
                        ty=SDY.ArrayType(
                            SDY.PredefType(SDY.SimpleType.FLOAT32),
                            SDY.LiteralExpr("2^5"),
                        ),
                    ),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="NewType_5",
            oid="9ba89631-df81-4fd6-8f4a-65cbb4b2009b",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="label",
                        ty=SDY.StructType(
                            [
                                SDY.StructFieldType(
                                    name="label", ty=SDY.NamedType("NewType_1")
                                )
                            ]
                        ),
                    )
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Wchar",
            oid="588735d1-a568-43be-9876-56cef6379579",
            definition=SDY.PredefType(SDY.SimpleType.WCHAR),
        ),
        SDY.TypeDefinition(
            name="U_Basic_Int32",
            oid="c0e5162c-807b-4f16-8b3b-cd48f0454fad",
            definition=SDY.PredefType(SDY.SimpleType.INT32),
        ),
        SDY.TypeDefinition(
            name="Int2",
            oid="c31d5d0e-e413-4fa2-b9e8-2b5f27915f66",
            definition=SDY.ArrayType(
                SDY.PredefType(SDY.SimpleType.INT), SDY.LiteralExpr("2")
            ),
        ),
        SDY.TypeDefinition(
            name="Struct2",
            oid="e55206be-f7bd-4083-9924-122b5684569d",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="l1", ty=SDY.PredefType(SDY.SimpleType.REAL)
                    ),
                    SDY.StructFieldType(
                        name="l2", ty=SDY.PredefType(SDY.SimpleType.INT)
                    ),
                ]
            ),
        ),
        SDY.TypeDefinition(
            name="Str_Array",
            oid="75b4e4b6-c94e-42b6-aefc-9922b9e4d4a0",
            definition=SDY.StructType(
                [
                    SDY.StructFieldType(
                        name="l1",
                        ty=SDY.StructType(
                            [
                                SDY.StructFieldType(
                                    name="l2", ty=SDY.NamedType("Struct2")
                                ),
                                SDY.StructFieldType(
                                    name="l7", ty=SDY.PredefType(SDY.SimpleType.INT)
                                ),
                            ]
                        ),
                    ),
                    SDY.StructFieldType(name="l3", ty=SDY.NamedType("Int2")),
                    SDY.StructFieldType(
                        name="l4",
                        ty=SDY.StructType(
                            [
                                SDY.StructFieldType(name="l5", ty=SDY.NamedType("Int2")),
                                SDY.StructFieldType(name="l8", ty=SDY.NamedType("Int2")),
                            ]
                        ),
                    ),
                    SDY.StructFieldType(name="l6", ty=SDY.PredefType(SDY.SimpleType.BOOL)),
                ]
            ),
        ),
        SDY.ConstantDefinition(
            name="S_Int_9",
            oid="5a09a5ed-39e1-40fa-92c4-6028cc826990",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.LiteralExpr("9"),
        ),
        SDY.ConstantDefinition(
            name="S_Bool_False",
            oid="eaa18a09-8a3c-43b2-890b-493b5da62aee",
            type=SDY.PredefType(SDY.SimpleType.BOOL),
            definition=SDY.LiteralExpr("false"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Int16_6",
            oid="d3dea5ec-be99-42c3-8741-f94fa0a9ea72",
            type=SDY.NamedType("U_Basic_Int16"),
            definition=SDY.LiteralExpr("6"),
        ),
        SDY.ConstantDefinition(
            name="S_Wchar_98",
            oid="35540eda-41a3-491b-b2bd-37421a7b3c73",
            type=SDY.PredefType(SDY.SimpleType.WCHAR),
            definition=SDY.LiteralExpr("98"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Int_27",
            oid="ad536ddc-c1d9-44cb-a616-fe43455598bc",
            type=SDY.NamedType("U_Basic_Int"),
            definition=SDY.LiteralExpr("27"),
        ),
        SDY.ConstantDefinition(
            name="S_Uint16_6",
            oid="32f07d2b-c03f-4cd4-b569-cfafc09227ef",
            type=SDY.PredefType(SDY.SimpleType.UINT16),
            definition=SDY.LiteralExpr("6"),
        ),
        SDY.ConstantDefinition(
            name="c_t_global_real_2",
            oid="6625103a-71a8-4c24-8326-d541d74942d3",
            type=SDY.NamedType("t_global_real_2"),
            definition=SDY.parse_expr("[50.0, 10.0]"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Int8_8",
            oid="e9c153fa-da6a-46f4-bd68-52babbc4f615",
            type=SDY.NamedType("U_Basic_Int8"),
            definition=SDY.LiteralExpr("8"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Uint32_2",
            oid="c8e01616-9987-40fb-86f3-aa0cc5444343",
            type=SDY.NamedType("U_Basic_Uint32"),
            definition=SDY.LiteralExpr("2"),
        ),
        SDY.ConstantDefinition(
            name="S_Int_Ne24_Expr",
            oid="eaa18a09-8a3c-43b2-890b-493b5da62aee",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.parse_expr("(6 - 30)"),
        ),
        SDY.ConstantDefinition(
            name="c_t_global_bool",
            oid="8b6b5d14-02af-4f35-a816-6648f44ac5dd",
            type=SDY.NamedType("t_global_bool"),
            definition=SDY.LiteralExpr("true"),
        ),
        SDY.ConstantDefinition(
            name="S_Char_97",
            oid="d8a4f312-6bb0-4673-bb1b-e668703cd4e3",
            type=SDY.PredefType(SDY.SimpleType.CHAR),
            definition=SDY.LiteralExpr("97"),
        ),
        SDY.ConstantDefinition(
            name="S_Int_2",
            oid="c19b362d-0ae2-43aa-9221-2224f4823118",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.LiteralExpr("2"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Float32_32",
            oid="7010db74-fa7f-4f13-8c18-c3341973a209",
            type=SDY.NamedType("U_Basic_Float32"),
            definition=SDY.LiteralExpr("32.0"),
        ),
        SDY.ConstantDefinition(
            name="S_Int8_8",
            oid="82cfc3bb-e891-458c-9836-b126adca30a4",
            type=SDY.PredefType(SDY.SimpleType.INT8),
            definition=SDY.LiteralExpr("8"),
        ),
        SDY.ConstantDefinition(
            name="S_Int_9_Ref",
            oid="db9d188c-6148-431b-a59b-bec2ec126d58",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.LiteralExpr("S_Int_9"),
        ),
        SDY.ConstantDefinition(
            name="C_Combination_1",
            oid="656116e0-68b7-454e-94e6-f2a6f5e32913",
            type=SDY.NamedType("{S1: Array_1, S2: Struct_1}^S_Int_2"),
            definition=SDY.parse_expr(
                "[{S1: [[S_Basic_Float32_32, 0.0], [(float32 S_Basic_Int16_6), 0.0], [3.2, 0.0]], S2: {S1: 5, S2: S_Int8_8}}, {S1: [[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]], S2: {S1: S_Int_9_Ref, S2: 0}}]"
            ),
        ),
        SDY.ConstantDefinition(
            name="S_Int32_2",
            oid="9bf2eb46-8eb6-42c5-8462-83baee39e11c",
            type=SDY.PredefType(SDY.SimpleType.INT32),
            definition=SDY.LiteralExpr("2"),
        ),
        SDY.ConstantDefinition(
            name="NewConstantabc",
            oid="8b93d1b5-3a62-493b-80b1-3807eac5ac6f",
            type=SDY.NamedType("int^5"),
            definition=SDY.parse_expr("[1, 2, 3, 4, 5]"),
        ),
        SDY.ConstantDefinition(
            name="S_Int_0",
            oid="4221292b-5132-417f-9c53-84c90597411e",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.LiteralExpr("0"),
        ),
        SDY.ConstantDefinition(
            name="S_Uint32_2",
            oid="df9e80c1-0d41-4f1e-9ba7-642d770d3b3a",
            type=SDY.PredefType(SDY.SimpleType.UINT32),
            definition=SDY.LiteralExpr("2"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Real_10",
            oid="4f050b44-2eb0-4eb4-95bf-d71d4c73a92c",
            type=SDY.NamedType("U_Basic_Real"),
            definition=SDY.LiteralExpr("10.0"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Float64_64",
            oid="da630047-b976-4119-81d4-d03f6c2a03ea",
            type=SDY.NamedType("U_Basic_Float64"),
            definition=SDY.LiteralExpr("64.0"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Uint64_4",
            oid="54a1aa20-8b96-4677-bed8-671aa5c3843a",
            type=SDY.NamedType("U_Basic_Uint64"),
            definition=SDY.LiteralExpr("4"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Uint16_6",
            oid="551d55c9-d290-4ebf-822f-c17008c1d3da",
            type=SDY.NamedType("U_Basic_Uint16"),
            definition=SDY.LiteralExpr("6"),
        ),
        SDY.ConstantDefinition(
            name="S_Int64_4",
            oid="77ab6f5c-840d-48bf-9c4c-bc5fce7ed48c",
            type=SDY.PredefType(SDY.SimpleType.INT64),
            definition=SDY.LiteralExpr("4"),
        ),
        SDY.ConstantDefinition(
            name="S_Uint64_4",
            oid="0b6a59d3-b5f2-4c35-813e-1561bf351570",
            type=SDY.PredefType(SDY.SimpleType.UINT64),
            definition=SDY.LiteralExpr("4"),
        ),
        SDY.ConstantDefinition(
            name="S_Float64_64",
            oid="db887364-1ec3-455c-b19e-048a139bd5e5",
            type=SDY.PredefType(SDY.SimpleType.FLOAT64),
            definition=SDY.LiteralExpr("64.0"),
        ),
        SDY.ConstantDefinition(
            name="C_Array_1",
            oid="6a9851ac-de70-4a33-baf7-26ad8176bcb9",
            type=SDY.NamedType("Array_1"),
            definition=SDY.parse_expr("[[0.0]]"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Char_100",
            oid="d1d5f929-82ab-421a-b166-903311f9350b",
            type=SDY.NamedType("U_Basic_Char"),
            definition=SDY.LiteralExpr("100"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Int32_2",
            oid="feb3bcc7-d56e-4223-8136-a3e072699b92",
            type=SDY.NamedType("U_Basic_Int32"),
            definition=SDY.LiteralExpr("2"),
        ),
        SDY.ConstantDefinition(
            name="S_Real_3",
            oid="7292fd82-851b-4a0a-8469-3aeb7fd0faab",
            type=SDY.PredefType(SDY.SimpleType.REAL),
            definition=SDY.LiteralExpr("3.0"),
        ),
        SDY.ConstantDefinition(
            name="S_Int_Ne5",
            oid="01dce4ba-deae-45a8-904d-620cd4819930",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.parse_expr("(- 5)"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Bool_False",
            oid="f9b6ee38-47b6-43fc-84fc-102786e42dcc",
            type=SDY.NamedType("U_Basic_Bool"),
            definition=SDY.LiteralExpr("false"),
        ),
        SDY.ConstantDefinition(
            name="c_t_global_int",
            oid="4ee1e5ea-d4a0-4b4a-a2dc-84db6601f5ce",
            type=SDY.NamedType("t_global_int"),
            definition=SDY.LiteralExpr("3"),
        ),
        SDY.ConstantDefinition(
            name="S_Float32_32",
            oid="708f7aeb-1813-49d7-b214-d1245a84d153",
            type=SDY.PredefType(SDY.SimpleType.FLOAT32),
            definition=SDY.LiteralExpr("32.0"),
        ),
        SDY.ConstantDefinition(
            name="C_T_Combination_1",
            oid="c7c69ec0-24c3-4756-9e06-52a3c806fe82",
            type=SDY.NamedType("T_Combination_1"),
            definition=SDY.parse_expr(
                "{CS_1: false, CS_2: 0, CS_3: [[0.0]], CS_4: E1_1, CS_6: {S1: 0, S2: 0}, CS_7: [[0]], CS_8: {AS_8_1: 0.0, AS_8_2: [0]}}"
            ),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Uint8_8",
            oid="998fe555-4f54-4d31-97bf-01cfb537e71d",
            type=SDY.NamedType("U_Basic_Uint8"),
            definition=SDY.LiteralExpr("8"),
        ),
        SDY.ConstantDefinition(
            name="S_Int_20_Expr",
            oid="578a2b20-8165-4fcf-a2ad-4b16da3df927",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.parse_expr("(5 + 15)"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Bool_True",
            oid="ec1705da-03de-4276-9cb8-067c1b0a2f7d",
            type=SDY.NamedType("U_Basic_Bool"),
            definition=SDY.LiteralExpr("true"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Int64_4",
            oid="6c3df760-8aaa-4b38-ace3-36bfaccff405",
            type=SDY.NamedType("U_Basic_Int64"),
            definition=SDY.LiteralExpr("4"),
        ),
        SDY.ConstantDefinition(
            name="S_Int16_6",
            oid="236de669-1495-4945-924c-2956ff33a2a6",
            type=SDY.PredefType(SDY.SimpleType.INT16),
            definition=SDY.LiteralExpr("6"),
        ),
        SDY.ConstantDefinition(
            name="S_Uint8_8",
            oid="c70f7cb7-1a49-44c8-a4eb-e8cfc2c5c5f2",
            type=SDY.PredefType(SDY.SimpleType.UINT8),
            definition=SDY.LiteralExpr("8"),
        ),
        SDY.ConstantDefinition(
            name="S_Basic_Wchar_99",
            oid="d158577e-87c9-4698-b597-5a17f4794425",
            type=SDY.NamedType("U_Basic_Wchar"),
            definition=SDY.LiteralExpr("99"),
        ),
        SDY.ConstantDefinition(
            name="C_Enum_1",
            oid="221dc698-f06d-4acd-875d-8c3d40b00422",
            type=SDY.NamedType("Enum_1"),
            definition=SDY.LiteralExpr("E1_1"),
        ),
        SDY.ConstantDefinition(
            name="S_Bool_True",
            oid="6d7ce189-0c9b-486c-a06e-5c86fe0c1fff",
            type=SDY.PredefType(SDY.SimpleType.BOOL),
            definition=SDY.LiteralExpr("true"),
        ),
        SDY.ConstantDefinition(
            name="C_Struct_1",
            oid="fded431b-a533-4689-98b3-5e929d2ec19b",
            type=SDY.NamedType("Struct_1"),
            definition=SDY.parse_expr("{S1: 0, S2: 0}"),
        ),
        SDY.ConstantDefinition(
            name="replication",
            oid="af34b36f-6aa5-4ec7-b61d-a14b02cf0f12",
            type=SDY.PredefType(SDY.SimpleType.INT),
            definition=SDY.LiteralExpr("3"),
        ),
        SDY.ConstantDefinition(
            name="Comb",
            oid="a3f7ba27-c2c5-4a40-ad2a-78e81036b725",
            type=SDY.NamedType("Str_Array"),
            definition=SDY.parse_expr(
                "{l1: {l1: {l1: 20.0, l2: 10}, l2: [5, 20]}, l2: {l1: [30, 2], l2: true}}"
            ),
        ),
        SDY.ConstantDefinition(
            name="C_Struct2",
            oid="ac5c8ae4-5bb4-46ee-b0a3-f3fa285c0fb9",
            type=SDY.NamedType("Struct2"),
            definition=SDY.parse_expr("{l1: 20.0, l2: 5}"),
        ),
        SDY.ConstantDefinition(
            name="C_Int2",
            oid="81755f81-5601-492e-8062-588e0dc158fb",
            type=SDY.NamedType("Int2"),
            definition=SDY.parse_expr("[1, 2]"),
        ),
        SDY.ConstantDefinition(
            name="C_NewType_2",
            oid="85859561-f451-ff5e-7236-699f1ed2690c",
            type=SDY.NamedType("NewType_2"),
            definition=SDY.LiteralExpr("imported _myImpInt"),
        ),
        
        
    ]
)
output_path = "./TestDisplayAPI/OutputModels/SDY_PythonAPI_TC_N_052.dgfx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
SDY.save_dgfx(defs, output_path)
