import argparse, json, hashlib, pathlib, datetime

p = argparse.ArgumentParser()
p.add_argument('--provider', required=True)
p.add_argument('--model', required=True)
p.add_argument('--channel', choices=['ui', 'api', 'local'], required=True)
p.add_argument('--prompt-file', required=True)
p.add_argument('--response-file', required=True)
p.add_argument('--trail-ref', required=True)
p.add_argument('--output', required=True)
p.add_argument('--reasoning-kind', choices=['opaque', 'provider-summary', 'explicit-rationale', 'derived-rationale'], default='opaque')
p.add_argument('--reasoning-file')
p.add_argument('--reasoning-route', default='')
a = p.parse_args()

prompt = pathlib.Path(a.prompt_file).read_text()
response = pathlib.Path(a.response_file).read_text()
h = lambda text: hashlib.sha256(text.encode()).hexdigest()

if a.reasoning_kind == 'opaque':
    if a.reasoning_file:
        raise SystemExit('opaque reasoning-kind cannot include a reasoning file')
    reasoning = {'kind':'opaque','present':False,'source':'none','summarySha256':'','summary':'','route':'','policy':'Private internal reasoning is not required or inferred.'}
else:
    if not a.reasoning_file:
        raise SystemExit('reasoning-file is required for non-opaque reasoning-kind')
    summary = pathlib.Path(a.reasoning_file).read_text()
    source = 'reasoning-agent' if a.reasoning_kind == 'derived-rationale' else 'provider-or-explicit-output'
    if a.reasoning_kind == 'derived-rationale' and not a.reasoning_route.startswith('@reasoning-agent /reasoning:'):
        raise SystemExit('derived-rationale requires an explicit @reasoning-agent /reasoning:<skill> route')
    reasoning = {'kind':a.reasoning_kind,'present':True,'source':source,'summarySha256':h(summary),'summary':summary,'route':a.reasoning_route,'policy':'This is an explicit or derived rationale artifact, not a private internal trace.'}

out = {'schema':'pmcro.model-exchange/v2','kind':'model.response','provider':a.provider,'modelLabel':a.model,'channel':a.channel,'trailRef':a.trail_ref,'capturedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'promptSha256':h(prompt),'responseSha256':h(response),'prompt':prompt,'response':response,'reasoningEvidence':reasoning,'authority':'untrusted-external-inference-until-checked'}
pathlib.Path(a.output).write_text(json.dumps(out, indent=2) + '\n')
print(a.output)
