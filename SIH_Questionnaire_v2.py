def ask_question(question, choices):
    print("\n" + question)  # Added space before each question for better readability
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")
    while True:
        try:
            answer = int(input("Enter the number of your choice: "))
            if 1 <= answer <= len(choices):
                return answer  # Return the actual selected answer index
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Please enter a number.")

def main():
    print("Welcome to the Comprehensive Skill Assessment!")
    
    # General Questions
    general_score = 0
    general_q1 = "What is your highest level of education?"
    general_choices1 = ["High School", "Bachelor's Degree", "Master's Degree", "Doctorate", "Other"]
    general_score += 1 if ask_question(general_q1, general_choices1) == 2 else 0  # Assuming Bachelor's Degree as the correct answer

    general_q2 = "How many years of professional experience do you have?"
    general_choices2 = ["0-1 years", "2-3 years", "4-5 years", "More than 5 years"]
    general_score += 1 if ask_question(general_q2, general_choices2) == 3 else 0  # Assuming "4-5 years" as the correct answer

    general_q3 = "Which industry domain are you interested in?"
    general_choices3 = ["Cybersecurity", "Data Science", "Artificial Intelligence", "Other"]
    domain_choice = ask_question(general_q3, general_choices3)  # Get the actual selected choice

    # Branching Questions for Cybersecurity
    if domain_choice == 1:  # Cybersecurity selected
        print("\nCybersecurity Domain Selected.")
        
        # Ask if the user has a preference in any domain within Cybersecurity
        preference_q = "Do you have a preference in any specific cybersecurity domain?"
        preference_choices = ["Yes", "No"]
        has_preference = ask_question(preference_q, preference_choices)  # Get the actual choice

        # Initialize scores and set them to 'N/A' by default
        network_security_score = "N/A"
        threat_analysis_score = "N/A"
        incident_response_score = "N/A"
        grc_score = "N/A"
        pentest_score = "N/A"

        if has_preference == 1:  # User has a preference
            skill_q = "Which domain are you interested in?"
            skill_choices = ["Network Security", "Threat Analysis", "Incident Response", "Governance, Risk & Compliance", "Penetration Testing"]
            skill_choice = ask_question(skill_q, skill_choices)  # Get the actual selected skill

            # Depending on user's preference, ask questions for that specific domain
            if skill_choice == 1:
                network_security_score = 0
                # Questions for Network Security
                net_sec_q1 = "Which tool is commonly used for network packet analysis?"
                net_sec_choices1 = ["Wireshark", "Metasploit", "Nmap", "John the Ripper"]
                network_security_score += (ask_question(net_sec_q1, net_sec_choices1) == 1) * 5

                net_sec_q2 = "What protocol is commonly used for secure communication over a network?"
                net_sec_choices2 = ["HTTP", "FTP", "SSH", "Telnet"]
                network_security_score += (ask_question(net_sec_q2, net_sec_choices2) == 3) * 5

            elif skill_choice == 2:
                threat_analysis_score = 0
                # Questions for Threat Analysis
                threat_analysis_q1 = "Which framework is widely used for threat intelligence sharing?"
                threat_analysis_choices1 = ["MITRE ATT&CK", "OWASP", "CVE", "NIST"]
                threat_analysis_score += (ask_question(threat_analysis_q1, threat_analysis_choices1) == 1) * 5

                threat_analysis_q2 = "What is the primary purpose of threat hunting?"
                threat_analysis_choices2 = ["To gather open-source intelligence", "To actively search for threats in an organization's environment", "To deploy honeypots", "To implement firewalls"]
                threat_analysis_score += (ask_question(threat_analysis_q2, threat_analysis_choices2) == 2) * 5

            elif skill_choice == 3:
                incident_response_score = 0
                # Questions for Incident Response
                incident_response_q1 = "What is the first step in the incident response process?"
                incident_response_choices1 = ["Identification", "Eradication", "Containment", "Recovery"]
                incident_response_score += (ask_question(incident_response_q1, incident_response_choices1) == 1) * 5

                incident_response_q2 = "Which of the following is NOT a phase of the incident response process?"
                incident_response_choices2 = ["Detection and Analysis", "Containment, Eradication, and Recovery", "Post-Incident Activity", "Penetration Testing"]
                incident_response_score += (ask_question(incident_response_q2, incident_response_choices2) == 4) * 5

            elif skill_choice == 4:
                grc_score = 0
                # Questions for Governance, Risk & Compliance
                grc_q1 = "Which of the following is a common standard for information security management?"
                grc_choices1 = ["ISO 27001", "PCI DSS", "HIPAA", "GDPR"]
                grc_score += (ask_question(grc_q1, grc_choices1) == 1) * 5

                grc_q2 = "What does 'Risk Appetite' mean in a cybersecurity context?"
                grc_choices2 = ["The maximum level of risk an organization is willing to accept", "The level of risk beyond which an organization will not tolerate", "The amount of risk an organization is exposed to", "None of the above"]
                grc_score += (ask_question(grc_q2, grc_choices2) == 1) * 5

            elif skill_choice == 5:
                pentest_score = 0
                # Questions for Penetration Testing
                pentest_q1 = "What does a black-box penetration test mean?"
                pentest_choices1 = ["No prior knowledge of the system", "Full knowledge of the system", "Partial knowledge of the system", "Focus on network infrastructure"]
                pentest_score += (ask_question(pentest_q1, pentest_choices1) == 1) * 5

                pentest_q2 = "Which of the following tools is used for web application penetration testing?"
                pentest_choices2 = ["Wireshark", "Burp Suite", "Nmap", "Snort"]
                pentest_score += (ask_question(pentest_q2, pentest_choices2) == 2) * 5

        else:  # No preference, ask questions for all domains
            network_security_score = 0
            threat_analysis_score = 0
            incident_response_score = 0
            grc_score = 0
            pentest_score = 0

            # Questions for Network Security
            net_sec_q1 = "Which tool is commonly used for network packet analysis?"
            net_sec_choices1 = ["Wireshark", "Metasploit", "Nmap", "John the Ripper"]
            network_security_score += (ask_question(net_sec_q1, net_sec_choices1) == 1) * 5

            net_sec_q2 = "What protocol is commonly used for secure communication over a network?"
            net_sec_choices2 = ["HTTP", "FTP", "SSH", "Telnet"]
            network_security_score += (ask_question(net_sec_q2, net_sec_choices2) == 3) * 5

            # Questions for Threat Analysis
            threat_analysis_q1 = "Which framework is widely used for threat intelligence sharing?"
            threat_analysis_choices1 = ["MITRE ATT&CK", "OWASP", "CVE", "NIST"]
            threat_analysis_score += (ask_question(threat_analysis_q1, threat_analysis_choices1) == 1) * 5

            threat_analysis_q2 = "What is the primary purpose of threat hunting?"
            threat_analysis_choices2 = ["To gather open-source intelligence", "To actively search for threats in an organization's environment", "To deploy honeypots", "To implement firewalls"]
            threat_analysis_score += (ask_question(threat_analysis_q2, threat_analysis_choices2) == 2) * 5

            # Questions for Incident Response
            incident_response_q1 = "What is the first step in the incident response process?"
            incident_response_choices1 = ["Identification", "Eradication", "Containment", "Recovery"]
            incident_response_score += (ask_question(incident_response_q1, incident_response_choices1) == 1) * 5

            incident_response_q2 = "Which of the following is NOT a phase of the incident response process?"
            incident_response_choices2 = ["Detection and Analysis", "Containment, Eradication, and Recovery", "Post-Incident Activity", "Penetration Testing"]
            incident_response_score += (ask_question(incident_response_q2, incident_response_choices2) == 4) * 5

            # Questions for Governance, Risk & Compliance
            grc_q1 = "Which of the following is a common standard for information security management?"
            grc_choices1 = ["ISO 27001", "PCI DSS", "HIPAA", "GDPR"]
            grc_score += (ask_question(grc_q1, grc_choices1) == 1) * 5

            grc_q2 = "What does 'Risk Appetite' mean in a cybersecurity context?"
            grc_choices2 = ["The maximum level of risk an organization is willing to accept", "The level of risk beyond which an organization will not tolerate", "The amount of risk an organization is exposed to", "None of the above"]
            grc_score += (ask_question(grc_q2, grc_choices2) == 1) * 5

            # Questions for Penetration Testing
            pentest_q1 = "What does a black-box penetration test mean?"
            pentest_choices1 = ["No prior knowledge of the system", "Full knowledge of the system", "Partial knowledge of the system", "Focus on network infrastructure"]
            pentest_score += (ask_question(pentest_q1, pentest_choices1) == 1) * 5

            pentest_q2 = "Which of the following tools is used for web application penetration testing?"
            pentest_choices2 = ["Wireshark", "Burp Su2ite", "Nmap", "Snort"]
            pentest_score += (ask_question(pentest_q2, pentest_choices2) == 2) * 5

    print("\nAssessment Complete!")
    print(f"Network Security Score: {network_security_score}")
    print(f"Threat Analysis Score: {threat_analysis_score}")
    print(f"Incident Response Score: {incident_response_score}")
    print(f"GRC Score: {grc_score}")
    print(f"Penetration Testing Score: {pentest_score}")

main()
