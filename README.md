# Modify ALM Document using ALM Gateway
ALM Gateway has a command to modify the elements of an ALM document in DNG and Polarion. This command is named `modifydocument`. 

Using this command, you can:
- Add a new element
- Remove an existing element
- Update the attribute of an existing element

## Content
- `actions`: Folder that contains JSON files employed by scenarios to apply a specific action executing `modifydocument` command. It contains only two actions: add a child element and remove element
- `almgateway`: Folder that contains the dependencies to execute scenarios in ALM Gateway
- `scenarios`: Folder that contains two scenarios:
    - `SuiteTest_add_child_elt_sce`: launch `modifydocument` to add a child element
    - `SuiteTest_remove_elt_sce`: launch `modifydocument` to remove a element
- `modify_document.py`: Script that executes scenarios to modify ALM document (add/remove element)
- `SuiteTest.almgr`: ALMGR file exemple to identify the attributes to fill in JSON files

## How to use 
1. Select a SCADE project with a DNG or Polarion connection
2. Modify the paths in both scenarios: `SuiteTest_add_child_elt_sce` and `SuiteTest_remove_elt_sce`. 
3. Modify JSON files in `actions`:
    `add_child_elt.json`:
        - `doc_id`: It's the ALM document ID found in ALMGR file. For instance,  in `SuiteTest.almgr`, it is `https://nicw2012doors.win.ansys.com:9443/rm/resources/_m7q2YulcEeui78les-BZIw` 
        - `parent_id`: It's the ID of an existing element in the ALM document. Once the action is executed, ALM Gateway will create a child in this element. For instance, in `SuiteTest.almgr`, it could be `https://nicw2012doors.win.ansys.com:9443/rm/resources/MB_abbbd049af184c7e982cae3f02b419b5`.
    `remove_elt.json`:
        - `doc_id`: It's the ALM document ID found in ALMGR file. For instance,  in `SuiteTest.almgr`, it is `https://nicw2012doors.win.ansys.com:9443/rm/resources/_m7q2YulcEeui78les-BZIw` 
        - `id`: It's the ALM element ID found in ALMGR file. For instance, in `SuiteTest.almgr`, it could be `https://nicw2012doors.win.ansys.com:9443/rm/resources/MB_3affacb9b7f74dca85f96c1851d5ad09`

## Limitations
- In DNG, it's not possible to append a new ALM element. It's only posible to add a child of an exisisting ALM element.# git_hub
