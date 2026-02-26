from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

profile_data = {
    "name": "Monark Mehta",
    "title": "Software Engineer",
    "roles": ["Software Engineer", "Data Scientist", "Python Developer", "Industrial Analytics", "Real-Time Systems"],
    "subtitle": "Python Developer · Data Scientist · Industrial Analytics · Real-Time Systems",
    "summary": "Software Engineer and Data Scientist with 3+ years of experience building scalable backend systems, industrial analytics platforms, and real-time monitoring solutions for power plant operations. Proficient in Python development, machine learning, data modeling, and computer vision. I design and deliver high-impact engineering software that combines backend architecture, data science, and AI to solve complex real-world operational challenges. Open to opportunities in Software Development, Data Science, and AI.",
    "email": "monarkmehta2001@gmail.com",
    "phone": "8279445436",
    "linkedin": "https://www.linkedin.com/in/monark-mehta-374814193/?isSelfProfile=true",
    "github": "https://github.com/monarkmehta",
    "location": "India",
    "experience": [
        {
            "company": "GE Vernova",
            "role": "Software Engineer",
            "period": "Feb 2023 – Present",
            "location": "India",
            "projects": [
                {
                    "name": "AHOPM – Asset Health & Operational Performance Monitoring",
                    "description": "Enterprise-level industrial monitoring platform for thermal power plants.",
                    "highlights": [
                        "Developed backend modules for real-time equipment monitoring and health analytics",
                        "Implemented KPIs: Boiler Efficiency, Turbine Efficiency, Heat Rate, Performance Deviation",
                        "Designed data ingestion pipelines for high-frequency sensor data",
                        "Integrated OPC & Modbus industrial communication systems",
                        "Built RESTful services using Flask for data processing layers",
                        "Developed real-time Grafana dashboards and anomaly detection logic",
                        "Containerized services using Docker for scalable deployment"
                    ],
                    "tech": ["Python", "Flask", "MS SQL Server", "Grafana", "OPC", "Modbus", "Docker", "Linux"]
                },
                {
                    "name": "Boiler Lifetime Monitoring (BLM)",
                    "description": "Standalone engineering software for creep and fatigue life estimation of boiler components.",
                    "highlights": [
                        "Designed full backend architecture using Python and Flask",
                        "Implemented thermal stress calculation and creep damage accumulation modeling",
                        "Fatigue damage estimation and Remaining Useful Life (RUL) prediction",
                        "Integrated statistical and ML-based predictive models",
                        "Structured SQL database for lifecycle data management"
                    ],
                    "tech": ["Python", "Flask", "Pandas", "NumPy", "ML Algorithms", "MS SQL Server", "Grafana", "Docker"]
                },
                {
                    "name": "Mill Response Time Analytics",
                    "description": "Performance modeling system for coal mill dynamic behavior analysis.",
                    "highlights": [
                        "Developed time-series models to evaluate mill load response",
                        "Calculated mill delay and dynamic response characteristics",
                        "Implemented smoothing and signal processing techniques",
                        "Identified degradation patterns using statistical analytics"
                    ],
                    "tech": ["Python", "SQL", "Time-Series Analysis", "Statistical Modeling", "Grafana"]
                }
            ]
        },
        {
            "company": "StampMyVisa",
            "role": "Software Developer Intern",
            "period": "Aug 2022 – Jan 2023",
            "location": "Remote",
            "projects": [
                {
                    "name": "AI-Driven Visa Processing Automation",
                    "description": "Developed AI-powered automation tools to streamline visa processing workflows and reduce manual data handling.",
                    "highlights": [
                        "Developed AI-powered chatbot using RASA NLP framework to automate customer queries",
                        "Designed conversational flows and intent classification models",
                        "Built OCR-based document extraction pipeline for automated form processing",
                        "Implemented backend APIs for document validation and workflow automation",
                        "Improved operational efficiency by reducing manual data handling processes",
                        "Collaborated with product and backend teams to enhance user experience"
                    ],
                    "tech": ["Python", "RASA", "NLP", "OCR", "Flask", "REST APIs"]
                }
            ]
        }
    ],
    "projects": [
        {
            "name": "Social Distancing Detector",
            "description": "AI-powered real-time computer vision monitoring system with person detection, distance measurement, and crowd density heatmap generation.",
            "tech": ["Python", "OpenCV", "Deep Learning", "Flask", "REST APIs", "Docker"],
            "highlights": ["Published in MDPI – Future Internet Journal", "Contributed to Springer Book Chapter"],
            "type": "AI/ML"
        },
        {
            "name": "E-Commerce Web App (Mobile Shoppe)",
            "description": "Full-stack web application for online mobile shopping with user auth, product listings, cart management, and admin interface.",
            "tech": ["PHP", "MySQL", "HTML", "CSS", "JavaScript", "Bootstrap"],
            "highlights": ["User authentication & authorization", "Shopping cart and order management", "Admin product management interface"],
            "type": "Web"
        }
    ],
    "skills": {
        "Programming Languages": ["Python", "Java Core", "SQL", "PHP"],
        "Backend Development": ["Flask", "REST APIs", "Microservices Architecture"],
        "Data Science & Analytics": ["Pandas", "NumPy", "Scikit-learn", "Machine Learning", "Statistical Modeling", "Time-Series Analysis", "Data Analysis", "Data Modeling"],
        "Frontend & Web": ["HTML", "CSS", "JavaScript", "Bootstrap"],
        "AI & Computer Vision": ["Computer Vision", "OpenCV", "Deep Learning", "RASA"],
        "Industrial Technologies": ["OPC Integration", "Modbus Communication", "IIoT Data Systems"],
        "Databases": ["MS SQL Server", "MSSQL", "MySQL", "Firebase"],
        "Visualization": ["Grafana", "Data Visualization"],
        "DevOps & Tools": ["Docker", "Git", "GitHub", "Linux", "Unix"]
    },
    "interests": [
        "Industrial AI Systems",
        "Predictive Maintenance",
        "Backend Architecture Design",
        "Machine Learning for Engineering",
        "Real-Time Monitoring Platforms",
        "Data Analysis",
        "Data Modeling",
        "Cloud Engineering",
        "Performance Optimization Systems"
    ],
    "publications": [
        {
            "title": "Social Distancing Detection using Computer Vision & Deep Learning",
            "journal": "MDPI – Future Internet Journal",
            "type": "Journal Paper",
            "url": "https://www.mdpi.com/1999-5903/13/12/308"
        },
        {
            "title": "Social Distancing Detection using Computer Vision & Deep Learning",
            "journal": "Springer Book Chapter",
            "type": "Book Chapter",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-16364-7_9"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', profile=profile_data)

@app.route('/api/profile')
def api_profile():
    return jsonify(profile_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
