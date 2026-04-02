from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import os
import re

videos = [
    {"url": "https://www.youtube.com/watch?v=nmPGcQvDnEg", "author": "richard-van-der-blom", "title": "linkedin-algorithm-explained"},
    {"url": "https://www.youtube.com/watch?v=vrtyIdOORAs", "author": "dave-gerhardt", "title": "b2b-linkedin-content-strategy"},
    {"url": "https://www.youtube.com/watch?v=6UzikJ9XCr8", "author": "ross-simmonds", "title": "content-distribution-saas"},
    {"url": "https://www.youtube.com/watch?v=O_VoBwHCNGw", "author": "chris-walker", "title": "dark-social-b2b-demand-gen"},
    {"url": "https://www.youtube.com/watch?v=uZsXZ2cSbjU", "author": "peep-laja", "title": "b2b-saas-marketing-strategy"},
    {"url": "https://www.youtube.com/watch?v=1ph8i-NDz4k", "author": "lara-acosta", "title": "linkedin-personal-brand-growth"},
    {"url": "https://www.youtube.com/watch?v=49Dduk-ThOM", "author": "koka-sexton", "title": "linkedin-social-selling"},
    {"url": "https://www.youtube.com/watch?v=J98cUdZl-JQ", "author": "amanda-natividad", "title": "zero-click-content-strategy"},
    {"url": "https://www.youtube.com/watch?v=D_12KNeS07k", "author": "justin-welsh", "title": "linkedin-growth-strategy"},
    {"url": "https://www.youtube.com/watch?v=2ClXwZInsZs", "author": "obaid-durrani", "title": "b2b-content-marketing"},
]

def get_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    return None

output_folder = "research/youtube-transcripts"
os.makedirs(output_folder, exist_ok=True)

for video in videos:
    url = video["url"]
    author = video["author"]
    title = video["title"]
    filename = f"{author}_{title}.txt"
    filepath = os.path.join(output_folder, filename)

    print(f"\nFetching transcript for: {author} — {title}")
    print(f"URL: {url}")

    video_id = get_video_id(url)

    if not video_id:
        print(f"  ERROR: Could not extract video ID from URL: {url}")
        continue

    try:
        ytt = YouTubeTranscriptApi()
        transcript_data = ytt.fetch(video_id)
        full_transcript = "\n".join([entry.text for entry in transcript_data])

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Video: {title}\n")
            f.write(f"Author: {author}\n")
            f.write(f"URL: {url}\n")
            f.write(f"{'─' * 60}\n\n")
            f.write(full_transcript)

        print(f"  SUCCESS: Saved to {filepath}")

    except TranscriptsDisabled:
        print(f"  SKIPPED: Transcripts are disabled for this video.")

    except NoTranscriptFound:
        print(f"  SKIPPED: No transcript found for this video.")

    except Exception as e:
        print(f"  ERROR: {str(e)}")

print("\nDone! Check your research/youtube-transcripts/ folder.")
