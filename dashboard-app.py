import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import matplotlib.pyplot as plt
import seaborn as sns

# Load pre-trained transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to calculate growth rate (month-over-month percentage growth)
def calculate_growth_rate(data):
    data['growth'] = ((data['month13'] - data['month1']) / data['month1']) * 100
    return data

# Function to filter city data
def filter_by_city(city, cities_data):
    if city != "All":
        return cities_data[cities_data['City'] == city]
    return cities_data

# Function to filter experience data
def filter_by_experience(experience, experience_data):
    return experience_data[experience_data['Bucket'] == experience]

# Map industries to relevant skills
industry_skill_map = {
    "Tech": ["Python", "Machine Learning", "Cloud Computing", "Cybersecurity"],
    "Finance": ["Financial Analysis", "Risk Management", "Data Analysis", "Excel"],
    "Healthcare": ["Medical Research", "Clinical Data Analysis", "Patient Management"],
    "Education": ["Curriculum Development", "Instructional Design", "E-Learning Platforms"]
}

# Function to get skills based on top growing industries
def get_skills_from_top_industries(top_industries, industry_skill_map):
    skills = []
    for industry in top_industries['Industry']:
        if industry in industry_skill_map:
            skills.extend(industry_skill_map[industry])
    return list(set(skills))  # Remove duplicates

# Streamlit app layout
def main():
    # Page configuration
    st.set_page_config(page_title="Real-Time Job Market Insights", layout="wide")

    st.sidebar.title("Filters")
    industry = st.sidebar.selectbox("Select Industry", ["All", "IT-Software/Software Services", "Banking/Financial Services/Broking", "Medical/Healthcare/Hospital", "Education/Teaching/Training"])
    location = st.sidebar.selectbox("Select Location", ["All", "Mumbai", "Delhi / NCR", "Bengaluru / Bangalore", "Chennai"])
    experience = st.sidebar.selectbox("Years of Experience", ["0-3", "4-7", "8-12", "13-16", "16 +"])

    st.title("Real-Time Job Market Insights")

    # Load the datasets (hardcoded file paths)
    industries_data = pd.read_csv('page8_table.csv')  # Industries
    cities_data = pd.read_csv('page9_table.csv')      # Cities
    experience_data = pd.read_csv('buckets_and_numbers.csv')  # Experience buckets

    # Filter cities and experience data
    filtered_city_data = filter_by_city(location, cities_data)
    filtered_experience_data = filter_by_experience(experience, experience_data)

    st.subheader(f"Metrics for {location} and {experience} years of experience")
    st.write(f"Filtered Data for {location}")
    st.write(filtered_city_data)

    st.write(f"Filtered Data for {experience} years of experience")
    st.write(filtered_experience_data)

    # Example input for candidate's skill
    candidate_skill = st.sidebar.text_input("Enter a candidate skill:", "computer science")

    if candidate_skill:
        # Embed the candidate skill
        skill_embedding = model.encode(candidate_skill, convert_to_tensor=True)

        # Embed each industry name
        industry_embeddings = model.encode(industries_data['Industry'].tolist(), convert_to_tensor=True)

        # Calculate cosine similarities
        similarities = util.pytorch_cos_sim(skill_embedding, industry_embeddings)

        # Append relevance scores to the dataframe
        industries_data['relevance'] = similarities[0].cpu().numpy()

        # Sort by relevance and get the top 5 industries
        top_5_industries = industries_data.sort_values(by='relevance', ascending=False).head(5)

        # Calculate growth rates
        top_5_industries = calculate_growth_rate(top_5_industries)

        # Display trending jobs section
        st.subheader("Trending Jobs")
        st.write(f"Top 5 Industries Relevant to the Skill: {candidate_skill}")
        st.write(top_5_industries[['Industry', 'month1', 'month2', 'month3', 'growth', 'relevance']])

        # Visualize industry growth over time
        st.subheader('Industry Growth Over Time')
        fig, ax = plt.subplots(figsize=(10, 6))
        for index, row in top_5_industries.iterrows():
            months = ['month1', 'month2', 'month3', 'month4', 'month5', 'month6', 'month7', 'month8', 'month9', 'month10', 'month11', 'month12']
            sns.lineplot(x=months, y=row[months].values, ax=ax, label=row['Industry'])
        ax.set_xlabel("Months")
        ax.set_ylabel("Number of Job Opportunities")
        ax.set_title("Job Opportunities Over Time for Top 5 Industries")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Get the top industries based on growth
        top_growing_industries = top_5_industries.sort_values(by='growth', ascending=False)

        # Skills in demand based on top-growing industries
        st.subheader("Skills in Demand")
        relevant_skills = get_skills_from_top_industries(top_growing_industries, industry_skill_map)
        if relevant_skills:
            skills_data = pd.DataFrame({
                'Skill': relevant_skills,
                'Demand Score': [85, 78, 75, 70][:len(relevant_skills)]  # Mock demand scores
            })
            st.bar_chart(skills_data.set_index('Skill'))
        else:
            st.write("No skills available for the selected industries.")

        # Salary benchmarks section
        st.subheader("Salary Benchmarks")
        salary_data = pd.DataFrame({
            'Role': ["Data Scientist", "Software Engineer", "Product Manager", "UX Designer"],
            'Salary (INR Lakhs)': [15, 12, 18, 10]
        })
        st.line_chart(salary_data.set_index('Role'))

        # Job recommendations section
        st.subheader("Recommended Jobs for You")
        st.write("Based on your profile and the current market trends, here are some job recommendations:")
        st.write(top_5_industries[['Industry', 'relevance']])

        # Skill gap analysis section
        st.subheader("Your Skill Gap Analysis")
        st.write("Here’s how your skills stack up against the current demands:")

if __name__ == "__main__":
    main()
