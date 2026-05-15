from mcp_aws_sa.tools.well_architected import PILLARS, review_well_architected


def test_empty_input_returns_zero_scores() -> None:
    out = review_well_architected("")
    assert all(out["score_by_pillar"][p] == 0 for p in PILLARS)


def test_missing_iam_triggers_security_finding() -> None:
    out = review_well_architected("Lambda + DynamoDB based app behind API Gateway.")
    sec_findings = [f for f in out["findings"] if f["pillar"] == "security"]
    assert any("IAM" in f["message"] or "least privilege" in f["message"] for f in sec_findings)


def test_iam_mention_avoids_security_finding() -> None:
    out = review_well_architected(
        "Lambda + DynamoDB with strict IAM least-privilege roles per function."
    )
    sec_messages = [f["message"] for f in out["findings"] if f["pillar"] == "security"]
    assert not any("No mention of IAM" in m for m in sec_messages)


def test_missing_multi_az_triggers_reliability_finding() -> None:
    out = review_well_architected("Single-instance EC2 hosting a Node.js app.")
    rel = [f for f in out["findings"] if f["pillar"] == "reliability"]
    assert any("multi-AZ" in f["message"] for f in rel)


def test_serverless_gives_sustainability_credit() -> None:
    out = review_well_architected("Fully serverless: Lambda + DynamoDB + S3.")
    sust = [f for f in out["findings"] if f["pillar"] == "sustainability"]
    assert sust


def test_scores_in_zero_to_hundred() -> None:
    out = review_well_architected("Just a Lambda function.")
    for score in out["score_by_pillar"].values():
        assert 0 <= score <= 100


def test_summary_present() -> None:
    out = review_well_architected("Lambda + DynamoDB with IAM and multi-AZ deployment.")
    assert out["summary"]
