# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import typing
import json

class FactChecker(gl.Contract):
    last_claim: str
    last_verdict: str
    last_reason: str

    def __init__(self):
        self.last_claim = ""
        self.last_verdict = ""
        self.last_reason = ""

    @gl.public.write
    def verify_claim(self, claim: str, evidence_url: str = "") -> typing.Any:
        """Fact-check any claim using AI + optional web evidence"""
        self.last_claim = claim

        prompt = f"""You are an impartial on-chain fact-checker.
Claim: "{claim}"

"""

        if evidence_url:
            try:
                web_data = gl.nondet.web.get(evidence_url)
                prompt += f"Evidence from {evidence_url}:\n{web_data[:2000]}...\n\n"
            except:
                prompt += "Could not fetch evidence URL.\n\n"

        prompt += """Analyze the claim and evidence. Respond with **ONLY** this exact JSON (no extra text):
{
  "verdict": "true" | "false" | "uncertain",
  "reason": "one short sentence explanation"
}"""

        # Non-comparative LLM call (official GenLayer pattern for simple AI responses)
        raw_result = gl.eq_principle.prompt_non_comparative(
            lambda: prompt,
            task="Return only valid JSON. Do not add explanations outside the JSON."
        )

        # Store the result
        self.last_verdict = raw_result
        try:
            parsed = json.loads(raw_result)
            self.last_reason = parsed.get("reason", raw_result)
        except:
            self.last_reason = raw_result

        print(f"✅ Fact checked: {claim} → {self.last_verdict}")
        return raw_result

    @gl.public.view
    def get_last_result(self) -> dict:
        return {
            "claim": self.last_claim,
            "verdict": self.last_verdict,
            "reason": self.last_reason
        }
