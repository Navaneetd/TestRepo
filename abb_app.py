from vsts.vss_connection import VssConnection
from vsts.build.v4_1.build_client import BuildClient
##from vsts.release.v4_1.release_client import ReleaseClient
from vsts.work_item_tracking.v4_1.work_item_tracking_client import WorkItemTrackingClient
from msrest.authentication import BasicAuthentication
from vsts.vss_client import VssClient
import sys
import config
import pprint
from flask import Flask

# Fill in with your personal access token and org URL
organization_url = config.organization #input("Enter Organization URL ex: https://dev.azure.com/OrgName: ")  #'https://dev.azure.com/mgendevops' 
personal_access_token = config.PAT #input("Enter Personal Access Token: ") #'sxidglzmnx6rxwjhjpgicfdw5zctxq5kp2stkcauxswdlwsv2beq'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = VssConnection(base_url=organization_url, creds=credentials)


# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.get_client('vsts.core.v4_1.core_client.CoreClient')

while(True):
    try:

        print("Enter Choice: \n")

        choice = input("1. Projects\n2. Processes\n3. Builds\n4. WorkItems\n")
        
        if (choice == '1'):
        # Get the list of projects in the org
            projects = core_client.get_projects()
            for project in projects:
                print("Project Name: " + project.name)
                print("Project ID: " + project.id)
                print("Description: " + str(project.description))
                print("Revision: " + str(project.revision))
                print("Project State: " + project.state)
                print("--------------------------------------")


        elif(choice == '2'):
        # Get the list of processes in the org
            processes = core_client.get_processes()
            for process in processes:
                print("Process Name: " + process.name)
                print("Description: " + process.description)
                print("Process ID: " + process.id)
                print("Process Type: " + process.type)
                print("--------------------------------------")

        elif(choice == '3'):
            project = input("Enter Project Name: ")
            build_client = BuildClient(base_url=organization_url, creds=credentials)
            builds = build_client.get_builds(project=project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None)
            for build in builds:
                print("Build Number: " + build.build_number)
                print("Build Number: " + str(build.id))
                print("Build Revision: " + str(build.build_number_revision))
                print("Build Result: " + build.result)
                print("--------------------------------------")

        
        elif(choice == '4'):
            #Get WorkItems
            WorkItemTrack = WorkItemTrackingClient(base_url=organization_url, creds=credentials)
            root_nodes = WorkItemTrack.get_root_nodes("TEST-AZURE", depth=None)
            for node in root_nodes:
                print(node.__dict__)

        elif(choice == '5'):
            project = input("Enter Project Name: ")
            build_client = BuildClient(base_url=organization_url, creds=credentials)
            builds = build_client.get_builds(project=project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None)
            for build in builds:
                pprint.pprint(build.__dict__)
                print("-----------------------------------------")
    except(KeyboardInterrupt):
        sys.exit("Exiting Applications")


#Get WorkItems
##WorkItemTrack = WorkItemTrackingClient(base_url=organization_url, creds=credentials)
##root_nodes = WorkItemTrack.get_root_nodes("TEST-AZURE", depth=None)
##pprint.pprint(root_nodes.__dict__)
##get_work = WorkItemTrack.get_work_artifact_link_types()
##pprint.pprint(get_work.__list__)

#Get Build with Build ID and Project Name
##build_client = BuildClient(base_url=organization_url, creds=credentials)
##build = build_client.get_build(1,project="TEST-AZURE",property_filters=None)
##
##pprint.pprint("Build Number: " + build.build_number)
##pprint.pprint("Build Status: " + build.status)


##release_client = ReleaseClient(base_url=organization_url, creds=credentials)
##release = release_client.get_release_definitions(project="TEST-AZURE", search_text=None, expand=None, artifact_type=None, artifact_source_id=None, top=None, continuation_token=None, query_order=None, path=None, is_exact_name_match=None, tag_filter=None, property_filters=None, definition_id_filter=None, is_deleted=None)
##pprint.pprint(release.__dict__)

##deployments = release_client.get_deployments("TEST-AZURE", definition_id=None, definition_environment_id=None, created_by=None, min_modified_time=None, max_modified_time=None, deployment_status=None, operation_status=None, latest_attempts_only=None, query_order=None, top=None, continuation_token=None, created_for=None, min_started_time=None, max_started_time=None)
##
##for dep in deployments:
##    pprint.pprint(dep.__dict__)

##get_app = release_client.get_approvals("TEST-AZURE", assigned_to_filter=None, status_filter=None, release_ids_filter=None, type_filter=None, top=None, continuation_token=None, query_order=None, include_my_group_approvals=None)
##pprint.pprint(get_app)
