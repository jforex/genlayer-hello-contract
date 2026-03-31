# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
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
    def verify_claim(self, claim: str, url: str = "") -> None:
        """Fact-check any claim using AI + optional live web evidence."""

        def build_prompt():
            evidence = ""
            if url:
                try:
                    evidence = gl.get_webpage(url, mode="text")[:2000]
                except:
                    evidence = ""

            return f"""You are an impartial on-chain fact-checker.
Claim: "{claim}"
{f'Evidence from {url}: {evidence}' if evidence else ''}

Respond using ONLY the following JSON format, nothing else:
{{
  "verdict": "true" or "false" or "uncertain",
  "reason": "one short sentence explanation"
}}
Don't include any other words or characters. Output must be only JSON.
This result should be perfectly parseable by a JSON parser without errors."""

        raw_result = gl.eq_principle.prompt_non_comparative(
            build_prompt,
            task="Fact-check the claim and return only valid JSON with verdict and reason fields.",
            criteria="The verdict must be true, false, or uncertain. The reason must be a short sentence."
        )

        verdict = "uncertain"
        reason = str(raw_result)
        try:
            parsed = json.loads(raw_result)
            verdict = str(parsed.get("verdict", "uncertain"))
            reason = str(parsed.get("reason", str(raw_result)))
        except:
            pass

        self.last_claim = claim
        self.last_verdict = verdict
        self.last_reason = reason

        print(f"Verdict: {verdict} | Claim: {claim}")

    @gl.public.view
    def get_last_result(self) -> str:
        return json.dumps({
            "claim": self.last_claim,
            "verdict": self.last_verdict,
            "reason": self.last_reason
        })
