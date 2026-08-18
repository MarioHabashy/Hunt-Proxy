# Hunt Proxy

Hunt Proxy is a desktop web application security testing platform built with Python and PyQt5. It combines an intercepting proxy workflow with testing utilities for request analysis, attack simulation, and reporting.

This project is intended for authorized security testing, research, and training.

## Why Hunt Proxy

- Unified workflow for intercepting, modifying, replaying, and analyzing HTTP traffic.
- Security-focused tools grouped in one interface (requester, fuzzer, scanner, decoder, mapping, and reporting).
- Built-in proxy process management using mitmproxy/mitmdump.
- Modular architecture to add or improve testing tabs and scanners.

## Core Features

- Intercept and edit requests/responses in real time.
- HTTP history and WebSocket history views.
- Requester and Fuzzer style request testing.
- Mapping and attack surface analysis views.
- Param miner and JavaScript miner tooling.
- Access control, JWT, API key testing, and bypass helpers.
- Proxy rule engine:
	- Match and replace (regex)
	- Header injection
	- Request/response drop rules
	- SSL and redirect behavior controls
	- Rate limiting
- Reporting and findings workflow.

## Tab-by-Tab Unique Features

This section highlights what is uniquely valuable in each area of Hunt Proxy, with emphasis on practical pentest workflows.

| Tab | Unique capabilities |
| --- | --- |
| HTTP History | High-volume live traffic ingestion from JSONL with performance-aware batching, rich request/response inspection, built-in analysis workflows, row highlighting/notes, multi-select URL copy, and direct handoff to Requester, Fuzzer, Scanner, Param Miner, JS Miner, Key Tester, Bypass, PoC, JWT, Attack Surface, Reports, and AI chat. |
| Intercept | Real-time interception and inline editing flow integrated with the main proxy lifecycle and status controls. |
| Requester | Advanced manual replay with integrated AI chat panel, custom payload workflow, parallel/race-style testing support, request mutation utilities, and direct send-to integrations for Fuzzer, Scanner, Attack Surface, and Reports. |
| Fuzzer | Dedicated request attack workflow for iterative payload testing and high-volume request mutation. |
| Scanner | Multi-engine active scanning from one queue (XSS, SQLi, LFI, CMDi, IDOR, Upload, SSRF, XXE, NoSQLi, CORS, Open Redirect, SSTI), with traffic monitor, per-request logs/results, configurable speed/concurrency controls, and optional AI-generated payload suggestions tuned to observed filters/WAF behavior. |
| Dashboard | Recon/task orchestration hub for domain operations (including technology detection and content discovery workflows) with persistent output management, scope-aware task organization, and parallel multi-task execution support. |
| Mapping | Functional endpoint mapping with smart risk categorization, endpoint grouping, attack-oriented navigation, and recorded findings integration to keep discovery and verification linked. |
| Attack Surface | Structured endpoint inventory and triage workspace with status/priority/tag models, quick notes, filtering, export (JSON/CSV/Markdown), context actions, and function/feature flow tracking to model business logic paths such as authentication and payment flows. |
| Tools - Param Miner | Hidden parameter discovery workflow connected directly to captured traffic and replay tabs. |
| Tools - JS Miner | JavaScript-focused mining for secrets, endpoints, and risky client-side patterns. |
| Tools - Bypass | Two-mode bypass engine for WAF evasion and access-control bypass probing, with phase-driven testing, live probe telemetry, confidence scoring, and evidence-centric result views. |
| Tools - Key Tester | API key discovery and validation lab with fetch/manual/text modes, broad provider regex coverage, confidence scoring, and live service validation attempts. |
| Tools - PoC Generator | Guided exploit PoC generation for CORS, CSRF, Clickjacking, and related browser attack paths, including configurable test/bypass scenarios and practical output for reproduction/reporting. |
| Tools - JWT | Full JWT attack lab: token extraction/decoding, smart algorithm-aware attack selection, alg-none and confusion paths, weak-secret testing, claim tampering workflows, token replay analysis, and helper key material workflows. |
| Tools - Access Control | Profile-based broken access control testing by replaying captured requests across multiple identities (cookies/headers/tokens), then comparing status/length/similarity to flag likely privilege boundary failures. |
| Decoder | Smart multi-layer decode/encode workspace for payload engineering: encoding/decoding families, hashing, entropy and pattern analysis, extraction helpers (URLs/IPs/emails/hashes), and pentest-oriented transform utilities. |
| Comparer | Side-by-side request/response comparison workflow for validating behavior differences quickly. |
| Reports | Persistent per-project vulnerability report manager with lifecycle status tracking, severity/CVSS fields, markdown/text export, and quick creation from multiple tabs. |
| WS History | Dedicated WebSocket message history view for real-time channel analysis alongside HTTP traffic. |
| Notes Panel | Project-scoped, multi-note workspace embedded in the main UI to track hypotheses, testing checkpoints, and target context without leaving the tool. |

