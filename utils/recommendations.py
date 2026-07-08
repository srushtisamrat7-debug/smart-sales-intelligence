def generate_recommendations(df):

    recommendations = []

    low_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .idxmin()
    )

    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    recommendations.append(
        f"⚠ Reduce discounts for {low_profit} products."
    )

    recommendations.append(
        f"📍 Increase marketing spend in {top_region}."
    )

    recommendations.append(
        "👥 Reward top customers using a loyalty program."
    )

    recommendations.append(
        "📦 Keep additional inventory for best-selling products."
    )

    return recommendations