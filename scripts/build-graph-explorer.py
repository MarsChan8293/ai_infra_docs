#!/usr/bin/env python3
"""Build a dependency-free focused graph explorer for the AI Infra docs site."""

from __future__ import annotations

import argparse
import json
import pathlib
from urllib.parse import quote


def load_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def href_for(node_id: str, base_path: str) -> str:
    base = base_path.rstrip("/")
    if node_id in {"00-ai-infra-map", "index"}:
        return f"{base}/"
    encoded = "/".join(quote(part, safe="-_.~") for part in node_id.split("/"))
    return f"{base}/{encoded}.html"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-path", default="/ai_infra_docs")
    args = parser.parse_args()

    generated = pathlib.Path(args.generated)
    output = pathlib.Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    nodes = load_json(generated / "nodes.json", [])
    edges = load_json(generated / "edges.json", [])
    if not nodes:
        raise SystemExit("nodes.json is empty; run build-knowledge-graph.py first")

    payload_nodes = []
    for node in nodes:
        fm = node.get("frontmatter") or {}
        aliases = fm.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        payload_nodes.append({
            "id": node["id"],
            "name": node.get("name") or node["id"].split("/")[-1],
            "aliases": aliases,
            "domain": node.get("domain") or "root",
            "kind": node.get("kind") or "note",
            "degree": node.get("degree") or 0,
            "bridgeScore": node.get("bridge_score") or 0,
            "href": href_for(node["id"], args.base_path),
        })

    payload_edges = [
        {
            "source": edge["source"],
            "target": edge["target"],
            "relation": edge.get("relation") or "wikilink",
        }
        for edge in edges
    ]

    data = {
        "nodes": payload_nodes,
        "edges": payload_edges,
        "basePath": args.base_path.rstrip("/"),
    }
    (output / "data.json").write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    html = r'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>AI Infra Docs · Knowledge Graph</title>
