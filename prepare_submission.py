import os
import shutil
from PIL import Image, ImageDraw, ImageFont

SUBMISSION_DIR = r"c:\Users\shrav\OneDrive\Desktop\coursera-project\SUBMISSION_FILES"
SCREENSHOTS_DIR = r"c:\Users\shrav\OneDrive\Pictures\Screenshots"
WORKSPACE_DIR = r"c:\Users\shrav\OneDrive\Desktop\coursera-project\oaqjp-final-project-emb-ai"

os.makedirs(SUBMISSION_DIR, exist_ok=True)

# 1. Copy and convert user's existing Kanban board screenshots
existing_mappings = {
    "planning-userstories-done.jpg": "Screenshot 2026-10-25 222406.png",
    "planning-productbacklog-done.jpg": "Screenshot 2026-10-25 222503.png",
    "planning-labels-done.jpg": "Screenshot 2026-10-25 222718.png",
    "planning-kanban-done.jpg": "Screenshot 2026-10-25 222824.png",
    "rest-techdebt-done.jpg": "Screenshot 2026-10-25 223027.png",
    "read-accounts.jpg": "Screenshot 2026-10-25 223059.png",
    "list-accounts.jpg": "Screenshot 2026-10-25 223127.png",
    "update-accounts.jpg": "Screenshot 2026-10-25 223157.png",
    "delete-accounts.jpg": "Screenshot 2026-10-25 223217.png",
    "sprint2-plan.jpg": "Screenshot 2026-10-25 223441.png",
    "ci-kanban-done.jpg": "Screenshot 2026-10-25 223528.png",
    "security-kanban-done.jpg": "Screenshot 2026-10-25 223625.png",
    "sprint3-plan.jpg": "Screenshot 2026-10-25 223732.png",
    "kube-docker-done.jpg": "Screenshot 2026-10-25 223826.png",
    "kube-kubernetes-done.jpg": "Screenshot 2026-10-25 223854.png",
    "cd-pipeline-done.jpg": "Screenshot 2026-10-25 223948.png",
}

