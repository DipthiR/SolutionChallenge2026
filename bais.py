import pandas as pd

def detect_bias(df):
    result = {}

    target = df.columns[-1]

    sensitive_features = ['gender', 'race', 'age']

    found_feature = None

    for feature in sensitive_features:
        if feature in df.columns:
            found_feature = feature
            break

    if not found_feature:
        return {
            "bias_detected": False,
            "fairness_score": "N/A",
            "recommendation": "No sensitive feature found",
            "group_stats": {}
        }

    group_stats = df.groupby(found_feature)[target].mean().to_dict()

    values = list(group_stats.values())
    diff = max(values) - min(values)

    fairness_score = round((1 - diff) * 100, 2)

    if diff > 0.25:
        recommendation = "⚠️ High Bias Detected. Balance dataset or remove sensitive feature."
    elif diff > 0.1:
        recommendation = "⚠️ Moderate Bias. Apply fairness techniques."
    else:
        recommendation = "✅ Low Bias. Model is fair."

    return {
        "bias_detected": True,
        "feature": found_feature,
        "group_stats": group_stats,
        "fairness_score": fairness_score,
        "recommendation": recommendation
    }
