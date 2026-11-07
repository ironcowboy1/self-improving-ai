# FREE_RESOURCE_INVENTORY_v0.1
Date: 2026-11-06
Status: Stress-tested against current free-tier limits (checked Nov 2026)

## Goal
Identify the minimal set of free / always-free resources that can later support a 24/7 Android-controllable runtime for the self-improving AI system.

## Priority Ranking (for this project)

### 1. Primary Compute + Storage Candidate: Oracle Cloud Always Free
**Current limits (enforced mid-2026):**
- Ampere A1 (ARM): total 2 OCPU + 12 GB RAM (1,500 OCPU-hours + 9,000 GB-hours/month)
- Can be one 2/12 VM or two 1/6 VMs
- 2 × AMD Micro VMs (1/8 OCPU, 1 GB each) as fallback
- 200 GB total block storage (boot volumes count against this)
- 10 TB/month outbound data
- Object storage + Autonomous DB also available in Always Free

**Stress-test results:**
- Still the only major cloud with genuine permanent free always-on compute of usable size.
- Known friction: signup capacity shortages in popular regions, occasional idle reclamation risk, complex console, card required for signup in most regions.
- Android control: OCI CLI + API fully usable from Termux / cloud shell; mobile browser works for console.
- Risk level: Medium (capacity + reclamation). Highest leverage if obtained.

**Verdict:** Highest priority to attempt. One successful Always Free tenancy is the strongest foundation for 24/7 operation.

### 2. Supporting / Fallback Resources

**GitHub Free**
- Unlimited public + private repos
- 2,000 Actions minutes/month (private; public unlimited)
- 120 Codespaces core-hours + 15 GB storage/month
- Excellent for code versioning, CI, and light automation
- Android: GitHub app + browser + Termux git fully functional
- Risk: Low. Must use for version control and backups regardless.

**Hugging Face Free**
- Free CPU Basic Spaces (2 vCPU / 16 GB, ephemeral disk)
- ZeroGPU limited free quota (≈5 min/day)
- 100 GB private storage
- Good for model hosting, demos, light inference experiments
- Persistent disk on Spaces is paid only
- Android: fully usable via browser + HF app / API
- Risk: Low for storage and demos; not suitable as primary always-on runtime.

**Render Free**
- Free web services (512 MB, spins down after 15 min idle)
- 750 instance-hours/month
- Free Postgres expires after 30 days
- Useful only for temporary endpoints or demos
- Not viable for 24/7 autonomous agent

**Railway / Fly.io**
- Railway: $1/month credit after trial → effectively not free for continuous use
- Fly.io: no free tier for new accounts (trial only)
- Rejected for primary runtime.

### 3. Explicitly Rejected for Primary Runtime
- Any service that sleeps on idle (Render free, most free PaaS)
- Services requiring ongoing paid credits after trial
- GPU-only free tiers with tiny daily quotas (insufficient for continuous self-improvement loops)

## Recommended Minimal Claim Set (in order)
1. GitHub Free account (immediate, zero friction) → code + versioning + Actions
2. Oracle Cloud Always Free tenancy (highest value, highest friction) → primary 24/7 compute + storage
3. Hugging Face Free account → model/dataset storage + experimental Spaces

## Next Action After This Inventory
Attempt to secure GitHub Free (trivial) and then Oracle Always Free, documenting every friction point and fallback in project state.

All claims must remain under user ownership and zero-trust approval for any irreversible or paid action.