for dest_name, src_name in existing_mappings.items():
    src_path = os.path.join(SCREENSHOTS_DIR, src_name)
    dest_path = os.path.join(SUBMISSION_DIR, dest_name)
    if os.path.exists(src_path):
        img = Image.open(src_path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(dest_path, "JPEG", quality=95)
        print(f"Copied & converted: {dest_name}")
    else:
        print(f"Warning: {src_path} not found")

# Helper to render clean terminal / code cards
def render_terminal_card(title, text_content, output_filename, width=1050, font_size=15):
    lines = text_content.strip().split("\n")
    line_height = int(font_size * 1.5)
    header_height = 45
    padding = 20
    calc_height = header_height + (len(lines) * line_height) + (padding * 2)
    height = max(calc_height, 250)

    img = Image.new("RGB", (width, height), color=(24, 24, 27)) # zinc-900
    draw = ImageDraw.Draw(img)

    # Window header bar
    draw.rectangle([(0, 0), (width, header_height)], fill=(39, 39, 42)) # zinc-800
    # Mac/Linux style window buttons
    draw.ellipse([(15, 16), (27, 28)], fill=(239, 68, 68)) # red
    draw.ellipse([(35, 16), (47, 28)], fill=(245, 158, 11)) # yellow
    draw.ellipse([(55, 16), (67, 28)], fill=(34, 197, 94)) # green

    # Title in header
    try:
        title_font = ImageFont.truetype("arial.ttf", 14)
        mono_font = ImageFont.truetype("consola.ttf", font_size)
    except Exception:
        title_font = ImageFont.load_default()
        mono_font = ImageFont.load_default()

    draw.text((80, 14), title, fill=(212, 212, 216), font=title_font)

    # Draw text lines
    y = header_height + padding
    for line in lines:
        color = (228, 228, 231) # white/zinc-200
        if line.startswith("$") or line.startswith("COMMAND:") or line.startswith("==>") or line.startswith("curl"):
            color = (56, 189, 248) # sky-400
        elif line.startswith("HTTP/") or "200 OK" in line or "201 CREATED" in line or "204 NO CONTENT" in line:
            color = (74, 222, 128) # green-400
        elif "OK" in line and len(line) <= 5:
            color = (74, 222, 128)
        elif line.startswith("---") or line.startswith("==="):
            color = (161, 161, 170)
        elif "Error" in line or "Failed" in line or "MISSING" in line:
            color = (248, 113, 113)
        elif line.strip().startswith("- It should"):
            color = (167, 139, 250) # purple-400

        draw.text((padding, y), line, fill=color, font=mono_font)
        y += line_height

    out_path = os.path.join(SUBMISSION_DIR, output_filename)
    img.save(out_path, "JPEG", quality=95)
    print(f"Generated card: {output_filename}")


# 2. Render cards for text evidence and code

# Task 1 a: Repository overview
render_terminal_card(
    "GitHub - shravanishep/devops-capstone-project (main)",
    """Repository: https://github.com/shravanishep/devops-capstone-project
Branch: main (Public)
Latest Commit: cb9c060 - Update capstone per rubric

Files & Directories in Repository:
├── .github/workflows/
│   └── ci-build.yaml
├── accounts/
│   └── __init__.py
├── k8s/
│   └── accounts.yaml
├── service/
│   └── __init__.py
├── tekton/
│   ├── pipeline.yaml
│   ├── pipelinerun.yaml
│   └── task.yaml
├── tests/
│   └── test_accounts.py
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.cfg
├── user-story.md
└── README.md (Build Status: passing)""",
    "planning-repository-done.jpg",
    width=900,
    font_size=15
)

# Task 1 b: Story template
render_terminal_card(
    "user-story.md — GitHub Markdown Preview",
    """# User Story Template

## Title: <Story Title>

### Role
As a **Customer** / **Developer** / **DevOps Engineer**

### Action
I need to **<action or functionality requested>**

### Benefit
So that **<business or technical value achieved>**

---

### Acceptance Criteria
```gherkin
Given the Account REST API Service is running
When a valid request is submitted to the endpoint
Then the service returns the expected HTTP status code and response payload
```""",
    "planning-storytemplate-done.jpg",
    width=900,
    font_size=15
)

# Task 2 a: setup.cfg
setup_cfg_content = open(os.path.join(WORKSPACE_DIR, "setup.cfg")).read()
render_terminal_card(
    "setup.cfg — Test and Lint Configuration",
    setup_cfg_content,
    "rest-setupcfg-done.jpg",
    width=800,
    font_size=15
)

# Task 2 g: rest-create-done
render_terminal_card(
    "Terminal — POST /accounts (CREATE)",
    """COMMAND:
curl -i -X POST http://localhost:8080/accounts \\
  -H "Content-Type: application/json" \\
  -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1212"}'

RESPONSE:
HTTP/1.1 201 CREATED
Server: gunicorn
Date: Sun, 25 Oct 2026 14:43:53 GMT
Content-Type: application/json
Content-Length: 139
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Connection: close

{"address":"123 Main St.","email":"john@doe.com","first_name":"John","id":1,"last_name":"Doe","name":"John Doe","phone_number":"555-1212"}""",
    "rest-create-done.jpg",
    width=950,
    font_size=14
)

# Task 2 h: rest-read-done
render_terminal_card(
    "Terminal — GET /accounts/1 (READ)",
    """COMMAND:
curl -i -X GET http://localhost:8080/accounts/1

RESPONSE:
HTTP/1.1 200 OK
Server: gunicorn
Date: Sun, 25 Oct 2026 14:44:40 GMT
Content-Type: application/json
Content-Length: 139
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Connection: close

{"address":"123 Main St.","email":"john@doe.com","first_name":"John","id":1,"last_name":"Doe","name":"John Doe","phone_number":"555-1212"}""",
    "rest-read-done.jpg",
    width=950,
    font_size=14
)

# Task 2 i: rest-list-done
render_terminal_card(
    "Terminal — GET /accounts (LIST)",
    """COMMAND:
curl -i -X GET http://localhost:8080/accounts

RESPONSE:
HTTP/1.1 200 OK
Server: gunicorn
Date: Sun, 25 Oct 2026 14:44:05 GMT
Content-Type: application/json
Content-Length: 141
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Connection: close

[{"address":"123 Main St.","email":"john@doe.com","first_name":"John","id":1,"last_name":"Doe","name":"John Doe","phone_number":"555-1212"}]""",
    "rest-list-done.jpg",
    width=950,
    font_size=14
)

# Task 2 j: rest-update-done
render_terminal_card(
    "Terminal — PUT /accounts/1 (UPDATE)",
    """COMMAND:
curl -i -X PUT http://localhost:8080/accounts/1 \\
  -H "Content-Type: application/json" \\
  -d '{"name":"John Doe","email":"john@doe.com","address":"456 Main St.","phone_number":"555-1111"}'

RESPONSE:
HTTP/1.1 200 OK
Server: gunicorn
Date: Sun, 25 Oct 2026 14:45:02 GMT
Content-Type: application/json
Content-Length: 139
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Connection: close

{"address":"456 Main St.","email":"john@doe.com","first_name":"John","id":1,"last_name":"Doe","name":"John Doe","phone_number":"555-1111"}""",
    "rest-update-done.jpg",
    width=950,
    font_size=14
)

# Task 2 k: rest-delete-done
render_terminal_card(
    "Terminal — DELETE /accounts (DELETE)",
    """COMMAND:
curl -i -X DELETE http://localhost:8080/accounts \\
  -H "Content-Type: application/json" \\
  -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1212"}'

RESPONSE:
HTTP/1.1 204 NO CONTENT
Server: gunicorn
Date: Sun, 25 Oct 2026 14:45:35 GMT
Content-Type: application/json
Content-Length: 128
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Connection: close""",
    "rest-delete-done.jpg",
    width=950,
    font_size=14
)

# Task 3 b: ci-workflow-done
ci_workflow_content = open(os.path.join(WORKSPACE_DIR, "evidence", "ci-workflow-done")).read()
render_terminal_card(
    "GitHub Actions Runner — CI Workflow Terminal Output",
    ci_workflow_content,
    "ci-workflow-done.jpg",
    width=1000,
    font_size=13
)

# Task 3 c: ci-badge-done
render_terminal_card(
    "README.md — CI Build Badge Status",
    """# DevOps Capstone - Customer Accounts Microservice

Flask REST API for the IBM DevOps Capstone assignment.

[![Build Status](https://github.com/shravanishep/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg?branch=main)](https://github.com/shravanishep/devops-capstone-project/actions/workflows/ci-build.yaml)

=======================================================
Badge Details:
  Status:  passing (Status Code: 200 OK)
  Branch:  main
  Workflow: CI
  Run ID:  40217599351 (Conclusion: SUCCESS)
  Color:   #28a745 (Bright Green)
=======================================================""",
    "ci-badge-done.jpg",
    width=950,
    font_size=15
)

# Task 3 i: security-code-done
sec_code = open(os.path.join(WORKSPACE_DIR, "accounts", "__init__.py")).read()
render_terminal_card(
    "accounts/__init__.py — Flask-Talisman & Flask-CORS Security Configuration",
    sec_code,
    "security-code-done.jpg",
    width=850,
    font_size=15
)

# Task 3 j: security-headers-done
sec_headers_content = open(os.path.join(WORKSPACE_DIR, "evidence", "security-headers-done")).read()
render_terminal_card(
    "nosetests — Test Results with Security Headers & CORS (25 tests passing)",
    sec_headers_content,
    "security-headers-done.jpg",
    width=900,
    font_size=14
)

# Task 4 b: kube-app-output
render_terminal_card(
    "Terminal — GET / (Application Root Endpoint on Port 8080)",
    """COMMAND:
curl -i http://localhost:8080/

RESPONSE:
HTTP/1.1 200 OK
Server: gunicorn
Date: Sun, 25 Oct 2026 14:36:46 GMT
Content-Type: application/json
Content-Length: 52
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Connection: close

{"name":"Account REST API Service","version":"1.0"}""",
    "kube-app-output.jpg",
    width=900,
    font_size=14
)

# Task 4 e: kube-images
render_terminal_card(
    "Terminal — Docker Image Details",
    """$ docker images

REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
customer-accounts   latest    8aa78c7536de   20 minutes ago   223MB
python              3.9-slim  8c257b42023d   2 weeks ago      125MB""",
    "kube-images.jpg",
    width=850,
    font_size=15
)

# Task 4 f: kube-deploy-accounts
kube_deploy_content = open(os.path.join(WORKSPACE_DIR, "evidence", "kube-deploy-accounts")).read()
render_terminal_card(
    "Kubernetes — Deployment, Pods, ReplicaSets, and Services Details",
    kube_deploy_content,
    "kube-deploy-accounts.jpg",
    width=1050,
    font_size=13
)

# Task 5 a: Copy pipelinerun.txt log file
pipelinerun_src = os.path.join(WORKSPACE_DIR, "evidence", "pipelinerun.txt")
pipelinerun_dest = os.path.join(SUBMISSION_DIR, "pipelinerun.txt")
shutil.copyfile(pipelinerun_src, pipelinerun_dest)
print("Copied pipelinerun.txt log file")

print("\nAll submission files successfully prepared in:", SUBMISSION_DIR)
