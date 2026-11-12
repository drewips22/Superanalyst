# Maintaining Superanalyst

The user-facing language is Indonesian. Preserve the data → patterns → decision workflow and all six analysis groups in the skill.

- Read `skills/superanalyst/SKILL.md` before changing methodology.
- Keep experimental hypotheses distinct from verified observations and calibrated coefficients. The proposed 22%, 35%, and 18% are not active model parameters.
- Cite sources for research changes and record the review date and scope. Do not turn lack of evidence into proof of no effect.
- Retain point-in-time boundaries, 90-minute outcome scope, provenance, and explicit missing values.
- Examples must remain visibly synthetic. Do not claim real-world accuracy from unit tests or synthetic examples.
- New dependencies require a concrete benefit; current tools use Python's standard library.
- After changing calculations or validation, run `python -m unittest discover -s tests -v` and the relevant example commands.
- Keep local data and forecast archives out of Git unless their inclusion is explicitly intended. The user authorized publication to the private `drewips22/Superanalyst` repository and inclusion of the UCL case study.
- Preserve frozen case inputs, code and analysis once graded. Create a new experiment directory for revisions; do not edit the existing case to make its predictions fit the result.
