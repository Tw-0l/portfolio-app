import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64
from streamlit_option_menu import option_menu
import numpy as np
import io

# Page configuration
st.set_page_config(
    page_title="Abdullah Altuwayjiri - Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- LOAD CSS, PDF & PROFILE PIC ----
def css_styling():
    # Custom CSS for styling
    st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-text {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(to right, #4776E6, #8E54E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subheader {
        font-size: 1.5rem;
        color: #8E54E9;
        font-weight: 600;
    }
    .project-card {
        border-radius: 10px;
        border: 1px solid rgba(130, 138, 146, 0.2);
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: rgba(255, 255, 255, 0.03);
        transition: transform 0.3s;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    .icon-link {
        color: #8E54E9;
        margin-right: 1rem;
        font-size: 1.2rem;
    }
    .cert-card {
        border-radius: 8px;
        border: 1px solid rgba(130, 138, 146, 0.2);
        padding: 1rem;
        margin-bottom: 0.8rem;
        background-color: rgba(255, 255, 255, 0.03);
    }
    .metric-card {
        border-radius: 10px;
        border: 1px solid rgba(130, 138, 146, 0.2);
        padding: 1.5rem;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.03);
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4776E6;
    }
    .metric-label {
        font-size: 1rem;
        color: #666;
    }
    .skill-pill {
        background-color: rgba(71, 118, 230, 0.1);
        border-radius: 20px;
        padding: 0.3rem 0.8rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        display: inline-block;
        font-size: 0.85rem;
        color: #4776E6;
    }
    </style>
    """, unsafe_allow_html=True)

css_styling()

# --- FUNCTIONS ---
def create_download_link(file_path):
    with open(file_path, "rb") as file:
        encoded_file = base64.b64encode(file.read()).decode()
    
    href = f'<a href="data:application/pdf;base64,{encoded_file}" download="{file_path}" class="btn btn-primary">Download Resume</a>'
    return href

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- YOUR INFORMATION --- 
# Your Information
YOUR_NAME = "ABDULLAH ALTUWAYJIRI"
YOUR_TITLE = "Data Scientist & Analyst"
YOUR_EMAIL = "A.abdullahtw@gmail.com"
YOUR_LINKEDIN = "https://www.linkedin.com/in/abdullah-aaltuwayjiri"
YOUR_GITHUB = "https://github.com/Tw-0l"
YOUR_PHONE = "+966 54 714 5479"
YOUR_BIO = """
Dedicated Data Scientist with expertise in machine learning, data analysis, and visualization. 
Currently working as a Data Analyst at SadaaCX where I calculate customer satisfaction metrics, 
develop tracking systems, and conduct text analysis of survey responses. Previously worked as a 
Data Scientist at Sequencive/NONPHI developing predictive models and implementing machine 
learning solutions.

With a strong foundation in Information Systems and specialized training through Tuwaiq Data Science 
and Machine Learning Bootcamp, I excel at transforming complex data into actionable insights 
that drive business decisions.
"""

# Skills Data
TECHNICAL_SKILLS = {
    "Programming": ["Python", "SQL"],
    "Data Analysis": ["Pandas", "NumPy", "Excel"],
    "Machine Learning": ["XGBoost", "CatBoost", "LGBM", "LSTM", "KNN", "K-means"],
    "Data Visualization": ["Matplotlib", "Plotly", "Seaborn", "Power BI"],
    "AI & NLP": ["TensorFlow", "NLP", "Text Analysis", "Deep Learning"],
    "Tools": ["Streamlit", "FastAPI", "Dtale"],
    "Skills": ["Data Mining", "Data Storytelling", "Data Tracking"]
}

# Projects Data - UPDATED
PROJECTS = [
    {
        "title": "Friday Night",
        "description": "An intelligent entertainment recommendation system designed specifically for weekend relaxation. This Streamlit application helps users discover personalized movie, music, restaurant, and activity suggestions for the perfect Friday night experience, based on their preferences, mood, and social context.",
        "technologies": ["Python", "Streamlit", "Pandas", "Scikit-learn"],
        "github_link": "https://github.com/Tw-0l/Friday-Night",
        "demo_link": "https://friday-night.streamlit.app/",
        "image": "https://via.placeholder.com/600x400?text=Friday+Night",
        "key_metrics": "Created a full entertainment recommendation system with mood-based suggestions for movies, music, dining and activities"
    },
    {
        "title": "Job Postings in Saudi Arabia",
        "description": "An interactive data analysis application that provides insights into the Saudi Arabian job market using data collected from Jadarat. This tool helps job seekers understand regional job distribution, salary expectations, and market trends.",
        "technologies": ["Streamlit", "Pandas", "Matplotlib", "Seaborn"],
        "github_link": "https://github.com/Tw-0l/job_postings_SA",
        "demo_link": "https://abdullah0altuwayjiri.streamlit.app/",
        "image": "https://via.placeholder.com/600x400?text=Job+Postings",
        "key_metrics": "Visualized employment trends across different regions of Saudi Arabia and salary ranges for fresh graduates"
    },
    {
        "title": "World Happiness Analysis",
        "description": "A comprehensive data analysis project exploring the World Happiness Report dataset to uncover global patterns, correlations, and insights into factors affecting national happiness scores across different countries and regions.",
        "technologies": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn"],
        "github_link": "https://github.com/Tw-0l/Happiness-Report",
        "demo_link": None,
        "image": "https://via.placeholder.com/600x400?text=World+Happiness",
        "key_metrics": "Identified key happiness indicators and regional patterns across different countries and regions"
    },
    {
        "title": "Football Players' Transfer Fee Prediction",
        "description": "A machine learning project that predicts football players' transfer fees based on performance metrics, player attributes, market conditions, and historical transfer data. This model helps clubs, agents, and football analysts estimate player valuations in the dynamic transfer market.",
        "technologies": ["Python", "Pandas", "NumPy", "Scikit-learn", "XGBoost", "LightGBM", "TensorFlow/PyTorch"],
        "github_link": "https://github.com/Tw-0l/Football-Players-Transfer-Fees-Predictions",
        "demo_link": None,
        "image": "https://via.placeholder.com/600x400?text=Football+Transfer",
        "key_metrics": "Developed ML models to predict player transfer fees with comprehensive analysis of performance metrics and market factors"
    },
    {
        "title": "Contract Generation using LSTM",
        "description": "This graduation project implements an advanced contract generation system using Long Short-Term Memory (LSTM) neural networks. The system is designed to learn from existing contract templates and generate new, legally sound contract documents based on user specifications.",
        "technologies": ["Python", "TensorFlow/Keras", "LSTM", "NLP"],
        "github_link": None,
        "demo_link": None,
        "image": "https://via.placeholder.com/600x400?text=Contract+Generation",
        "key_metrics": "Developed an automated contract generation system with template learning, customization options, and multi-format export capabilities"
    }
]

# Certifications Data
CERTIFICATIONS = [
    {
        "name": "Data Scientist Certification",
        "issuer": "Tuwaiq Academy",
        "date": "2024",
        "link": "https://drive.google.com/uc?export=download&id=1mhgWP4HiBWge8uKxWBGCzFn_km2P3iJY"
    },
    {
        "name": "Artificial Intelligence Analyst Certificate",
        "issuer": "IBM",
        "date": "2024",
        "link": "https://www.credly.com/badges/1e4df6b3-c410-4cd3-a723-e4c56f0bef59/public_url"
    }
]

# Experience Data
EXPERIENCE = [
    {
        "position": "Data Analyst",
        "company": "SadaaCX",
        "duration": "October 2024 - Present",
        "description": [
            "Calculate customer satisfaction metrics for performance evaluation of public entities",
            "Develop and maintain trackers to monitor data collection progress",
            "Conduct in-depth text analysis of survey responses, extracting insights and trends",
            "Compile comprehensive final reports summarizing project findings with actionable recommendations"
        ]
    },
    {
        "position": "Data Scientist",
        "company": "Sequencive / NONPHI",
        "duration": "Jan 2024 - Jun 2024",
        "description": [
            "Developed predictive models for client applications",
            "Performed data analysis on large datasets to identify patterns and trends",
            "Implemented machine learning algorithms for classification and prediction tasks",
            "Generated client insights through statistical analysis and data visualization"
        ]
    }
]

# Education Data
EDUCATION = [
    {
        "degree": "Bachelor Degree of Information System (IS)",
        "institution": "Prince Sattam Bin Abdulaziz University",
        "year": "2024",
        "details": "College of Computer Engineering and Science"
    },
    {
        "degree": "Data Science and Machine Learning Bootcamp",
        "institution": "Tuwaiq Academy",
        "year": "2024",
        "details": "Gained hands-on experience in data analysis, predictive modeling, and deep learning for decision-making"
    }
]

# --- SIDEBAR ---
with st.sidebar:
    # Replace with your profile picture
    # profile_pic = Image.open("profile.jpg")  # Uncomment when you have a profile picture
    # st.image(profile_pic, width=150)
    
    st.markdown(f"<h2 style='text-align: center;'>{YOUR_NAME}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #8E54E9;'>{YOUR_TITLE}</p>", unsafe_allow_html=True)
    
    # Navigation
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects", "Skills", "Experience", "Education", "Contact"],
        icons=["person", "code-slash", "gear", "briefcase", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#8E54E9", "font-size": "16px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "rgba(142, 84, 233, 0.1)", "color": "#8E54E9"},
        }
    )
    
    st.markdown("---")
    
    # Download Resume button
    # st.markdown(create_download_link("your_resume.pdf"), unsafe_allow_html=True)  # Uncomment when you have a resume file
    st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <a href="https://drive.google.com/uc?export=download&id=1zR2vwm7djOGFL4wIZchPzBEO3xf76_28" target="_blank" 
    class="btn btn-primary" style='background-color: #8E54E9; color: white; 
    padding: 8px 16px; border-radius: 4px; text-decoration: none; font-weight: 500;'>
    Download Resume</a>
</div>
""", unsafe_allow_html=True)
    
    # Contact info in sidebar
    st.markdown("---")
    st.markdown("<h6 style='text-align: center;'>Contact</h6>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<a href='{YOUR_LINKEDIN}' target='_blank'><i class='fab fa-linkedin fa-2x'></i> LinkedIn</a>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<a href='{YOUR_GITHUB}' target='_blank'><i class='fab fa-github fa-2x'></i> GitHub</a>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='text-align: center; font-size: 0.9rem;'><i class='fas fa-envelope'></i> {YOUR_EMAIL}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 0.9rem;'><i class='fas fa-phone'></i> {YOUR_PHONE}</p>", unsafe_allow_html=True)

# --- MAIN PAGE CONTENT ---
# ABOUT SECTION
if selected == "About":
    st.markdown("<h1 class='header-text'>About Me</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"<p style='font-size: 1.1rem; line-height: 1.6;'>{YOUR_BIO}</p>", unsafe_allow_html=True)
        
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
        st.markdown("<h3 class='subheader'>My Journey</h3>", unsafe_allow_html=True)
        st.write("""
        My data science journey began with a strong foundation in Information Systems at Prince Sattam Bin Abdulaziz University. 
        I enhanced my skills through specialized training at Tuwaiq Academy's Data Science and Machine Learning Bootcamp, 
        where I gained hands-on experience in data analysis, predictive modeling, and deep learning.
        
        I've since applied these skills in professional settings at Sequencive/NONPHI and SadaaCX, developing predictive models, 
        performing in-depth data analysis, and generating actionable insights for clients and stakeholders.
        
        I'm passionate about using data to solve complex problems and believe in the power of data-driven decision making to 
        transform businesses and improve outcomes.
        """)
    
    with col2:
        # Key metrics/stats about your work
        metrics = [
            {"value": "5+", "label": "Projects Completed"},
            {"value": "2", "label": "Professional Roles"},
            {"value": "2", "label": "Certifications"}
        ]
        
        for metric in metrics:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            <div style='height: 20px;'></div>
            """, unsafe_allow_html=True)
    
    # Languages
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Languages</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='background-color: rgba(71, 118, 230, 0.1); padding: 15px; border-radius: 10px;'>
            <h4>Arabic</h4>
            <p>Native</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: rgba(71, 118, 230, 0.1); padding: 15px; border-radius: 10px;'>
            <h4>English</h4>
            <p>Fluent</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Personal touch
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>What Drives Me</h3>", unsafe_allow_html=True)
    st.write("""
    I'm passionate about using data science and machine learning to solve real-world problems. I'm particularly 
    interested in how AI and data analytics can transform traditional sectors like real estate, sports analytics, 
    and legal document processing, as evidenced by my portfolio projects.
    
    My goal is to continue expanding my expertise in predictive modeling and deep learning while applying these 
    skills to create impactful solutions that drive business value and innovation.
    """)

# PROJECTS SECTION
elif selected == "Projects":
    st.markdown("<h1 class='header-text'>My Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p>A collection of my data science projects showcasing my skills and expertise.</p>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Interactive project filter
    project_categories = ["All"] + list(set([tech for project in PROJECTS for tech in project["technologies"]]))
    selected_category = st.selectbox("Filter by technology:", project_categories)
    
    # Display projects (filtered if necessary)
    projects_to_display = PROJECTS if selected_category == "All" else [
        project for project in PROJECTS if selected_category in project["technologies"]
    ]
    
    # Use native Streamlit components instead of complex HTML
    for project in projects_to_display:
        with st.container():
            # Create a styled box with CSS
            st.markdown("<div style='border-radius: 10px; border: 1px solid rgba(130, 138, 146, 0.2); padding: 1.5rem; margin-bottom: 1rem; background-color: rgba(255, 255, 255, 0.03);'>", unsafe_allow_html=True)
            
            # Project title
            st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)
            
            # Project description
            st.markdown(f"<p>{project['description']}</p>", unsafe_allow_html=True)
            
            # Technologies
            tech_html = "".join([f'<span class="skill-pill">{tech}</span>' for tech in project["technologies"]])
            st.markdown(f"<div style='margin: 15px 0;'>{tech_html}</div>", unsafe_allow_html=True)
            
            # Impact
            st.markdown(f"<p><strong>Impact:</strong> {project.get('key_metrics', 'N/A')}</p>", unsafe_allow_html=True)
            
            # Links
            links_html = ""
            if project.get("github_link"):
                links_html += f'<a href="{project["github_link"]}" target="_blank" class="icon-link"><i class="fab fa-github"></i> GitHub</a>'
            if project.get("demo_link"):
                links_html += f'<a href="{project["demo_link"]}" target="_blank" class="icon-link"><i class="fas fa-external-link-alt"></i> Live Demo</a>'
            
            st.markdown(f"<div style='margin-top: 15px;'>{links_html}</div>", unsafe_allow_html=True)
            
            # Close the box
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Add space between projects
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Interactive visualization of projects by technology
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Technologies Used Across Projects</h3>", unsafe_allow_html=True)
    
    # Prepare data for visualization
    tech_counts = {}
    for project in PROJECTS:
        for tech in project["technologies"]:
            tech_counts[tech] = tech_counts.get(tech, 0) + 1
            
    tech_df = pd.DataFrame({
        "Technology": list(tech_counts.keys()),
        "Count": list(tech_counts.values())
    }).sort_values("Count", ascending=False)
    
    fig = px.bar(
        tech_df, 
        x='Technology', 
        y='Count',
        color='Count',
        color_continuous_scale=px.colors.sequential.Purp,
        labels={'Count': 'Number of Projects', 'Technology': 'Technology Used'},
        title="Technology Distribution Across Projects"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="",
        yaxis_title="Number of Projects",
        coloraxis_showscale=False
    )
    
    st.plotly_chart(fig, use_container_width=True)


# SKILLS SECTION
elif selected == "Skills":
    st.markdown("<h1 class='header-text'>Skills & Expertise</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Skills visualization using bar chart instead of radar
    categories = list(TECHNICAL_SKILLS.keys())
    values = [len(skills) for skills in TECHNICAL_SKILLS.values()]
    
    # Create a polar bar chart as an alternative to radar
    fig = px.bar(
        x=categories, 
        y=values,
        color=values,
        color_continuous_scale=px.colors.sequential.Purp,
        labels={'x': 'Skill Category', 'y': 'Number of Skills'},
        title="Technical Skills Overview"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="",
        yaxis_title="Number of Skills",
        coloraxis_showscale=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Detailed skills by category
    col1, col2 = st.columns(2)
    
    categories_col1 = list(TECHNICAL_SKILLS.keys())[:len(TECHNICAL_SKILLS)//2 + len(TECHNICAL_SKILLS)%2]
    categories_col2 = list(TECHNICAL_SKILLS.keys())[len(TECHNICAL_SKILLS)//2 + len(TECHNICAL_SKILLS)%2:]
    
    with col1:
        for category in categories_col1:
            st.markdown(f"<h3 class='subheader'>{category}</h3>", unsafe_allow_html=True)
            st.markdown("".join([f'<span class="skill-pill">{skill}</span>' for skill in TECHNICAL_SKILLS[category]]), unsafe_allow_html=True)
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    with col2:
        for category in categories_col2:
            st.markdown(f"<h3 class='subheader'>{category}</h3>", unsafe_allow_html=True)
            st.markdown("".join([f'<span class="skill-pill">{skill}</span>' for skill in TECHNICAL_SKILLS[category]]), unsafe_allow_html=True)
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Skill proficiency visualization
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Core Competencies</h3>", unsafe_allow_html=True)
    
    core_skills = {
        "Python": 90,
        "SQL": 85,
        "Data Visualization": 85,
        "Machine Learning": 80,
        "Statistical Analysis": 85,
        "Deep Learning": 75,
        "NLP": 70,
        "Data Storytelling": 90
    }
    
    skill_df = pd.DataFrame({
        "Skill": list(core_skills.keys()),
        "Proficiency": list(core_skills.values())
    })
    
    fig = px.bar(
        skill_df,
        x="Proficiency",
        y="Skill",
        orientation='h',
        color="Proficiency",
        color_continuous_scale=px.colors.sequential.Viridis,
        labels={"Proficiency": "Proficiency Level (%)"},
        text="Proficiency"
    )
    
    fig.update_traces(
        texttemplate='%{text}%', 
        textposition='inside',
        marker_line_color='rgba(255, 255, 255, 0.5)',
        marker_line_width=1
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="",
        yaxis_title="",
        coloraxis_showscale=False,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
# EXPERIENCE SECTION
elif selected == "Experience":
    st.markdown("<h1 class='header-text'>Professional Experience</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Professional experience timeline
    for exp in EXPERIENCE:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"<h3>{exp['position']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h4>{exp['company']}</h4>", unsafe_allow_html=True)
            st.markdown("<ul>", unsafe_allow_html=True)
            for item in exp['description']:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<p style='text-align: right;'>{exp['duration']}</p>", unsafe_allow_html=True)
        
        st.markdown("<hr>", unsafe_allow_html=True)
    
    # Certifications
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Certifications</h3>", unsafe_allow_html=True)
    
    for cert in CERTIFICATIONS:
        st.markdown(f"""
        <div class="cert-card">
            <h3>{cert['name']}</h3>
            <p><strong>Issuer:</strong> {cert['issuer']}</p>
            <p><strong>Date:</strong> {cert['date']}</p>
            <a href="{cert['link']}" target="_blank" class="icon-link">
                <i class="fas fa-certificate"></i> View Certificate
            </a>
        </div>
        """, unsafe_allow_html=True)

# EDUCATION SECTION
elif selected == "Education":
    st.markdown("<h1 class='header-text'>Education</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    for edu in EDUCATION:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"<h3>{edu['degree']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h4>{edu['institution']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p><em>{edu['details']}</em></p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='text-align: right;'>{edu['year']}</p>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
    
    # Skills gained through education
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Key Skills Gained Through Education</h3>", unsafe_allow_html=True)
    
    education_skills = [
        "Data Analysis & Interpretation",
        "Machine Learning Algorithms",
        "Statistical Modeling",
        "Deep Learning Techniques",
        "Data Visualization",
        "Information Systems Management",
        "Database Design & Management",
        "Programming (Python, SQL)",
        "Predictive Modeling",
        "NLP & Text Analysis"
    ]
    
    col1, col2 = st.columns(2)
    
    for i, skill in enumerate(education_skills):
        with col1 if i < len(education_skills) // 2 else col2:
            st.markdown(f"<div class='skill-pill'>{skill}</div>", unsafe_allow_html=True)

# Contact Section (Updated)
elif selected == "Contact":
    st.markdown("<h1 class='header-text'>Get In Touch</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.03); padding: 2rem; border-radius: 10px;'>
            <h3 class='subheader'>Contact Information</h3>
            <div style='margin: 2rem 0;'>
                <p><i class='fas fa-envelope' style='color: #8E54E9; margin-right: 10px;'></i> Email: 
                <a href='mailto:A.abdullahtw@gmail.com'>A.abdullahtw@gmail.com</a></p>
                <p><i class='fab fa-linkedin' style='color: #8E54E9; margin-right: 10px;'></i> LinkedIn: 
                <a href='https://www.linkedin.com/in/abdullah-aaltuwayjiri' target='_blank'>linkedin.com/in/abdullah-aaltuwayjiri</a></p>
                <p><i class='fab fa-github' style='color: #8E54E9; margin-right: 10px;'></i> GitHub: 
                <a href='https://github.com/Tw-0l' target='_blank'>github.com/Tw-0l</a></p>
                <p><i class='fas fa-phone' style='color: #8E54E9; margin-right: 10px;'></i> Phone: 
                +966 54 714 5479</p>
                <p><i class='fas fa-map-marker-alt' style='color: #8E54E9; margin-right: 10px;'></i> Location: 
                Riyadh, Saudi Arabia</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.03); padding: 2rem; border-radius: 10px;'>
            <h3 class='subheader'>Available For</h3>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li style='margin-bottom: 10px;'>
                    <i class='fas fa-check-circle' style='color: #8E54E9; margin-right: 10px;'></i> 
                    Data Analysis Projects
                </li>
                <li style='margin-bottom: 10px;'>
                    <i class='fas fa-check-circle' style='color: #8E54E9; margin-right: 10px;'></i> 
                    Machine Learning Implementation
                </li>
                <li style='margin-bottom: 10px;'>
                    <i class='fas fa-check-circle' style='color: #8E54E9; margin-right: 10px;'></i> 
                    Data Visualization
                </li>
                <li style='margin-bottom: 10px;'>
                    <i class='fas fa-check-circle' style='color: #8E54E9; margin-right: 10px;'></i> 
                    Predictive Modeling
                </li>
                <li style='margin-bottom: 10px;'>
                    <i class='fas fa-check-circle' style='color: #8E54E9; margin-right: 10px;'></i> 
                    NLP & Text Analysis
                </li>
            </ul>
            
           <h3 class='subheader' style='margin-top: 2rem;'>Response Time</h3>
            <p>I typically respond to inquiries within 24-48 hours.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
st.markdown("""
<footer style='text-align: center; color: #666; padding: 20px 0; font-size: 0.8rem;'>
    © 2025 | Abdullah Altuwayjiri | Data Scientist & Analyst
</footer>
""", unsafe_allow_html=True)