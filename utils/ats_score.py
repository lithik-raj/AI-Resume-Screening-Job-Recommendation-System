def calculate_ats(skills):

    max_skills = 16

    score = (len(skills) / max_skills) * 100

    return round(score, 2)