#!/usr/bin/env python3
"""
Dynamic GitHub Repositories Sync Engine for Arun B Academic Portfolio
Author: Arun B (School of Physics, University of Hyderabad)
GitHub Account: ArunBhas

Fetches public repositories from GitHub API, filters out specified repositories (like 'portfolio'),
merges rich scientific descriptions for known laboratory tools,
and updates website/index.html to automatically showcase newly added projects.
"""

import os
import sys
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

GITHUB_USER = "ArunBhas"
EXCLUDE_REPOS = {"portfolio"}

# Curated rich scientific descriptions and badges for known core tools
KNOWN_REPOS = {
    "moke": {
        "title": "MOKE",
        "badge": "Python",
        "desc": (
            "Calculates and plots Kerr rotation and Kerr ellipticity from raw Magneto-Optical Kerr Effect data collected "
            "using a Hinds Photoelastic Modulator (PEM) and dual-phase lock-in amplifier."
        ),
        "priority": 1,
    },
    "emi-shielding-effectiveness-calculator": {
        "title": "EMI-Shielding-Effectiveness-Calculator",
        "badge": "Python",
        "desc": (
            "Directly extracts reflection shielding (SE<sub>R</sub>), absorption shielding (SE<sub>A</sub>), multiple internal "
            "reflection shielding (SE<sub>M</sub>), and total shielding (SE<sub>T</sub>) from VNA scattering S-parameters (S11, S21)."
        ),
        "priority": 2,
    },
    "em-material-studio": {
        "title": "EM-Material-Studio",
        "badge": "Python",
        "desc": (
            "A comprehensive Python package for electromagnetic material characterization, reflection loss mapping, "
            "and impedance matching calculations across broadband frequencies."
        ),
        "priority": 3,
    },
    "lambda_g_calculator": {
        "title": "lambda_g_calculator",
        "badge": "Python",
        "desc": (
            "Calculates guided wavelength (&lambda;<sub>g</sub>), cutoff frequency (f<sub>c</sub>), and propagation constant "
            "in standard rectangular waveguides (WR-90, WR-62, WR-42) for microwave testing."
        ),
        "priority": 4,
    },
    "rotationfmr": {
        "title": "RotationFMR",
        "badge": "G-Code / Embedded",
        "desc": (
            "Automated stepper-motor stage control for in-plane angular dependent Ferromagnetic Resonance measurements, "
            "executing precise angle increments with synchronized VNA acquisition triggers."
        ),
        "priority": 5,
    },
    "ntc-thermistor-monitor-audrino-programme": {
        "title": "NTC-Thermistor-monitor",
        "badge": "Arduino C++",
        "desc": (
            "Arduino firmware with Steinhart-Hart polynomial linearization to accurately log temperature profiles during "
            "chemical synthesis and thermal annealing cycles."
        ),
        "priority": 6,
    },
}

GITHUB_SVG_ICON = (
    '<svg fill="none" height="22" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="22">'
    '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7'
    'A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0'
    'C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7'
    'A3.37 3.37 0 0 0 9 18.13V22"></path></svg>'
)

def fetch_github_repos():
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?sort=updated&per_page=100"
    headers = {
        "User-Agent": "ArunB-Academic-Portfolio-Sync/1.0",
        "Accept": "application/vnd.github.v3+json",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except Exception as e:
        print(f"Error fetching GitHub repos from API: {e}")
        return None

def process_repos(api_repos):
    filtered = []
    for r in api_repos:
        name = r.get("name", "")
        # Filter out excluded repos (like 'portfolio') and forks
        if name.lower() in EXCLUDE_REPOS:
            continue
        if r.get("fork", False):
            continue

        key = name.lower()
        known = KNOWN_REPOS.get(key)

        title = known["title"] if known else name
        badge = known["badge"] if known else (r.get("language") or "Software")
        desc = known["desc"] if known else (r.get("description") or "Open-source scientific repository and laboratory automation tools authored by Arun B.")
        priority = known["priority"] if known else 99

        filtered.append({
            "name": name,
            "title": title,
            "badge": badge,
            "desc": desc,
            "url": r.get("html_url", f"https://github.com/{GITHUB_USER}/{name}"),
            "priority": priority,
            "updated_at": r.get("updated_at", ""),
            "stars": r.get("stargazers_count", 0),
        })

    # Sort by priority first (known tools in canonical order), then most recently updated
    filtered.sort(key=lambda x: (x["priority"], x["name"]))
    return filtered

def generate_repo_card_html(repo):
    return (
        '          <div class="repo-card">\n'
        '            <div class="repo-header">\n'
        '              <span class="repo-icon">\n'
        f'                {GITHUB_SVG_ICON}\n'
        '              </span>\n'
        f'              <span class="repo-lang-badge">{repo["badge"]}</span>\n'
        '            </div>\n'
        f'            <h3 class="repo-title">{repo["title"]}</h3>\n'
        '            <p class="repo-desc">\n'
        f'              {repo["desc"]}\n'
        '            </p>\n'
        f'            <a class="repo-link" href="{repo["url"]}" rel="noopener noreferrer" target="_blank">\n'
        '              View on GitHub &rarr;\n'
        '            </a>\n'
        '          </div>'
    )

def update_index_html(repos):
    target_files = ["website/index.html", "index.html"]
    for path in target_files:
        if not os.path.exists(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        cards_html = "\n".join([generate_repo_card_html(r) for r in repos])

        # Match the repos-grid container in website/index.html
        pattern = r'(<div class="repos-grid">)[\s\S]*?(</div>\s*</div>\s*</section>)'
        replacement = f'\\1\n<!-- REPOS_GRID_START -->\n{cards_html}\n<!-- REPOS_GRID_END -->\n          \\2'

        new_content, count = re.subn(pattern, replacement, content, count=1)
        if count == 0:
            # File might not have repos-grid (e.g. root redirect index.html)
            continue

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Successfully updated {path} with {len(repos)} repositories (excluded 'portfolio').")

def main():
    print("=" * 60)
    print("Arun B - Dynamic GitHub Repositories Sync Engine")
    print(f"Fetching public repositories for: {GITHUB_USER}...")
    print(f"Excluding repositories: {EXCLUDE_REPOS}")
    print("=" * 60)

    data = fetch_github_repos()
    if data is None:
        print("Failed to fetch repository data from GitHub.")
        sys.exit(1)

    repos = process_repos(data)
    print(f"Found {len(repos)} eligible repositories:")
    for r in repos:
        print(f"  - [{r['badge']}] {r['title']} ({r['url']})")

    update_index_html(repos)
    print("=" * 60)
    print(f"Repository synchronization finished on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
    print("=" * 60)

if __name__ == "__main__":
    main()

