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

list_scope = ['Input', 'Output']
# list_scope = ['Input', 'Output', 'Probe']


layer = SDY.Layer(
    name="symbology_layer1",
    oid="bb42e795-6c6b-4123-b242-ceaecf2ed120",
    ratio=(1.0, 1.0),
    origin=(0.0, 0.0),
)
model = SDY.Specification(width=768, height=768, layers=[layer])

def var_content(var_prefix, content):
    for scalar_type in scalar_type_list:
        for rep in array_repensation:
            name = f"{var_prefix}_Array_{scalar_type}_{rep}"
            upper_type = f"{scalar_type.upper()}"
            var1 = getattr(SDY.SimpleType,'%s' % upper_type)
            if scalar_type in ['int', 'int32', 'uint8','wchar','char']:
                upper_rep = f"{rep.upper()}"
                array_rep = getattr(SDY.Representation,'%s' % upper_rep)
            else:
                array_rep= SDY.Representation.NONE
            ctype = SDY.ArrayType(SDY.PredefType(var1), SDY.LiteralExpr("5"))
            if "int" in scalar_type:
                init=SDY.LiteralExpr("[0]")
            elif "char" in scalar_type:
                init=SDY.LiteralExpr("[0]")
            elif "bool" in scalar_type:
                init=SDY.LiteralExpr("[false]")
            else:
                init=SDY.LiteralExpr("[0.0]")
            content.append(SDY.Variable(name=name, representation=array_rep, type=ctype, init=init))
            
    

for var_scope in list_scope:
    if var_scope == "Input":
        name_prefix = "I"
        inputs = layer.declaration.input
        input_var_content = var_content(name_prefix, inputs)
    elif var_scope == "Output":
        name_prefix = "O"
        outputs = layer.declaration.output
        output_var_content = var_content(name_prefix, outputs)
    elif var_scope == "Probe":
        name_prefix = "P"
        probes = layer.declaration.probe
        probes_var_content = var_content(name_prefix, probes)
        probes.append(probes_var_content)
    else:
        pass

output_path = "a.sgfx"
SDY.save_sgfx(model, output_path)
