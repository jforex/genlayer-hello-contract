# OnChain AI Fact-Checker
### Built on GenLayer Bradbury Testnet

A decentralized AI fact-checking application built with GenLayer Intelligent Contracts. Submit any claim and 5 independent AI validators fetch live web data, analyze the evidence, and reach consensus on a verdict — stored permanently on the blockchain. No oracle needed.

---

## Live Demo

- **Frontend:** [https://genlayer-hello-contract.vercel.app/](https://your-vercel-url.vercel.app)
- **Contract:** `0x4F4e89d636BFC442d1fFfE488F873271b498eBBc`
- **Network:** GenLayer Bradbury Testnet
- **Demo Video:** [Watch on Loom](https://www.loom.com/share/5db7d4517e4843729ccffcea7dfee09a)

---

## What It Does

Traditional smart contracts can't reason about language or fetch live web data. GenLayer changes this.

Submit a claim → the contract fetches live web data on-chain → 5 independent AI validators analyze the evidence and reach consensus → verdict is stored permanently on the blockchain.

**Verdict options:**
- ✅ **True** — claim is supported by evidence
- ❌ **False** — claim is not supported by evidence
- ⚠️ **Uncertain** — insufficient evidence to decide

---

## How It Works

```
User submits claim + optional URL
         ↓
Contract fetches live web data (gl.get_webpage)
         ↓
5 AI validators independently analyze the claim
         ↓
Validators reach consensus (Optimistic Democracy)
         ↓
Verdict stored on-chain permanently
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Blockchain | GenLayer Bradbury Testnet |
| Smart Contract | Python (Intelligent Contract) |
| AI Consensus | gl.eq_principle.prompt_non_comparative |
| Web Fetching | gl.get_webpage (no oracle needed) |
| Frontend | HTML / CSS / JavaScript |
| Deployment | Vercel |

---

## Contract Details

**File:** `FactCheckerV2.py`

**Methods:**

| Method | Type | Description |
|---|---|---|
| `verify_claim(claim, url)` | Write | Fact-checks a claim using AI + optional live web data |
| `get_last_result()` | Read | Returns the last verdict as JSON |

**Example response from `get_last_result()`:**
```json
{
  "claim": "The Earth is flat",
  "verdict": "false",
  "reason": "Overwhelming scientific evidence supports that the Earth is an oblate spheroid."
}
```

---

## Project Structure

```
genlayer-hello-contract/
├── HelloGenLayer.py      # First deployed contract (Hello World)
├── FactChecker.py        # AI Fact-Checker V1
├── FactCheckerV2.py      # AI Fact-Checker V2 with live web fetching
├── index.html            # Frontend dApp
└── README.md             # This file
```

---

## Getting Started

### Prerequisites
- MetaMask wallet
- GenLayer Bradbury testnet configured
- Free testnet GEN tokens from the faucet

### Add GenLayer Bradbury to MetaMask
- **Network Name:** GenLayer Bradbury Testnet
- **RPC URL:** https://studio.genlayer.com:8443/api
- **Chain ID:** Check studio.genlayer.com

### Get Testnet Tokens
Go to: [testnet-faucet.genlayer.foundation](https://testnet-faucet.genlayer.foundation)

### Interact with the Contract
1. Go to [studio.genlayer.com](https://studio.genlayer.com)
2. Load the contract at `0x4F4e89d636BFC442d1fFfE488F873271b498eBBc`
3. Call `verify_claim` with any claim and optional URL
4. Wait 30-60 seconds for AI consensus
5. Call `get_last_result` to see the verdict

---

## Example Claims to Try

```
Claim: "Bitcoin is the largest cryptocurrency by market cap"
URL:   "https://coinmarketcap.com"

Claim: "The Earth is flat"
URL:   (leave empty)

Claim: "Elon Musk founded Tesla"
URL:   "https://en.wikipedia.org/wiki/Tesla,_Inc."
```

---

## Why GenLayer?

GenLayer Intelligent Contracts can:
- **Fetch live web data** directly on-chain — no oracle needed
- **Reason in natural language** using LLMs
- **Reach consensus** across 5 independent AI validators
- Handle **subjective decisions** that traditional smart contracts cannot

This makes it perfect for fact-checking, dispute resolution, prediction markets, and AI governance.

---

## Hackathon

Submitted to the **GenLayer Bradbury Builders Hackathon** (March 20 – April 3, 2026)
- Track: Onchain Justice / AI Governance
- Platform: DoraHacks

---

## Builder Program

Built as part of the **GenLayer Incentivized Builder Program**.
Learn more: [portal.genlayer.foundation](https://portal.genlayer.foundation)

---

## Author

**Christian** — [@Christi52875647](https://x.com/Christi52875647)

---

## License

MIT
