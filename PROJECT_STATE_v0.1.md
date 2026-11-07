# PROJECT_STATE_v0.1 — Bootstrap
Date: 2026-11-06
Updated: 2026-11-06 21:08 PST

## Current Overall Status
Bootstrap complete. Free-resource inventory produced and saved. Ready to claim first resources.

## Major Decisions Already Made
- Strict free / self-obtained resources only
- Android-only control surface (Galaxy Z Fold 7 class)
- Zero-trust human approval gates for irreversible or authenticated actions
- Mandatory versioning + backups + email delivery of important updates
- Target capabilities 1–12 as defined in core instructions
- Oracle Cloud Always Free is the primary compute target; GitHub Free is mandatory supporting infrastructure

## Completed Steps
- PROJECT_STATE_v0.1.md created
- FREE_RESOURCE_INVENTORY_v0.1.md created and stress-tested (Nov 2026 limits)
- GitHub repository 'self-improving-ai' created (empty)

## Key Technical Choices
- Primary runtime target: Oracle Always Free (2 OCPU / 12 GB ARM + 200 GB storage)
- Version control + automation: GitHub Free
- Model/demo storage: Hugging Face Free

## Open Issues / Blockers
- No accounts claimed yet beyond GitHub
- Oracle signup capacity and card-verification friction remain unknown until attempted
- No self-modification sandbox defined

## Exact Next Recommended Focus
Upload remaining project files to the GitHub repo, then attempt Oracle Always Free tenancy.

## Current Runtime Status (2026-11-07)
- Free A1 instance free-server Running in us-phoenix-1 AD-2
- Public IP: 129.146.4.146
- SSH access working from Termux (ed25519 key)
- System packages updated
- git, python3, pip installed
