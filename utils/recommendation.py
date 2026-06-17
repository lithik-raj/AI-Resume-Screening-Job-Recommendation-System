job_map = {

    "Data Scientist":[
        "Machine Learning Engineer",
        "AI Engineer",
        "Data Analyst"
    ],

    "Web Developer":[
        "Frontend Developer",
        "UI Developer",
        "React Developer"
    ],

    "Java Developer":[
        "Backend Developer",
        "Spring Boot Developer"
    ]
}

def recommend_jobs(role):

    return job_map.get(role, [])