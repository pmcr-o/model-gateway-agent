[CmdletBinding()]param([Parameter(Mandatory=$true)][string]$ExchangePath,[Parameter(Mandatory=$true)][string]$Endpoint,[switch]$Apply)
Set-StrictMode -Version Latest;$ErrorActionPreference='Stop';$u=[uri]$Endpoint;if($u.Scheme -notin @('http','https')){throw 'endpoint must be http/https'}
if($u.Host -notin @('localhost','127.0.0.1','::1')){throw 'v1 bridge is loopback-only'};$x=Get-Content -LiteralPath $ExchangePath -Raw|ConvertFrom-Json -DateKind String;if($x.schema -ne 'pmcro.model-exchange/v1'){throw 'invalid model exchange'}
if(-not $Apply){Write-Output "dry run: POST $Endpoint model=$($x.modelLabel) responseSha256=$($x.responseSha256)";return}
$r=Invoke-RestMethod -Method Post -Uri $Endpoint -ContentType 'application/json' -Body (Get-Content -LiteralPath $ExchangePath -Raw);$r|ConvertTo-Json -Depth 20;return
