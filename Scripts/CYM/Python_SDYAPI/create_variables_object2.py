import os
import sys


# load test environment
try:
    import ENVIRONMENT as ENV
except Exception as e:
    print("Test Environment not set in 'ENVIRONMENT.py'.")
    print("You can use template 'ENVIRONMENT_Template.py' to do so!")
    raise

# Get the installation path and initial directory of API
api_dir = os.path.join(ENV.SCADE_DIR, "SCADE/APIs/Python/lib")

# NOTE: to get coverage, run "copy_api.py" prior to running the tests
sys.path.append(api_dir)

import scade.model.display as SDY

scalar_type_list = ['int', 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64','wchar','bool','char','real','float32','float64']
# scalar_type_list = ['int']


list_scope = ['Input', 'Output']


# layer = SDY.Layer(
#     name="symbology_layer1",
#     oid="bb42e795-6c6b-4123-b242-ceaecf2ed120",
#     ratio=(1.0, 1.0),
#     origin=(0.0, 0.0),
# )
# model = SDY.Specification(width=768, height=768, layers=[layer])

a_container = SDY.Container(
    name="group",
)
model = SDY.ReferenceObject(width=768, height=768, children=a_container)

for scalar_type in scalar_type_list:
    for i in range(0, 667):
        input_name = ""
        output_name = ""
        probe_name = ""
        for var_scope in list_scope:

            #define the variable type
            upper_type = f"{scalar_type.upper()}"
            var1 = getattr(SDY.SimpleType,'%s' % upper_type)
            ctype = SDY.PredefType(var1)
            

            #define the variable initial value
            if "int" in scalar_type:
                init=SDY.LiteralExpr("0")
            elif "char" in scalar_type:
                init=SDY.LiteralExpr("0")
            elif "bool" in scalar_type:
                init=SDY.LiteralExpr("false")
            else:
                init=SDY.LiteralExpr("0.0")
            
            if var_scope == "Input":
                inputs = model.declaration.input
                input_name = f"I_{scalar_type}_{i}"
                inputs.append(SDY.Variable(name=input_name, type=ctype, init=init))
            elif var_scope == "Output":
                outputs = model.declaration.output
                output_name = f"O_{scalar_type}_{i}"
                outputs.append(SDY.MemVariable(name=output_name, memory=SDY.MemVariable("true"), type=ctype, init=init))
            elif var_scope == "Probe":
                probes = model.declaration.probe
                probe_name = f"P_{scalar_type}_{i}"
                probes.append(SDY.Variable(name=input_name, type=ctype, init=init))
            else:
                pass
            #end of for loop: list_scope
                
        #create assignment variable for input and output
        assignment_object = SDY.Assignment(
            name=f"assignment_object_{i}",
        )
        assignment_object.input.expr= SDY.IdentifierExpr(input_name)
        assignment_object.output.expr= SDY.IdentifierExpr(output_name)
        a_container.children.append(assignment_object)


    # output_path = f"Perf_{scalar_type}.sgfx"
    # SDY.save_sgfx(model, output_path)
    output_path = f"test2/Perf_{scalar_type}.ogfx"
    SDY.save_ogfx(model, output_path)