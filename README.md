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


---

**Research Project: LinkedIn Organic Content Strategy for B2B SaaS**
 
**Details**
* This research project explores LinkedIn organic content strategy for B2B SaaS companies about specifically how founders, marketing leaders and agency owners use LinkedIn to build pipeline, establish thought leadership, and grow their businesses without paid advertising.

\---
 
**Expert Selection Criteria**
 10 experts were selected based on the following criteria:
 
*  They actively run an agency, SaaS company or marketing team.
*  They use LinkedIn themselves as a primary growth channel.
*  They publish documented systems and frameworks, not just opinions.
*  They are cited and recommended by other practitioners in the space.

 The goal was to find people who practice what they teach, not just 
 commentators or educators who write about LinkedIn without doing it.
 
 \---
 
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
 
\---
 
* **Tools Used**
* Python - `youtube-transcript-api` library for transcript collection
* Claude Code (Sonnet 4.6) - Used inside Cursor IDE to generate scripts, format research files and structure content
* Cursor IDE - Development environment for writing and running code
* Git \& GitHub - Version control with regular commits throughout the research process
 
\---

 **Experts Researched**
 
  | # | Name | Role | LinkedIn |

* | 1 | Richard van der Blom | Founder, Just Connecting HUB | \ https://www.linkedin.com/in/richardvanderblom 
* | 2 | Dave Gerhardt | Founder, Exit Five | \ https://www.linkedin.com/in/davegerhardt 
* | 3 | Ross Simmonds | Founder, Foundation Marketing | \ https://www.linkedin.com/in/rosssimmonds 
* | 4 | Chris Walker | CEO, Passetto | \ https://www.linkedin.com/in/chriswalker171 
* | 5 | Justin Welsh | Solopreneur \& LinkedIn Educator | \ https://www.linkedin.com/in/justinwelsh 
* | 6 | Peep Laja | Founder, Wynter \& CXL | \ https://www.linkedin.com/in/peeplaja 
* | 7 | Lara Acosta | Founder, LA Digital | \ https://www.linkedin.com/in/laraacosta 
* | 8 | Koka Sexton | B2B SaaS Demand Gen Consultant | \ https://www.linkedin.com/in/kokasexton 
* | 9 | Obaid Durrani | Content Strategist, Clay | \ https://www.linkedin.com/in/obaidbot 
* | 10 | Amanda Natividad | VP Marketing, SparkToro | \ https://www.linkedin.com/in/amandanat 
 
 \---
 
* Notes
* YouTube transcripts were collected manually due to platform restrictions on automated scraping. This was a deliberate and documented decision the manual approach ensured higher quality, more relevant posts were selected rather than bulk automated collection.
 
* All commits were made incrementally throughout the research process rather than in one large push at the end.
```
 

