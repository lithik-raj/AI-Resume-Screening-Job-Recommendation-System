skills_db = [

    "python",
    "sql",
    "mysql",
    "machine learning",
    "deep learning",
    "data science",
    "html",
    "css",
    "javascript",
    "react",
    "java",
    "flask",
    "docker",
    "aws",
    "git",
    "github"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill in text:
            found_skills.append(skill)

    return found_skills