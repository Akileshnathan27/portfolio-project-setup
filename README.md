# portfolio-project-setup

This is a portfolio project setup for junior growth marketing specialist role.

## Tools Installed

* Cursor IDE
* Claude Code extension
* Codex extension

## Steps Completed

1. Downloaded and installed Cursor IDE.
2. Navigated to the Extensions marketplace within Cursor to install and authenticate both Claude Code and Codex.
3. Created a new public repository on GitHub.
4. Cloned the repository to my local machine using Cursor.
5. Authored this README to document the setup process.

## Issues Encountered and Solutions

* **Issue:** I was a little confused when creating a GitHub repository and adding it in Cursor.
* **Solution:** I watched a couple of youtube tutorials about creating a GitHub repository and then I also used Gemini to give a step by step process on how to do it.




**Research Project: LinkedIn Organic Content Strategy for B2B SaaS**
 
 **Details**
* This research project explores LinkedIn organic content strategy for B2B SaaS companies about specifically how founders, marketing leaders and agency owners use LinkedIn to build pipeline, establish thought leadership, and grow their businesses without paid advertising.

 
 **Expert Selection Criteria**
 10 experts were selected based on the following criteria:
 
*  They actively run an agency, SaaS company or marketing team.
*  They use LinkedIn themselves as a primary growth channel.
*  They publish documented systems and frameworks, not just opinions.
*  They are cited and recommended by other practitioners in the space.

 The goal was to find people who practice what they teach, not just 
 commentators or educators who write about LinkedIn without doing it.
 
 
 **Repository Structure**

* `/research/sources.md`
* A structured list of all 10 experts with their LinkedIn profiles, YouTube channels, podcast names, and a detailed annotation explaining why each person was chosen. Includes selection criteria at the bottom.

* `/research/linkedin-posts/`
* 2 LinkedIn posts per expert (20 posts total), manually collected from each expert's LinkedIn profile. Posts were selected for relevance to LinkedIn content strategy, B2B marketing and SaaS growth. Each file includes the post date, URL, engagement metrics, full post text and   a note on why it was saved.

* `/research/youtube-transcripts/`
* 1 YouTube video transcript per expert (10 transcripts total). 
* Transcripts were collected using the following approach:
* A Python script (`get\_transcripts.py`) was written to fetch transcripts programmatically using the `youtube-transcript-api` library
* YouTube blocked requests from the local IP during execution
* Transcripts were then collected manually using YouTube's built-in transcript feature as a fallback
* All transcripts are saved in structured .txt files
* `/research/other/`
* Additional research materials including:
* `podcast-episodes.md` - A curated list of relevant podcast episodes from 4 experts (Chris Walker, Dave Gerhardt, Peep Laja, Ross Simmonds) with episode topics, links and annotations on why each podcast is relevant to the research topic
 
 
 **Tools Used**
* Python - `youtube-transcript-api` library for transcript collection
* Claude Code (Sonnet 4.6) - Used inside Cursor IDE to generate scripts, format research files and structure content
* Cursor IDE - Development environment for writing and running code
* Git \& GitHub - Version control with regular commits throughout the research process
 

 **Experts Researched**
 
 | # | Name | Role | LinkedIn |

* | 1 | Richard van der Blom | Founder, Just Connecting HUB | https://www.linkedin.com/in/richardvanderblom 
* | 2 | Dave Gerhardt | Founder, Exit Five | https://www.linkedin.com/in/davegerhardt 
* | 3 | Ross Simmonds | Founder, Foundation Marketing | https://www.linkedin.com/in/rosssimmonds 
* | 4 | Chris Walker | CEO, Passetto | https://www.linkedin.com/in/chriswalker171 
* | 5 | Justin Welsh | Solopreneur \& LinkedIn Educator | https://www.linkedin.com/in/justinwelsh 
* | 6 | Peep Laja | Founder, Wynter \& CXL | https://www.linkedin.com/in/peeplaja 
* | 7 | Lara Acosta | Founder, LA Digital | https://www.linkedin.com/in/laraacostar 
* | 8 | Koka Sexton | B2B SaaS Demand Gen Consultant | https://www.linkedin.com/in/kokasexton 
* | 9 | Obaid Durrani | Content Strategist, Clay | https://www.linkedin.com/in/obaidbot 
* | 10 | Amanda Natividad | VP Marketing, SparkToro | https://www.linkedin.com/in/amandanat 

**Why Each Expert Was Chosen**

**1. Richard van der Blom**
Chosen because he publishes the only data-driven annual LinkedIn Algorithm Insights Report backed by large-sample research from real user interactions. He is the founder of Just Connecting HUB and has trained 300,000+ B2B professionals across 900+ companies. No other voice on this list has more raw data about how LinkedIn actually works.

