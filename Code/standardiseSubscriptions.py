def rename_subs(sub):
    if "Youth" in sub:
        sub = sub.replace(sub, "Annual - Youth (age 13-17 riders)")
    elif "ACL" in sub:
        sub = sub.replace(sub, "ACL Pass 2019")
    elif "Annual" in sub or "Local365" in sub or "one-year" in sub:
        sub = sub.replace(sub, "Annual")
    elif "Found" in sub:
        sub = sub.replace(sub, "Founding Member")
    elif "Walk" in sub or "24" in sub:
        sub = sub.replace(sub, "Daily")
    elif "Weekend" in sub:
        sub = sub.replace(sub, "Weekender")
    elif "Month" in sub or "30" in sub or "31" in sub:
        sub = sub.replace(sub, "Monthly")
    elif "Explorer" in sub:
        sub = sub.replace(sub, "Explorer")
    elif "Single" in sub or "Pay-as-you-ride" in sub:
        sub = sub.replace(sub, "Single Ride") 
    elif "Semester" in sub or "Student" in sub:
        sub = sub.replace(sub, "Student Membership")
    elif "7-Day" in sub:
        sub = sub.replace(sub, "Weekly")
    else:
        return sub
    return sub