<style>
:root{color-scheme:light dark;--bg:#f7f8fa;--panel:#fff;--text:#20242a;--muted:#6d7480;--line:#d9dee5;--chip:#eef2f6;--accent:#315f7d;--shadow:0 12px 34px rgba(0,0,0,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#15171a;--panel:#202328;--text:#eef0f3;--muted:#a4abb4;--line:#3a4048;--chip:#292f36;--accent:#8bb7d2;--shadow:0 12px 34px rgba(0,0,0,.30)}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.shell{max-width:1540px;margin:auto;padding:18px}.top{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:14px}.title{font-size:23px;font-weight:760}.sub{margin-top:3px;color:var(--muted);font-size:12px}.home{color:var(--accent);text-decoration:none;white-space:nowrap}.grid{display:grid;grid-template-columns:minmax(280px,350px) minmax(0,1fr);gap:14px}@media(max-width:920px){.grid{grid-template-columns:1fr}.canvas-wrap{min-height:60vh}}.panel,.canvas-wrap{background:var(--panel);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow)}.panel{padding:14px;max-height:calc(100vh - 85px);overflow:auto}.section{padding:10px 0;border-bottom:1px solid var(--line)}.section:last-child{border-bottom:0}.section h3{font-size:13px;margin:0 0 8px}.row{display:flex;gap:7px;align-items:center;flex-wrap:wrap}input,button{font:inherit}input[type=text]{width:100%;padding:9px 10px;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--text)}button,.chip{border:1px solid var(--line);background:var(--chip);color:var(--text);padding:6px 9px;border-radius:999px;cursor:pointer}.chip.active,button.active{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 16%,var(--panel));color:var(--accent)}button.primary{border-color:var(--accent);background:var(--accent);color:white}.small{font-size:12px;color:var(--muted)}.filter-list{display:flex;gap:6px;flex-wrap:wrap}.canvas-wrap{position:relative;min-height:760px;overflow:hidden}.toolbar{position:absolute;z-index:3;left:12px;top:12px;display:flex;gap:6px;flex-wrap:wrap}.stats{position:absolute;z-index:3;right:12px;top:12px;color:var(--muted);background:color-mix(in srgb,var(--panel) 92%,transparent);border:1px solid var(--line);padding:6px 9px;border-radius:999px}.status{position:absolute;left:12px;bottom:10px;color:var(--muted);background:color-mix(in srgb,var(--panel) 92%,transparent);padding:5px 8px;border-radius:8px;z-index:3}.path-result{margin-top:8px;padding:8px;border-radius:9px;background:var(--chip);min-height:38px}.path-node{color:var(--accent);cursor:pointer;text-decoration:none}.path-node:hover{text-decoration:underline}svg{width:100%;height:100%;min-height:760px;display:block}.edge{stroke:var(--line);stroke-width:1.15;opacity:.62}.edge.cross-domain{stroke-width:2;opacity:.9}.node{cursor:pointer}.node circle{stroke:var(--panel);stroke-width:2}.node text{fill:var(--text);font-size:11px;paint-order:stroke;stroke:var(--panel);stroke-width:3px;stroke-linejoin:round}.node.focus text{font-size:13px;font-weight:750}.legend{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:5px 8px;font-size:12px}.dot{width:9px;height:9px;border-radius:50%;display:inline-block;margin-right:5px}
</style>
</head>
<body>
<div class="shell">
  <div class="top"><div><div class="title">AI Infra Docs · 知识图谱</div><div class="sub">基于仓库 Markdown 双链自动生成。默认查看焦点节点的 1-hop / 2-hop 邻域，可筛选领域、节点类型与关系类型，并寻找最短路径。</div></div><a class="home" id="homeLink" href="#">返回知识库</a></div>
  <div class="grid">
    <aside class="panel">
      <div class="section"><h3>焦点节点</h3><input id="focusInput" type="text" list="nodeList" placeholder="输入 H100 / KV Cache / 异构推理 / Qwen…"/><datalist id="nodeList"></datalist><div class="row" style="margin-top:7px"><button id="focusBtn" class="primary">聚焦</button><button id="openBtn">打开页面</button></div></div>
      <div class="section"><h3>领域</h3><div id="domainFilters" class="filter-list"></div></div>
      <div class="section"><h3>节点类型</h3><div id="kindFilters" class="filter-list"></div></div>
      <div class="section"><h3>关系类型</h3><div id="relationFilters" class="filter-list"></div></div>
      <div class="section"><h3>Path Finder</h3><input id="pathFrom" type="text" list="nodeList" placeholder="起点"/><input id="pathTo" type="text" list="nodeList" placeholder="终点" style="margin-top:6px"/><button id="pathBtn" class="primary" style="margin-top:7px">寻找最短路径</button><div id="pathResult" class="path-result small">路径计算会遵守当前筛选条件。</div></div>
      <div class="section"><h3>领域图例</h3><div id="legend" class="legend"></div></div>
      <div class="section"><div class="small">点击节点重新聚焦，双击节点打开原文。2-hop 邻域过大时优先显示 bridge score 和 degree 更高的节点。</div></div>
    </aside>
    <main class="canvas-wrap">
      <div class="toolbar"><button id="hop1" class="active">1-hop</button><button id="hop2">2-hop</button><button id="resetBtn">恢复筛选</button></div>
      <div id="stats" class="stats"></div>
      <svg id="graph" viewBox="0 0 1120 760" role="img" aria-label="AI Infra knowledge graph"></svg>
      <div id="status" class="status"></div>
    </main>
  </div>
</div>
<script>
(async()=>{
const data=await fetch('./data.json').then(r=>r.json());
const nodes=data.nodes,edges=data.edges,byId=new Map(nodes.map(n=>[n.id,n]));
const adj=new Map(nodes.map(n=>[n.id,[]]));
for(const e of edges){adj.get(e.source)?.push({id:e.target,edge:e});adj.get(e.target)?.push({id:e.source,edge:e});}
const domainColors={chip:'#4f7da5',system:'#5f8b62',models:'#a36b47',root:'#8a6faf'};
const domainNames={chip:'芯片 / 硬件',system:'系统架构',models:'模型',root:'入口 / 规则'};
const relationNames={'cross-domain':'跨域关系','concept-link':'概念关系','navigation':'导航关系','vendor-chip':'厂商-芯片','wikilink':'普通双链'};
const domains=[...new Set(nodes.map(n=>n.domain))].sort();
const kinds=[...new Set(nodes.map(n=>n.kind))].sort();
const relations=[...new Set(edges.map(e=>e.relation))].sort();
let enabledDomains=new Set(domains),enabledKinds=new Set(kinds),enabledRelations=new Set(relations),focusId=byId.has('00-ai-infra-map')?'00-ai-infra-map':nodes.sort((a,b)=>b.bridgeScore-a.bridgeScore)[0].id,hop=1;
const $=id=>document.getElementById(id);$('homeLink').href=data.basePath+'/';
function label(n){return n.name||n.id.split('/').pop()}
function searchable(n){return [n.id,n.name,...(n.aliases||[])].filter(Boolean).join(' ').toLowerCase()}
for(const n of [...nodes].sort((a,b)=>label(a).localeCompare(label(b)))){const o=document.createElement('option');o.value=n.id;o.label=label(n);$('nodeList').appendChild(o)}
function resolveInput(v){const q=(v||'').trim().toLowerCase();if(!q)return null;if(byId.has(v.trim()))return v.trim();const exact=nodes.find(n=>label(n).toLowerCase()===q||(n.aliases||[]).some(a=>String(a).toLowerCase()===q));if(exact)return exact.id;const hits=nodes.filter(n=>searchable(n).includes(q));return hits.length===1?hits[0].id:null}
function makeFilters(id,values,enabled,namer){const root=$(id);root.innerHTML='';for(const v of values){const b=document.createElement('button');b.className='chip'+(enabled.has(v)?' active':'');b.textContent=namer(v);b.onclick=()=>{enabled.has(v)?enabled.delete(v):enabled.add(v);render();makeFilters(id,values,enabled,namer)};root.appendChild(b)}}
makeFilters('domainFilters',domains,enabledDomains,v=>domainNames[v]||v);makeFilters('kindFilters',kinds,enabledKinds,v=>v);makeFilters('relationFilters',relations,enabledRelations,v=>relationNames[v]||v);
$('legend').innerHTML=domains.map(d=>`<div><span class="dot" style="background:${domainColors[d]||'#888'}"></span>${domainNames[d]||d}</div>`).join('');
function edgeAllowed(e){return enabledRelations.has(e.relation)&&enabledDomains.has(byId.get(e.source)?.domain)&&enabledDomains.has(byId.get(e.target)?.domain)&&enabledKinds.has(byId.get(e.source)?.kind)&&enabledKinds.has(byId.get(e.target)?.kind)}
function nodeAllowed(n){return enabledDomains.has(n.domain)&&enabledKinds.has(n.kind)}
function neighborhood(start,depth){const seen=new Set([start]),levels=new Map([[start,0]]),q=[start];while(q.length){const cur=q.shift(),d=levels.get(cur);if(d>=depth)continue;for(const item of adj.get(cur)||[]){if(!edgeAllowed(item.edge))continue;if(!nodeAllowed(byId.get(item.id)))continue;if(!seen.has(item.id)){seen.add(item.id);levels.set(item.id,d+1);q.push(item.id)}}}return {seen,levels}}
function selectVisible(){let {seen,levels}=neighborhood(focusId,hop);const max=hop===1?90:150;if(seen.size>max){const keep=[...seen].sort((a,b)=>{if(a===focusId)return -1;if(b===focusId)return 1;const na=byId.get(a),nb=byId.get(b);return (nb.bridgeScore-na.bridgeScore)||(nb.degree-na.degree)}).slice(0,max);seen=new Set(keep)}return {seen,levels}}
function layout(ids,levels){const pos=new Map(),cx=560,cy=380;pos.set(focusId,{x:cx,y:cy});const rings={};for(const id of ids){if(id===focusId)continue;const d=Math.min(levels.get(id)||1,2);(rings[d]??=[]).push(id)}for(const [d,arr] of Object.entries(rings)){arr.sort((a,b)=>byId.get(b).bridgeScore-byId.get(a).bridgeScore);const radius=Number(d)===1?210:340;arr.forEach((id,i)=>{const angle=(-Math.PI/2)+(i/arr.length)*Math.PI*2;pos.set(id,{x:cx+Math.cos(angle)*radius,y:cy+Math.sin(angle)*radius})})}return pos}
function render(){if(!byId.has(focusId)||!nodeAllowed(byId.get(focusId))){const fallback=nodes.filter(nodeAllowed).sort((a,b)=>b.bridgeScore-a.bridgeScore)[0];if(!fallback)return;focusId=fallback.id}$('focusInput').value=focusId;const {seen,levels}=selectVisible(),ids=[...seen],pos=layout(ids,levels),visibleEdges=edges.filter(e=>seen.has(e.source)&&seen.has(e.target)&&edgeAllowed(e));const svg=$('graph');svg.innerHTML='';const ns='http://www.w3.org/2000/svg';for(const e of visibleEdges){const a=pos.get(e.source),b=pos.get(e.target);if(!a||!b)continue;const l=document.createElementNS(ns,'line');l.setAttribute('x1',a.x);l.setAttribute('y1',a.y);l.setAttribute('x2',b.x);l.setAttribute('y2',b.y);l.setAttribute('class','edge '+e.relation);l.innerHTML=`<title>${relationNames[e.relation]||e.relation}</title>`;svg.appendChild(l)}for(const id of ids){const n=byId.get(id),p=pos.get(id);if(!p)continue;const g=document.createElementNS(ns,'g');g.setAttribute('class','node'+(id===focusId?' focus':''));g.setAttribute('transform',`translate(${p.x},${p.y})`);const c=document.createElementNS(ns,'circle');const r=id===focusId?12:Math.max(6,Math.min(10,6+Math.log2(1+n.degree)));c.setAttribute('r',r);c.setAttribute('fill',domainColors[n.domain]||'#888');g.appendChild(c);const t=document.createElementNS(ns,'text');t.setAttribute('x',r+5);t.setAttribute('y','4');t.textContent=label(n).slice(0,30);g.appendChild(t);g.onclick=()=>{focusId=id;render()};g.ondblclick=()=>window.location.href=n.href;g.innerHTML+=`<title>${label(n)}\n${n.id}\ndegree=${n.degree} bridge=${n.bridgeScore}</title>`;svg.appendChild(g)}$('stats').textContent=`${ids.length} 节点 · ${visibleEdges.length} 边`;$('status').textContent=`焦点：${label(byId.get(focusId))} · ${hop}-hop`}
function setFocus(){const id=resolveInput($('focusInput').value);if(id){focusId=id;render()}else $('status').textContent='未找到唯一节点，请输入更精确的名称或路径'}
$('focusBtn').onclick=setFocus;$('focusInput').onkeydown=e=>{if(e.key==='Enter')setFocus()};$('openBtn').onclick=()=>window.location.href=byId.get(focusId).href;$('hop1').onclick=()=>{hop=1;$('hop1').classList.add('active');$('hop2').classList.remove('active');render()};$('hop2').onclick=()=>{hop=2;$('hop2').classList.add('active');$('hop1').classList.remove('active');render()};$('resetBtn').onclick=()=>{enabledDomains=new Set(domains);enabledKinds=new Set(kinds);enabledRelations=new Set(relations);makeFilters('domainFilters',domains,enabledDomains,v=>domainNames[v]||v);makeFilters('kindFilters',kinds,enabledKinds,v=>v);makeFilters('relationFilters',relations,enabledRelations,v=>relationNames[v]||v);render()};
function shortest(a,b){if(a===b)return[a];const prev=new Map([[a,null]]),q=[a];while(q.length){const cur=q.shift();for(const item of adj.get(cur)||[]){if(!edgeAllowed(item.edge)||!nodeAllowed(byId.get(item.id))||prev.has(item.id))continue;prev.set(item.id,cur);if(item.id===b){const out=[b];let x=cur;while(x){out.push(x);x=prev.get(x)}return out.reverse()}q.push(item.id)}}return null}
$('pathBtn').onclick=()=>{const a=resolveInput($('pathFrom').value),b=resolveInput($('pathTo').value),box=$('pathResult');if(!a||!b){box.textContent='起点或终点无法唯一解析。';return}const p=shortest(a,b);if(!p){box.textContent='当前筛选条件下没有路径。';return}box.innerHTML=p.map(id=>`<a class="path-node" href="${byId.get(id).href}">${label(byId.get(id))}</a>`).join(' → ')};
render();
})();
</script>
</body>
</html>'''

    (output / "index.html").write_text(html, encoding="utf-8")
    print(f"graph explorer: {len(payload_nodes)} nodes, {len(payload_edges)} edges -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
