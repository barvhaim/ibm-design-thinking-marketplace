# Wireframes: format examples

These examples show the fidelity level and file structure only. The content is illustrative (a hypothetical expense flow), not research.

## ASCII screen

```
+----------------------------------------------------------+
| WIREFRAME · Step 1 · Trips needing receipts              |
+----------------------------------------------------------+
| [=] Expenses                                 Maya R. [v] |
|----------------------------------------------------------|
| Trips needing receipts (2)                    [A1]       |
| +------------------------------------------------------+ |
| | Austin client visit · Mar 3-5      $412   [Add >]    | |
| | Boston offsite · Feb 20            $96    [Add >]    | |
| +------------------------------------------------------+ |
| Month closes in 4 days                        [Q1]       |
|                                       [ New expense ]    |
+----------------------------------------------------------+
[A1] Users start from the trip, not from the receipt.
[Q1] Does the close date create urgency, or anxiety?
```

## HTML skeleton

Copy this skeleton, then add one `<section>` per step. It needs no build step and no network. Screens switch with `:target`, and the checkbox hides the annotations for user tests.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wireframe: Expense flow</title>
<style>
  :root{--bg:#fff;--line:#999;--fill:#eee;--mid:#ccc;--ink:#222;}
  *{box-sizing:border-box} body{margin:0;font:15px/1.4 system-ui,sans-serif;color:var(--ink);background:var(--bg)}
  .banner{padding:8px 16px;background:var(--fill);border-bottom:1px dashed var(--line);font-size:13px}
  main{max-width:960px;margin:0 auto;padding:16px}
  section{display:none;border:2px solid var(--line);padding:16px;margin-top:12px}
  section:target, body:not(:has(section:target)) #step-1{display:block}
  .step{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:#666}
  .box{border:1px solid var(--line);padding:12px;margin:8px 0}
  .img{background:var(--fill);border:1px solid var(--line);display:grid;place-items:center;height:120px}
  button,a.btn{font:inherit;border:1px solid var(--ink);background:var(--bg);padding:6px 12px;color:var(--ink);text-decoration:none}
  .note{display:inline-block;font-size:12px;background:var(--mid);padding:0 6px;margin-left:6px}
  #show-notes:not(:checked) ~ main .note{display:none}
</style></head>
<body>
<div class="banner">Low-fidelity wireframe for feedback on flow and content, not visual design. Not every control works.</div>
<input type="checkbox" id="show-notes" checked> <label for="show-notes">Show annotations</label>
<main>
  <section id="step-1">
    <div class="step">Step 1 · Trips needing receipts</div>
    <h2>Trips needing receipts (2) <span class="note">A1</span></h2>
    <div class="box">Austin client visit · Mar 3-5 · $412 <a class="btn" href="#step-2">Add receipts</a></div>
    <div class="box">Boston offsite · Feb 20 · $96 <button>Add receipts</button></div>
    <p>Month closes in 4 days <span class="note">Q1</span></p>
  </section>
  <section id="step-2">
    <div class="step">Step 2 · Attach receipts</div>
    <div class="img">[ X ] Receipt photo</div>
    <a class="btn" href="#step-1">Back</a> <a class="btn" href="#step-3">Submit for approval</a>
  </section>
  <section id="step-3">
    <div class="step">Step 3 · Confirmation</div>
    <p>Sent to your approver. You'll hear back within 2 working days.</p>
  </section>
</main>
</body></html>
```
