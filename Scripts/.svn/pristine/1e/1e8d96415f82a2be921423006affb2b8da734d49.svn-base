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

array_repensation = ['as_string', 'as_int_array', 'as_multiline_string', 'as_rich_string']

# list_scope = ['Input', 'Output']
list_scope = ['Input', 'Probe']


layer = SDY.Layer(
    name="symbology_layer1",
    oid="bb42e795-6c6b-4123-b242-ceaecf2ed120",
    ratio=(1.0, 1.0),
    origin=(0.0, 0.0),
)
model = SDY.Specification(width=768, height=768, layers=[layer])

for scalar_type in scalar_type_list:
    for rep in array_repensation:
        input_name = ""
        output_name = ""
        probe_name = ""
        for var_scope in list_scope:
            
            #define the variable type
            upper_type = f"{scalar_type.upper()}"
            var1 = getattr(SDY.SimpleType,'%s' % upper_type)
            ctype = SDY.ArrayType(SDY.PredefType(var1), SDY.LiteralExpr("5^3^2"))
            
            #define the variable representation
            if scalar_type in ['int', 'int32', 'uint8','wchar','char']:
                upper_rep = f"{rep.upper()}"
                array_rep = getattr(SDY.Representation,'%s' % upper_rep)
            else:
                array_rep= SDY.Representation.NONE
            
            
            #define the variable initial value
            if "int" in scalar_type:
                init=SDY.LiteralExpr("[[[0]]]")
            elif "char" in scalar_type:
                init=SDY.LiteralExpr("[[[0]]]")
            elif "bool" in scalar_type:
                init=SDY.LiteralExpr("[[[false]]]")
            else:
                init=SDY.LiteralExpr("[[[0.0]]]")
            
            if var_scope == "Input":
                inputs = layer.declaration.input
                input_name = f"I_Array_{scalar_type}_{rep}_D3"
                inputs.append(SDY.Variable(name=input_name, representation=array_rep, type=ctype, init=init))
            elif var_scope == "Output":
                outputs = layer.declaration.output
                output_name = f"O_Array_{scalar_type}_{rep}_D3"
                outputs.append(SDY.MemVariable(name=output_name, memory=SDY.MemVariable("true"), representation=array_rep, type=ctype, init=init))
            elif var_scope == "Probe":
                probes = layer.declaration.probe
                probe_name = f"P_Array_{scalar_type}_{rep}_D3"
                probes.append(SDY.Variable(name=input_name, representation=array_rep, type=ctype, init=init))
            else:
                pass
            #end of for loop: list_scope
                
        #create assignment variable for input and output
        assignment_object = SDY.Assignment(
            name="assignment_object_D3",
        )
        assignment_object.input.expr= SDY.IdentifierExpr(input_name)
        assignment_object.output.expr= SDY.IdentifierExpr(output_name)
        layer.children.append(assignment_object)


output_path = "with_obj_D3.sgfx"
SDY.save_sgfx(model, output_path)
