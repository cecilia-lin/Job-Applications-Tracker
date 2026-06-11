from extractor import extract_job_details

def run_tests():
    # --- TEST 1: Normal Job Description ---
    print("\n[TEST 1] Standard Job Description...")
    good_description = """
        Business Analyst
        330 Sepulveda Manhattan Beach, CA 90266 United States of America
        Category:Corporate
        Job ID:JR126626
        widget:Full time
        Posted Date:June 9th 2026
        City State Country:Manhattan Beach, California, United States of America
        Description
        WHO WE ARE:
        Headquartered in Southern California, Skechers—the Comfort Technology Company®—has spent over 30 years helping men, women, and kids everywhere look and feel good. Comfort innovation is at the core of everything we do, driving the development of stylish, high-quality products at a great value. From our diverse footwear collections to our expanding range of apparel and accessories, Skechers is a complete lifestyle brand.

        ABOUT THE ROLE:
        The Business Analyst partners closely with the Director of Business Operations and Vice President of Product Development to drive operational excellence across the Product Development organization. This role is responsible for developing and managing analytical reporting, identifying performance trends, and translating data into actionable insights that improve efficiency, accountability, and execution.
        WHAT YOU'LL DO:

        Decision Support & Business Partnership

        Partner with PLMs and cross-functional stakeholders to review reporting outputs and drive data-informed action plans.
        Support leadership with scenario analysis, and performance modeling to guide strategic decisions.
        Monitor performance metrics and proactively flag risks or deviations from plan.
        Conduct root cause analysis to support continuous improvement initiatives.
        Cross-Functional Collaboration

        Collaborate with Digital Innovation, Business Insight, and Data Analytics teams to enhance reporting capabilities and support future-state data initiatives.
        Serve as a liaison between operations and analytics teams to ensure reporting solutions align with business needs.
        Oversee communication and distribution of analytical reporting to ensure clarity and alignment across stakeholders.
        Process Improvement

        Identify opportunities to streamline reporting workflows and improve automation.
        Standardize reporting documentation and best practices to ensure consistency and scalability.
        Support operational issue resolution through data validation and analysis.
        Additional Responsibilities

        Assist in resolving day-to-day operational challenges within the department.
        Support special projects and strategic initiatives as assigned.
        Perform other duties as needed.
        WHAT YOU'LL BRING:

        Team player attitude.
        Detail oriented.
        Follows procedures.
        Ability to multi-task.
        Ability to work at a fast pace.
        Excellent follow up.
        Ability to work independently with limited supervision.
        Excellent communication skills, both written and verbal.
        Flexible work schedule; able to work extra hours as needed.
        REQUIREMENTS:

        Education: Bachelor or relevant work experience.
        One to three years of footwear experience preferred.
        Highly proficient in Microsoft Excel with skills including, creating unique Formulas, Pivot Tables, Data Validation, & Conditional Formatting.
        Experience working with a PLM system.
        Understanding of how to utilize a data analytic dashboard such as Incorta.
        The pay range for this position is $85,000-$98,000/yr USD.

        About Skechers

        Skechers, a global Fortune 500® company, develops and markets a diverse range of lifestyle and performance footwear, apparel, and accessories. Serving over 180 countries and territories, Skechers connects customers to products through department and specialty stores, e-commerce and digital stores, and through our more than 5,300 Skechers retail locations.


        Equal Employment Opportunity
        Skechers is committed to providing a safe, inclusive, and respectful work environment. Skechers provides equal employment opportunities for all employees and applicants for employment without regard race, color, religion, gender, gender identification and expression, national origin, marital status, age, disability, genetic information, military status, sexual orientation, or any other protected characteristic established by local, state or federal law.


        Reasonable Accommodation
        Applicants for employment who require a reasonable accommodation to apply for a job should request appropriate accommodation by emailing benefits@skechers.com.
        To perform this job successfully, an individual must be able to perform each job responsibility satisfactorily.  The skills, abilities and physical demands described are representative of those duties that must be met by an employee to successfully perform the essential functions of this job. Reasonable accommodation may be made to enable individuals with disabilities, who are otherwise qualified for the job position, to perform the essential functions.
    """
    
    result1 = extract_job_details(good_description)
    if result1:
        print("Success! Extracted Data:")
        print(result1.model_dump_json(indent=2))
    else:
        print("Failed to extract data.")


    # --- TEST 2: Garbage Text ---
    print("\n--------------------------------------------------")
    print("\n[TEST 2] Garbage Text (Testing Fallbacks)...")
    bad_description = "An agent is an individual, entity, or software program authorized and equipped to act on behalf of another to achieve specific goals. Depending on the context—such as law, business, or technology—an agent takes on distinct functions, ranging from negotiating contracts to performing self-directed digital tasks."
    
    result2 = extract_job_details(bad_description)
    if result2:
        print("Handled gracefully. Notice the 'Unknown' fallbacks:")
        print(result2.model_dump_json(indent=2))
    else:
        print("Extraction failed completely.")

if __name__ == "__main__":
    run_tests()