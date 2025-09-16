from django.shortcuts import render


def cv_view(request):
    context = {
        'name': 'Michael Blanchette',
        'email': 'michaeldblanchette@gmail.com',
        'phone': '+1 6464213552',
        'phone_hk': '+852 94215885',
        'linkedin': 'https://www.linkedin.com/in/michaelblanchette/',
        'github': 'https://github.com/mdblanchette',
        'website': 'https://michaeldblanchette.com',

        'education': [
            {
                'institution': 'New York University',
                'dates': 'Sep 2025 - May 2027 (Expected)',
                'degree': 'MS in Computer Science',
            },
            {
                'institution': 'The Hong Kong University of Science and Technology',
                'dates': 'Sep 2020 - Jun 2025',
                'degree': 'BEng in Computer Science & BBA in Marketing',
                'extra': 'Dual Degree Program in Technology & Management (DDP)',
            },
            {
                'institution': 'CFA Institute',
                'dates': 'Exam Date: Aug 2024',
                'degree': 'Passed CFA Level I Exam',
            },
        ],

        'skills': {
            'Programming Languages': ['Python', 'Java', 'JavaScript', 'TypeScript', 'C++', 'C'],
            'Web Dev Frameworks/Libraries': ['React', 'Next.js', 'Django'],
            'ML Frameworks/Libraries': ['TensorFlow', 'PyTorch', 'Keras', 'Pandas', 'NumPy'],
        },

        'work_experience': [
            {
                'company': 'Stealth BioTech Startup',
                'dates': 'Jul 2024 - Aug 2024',
                'role': 'Machine Learning Developer Intern',
                'location': 'Hong Kong, China',
                'items': [
                    'Developed RNN and DCNN TensorFlow models based on a research paper to predict knee joint angles from muscle signal data with 85% accuracy for real-time prosthetic and exoskeleton control.',
                    'Prototyped a medical diagnosis chatbot integrating MongoDB, Llama 3.1, and RAG to streamline medical consultations and provide symptom-based diagnoses through semantic search.',
                ],
            },
            {
                'company': 'Deloitte',
                'dates': 'Jun 2023 - Aug 2023',
                'role': 'Consulting Intern - Deloitte Digital',
                'location': 'Hong Kong, China',
                'items': [
                    'Maintained ServiceNow management dashboards serving over 1000+ employees and customers across 4 global corporations.',
                    'Supervised 150 to 200 Chinese-English translations of dashboard notifications daily to optimize cross-cultural communication.',
                    'Produced meeting minutes for up to five stakeholders at a time, distilling key actionables and reducing follow-up time by 30%.',
                ],
            },
            {
                'company': 'Project Melo | <a href="https://www.projectmelo.com/" target="_blank">Website</a>',
                'dates': 'Jan 2022 - Jul 2022',
                'role': 'Fellow',
                'location': 'Hong Kong, China',
                'items': [
                    "Co-founded McDonald’s HK’s first youth-led committee alongside Bowtie CEO Fred Ngan and Miss Hong Kong 2015 Winner Louisa Mak, advising McDonald's HK CEO Randy Lai and board members on youth-related business decisions.",
                    'Curated the “Coach McNugget Art World” Exhibition featuring 20+ artworks for the brand’s 40th anniversary. | <a href="https://www.scmp.com/yp/discover/news/hong-kong/article/3230231/mcdonalds-hong-kong-celebrates-40-years-mcnuggets-arts-exhibition" target="_blank">Article</a>',
                    'Selected as one of 20 fellows from 200+ applicants to drive social empowerment initiatives with 45+ prominent Hong Kong CEOs and business leaders. Delivered a TED-style talk to 500+ global CEOs to advocate for our project. | <a href="https://www.scmp.com/events/news/hong-kong/topics/melo-summit-2022/article/3187735/project-melo-hong-kong-youth" target="_blank">Article</a>',
                ],
            },
        ],

        'project_experience': [
            {
                'name': 'Smart Debt Settler | <a href="https://www.michaeldblanchette.com/project/2024/smart-debt-settler/" target="_blank">Blog</a> | <a href="https://github.com/mdblanchette/smart-settler" target="_blank">GitHub</a>',
                'dates': 'Dec 2024 - Feb 2025',
                'role': 'Developer',
                'location': 'Hong Kong, China',
                'items': [
                    'Developed a Python-based debt simplification tool using max and min heaps to determine the minimum number of transactions required to settle group expenses fairly, reducing work that usually took 30 minutes to only take 30 seconds (98% improvement).',
                ],
            },
            {
                'name': 'HKUST Corporate Consulting Project with JPMorgan Chase & Co | <a href="https://www.michaeldblanchette.com/project/2023/temg4950l/" target="_blank">Blog</a>',
                'dates': 'Sep 2023 - Jan 2024',
                'role': 'ETF Trading Student Consultant',
                'location': 'Hong Kong, China',
                'items': [
                    'Designed a Global ETF Sales Dashboard to aggregate trends from news and social media for JP Morgan Asset Management\'s ETF sales team. Achieved 1st place in the competition. | <a href="https://www.jpmorgan.com/technology/technology-blog/bridging-industry-and-academia" target="_blank">Article 1</a> | <a href="https://ais.hkust.edu.hk/whats-happening/news/temg4950l-tm-corporate-consulting-project-global-etf-dashboard-jpmc" target="_blank">Article 2</a>',
                    'Developed an ETF filtering tool leveraging Llama 2 and MongoDB to accelerate ETF identification for JPM salespeople through RAG semantic search, reducing the time needed to pinpoint promising ETFs for their clients by 70%.',
                    'Presented a proof of concept of a customer profiling tool by integrating CRM data from Salesforce, financial news, client meeting logs, and Hugging Face models to dynamically generate 2 to 5 ETF recommendations per month.',
                ],
            },
            {
                'name': 'HKUST Corporate Prototyping Project | <a href="https://www.michaeldblanchette.com/project/2023/temg4940c/" target="_blank">Blog</a>',
                'dates': 'Jun 2023 - Aug 2023',
                'role': 'Fixed Income Student Analyst / Full-stack Developer',
                'location': 'Hong Kong, China',
                'items': [
                    'Created a yearly bond pricing and credit spread migration prediction dashboard for two corporate banking and fixed-income related sponsors. Led mainly front-end development and achieved 2nd place in the competition. | <a href="https://ais.hkust.edu.hk/whats-happening/news/temg4940c-tm-prototyping-and-research-project-ai-bond-prediction" target="_blank">Article</a>',
                    'Built dashboard on Next.js and Google Cloud. Sourced data from Eikon Terminal and Yahoo Finance for machine learning models and identified 62 features used to predict yearly credit rating migrations with 79.71% back-tested accuracy.',
                ],
            },
        ],

        'additional': {
            'Languages': 'English (Native), Thai (Fluent), Mandarin (Studying), Cantonese (Studying), Spanish (Studying)',
            'Awards/Scholarships': 'California Critical Thinking Skills Test - 99th Percentile, HKUST Full Tuition Scholarship + Allowance (one-off), ESF Chairman\'s Award for Excellence, Technology and Management Elite Student Scholarship, Discovery College Academic Scholarship, Venture Scout Award, Chief Scout Award, Taekwondo Dan 2 Black Belt',
            'Extracurriculars': 'Scouts Instructor for 29th SJD Group, HKUST Volleyball Society Member, Guitar, Gym, Hiking',
        },
    }
    return render(request, 'cv.html', context)
