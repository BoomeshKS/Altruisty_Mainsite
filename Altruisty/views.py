from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"ai-agency.html")

def interns(request):
    return render(request,"internship.html")

def studentform(request):
    return render(request,"studentform.html")

def mentorform(request):
    return render(request,"mentorform.html")

def startupform(request):
    return render(request,"startupform.html")

def aboutus(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contactus.html")

def verify(request):
    return render(request,"verifyintern.html")
def services(request):
    return render(request,"service.html")
def DetailsPage(request,heading):
    data = {
        'Idea To Product Development':{
            'title':['Idea Validation Analyst',
                     'Concept to Prototype Development',
                     'MVP Development','Product Development',
                     'Idea Implementation Consultant',
                     'Product Roadmap Consultant'
                     ],
             'images': [
                'id1.png',
                'id2.png',
                'ss.jpg',
                'invest4.png',
                'black.jpg',
                'Student.png'
            ],
            'description': [
                'Assess the potential of your innovative ideas through comprehensive market research. We evaluate market demand, competition, and challenges to help you make informed decisions about your concept.',
                'Bring your idea to life with our expert team. We work with you to refine your concept and create a detailed prototype that captures the essence of your products key features and functionality.',
                'Quickly develop and launch a Minimum Viable Product (MVP) to test your concept in the market. Gather valuable user feedback and iterate on your product to meet real-world needs.',
                'Transform your MVP into a full-scale product. We guide you through every stage, from design and development to testing and deployment, ensuring your product is ready for the market.',
                'Turn your vision into reality with our strategic support. We help you navigate the complexities of implementation, optimize workflows, and achieve your goals efficiently.',
                'Create a comprehensive product roadmap that aligns with your business goals. We help you prioritize features, allocate resources effectively, and adapt to changing market dynamics.'
            ]
        },
        'Patent And Copy Rights':{
            'title':['Patent Research Assistant',
                     'Patent Filing Assistant & Consultant',
                     'Trademark Registration',
                     'Patent Litigation Support & Consultant',
                     'Patent & Copyright Registration',
                     'Copyright Renewal Assistant & Consultant'
                     ],
            'images': [
                'ptnt.png',
                'ptnt2.png',
                'ptnt3.png',
                'reg2.png',
                'fund4.png',
                'b.jpg'
            ],
            'description':[
                "Unlock your innovation's potential with our Patent Research Assistant service. We conduct thorough patent searches and provide in-depth analysis to ensure your ideas are unique and protectable.",
                "Navigate the patent filing process with confidence. Our experts offer personalized support, from drafting applications to meeting regulatory requirements, ensuring your intellectual property is well-protected.",
                "Secure your brand identity with ease through our Trademark Registration service. We guide you through the trademark process, helping you protect your brand and stand out in the market.",
                "When disputes arise, our Patent Litigation Support & Consultant service provides strategic guidance and expert assistance. We help you navigate the complexities of patent litigation, ensuring your intellectual property rights are effectively protected.",
                "Protect your creative works. We offer comprehensive services for patent and copyright registration, safeguarding your intellectual property assets and maximizing their value.",
                "Stay ahead with copyright renewals. We manage the entire process, ensuring your works remain protected and compliant with all deadlines.",                
            ]
        },
        'Company Registration And Other Registration':{
            'title':['Startup Registration Coordinator',
                     'Company Incorporation Advisor',
                     'Professional Corporation Formation Consultant',
                     'Company & Business Registration Consultant',
                     'Legal Entity Formation Consultant',
                     'Import-Export License Assistant'
                     ],
            'images': [
                'reg1.png',
                'reg2.png',
                'reg3.png',
                'reg4.png',
                'invest4.png',
                'invest3.png'
            ],
            'description':[
                "Starting your entrepreneurial journey? Our Startup Registration Coordinator service simplifies the process, handling paperwork and legalities so you can focus on realizing your vision.",
                "Establishing your business? Our Company Incorporation Advisor service offers expert guidance on choosing the right structure and navigating legal requirements to set your company up for success.",
                "Enhance your professional practice with tailored corporate structures. Our Professional Corporation Formation Consultant service is designed for doctors, lawyers, and accountants, ensuring compliance with industry standards.",
                "Starting or expanding your business? Our Company & Business Registration Consultant service provides comprehensive support for all registration and licensing needs, streamlining the process for a smooth start.",
                "Forming a corporation, LLC, or partnership? Our Legal Entity Formation Consultant service guides you through every step, ensuring compliance with regulatory requirements.",
                "Entering international trade? Our Import-Export License Assistant service simplifies obtaining licenses and permits, handling customs documentation, and ensuring trade compliance.",
            ]
        },
        'Funding Preparation':{
            'title':['Funding Proposal Writer',
                     'Grant Application Consultant',
                     'Investor Pitch Deck Designer',
                     'Business Valuation Analyst',
                     'Fundraising Consultant',
                     'Funding Strategy Advisor',
                     'Investor Matchmaker',
                     'Pitch Competition Coordinator',
                     'Investor Engagement Specialist',
                     'Investor Presentation Coach',
                     'Angel Investor Outreach Coordinator',
                     'Investor Outreach Strategist'
                     ],
            'images': [
                'fund2.png',
                'fund3.png',
                'fund1.png',
                'fund4.png',
                'fund5.png',
                'fund6.png',
                'invest1.png',
                'invest2.png',
                'invest3.png',
                'invest4.png',
                'invest5.png',
                'invest6.png'
            ],
            'description':[
                "Are you seeking financial support for your project or organization? Let our experienced funding proposal writers craft compelling proposals that resonate with donors, investors, and grant-making bodies.",
                "Navigating the intricacies of grant applications can be daunting. Our seasoned consultants specialize in guiding you through the process, from identifying relevant funding opportunities to developing winning proposals.",
                "Captivate investors and stakeholders with visually stunning pitch decks that tell your story with clarity and impact. Our design team combines creativity and strategic thinking to craft compelling presentations.",
                "Understanding the true value of your business is crucial for making informed decisions and attracting investors. Our team of skilled analysts employs rigorous methodologies to conduct comprehensive business valuations.",
                "Unlock the full potential of your fundraising efforts with expert guidance from our consultants. From donor engagement strategies to campaign planning and execution, we offer personalized solutions.",
                "Developing a robust funding strategy is essential for sustaining and growing your organization. Our advisors work closely with you to assess your financial needs, identify opportunities for diversification.",  
                "Welcome to Investor Matchmaker, where we connect entrepreneurs with the perfect investors to fuel their dreams. Whether you're a startup seeking funding or an investor looking for promising opportunities, our platform brings together the ideal matches to foster growth and innovation. Let us be your bridge to success.",
                "Are you ready to showcase your startup's potential on a grand stage? As Pitch Competition Coordinators, we curate electrifying events where entrepreneurs pitch their ideas to a panel of esteemed judges. Join us in this exhilarating journey of innovation, where the boldest ideas transform into reality.",
                "Unlock the power of meaningful connections with our Investor Engagement Specialists. We understand that building relationships with investors is paramount to your business's success. Let us craft personalized strategies to captivate investors, turning interest into investment.",
                "Crafting the perfect investor pitch is an art form, and our Investor Presentation Coaches are here to guide you every step of the way. From refining your message to perfecting your delivery, we'll ensure your presentation leaves a lasting impression, setting the stage for investment success.",
                "Calling all entrepreneurs seeking the backing of angel investors! Our Angel Investor Outreach Coordinators specialize in connecting innovative startups with high-net-worth individuals eager to support promising ventures. Let us navigate the intricacies of angel investing to help turn your vision into reality.",
                "In today's competitive landscape, strategic investor outreach is essential for securing funding and driving growth. Our Investor Outreach Strategists are experts in crafting tailored approaches to engage investors effectively. Partner with us to unlock new opportunities and propel your business forward."
            ]
            
        },
        'Investor Connect': {
    'title': [
        'Investor Matchmaker',
        'Pitch Competition Coordinator',
        'Investor Engagement Specialist',
        'Investor Presentation Coach',
        'Angel Investor Outreach Coordinator',
        'Investor Outreach Strategist'
    ],
    'images': [
        'invest1.png',
        'invest2.png',
        'invest3.png',
        'invest4.png',
        'invest5.png',
        'invest6.png'
    ],
    'description': [
        "Welcome to Investor Matchmaker, where we connect entrepreneurs with the perfect investors to fuel their dreams. Whether you're a startup seeking funding or an investor looking for promising opportunities, our platform brings together the ideal matches to foster growth and innovation. Let us be your bridge to success.",
        "Are you ready to showcase your startup's potential on a grand stage? As Pitch Competition Coordinators, we curate electrifying events where entrepreneurs pitch their ideas to a panel of esteemed judges. Join us in this exhilarating journey of innovation, where the boldest ideas transform into reality.",
        "Unlock the power of meaningful connections with our Investor Engagement Specialists. We understand that building relationships with investors is paramount to your business's success. Let us craft personalized strategies to captivate investors, turning interest into investment.",
        "Crafting the perfect investor pitch is an art form, and our Investor Presentation Coaches are here to guide you every step of the way. From refining your message to perfecting your delivery, we'll ensure your presentation leaves a lasting impression, setting the stage for investment success.",
        "Calling all entrepreneurs seeking the backing of angel investors! Our Angel Investor Outreach Coordinators specialize in connecting innovative startups with high-net-worth individuals eager to support promising ventures. Let us navigate the intricacies of angel investing to help turn your vision into reality.",
        "In today's competitive landscape, strategic investor outreach is essential for securing funding and driving growth. Our Investor Outreach Strategists are experts in crafting tailored approaches to engage investors effectively. Partner with us to unlock new opportunities and propel your business forward."
        ]
        },
    }
    selectedheading = data.get(heading, {})
    if 'title' in selectedheading and 'images' in selectedheading and 'description' in selectedheading:
        service_details = zip(selectedheading['title'], selectedheading['images'], selectedheading['description'])
    else:
        service_details = []

    return render(request, 'details.html', {'service_details': service_details, 'heading': heading})
