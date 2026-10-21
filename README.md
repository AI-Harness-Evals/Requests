# Requests

A public home for investigation examples and for proposing the next question.

This repository is deliberately lightweight. An example is a self-contained write-up of a question, the evidence used to answer it, and the limits of that answer. Examples are illustrative, not benchmark scores or hiring recommendations.

## Request an investigation

Open an issue using the **Investigation request** template. A useful request is specific enough to answer and small enough to finish.

Please include:

- **The question.** One sentence, phrased as something that can be wrong.
- **The decision it informs.** What changes if the answer is yes versus no.
- **The evidence.** A public dataset, a synthetic design, or data you are authorized to share.
- **The comparison.** Baseline, treatment, and the unit of analysis.
- **The deliverable.** A short report, chart, table, or reproducible analysis.
- **The constraints.** Time, budget, privacy, and anything that must not be published.
- **The stop condition.** What result would make you stop rather than iterate.

If the request needs private data, say so in the issue without posting the data. The public output can be an aggregate or a sanitized example.

## Examples

| Example | Question |
|---|---|
| [CV-screening-600](examples/cv-screening-600/README.md) | How much do candidate name, university, degree subject, degree classification, and A-level profile move a hosted model's CV scores? |

## Example layout

```text
examples/<slug>/
  README.md          Question, method, findings, limitations
  charts/            Publication-ready PNGs
  data/              Aggregate or sanitized tables
```

## Publication and privacy

Every file added here must be safe to publish:

- Use public, synthetic, or explicitly authorized data.
- Remove private repository names, internal issue and PR numbers, run identifiers, configuration paths, credentials, endpoints, proxy details, and infrastructure internals.
- Do not publish raw prompts, personal data, or candidate records unless consent is explicit.
- Publish aggregates, synthetic rows, or scores with direct identifiers removed.
- Keep secrets out of commits, charts, notebooks, and issue bodies.
- When in doubt, omit the detail. The research claim should stand without it.

The examples are derived outputs. They do not include private evaluation tooling or private repository internals.
