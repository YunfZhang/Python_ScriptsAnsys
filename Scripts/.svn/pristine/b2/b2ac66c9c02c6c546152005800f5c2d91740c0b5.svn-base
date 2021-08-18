from azure.devops.connection import Connection
from azure.devops.v5_1.work_item_tracking.models import Wiql, WorkItem
from azure.devops.v5_1.work_item_tracking.models import JsonPatchOperation
from msrest.authentication import BasicAuthentication
from pprint import pprint
import sys
from typing import List, Dict, Any, Optional
import yaml
import argparse

# cspell:word Wiql, usid, ANSYS, msrest



def verify_given_usid(conn: Connection, us_id: int) -> Optional[WorkItem]:
    wit_client = conn.clients.get_work_item_tracking_client()
    wiql = Wiql(
        query=f"""
            select [System.Id],
                [System.WorkItemType],
                [System.Title],
                [System.State],
                [System.AreaPath],
                [System.IterationPath]
            from WorkItems
            where [System.Id] = {us_id}
            order by [System.ChangedDate] desc"""
    )
    wiql_results = wit_client.query_by_wiql(wiql).work_items
    if wiql_results and len(wiql_results) == 1:
        wid = int(wiql_results[0].id)
        return wit_client.get_work_item(wid)
    else:
        return None


def parse_local_yaml_file(filepath):
    '''load a yaml file'''
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
    return data


def connect_to_tfs(url, token):
    # create a connection to the tfs url
    credentials = BasicAuthentication('', token)
    connection = Connection(base_url=url, creds=credentials)
    return connection


def create_us_task(conn, system_title, w_type, usid, areapath, assign_to, iteration_path="Portfolio"):
    wit_client = conn.clients.get_work_item_tracking_client()
    if w_type == "User Story":
        patch_document_lst = [
            JsonPatchOperation(
                op="add",
                path="/fields/System.Title",
                value=system_title
            ),
            JsonPatchOperation(
                op="add",
                path="/fields/ANSYS.Custom.StoryType",
                value="Testing"
            ),
        ]
    else:
        patch_document_lst = [
            JsonPatchOperation(
                op="add",
                path="/fields/System.Title",
                value=system_title
            ),
            JsonPatchOperation(
                op="add",
                path="/fields/Microsoft.VSTS.Common.Activity",
                value="Testing"
            ),
        ]
    project = "Portfolio"
    workitem = wit_client.create_work_item(
        patch_document_lst,  project, w_type)
    if workitem:
        print(f"{w_type} {workitem.id}:{system_title} has been created")
        update_us_task_link(wit_client, usid, workitem.id, areapath, assign_to, iteration_path)
        return workitem.id
    else:
        print(f"Error: {w_type}:{system_title} is not created")
        pass


def update_us_task_link(wit_client, parent_id, current_id, areapath, assign_to, iteration_path="Portfolio"):
    patch_document_lst = [
        JsonPatchOperation(
            op="add",
            path="/relations/-",
            value={
                "rel": "System.LinkTypes.Hierarchy-Reverse",
                "url": f"https://tfs.ansys.com:8443/tfs/ANSYS_Development/b1eae7de-0480-4e7a-93de-cf6a6254d856/_apis/wit/workItems/{parent_id}"
            }
        ),
        JsonPatchOperation(
            op="add",
            path="/fields/System.AreaPath",
            value=areapath
        ),
        JsonPatchOperation(
            op="add",
            path="/fields/System.AssignedTo",
            value=f"{assign_to}"
        ),
        JsonPatchOperation(
            op="add",
            path="/fields/System.IterationPath",
            value=f"{iteration_path}"
        ),
        JsonPatchOperation(
            op="add",
            path="/fields/Microsoft.VSTS.Scheduling.OriginalEstimate",
            value=8
        ),
        JsonPatchOperation(
            op="add",
            path="/fields/Microsoft.VSTS.Scheduling.RemainingWork",
            value=8
        ),
    ]
    update_item = wit_client.update_work_item(patch_document_lst, current_id)
    if update_item:
        print(f"{current_id} add its parent user story ===> pass")
    else:
        print(f"Error: {current_id} add its parent user story ===> failed")


def main():
    parser = argparse.ArgumentParser(description="", prog=None)
    parser.add_argument("-p", "--parent", type=int, help="Set the parent user story id")
    parser.add_argument("-f", "--file", help="Get the yaml file")
    try:
        args = parser.parse_args()
        if args.parent is None or args.file is None:
            parser.print_help()
            sys.exit(0)
    except:
        parser.print_help()
        sys.exit(0)
    filepath = args.file #get the yaml file from the command line
    parent_id = args.parent #get the parent user story id from command line

    data = parse_local_yaml_file(filepath)

    # start to connect to tfs
    connection = connect_to_tfs(data["Team instance"], data["API token"])

    parent_us = verify_given_usid(connection, parent_id)
    if not parent_us:
        print(f"the user story {parent_id} cannot be found, please check it")
        sys.exit()

    area = data["Areas"][0].replace("-", "")
    author = data["Author"]
    for name, value in data.items():
        if name == "User Stories & Tasks":
            for us_name, tasks in value.items():
                if "#" in us_name:
                    us_title, us_iteration = us_name.split("#")
                    usid = create_us_task(connection, us_title, "User Story", parent_id, area, author, us_iteration)
                else:
                    usid = create_us_task(connection, us_name, "User Story", parent_id, area, author)
                for task in tasks:
                    if "#" in task:
                        task_title, task_iteration = task.split("#")
                        create_us_task(connection, task_title, "Task", usid, area, author, task_iteration)
                    else:
                        create_us_task(connection, task, "Task", usid, area, author)

    print("************Finished of creation US an Tasks************")


if __name__ == "__main__":
    main()
