from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Your Name', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Backend Developer', 0, 1, 'C')
        self.cell(0, 10, 'Dallas, USA  •  (123) 456-789  •  yourname@resumeworded.com  •  linkedin.com/in/your-profile', 0, 1, 'C')
        self.ln(10)
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)
    
    def section_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, body)
        self.ln(5)

pdf = PDF()
pdf.add_page()

# Experience Section
pdf.section_title('EXPERIENCE')

experience_content = [
    {
        "title": "Coached.com\nLos Angeles, USA\nJanuary 2021 - Present\nSenior Backend Developer",
        "body": (
            "Optimized application's data processing speed by over 40% using advanced cache management techniques in Redis.\n"
            "Engineered and implemented an API integration solution that improved system interoperability and reduced integration time by 35%.\n"
            "Modernized outdated code, improving system stability and increasing runtime efficiency by 20%. Used tools like Node.js, Java and Python.\n"
            "Mentored a team of junior developers, introducing code review processes that improved code quality by 30%.\n"
            "Deployed CI/CD pipelines in Jenkins, decreasing code integration time by 25% and increasing the productivity of the development team."
        )
    },
    {
        "title": "Resume Worded\nNew York City, USA\nApril 2018 - December 2020\nMiddleware Developer",
        "body": (
            "Led middleware development using Java and Spring, resulting in a 60% improvement in request handling efficiency.\n"
            "Designed and implemented secure database transactions which reduced data breaches by 45%.\n"
            "Achieved a 20% improvement in system performance through effective SQL optimization."
        )
    },
    {
        "title": "Microsoft\nFort Worth, USA\nJune 2015 - March 2018\nJunior Developer",
        "body": (
            "Introduced automated testing strategies, reducing manual testing time by 70%.\n"
            "Enhanced user interface responsiveness, improving user satisfaction by 35%.\n"
            "Participated in code review sessions, reducing coding errors by 24%."
        )
    }
]

for exp in experience_content:
    pdf.section_body(exp["title"])
    pdf.section_body(exp["body"])

# Education Section
pdf.section_title('EDUCATION')

education_content = (
    "Resume Worded University\nIndianapolis, USA\nMay 2015\nMaster of Science in Computer Engineering\n"
    "Specialization in Software Development and Database Management\n\n"
    "Resume Worded University\nSan Francisco, USA\nMay 2013\nBachelor of Science in Computer Science\n"
    "Minors in Mathematics\nAwards: Resume Worded Academic Achievement Award (Top 5% of Class)"
)

pdf.section_body(education_content)

# Skills Section
pdf.section_title('SKILLS')

skills_content = (
    "Programming Languages: Java, C#, Python, JavaScript, TypeScript, SQL, C++\n"
    "Web Technologies: HTML, CSS, XML, JSON, RESTful APIs, SOAP\n"
    "Database Management: MySQL, PostgreSQL, MongoDB, Microsoft SQL Server, Oracle Database, SQLite\n"
    "Tools & Frameworks: Node.js, .NET, Django, Spring, Ruby on Rails, AWS, Docker, Git"
)

pdf.section_body(skills_content)

# Other Section
pdf.section_title('OTHER')

other_content = (
    "Certifications: Oracle Certified Professional, Java SE 8 Programmer; AWS Certified Solutions Architect\n"
    "Professional Affiliations: Member, Association for Computing Machinery (ACM); Member, Python Software Foundation\n"
    "Volunteering: Mentor, Code.org; Volunteer Developer, Code for America\n"
    "Projects: Lead developer for open-source project contributing to Python ecosystems, with 1,000+ stars on GitHub"
)

pdf.section_body(other_content)

# Save PDF
pdf_output_path = "resume.pdf"
pdf.output(pdf_output_path)

