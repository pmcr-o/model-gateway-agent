param()
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$r=Split-Path -Parent $PSScriptRoot
foreach($p in @('SKILL.md','agents','scripts','references','assets','tests')){if(-not(Test-Path -LiteralPath (Join-Path $r $p))){throw "missing $p"}}
'PASS'
return
