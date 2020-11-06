# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az automation|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az automation` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az automation runbook|Runbook|[commands](#CommandsInRunbook)|
|az automation automation-account|AutomationAccount|[commands](#CommandsInAutomationAccount)|

## COMMANDS
### <a name="CommandsInAutomationAccount">Commands in `az automation automation-account` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az automation automation-account list](#AutomationAccountListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersAutomationAccountListByResourceGroup)|[Example](#ExamplesAutomationAccountListByResourceGroup)|
|[az automation automation-account list](#AutomationAccountList)|List|[Parameters](#ParametersAutomationAccountList)|[Example](#ExamplesAutomationAccountList)|
|[az automation automation-account show](#AutomationAccountGet)|Get|[Parameters](#ParametersAutomationAccountGet)|[Example](#ExamplesAutomationAccountGet)|
|[az automation automation-account create](#AutomationAccountCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersAutomationAccountCreateOrUpdate#Create)|[Example](#ExamplesAutomationAccountCreateOrUpdate#Create)|
|[az automation automation-account update](#AutomationAccountUpdate)|Update|[Parameters](#ParametersAutomationAccountUpdate)|[Example](#ExamplesAutomationAccountUpdate)|
|[az automation automation-account delete](#AutomationAccountDelete)|Delete|[Parameters](#ParametersAutomationAccountDelete)|[Example](#ExamplesAutomationAccountDelete)|

### <a name="CommandsInRunbook">Commands in `az automation runbook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az automation runbook list](#RunbookListByAutomationAccount)|ListByAutomationAccount|[Parameters](#ParametersRunbookListByAutomationAccount)|[Example](#ExamplesRunbookListByAutomationAccount)|
|[az automation runbook show](#RunbookGet)|Get|[Parameters](#ParametersRunbookGet)|[Example](#ExamplesRunbookGet)|
|[az automation runbook create](#RunbookCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersRunbookCreateOrUpdate#Create)|[Example](#ExamplesRunbookCreateOrUpdate#Create)|
|[az automation runbook update](#RunbookUpdate)|Update|[Parameters](#ParametersRunbookUpdate)|[Example](#ExamplesRunbookUpdate)|
|[az automation runbook delete](#RunbookDelete)|Delete|[Parameters](#ParametersRunbookDelete)|[Example](#ExamplesRunbookDelete)|
|[az automation runbook publish](#RunbookPublish)|Publish|[Parameters](#ParametersRunbookPublish)|[Example](#ExamplesRunbookPublish)|


## COMMAND DETAILS

### group `az automation automation-account`
#### <a name="AutomationAccountListByResourceGroup">Command `az automation automation-account list`</a>

##### <a name="ExamplesAutomationAccountListByResourceGroup">Example</a>
```
az automation automation-account list --resource-group "rg"
```
##### <a name="ParametersAutomationAccountListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|

#### <a name="AutomationAccountList">Command `az automation automation-account list`</a>

##### <a name="ExamplesAutomationAccountList">Example</a>
```
az automation automation-account list
```
##### <a name="ParametersAutomationAccountList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="AutomationAccountGet">Command `az automation automation-account show`</a>

##### <a name="ExamplesAutomationAccountGet">Example</a>
```
az automation automation-account show --name "myAutomationAccount9" --resource-group "rg"
```
##### <a name="ParametersAutomationAccountGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|

#### <a name="AutomationAccountCreateOrUpdate#Create">Command `az automation automation-account create`</a>

##### <a name="ExamplesAutomationAccountCreateOrUpdate#Create">Example</a>
```
az automation automation-account create --automation-account-name "myAutomationAccount9" --name "myAutomationAccount9" \
--location "East US 2" --sku name="Free" --resource-group "rg"
```
##### <a name="ParametersAutomationAccountCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--name**|string|Gets or sets name of the resource.|name|name|
|**--location**|string|Gets or sets the location of the resource.|location|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|tags|
|**--sku**|object|Gets or sets account SKU.|sku|sku|

#### <a name="AutomationAccountUpdate">Command `az automation automation-account update`</a>

##### <a name="ExamplesAutomationAccountUpdate">Example</a>
```
az automation automation-account update --automation-account-name "myAutomationAccount9" --name "myAutomationAccount9" \
--location "East US 2" --sku name="Free" --resource-group "rg"
```
##### <a name="ParametersAutomationAccountUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--name**|string|Gets or sets the name of the resource.|name|name|
|**--location**|string|Gets or sets the location of the resource.|location|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|tags|
|**--sku**|object|Gets or sets account SKU.|sku|sku|

#### <a name="AutomationAccountDelete">Command `az automation automation-account delete`</a>

##### <a name="ExamplesAutomationAccountDelete">Example</a>
```
az automation automation-account delete --name "myAutomationAccount9" --resource-group "rg"
```
##### <a name="ParametersAutomationAccountDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|

### group `az automation runbook`
#### <a name="RunbookListByAutomationAccount">Command `az automation runbook list`</a>

##### <a name="ExamplesRunbookListByAutomationAccount">Example</a>
```
az automation runbook list --automation-account-name "ContoseAutomationAccount" --resource-group "rg"
```
##### <a name="ParametersRunbookListByAutomationAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|

#### <a name="RunbookGet">Command `az automation runbook show`</a>

##### <a name="ExamplesRunbookGet">Example</a>
```
az automation runbook show --automation-account-name "ContoseAutomationAccount" --resource-group "rg" --name \
"Get-AzureVMTutorial"
```
##### <a name="ParametersRunbookGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--runbook-name**|string|The runbook name.|runbook_name|runbookName|

#### <a name="RunbookCreateOrUpdate#Create">Command `az automation runbook create`</a>

##### <a name="ExamplesRunbookCreateOrUpdate#Create">Example</a>
```
az automation runbook create --automation-account-name "ContoseAutomationAccount" --draft-parameters \
"{\\"name\\":\\"Get-AzureVMTutorial\\",\\"location\\":\\"East US 2\\",\\"properties\\":{\\"description\\":\\"Descriptio\
n of the Runbook\\",\\"logActivityTrace\\":1,\\"logProgress\\":true,\\"logVerbose\\":false,\\"publishContentLink\\":{\\\
"contentHash\\":{\\"algorithm\\":\\"SHA256\\",\\"value\\":\\"115775B8FF2BE672D8A946BD0B489918C724DDE15A440373CA54461D53\
010A80\\"},\\"uri\\":\\"https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-automation-runboo\
k-getvms/Runbooks/Get-AzureVMTutorial.ps1\\"},\\"runbookType\\":\\"PowerShellWorkflow\\"},\\"tags\\":{\\"tag01\\":\\"va\
lue01\\",\\"tag02\\":\\"value02\\"}}" --resource-group "rg" --runbook-name "Get-AzureVMTutorial"
```
##### <a name="ExamplesRunbookCreateOrUpdate#Create">Example</a>
```
az automation runbook create --automation-account-name "ContoseAutomationAccount" --draft-parameters \
"{\\"name\\":\\"Get-AzureVMTutorial\\",\\"location\\":\\"East US 2\\",\\"properties\\":{\\"description\\":\\"Descriptio\
n of the Runbook\\",\\"draft\\":{},\\"logProgress\\":false,\\"logVerbose\\":false,\\"runbookType\\":\\"PowerShellWorkfl\
ow\\"},\\"tags\\":{\\"tag01\\":\\"value01\\",\\"tag02\\":\\"value02\\"}}" --resource-group "rg" --runbook-name \
"Get-AzureVMTutorial"
```
##### <a name="ParametersRunbookCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--runbook-name**|string|The runbook name.|runbook_name|runbookName|
|**--runbook-type**|choice|Gets or sets the type of the runbook.|runbook_type|runbookType|
|**--name**|string|Gets or sets the name of the resource.|name|name|
|**--location**|string|Gets or sets the location of the resource.|location|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|tags|
|**--log-verbose**|boolean|Gets or sets verbose log option.|log_verbose|logVerbose|
|**--log-progress**|boolean|Gets or sets progress log option.|log_progress|logProgress|
|**--description**|string|Gets or sets the description of the runbook.|description|description|
|**--log-activity-trace**|integer|Gets or sets the activity-level tracing options of the runbook.|log_activity_trace|logActivityTrace|
|**--publish-content-link-uri**|string|Gets or sets the uri of the runbook content.|uri|uri|
|**--publish-content-link-content-hash**|object|Gets or sets the hash.|content_hash|contentHash|
|**--publish-content-link-version**|string|Gets or sets the version of the content.|version|version|
|**--draft-in-edit**|boolean|Gets or sets whether runbook is in edit mode.|in_edit|inEdit|
|**--draft-draft-content-link**|object|Gets or sets the draft runbook content link.|draft_content_link|draftContentLink|
|**--draft-creation-time**|date-time|Gets or sets the creation time of the runbook draft.|creation_time|creationTime|
|**--draft-last-modified-time**|date-time|Gets or sets the last modified time of the runbook draft.|last_modified_time|lastModifiedTime|
|**--draft-parameters**|dictionary|Gets or sets the runbook draft parameters.|parameters|parameters|
|**--draft-output-types**|array|Gets or sets the runbook output types.|output_types|outputTypes|

#### <a name="RunbookUpdate">Command `az automation runbook update`</a>

##### <a name="ExamplesRunbookUpdate">Example</a>
```
az automation runbook update --automation-account-name "ContoseAutomationAccount" --description "Updated Description \
of the Runbook" --log-activity-trace 1 --log-progress true --log-verbose false --resource-group "rg" --runbook-name \
"Get-AzureVMTutorial"
```
##### <a name="ParametersRunbookUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--runbook-name**|string|The runbook name.|runbook_name|runbookName|
|**--name**|string|Gets or sets the name of the resource.|name|name|
|**--location**|string|Gets or sets the location of the resource.|location|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|tags|
|**--description**|string|Gets or sets the description of the runbook.|description|description|
|**--log-verbose**|boolean|Gets or sets verbose log option.|log_verbose|logVerbose|
|**--log-progress**|boolean|Gets or sets progress log option.|log_progress|logProgress|
|**--log-activity-trace**|integer|Gets or sets the activity-level tracing options of the runbook.|log_activity_trace|logActivityTrace|

#### <a name="RunbookDelete">Command `az automation runbook delete`</a>

##### <a name="ExamplesRunbookDelete">Example</a>
```
az automation runbook delete --automation-account-name "ContoseAutomationAccount" --resource-group "rg" --name \
"Get-AzureVMTutorial"
```
##### <a name="ParametersRunbookDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--runbook-name**|string|The runbook name.|runbook_name|runbookName|

#### <a name="RunbookPublish">Command `az automation runbook publish`</a>

##### <a name="ExamplesRunbookPublish">Example</a>
```
az automation runbook publish --automation-account-name "ContoseAutomationAccount" --resource-group "rg" --name \
"Get-AzureVMTutorial"
```
##### <a name="ParametersRunbookPublish">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|resourceGroupName|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|automationAccountName|
|**--runbook-name**|string|The parameters supplied to the publish runbook operation.|runbook_name|runbookName|
