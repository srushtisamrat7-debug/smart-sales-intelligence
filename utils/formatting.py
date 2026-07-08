def format_currency(amount):
    return f"₹{amount:,.0f}"
def format_currency(num):
    if num >= 10000000:
        return f"₹{num / 10000000:.2f} Cr"
    elif num >= 100000:
        return f"₹{num / 100000:.2f} L"
    else:
        return f"₹{num:,.0f}"