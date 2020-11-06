# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

RUNBOOK_CONTENT = '''
<#
    .DESCRIPTION
        An example runbook which gets all the ARM resources using the Run As Account (Service Principal)

    .NOTES
        AUTHOR: Azure Automation Team
        LASTEDIT: Mar 14, 2016
#>

$connectionName = "AzureRunAsConnection"
try
{
    # Get the connection "AzureRunAsConnection "
    $servicePrincipalConnection=Get-AutomationConnection -Name $connectionName

    "Logging in to Azure..."
    Add-AzureRmAccount `
        -ServicePrincipal `
        -TenantId $servicePrincipalConnection.TenantId `
        -ApplicationId $servicePrincipalConnection.ApplicationId `
        -CertificateThumbprint $servicePrincipalConnection.CertificateThumbprint
}
catch {
    if (!$servicePrincipalConnection)
    {
        $ErrorMessage = "Connection $connectionName not found."
        throw $ErrorMessage
    } else{
        Write-Error -Message $_.Exception
        throw $_.Exception
    }
}

#Get all ARM resources from all resource groups
$ResourceGroups = Get-AzureRmResourceGroup

foreach ($ResourceGroup in $ResourceGroups)
{
    Write-Output ("Showing resources in resource group " + $ResourceGroup.ResourceGroupName)
    $Resources = Find-AzureRmResource -ResourceGroupNameContains $ResourceGroup.ResourceGroupName | Select ResourceName, ResourceType
    ForEach ($Resource in $Resources)
    {
        Write-Output ($Resource.ResourceName + " of type " +  $Resource.ResourceType)
    }
    Write-Output ("")
}
'''


class AutomationScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_automation_', key='rg')
    def test_automation(self, resource_group):
        self.kwargs.update({
            'account_name': self.create_random_name(prefix='test-account-', length=24),
            'runbook_name': self.create_random_name(prefix='test-runbook-', length=24),
            'runbook_content': RUNBOOK_CONTENT
        })
        self.cmd('automation account create --resource-group {rg} --name {account_name} --location "West US 2"',
                 checks=[self.check('name', '{account_name}')])
        self.cmd('automation account update --resource-group {rg} --name {account_name} --tags A=a', checks=[
            self.check('name', '{account_name}'),
            self.check('tags.A', 'a')
        ])
        self.cmd('automation account show --resource-group {rg} --name {account_name}', checks=[
            self.check('name', '{account_name}'),
        ])
        self.cmd('automation account list --resourece-group {rg}', checks=[
            self.check('length(@)', 1)
        ])

        self.cmd('automation runbook create --resourece-group {rg} --automation-account-name {account_name}'
                 '--name {runbook_name} --type PowerShell',
                 checks=[self.check('name', '{runbook_name}'),
                         self.check('runbookType', 'PowerShell')])
        self.cmd('automation runbook update --resourece-group {rg} --automation-account-name {account_name}'
                 '--name {runbook_name} --log-activity-trace 1 --log-verbose true --log-progress true',
                 checks=[self.check('name', '{runbook_name}'),
                         self.check('logActivityTrace', '1'),
                         self.check('logProgress', 'true'),
                         self.check('logVerbose', 'true')])
        self.cmd('automation runbook replace-content --resourece-group {rg} --automation-account-name {account_name}'
                 '--name {runbook_name} --content {runbook_content}')
        self.cmd('automation runbook publish --resourece-group {rg} --automation-account-name {account_name}'
                 '--name {runbook_name}')
        job = self.cmd('automation runbook start --resourece-group {rg} --automation-account-name {account_name}'
                 '--name {runbook_name}').get_output_in_json()

        self.kwargs.update({
            'job_name': job['name']
        })
        self.cmd('automation job list --resource-group {rg} --automation-account-name {account_name}', checks=[
            self.check('length(@)', 1)
        ])
        self.cmd('automation job show --resource-group {rg} --automation-account-name {account_name} --name {job_name}',
                 checks=[self.check('name', '{job_name}')])

        self.cmd('automation account delete --resourece-group {rg} --name {account_name}')