## AI Integration Highlights

- AI chat is integrated into traffic-centric workflows and can be invoked from history/replay contexts.
- Scanner can optionally request AI-tailored payload ideas based on live response fingerprints.
- Reporting includes AI-assisted draft generation for faster writeups.

## Workflow Strengths

- Cross-tab handoff model: capture once, pivot immediately into replay, scanning, bypass, PoC, JWT, access control, and reporting.
- Project-oriented persistence: findings, reports, and attack-surface tracking stay organized per target/project.
- Operator-focused design: supports both broad recon/automation and deep manual verification in the same interface.

## Project Structure

- `main.py`: main GUI entry point and proxy lifecycle handling.
- `modules/`: UI tabs, dialogs, helpers, and addon integration.
- `scans/`: scan modules for common web vulnerabilities.
- `hunt-proxy_installer.sh`: installer for Linux systems.

## Requirements

- Linux environment (installer is Linux-oriented).
- Python 3.10+ (3.11/3.12 recommended).
- pip and venv.
- mitmproxy (installed by the installer or via pip).

## Installation

### Option 1: One-line installer (recommended)

```bash
wget -O- https://raw.githubusercontent.com/MarioHabashy/Hunt-proxy/main/hunt-proxy_installer.sh | bash
```

What this does:

- Clones the repository into `/usr/share/hunt-proxy`.
- Creates a virtual environment.
- Installs system and Python dependencies.
- Creates desktop entry and launcher command (`hunt-proxy`).

### Option 2: Manual development setup

```bash
git clone https://github.com/MarioHabashy/hunt-proxy.git
cd hunt-proxy/hunt_gui
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install \
	PyQt5 requests urllib3 beautifulsoup4 mitmproxy cryptography regex \
	keyring pyOpenSSL gmpy2 brotli zstandard websocket-client wsproto \
	pyngrok boto3 botocore stripe qtawesome
python3 main.py
```

## Quick Start

1. Start the application.
2. Confirm the local proxy is running (default port: `8888`).
3. Configure your browser or testing client to use `127.0.0.1:8888`.
4. Browse the target application and inspect traffic in History/Intercept.
5. Send interesting requests to Requester, Fuzzer, or Scanner workflows.


## Uninstall

If installed with the installer script:

```bash
/usr/share/hunt-proxy/uninstall.sh
```

## Security and Legal Notice

Use this tool only on systems you own or are explicitly authorized to test. You are responsible for complying with laws, regulations, and program scope restrictions.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make focused changes with clear commit messages.
4. Open a pull request describing:
	 - Problem solved
	 - Design/implementation details
	 - Screenshots or short demo notes (if UI changes)

For larger features, open an issue first to discuss scope.

## Reporting Issues

- Use GitHub Issues for bugs, feature requests, and usability feedback.
- Include steps to reproduce, expected behavior, actual behavior, and environment details.

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.
