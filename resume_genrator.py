from fpdf import FPDF

class ReadableResumePDF(FPDF):
     def header(self):
        self.set_font("Arial", "B", 13)  # was 15
        self.cell(0, 8, "YASH DUBEY", ln=True, align="C")
        self.set_font("Arial", "", 10)  # was 11
        self.cell(0, 6, "Artificial Intelligence & Machine Learning Enthusiast | Aspiring AI/ML Engineer", ln=True, align="C")
        self.ln(4)

     def add_section(self, title, content):
        self.set_font("Arial", "B", 10)  # was 11
        self.cell(0, 6, title, ln=True)
        self.set_font("Arial", "", 9)   # was 10
        for line in content.strip().split("\n"):
            self.multi_cell(0, 5, line.strip())  # line spacing reduced from 5.5 to 5
        self.ln(1)

resume_text = """
Phone: +91 8269962756 | Email: yashdubey356ab@gmail.com
Location: Bhopal, India
LinkedIn: www.linkedin.com/in/yash-dubey-46856b25a | GitHub: https://github.com/thevisualizer-yash

---

PROFESSIONAL SUMMARY
Aspiring AI/ML Engineer and B.Tech undergraduate in Artificial Intelligence and Machine Learning at LNCT, Bhopal. Proficient in Python and Java, with hands-on experience in deep learning, GANs, and PyTorch Lightning. Skilled in developing machine learning models, working with datasets like MNIST, and applying key AI concepts such as CNNs, supervised learning, and PCA. Demonstrated ability to complete academic and self-driven AI projects, participate in hackathons, and collaborate in team-based environments. Eager to apply AI knowledge to solve real-world problems through internships and innovative projects.

---

TECHNICAL SKILLS
Languages: Python, Java(Basic), SQL
Libraries/Frameworks: PyTorch, PyTorch Lightning, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn
Tools: Jupyter Notebook, Google Colab, Git, VS Code , AWS 
Databases: MySQL
Concepts: Supervised/Unsupervised Learning, Deep Learning, CNN, GANs, PCA, Clustering, Model Evaluation

---

SOFT SKILLS
Problem Solving, Teamwork, Leadership, Communication, Time Management, Adaptability, Critical Thinking, Collaboration,  Fast
 Learner

---

EDUCATION
B.Tech in AI and ML | LNCT, Bhopal
Expected Graduation: June 2026

---

PROJECTS
A Comparative Study and Implementation of Different GAN Models using PyTorch Lightning
Tech: PyTorch Lightning, Python, MNIST, Matplotlib
- Built and compared multiple GAN architectures to evaluate training stability and output quality.
- Used PyTorch Lightning to streamline training and ensure modularity.
- Visualized generator outputs to track convergence and sample improvement over epochs.

PDF Resume Generator using Python
Tech: Python, FPDF, OOP
- Built a Python tool to generate professional PDF resumes using fpdf.
- Used object-oriented design to modularize layout, styling, and content sections.
- Produced clean, ATS-friendly resumes with customizable text and structure.

Netflix Landing Page Clone
Tech: HTML, CSS
- Recreated Netflixs homepage using semantic HTML and modern CSS.
- Ensured clean, accessible code following web development best practices.

---

CERTIFICATIONS & ACHIEVEMENTS
- Microsoft : Azure Fundamentals
- AWS Cloud Practitioner
- Top performer in AI/ML coursework
- Regular hackathon participations.

---

LANGUAGES
English (Professional), Hindi (Native)
"""

# Generate PDF with slightly larger text for readability
pdf = ReadableResumePDF(format='A4')
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()

# Add content
sections = resume_text.split('---')
for section in sections:
    if section.strip():
        lines = section.strip().split("\n", 1)
        title = lines[0].strip()
        content = lines[1] if len(lines) > 1 else ""
        pdf.add_section(title, content)
# Save the readable version
readable_path = "Yash_Dubey_Resume_Readable.pdf"

pdf.output("Yash_Resume_Final.pdf")


readable_path
