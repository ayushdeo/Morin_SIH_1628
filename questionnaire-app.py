import streamlit as st

class SkillAssessmentApp:
    def __init__(self):
        self.general_score = 0
        self.current_question = 0
        self.domain_choice = None
        self.scores = {
            "network_security_score": 0,
            "threat_analysis_score": 0,
            "incident_response_score": 0,
            "grc_score": 0,
            "pentest_score": 0
        }
        
        self.questions = [
            {
                "question": "What is your highest level of education?",
                "choices": ["High School", "Bachelor's Degree", "Master's Degree", "Doctorate", "Other"],
                "correct_answer": 2
            },
            {
                "question": "How many years of professional experience do you have?",
                "choices": ["0-1 years", "2-3 years", "4-5 years", "More than 5 years"],
                "correct_answer": 3
            },
            {
                "question": "Which industry domain are you interested in?",
                "choices": ["Cybersecurity", "Data Science", "Artificial Intelligence", "Other"],
                "is_domain_choice": True
            }
        ]
        
        self.cybersecurity_questions = [
            # Network Security Questions
            {
                "question": "Which tool is commonly used for network packet analysis?",
                "choices": ["Wireshark", "Metasploit", "Nmap", "John the Ripper"],
                "domain": "network_security_score",
                "correct_answer": 1
            },
            {
                "question": "What protocol is commonly used for secure communication over a network?",
                "choices": ["HTTP", "FTP", "SSH", "Telnet"],
                "domain": "network_security_score",
                "correct_answer": 3
            },
            # Threat Analysis Questions
            {
                "question": "Which framework is widely used for threat intelligence sharing?",
                "choices": ["MITRE ATT&CK", "OWASP", "CVE", "NIST"],
                "domain": "threat_analysis_score",
                "correct_answer": 1
            },
            {
                "question": "What is the primary purpose of threat hunting?",
                "choices": ["To gather open-source intelligence", "To actively search for threats in an organization's environment", "To deploy honeypots", "To implement firewalls"],
                "domain": "threat_analysis_score",
                "correct_answer": 2
            },
            # Incident Response Questions
            {
                "question": "What is the first step in the incident response process?",
                "choices": ["Identification", "Eradication", "Containment", "Recovery"],
                "domain": "incident_response_score",
                "correct_answer": 1
            },
            {
                "question": "Which of the following is NOT a phase of the incident response process?",
                "choices": ["Detection and Analysis", "Containment, Eradication, and Recovery", "Post-Incident Activity", "Penetration Testing"],
                "domain": "incident_response_score",
                "correct_answer": 4
            },
            # GRC Questions
            {
                "question": "Which of the following is a common standard for information security management?",
                "choices": ["ISO 27001", "PCI DSS", "HIPAA", "GDPR"],
                "domain": "grc_score",
                "correct_answer": 1
            },
            {
                "question": "What does 'Risk Appetite' mean in a cybersecurity context?",
                "choices": ["The maximum level of risk an organization is willing to accept", "The level of risk beyond which an organization will not tolerate", "The amount of risk an organization is exposed to", "None of the above"],
                "domain": "grc_score",
                "correct_answer": 1
            },
            # Penetration Testing Questions
            {
                "question": "What does a black-box penetration test mean?",
                "choices": ["No prior knowledge of the system", "Full knowledge of the system", "Partial knowledge of the system", "Focus on network infrastructure"],
                "domain": "pentest_score",
                "correct_answer": 1
            },
            {
                "question": "Which of the following tools is used for web application penetration testing?",
                "choices": ["Wireshark", "Burp Suite", "Nmap", "Snort"],
                "domain": "pentest_score",
                "correct_answer": 2
            }
        ]
        
    def display_question(self, question_data, question_number):
        st.subheader(f"Question {question_number + 1}: {question_data['question']}")
        user_answer = st.radio("Choose an answer:", question_data['choices'], key=question_number)
        return user_answer

    def run(self):
        st.title("Comprehensive Skill Assessment")

        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
            st.session_state.general_score = 0
            st.session_state.domain_choice = None
            st.session_state.scores = self.scores.copy()

        if st.session_state.current_question < len(self.questions):
            # Display general questions
            question_data = self.questions[st.session_state.current_question]
            user_answer = self.display_question(question_data, st.session_state.current_question)
            
            if st.button("Next Question"):
                if user_answer is None:
                    st.error("Please select an answer before proceeding.")
                else:
                    correct_answer = question_data.get('correct_answer')
                    if correct_answer is not None and isinstance(correct_answer, int):
                        if user_answer == question_data['choices'][correct_answer]:
                            st.session_state.general_score += 1
                    if 'is_domain_choice' in question_data:
                        st.session_state.domain_choice = user_answer

                    st.session_state.current_question += 1

        elif st.session_state.current_question < len(self.questions) + len(self.cybersecurity_questions):
            # Display cybersecurity-specific questions
            question_data = self.cybersecurity_questions[st.session_state.current_question - len(self.questions)]
            user_answer = self.display_question(question_data, st.session_state.current_question)
            
            if st.button("Next Question"):
                if user_answer is None:
                    st.error("Please select an answer before proceeding.")
                else:
                    correct_answer = question_data.get('correct_answer')
                    if correct_answer is not None and isinstance(correct_answer, int):
                        if user_answer == question_data['choices'][correct_answer]:
                            st.session_state.scores[question_data['domain']] += 5

                    st.session_state.current_question += 1

        else:
            # Display results
            st.subheader("Assessment Complete!")
            st.write(f"General Score: {st.session_state.general_score}")
            st.write(f"Domain Choice: {st.session_state.domain_choice}")
            st.write(f"Network Security Score: {st.session_state.scores['network_security_score']}")
            st.write(f"Threat Analysis Score: {st.session_state.scores['threat_analysis_score']}")
            st.write(f"Incident Response Score: {st.session_state.scores['incident_response_score']}")
            st.write(f"GRC Score: {st.session_state.scores['grc_score']}")
            st.write(f"Penetration Testing Score: {st.session_state.scores['pentest_score']}")
            st.button("Restart", on_click=self.restart)

    def restart(self):
        st.session_state.current_question = 0
        st.session_state.general_score = 0
        st.session_state.domain_choice = None
        st.session_state.scores = self.scores.copy()

if __name__ == "__main__":
    app = SkillAssessmentApp()
    app.run()