**2. Dave Gerhardt**
Chosen because he scaled Drift to a $1B exit and Privy to a $100M+ acquisition using content-led growth strategies and then built Exit Five, the largest community for B2B marketers, using the same LinkedIn organic approach he teaches. His own LinkedIn presence is a live proof of concept of everything he publishes.

**3. Ross Simmonds**
Chosen because he runs Foundation, a B2B content marketing agency working with brands like Canva, Bitly and Snowflake. He coined the phrase "Create once, distribute forever" which is a foundational principle for LinkedIn organic strategy. He also built Distribution.ai, meaning he doesn't just teach content distribution, he built a software product around it.

**4. Chris Walker**
Chosen because he built his entire business pipeline through organic LinkedIn content and dark social before anyone else was talking about it. He then built Refine Labs into a leading demand generation agency for SaaS companies and now runs Passetto. His LinkedIn posts are consistently cited by other B2B marketers as the most data-driven takes on modern GTM strategy.

**5. Justin Welsh**
Chosen because he is the clearest proof point that LinkedIn organic content alone can build a scalable business. He went from CCO of PatientPop (scaled to $50M ARR) to building a $5M+ one-person business using only LinkedIn. He publishes his exact systems publicly, making him one of the most transparent practitioners on this list.

**6. Peep Laja**
Chosen because he brings a unique angle to LinkedIn content strategy he frames content not as a posting exercise but as a positioning and messaging tool. As founder of Wynter (B2B messaging research platform) and CXL (marketing education company), his advice is grounded in actual data about what messaging resonates with buyers, not guesswork.

**7. Lara Acosta**
Chosen because she built from zero to the #1 female LinkedIn creator in the UK in under two years using a documented framework called SLAY. She now runs LA Digital, a LinkedIn content agency. She represents the most recent and fastest documented case study of systematic organic LinkedIn growth on this list.

**8. Koka Sexton**
Chosen because he is one of LinkedIn's earliest Social Selling evangelists and he worked at LinkedIn itself before moving into B2B SaaS consulting. This gives him a uniquely inside perspective on how the platform is designed to work for B2B companies, which no other expert on this list has.

**9. Obaid Durrani**
Chosen because he created the Easy Mode content framework now adopted by 20+ SaaS companies and architected HockeyStack's LinkedIn and owned media strategy, widely considered one of the most creative B2B brand builds in martech. He represents the next generation of practitioner-led B2B content thinking that goes beyond traditional LinkedIn advice.

**10. Amanda Natividad**
Chosen because she coined the term "zero-click content", a framework that directly applies to LinkedIn organic strategy where content must deliver full value without requiring a link click. As VP of Marketing at SparkToro she leads an active marketing team and teaches from live campaigns. Her newsletter has 50,000+ subscribers with a 40% open rate, proving her content frameworks actually work in practice.
 
 
**Notes**
* YouTube transcripts were collected manually due to platform restrictions on automated scraping. This was a deliberate and documented decision the manual approach ensured higher quality, more relevant posts were selected rather than bulk automated collection.
 
* All commits were made incrementally throughout the research process rather than in one large push at the end.



## Assignment 3 - Playbook / SOP

**Status: Completed**

A full Playbook and SOP for LinkedIn Organic Content Strategy for B2B SaaS has been created and saved at `/research/playbook.md`.

### Playbook Structure

The playbook is divided into regular content sections and special analytical sections.

**Content Sections:**
- Section 1: Foundation - Before You Post Anything
- Section 2: Content Strategy - What to Post and Why
- Section 3: Engagement and Distribution
- Section 4: Measurement - How to Know If It Is Working

**Special Sections:**
- Where Experts Disagree - 3 examples of genuine disagreement between experts, with a clear position taken on each
- What I Rejected and Why - 2 ideas from the research that were deliberately excluded, with full reasoning
- My Original Ideas - 1 original strategic idea not found in any source, with explanation of why it could work
- Weaknesses of This Playbook - honest account of limitations, untested assumptions and gaps
- Who I Would NOT Recommend Following and Why - honest assessment of 2 experts from the research list

### Methodology

Every recommendation in the playbook is cited with the author name, exact post URL and date in DD.MM.YYYY format. No claim is made without a direct source from the research collected 
in Assignment 2.

All 20 LinkedIn posts collected during Assignment 2 were reviewed for usability. Posts that did not directly support LinkedIn organic content strategy recommendations were excluded from citations, regardless of the expert's reputation. This decision is documented in the playbook.

 

