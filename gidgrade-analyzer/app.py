import streamlit as st
from analyzer import extract_repo_info, get_level
from scoring import calculate_score
from roadmap import generate_roadmap

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GitGrade – Recruiter-style GitHub Repository Evaluation",
    page_icon="🚀",
    layout="centered"
)

# ---------------- CUSTOM STYLES ----------------
st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: 800;
}
.sub-title {
    font-size: 18px;
    color: #9aa0a6;
}
.card {
    background-color: #111827;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 22px;
}
.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 14px;
    background-color: #2563eb;
    color: white;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="big-title">🚀 GitGrade</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Recruiter-style GitHub Repository Evaluation</div>',
    unsafe_allow_html=True
)
st.write("")

# ---------------- INPUT CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

repo_url = st.text_input(
    "🔗 Enter GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

analyze_clicked = st.button("🔍 Analyze Repository", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ANALYSIS ----------------
if analyze_clicked:
    if repo_url.strip() == "":
        st.warning("Please enter a valid GitHub repository URL.")
    else:
        with st.spinner("Analyzing repository using recruiter-style signals..."):
            repo_data = extract_repo_info(repo_url)
            score, details = calculate_score(repo_data)
            level = get_level(score)
            roadmap = generate_roadmap(repo_data, details)

        st.success("Analysis Complete ✅")

        # -------- SCORE CARD --------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 Repository Quality Score")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"<h1>{score} / 100</h1>", unsafe_allow_html=True)
            st.markdown(f"<div class='badge'>{level}</div>", unsafe_allow_html=True)

        with col2:
            st.progress(score / 100)
            st.caption(
                "Score is based on documentation, commits, structure, "
                "testing practices, and real-world relevance."
            )

        st.markdown('</div>', unsafe_allow_html=True)

        # -------- SUMMARY CARD --------
        summary = "Project shows "
        summary += "good documentation. " if details["readme"] else "weak documentation. "
        summary += (
            "Commit history is healthy."
            if repo_data["commit_count"] >= 10
            else "Commit history needs improvement."
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧑‍💼 Recruiter-Style Evaluation")
        st.write(summary)
        st.markdown('</div>', unsafe_allow_html=True)

        # -------- ROADMAP CARD --------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🛣️ Actionable Improvement Roadmap")

        for step in roadmap:
            st.checkbox(step)

        st.caption("✔️ These steps can directly improve hiring readiness.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption(
    "GitGrade mirrors how real recruiters and mentors evaluate GitHub profiles — "
    "focusing on clarity, consistency, and real-world engineering practices."
)
