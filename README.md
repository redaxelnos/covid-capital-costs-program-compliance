COVID-19 Capital Costs Tax Credit Program: Compliance & Distribution Platform
Author: Alexander Morrison, MPP Role: Program Strategy Manager / Policy Researcher Client Focus: New York State (Empire State Development - NY ESD)

Overview
This repository outlines the structural framework, compliance logic, and geographic data analysis architecture developed for the implementation of the COVID-19 Capital Costs Tax Credit Program.

Administered via a centralized SaaS platform, this initiative provided financial relief to small businesses that incurred qualifying structural and operational costs to comply with COVID-19 safety guidelines. The primary challenge was translating complex state and federal statutory requirements into a seamless, automated digital application pipeline and dashboard for government stakeholders.

Project Scope & Methodologies
1. Statutory Compliance & Scope Analysis
Translated legislative text (state and federal rules) into definitive technical requirements for the SaaS application portal.
Developed eligibility logic matrices to verify applicant criteria (e.g., maximum employee counts, gross receipts thresholds, and qualifying expense date ranges).
Ensured audit-readiness and strict data governance in the handling of tax IDs, financial records, and grant distributions.
2. Eligibility Verification Engine
Designed the workflow for automated and manual review of application documents (receipts, tax returns, safety protocol documentation).
Implemented fraud-prevention guardrails and standardized approval/denial workflows to maintain program integrity.
3. Geographic & Fiscal Impact Analysis
Utilized GIS mapping and heat maps to visualize program reach, identifying underserved rural and urban corridors.
Performed gap analysis on program distribution to assess cost efficiency and ensure equitable allocation of the state's tax credit funds.
Built executive-level dashboards for government clients, providing real-time insights into fund depletion, application volume, and demographic impact.

Repository Contents
eligibility_validator.py: A sample Python framework demonstrating how statutory business rules are translated into programmatic validation checks.
/docs/compliance_matrix.md: (Placeholder) Documentation of the policy-to-product translation mapping.
/analysis/spatial_distribution.ipynb: (Placeholder) Jupyter notebook demonstrating GIS heat-mapping of fund distribution across NY counties.

Technologies & Skills
Policy & Compliance: Federal/State Regulatory Analysis, Statutory Translation, Audit Preparation.
Data & Analytics: GIS Mapping, Spatial Analysis, Heat Maps, Gap Analysis, Python (Pandas, GeoPandas).
Product & Program Management: SaaS Implementation, Agile/Waterfall methodologies, Executive Advisory, Stakeholder Liaison.

Note: This repository contains simulated frameworks and logic models for portfolio demonstration purposes. All proprietary client data, PII, and specific SaaS source code from the original Forward deployment have been excluded or anonymized.
