# Career Skills Translator - Requirements Specification

**Course:** COSC 4272 Senior Seminar, Lamar University  
**Project:** Career Skills Translator  
**Document version:** 0.1 (initial AI-assisted draft)  
**Draft date:** 2026-11-14  
**Status:** Approved requirements baseline (student approval: 2026-11-15)  
**Development phase:** Phase 1 - Requirements Analysis

> This document defines the student-approved MVP requirements baseline. It does not indicate that any
> software has been implemented, tested, deployed, or committed to Git.

## 1. Problem statement

Professionals seeking to transition into different career fields may struggle to
recognize how their existing occupational knowledge, responsibilities, and
competencies apply to unfamiliar roles. Career Skills Translator will use an AI
language model to analyze self-described experience and explain plausible,
evidence-based skill transfers to a user-selected career field. It must avoid
inventing experience or presenting transferable skills as proof of specialized
qualifications or proficiency in the target field.

## 2. Intended users and objectives

**Primary users:** Professionals exploring a potential change of occupation or
industry, including workers with substantial domain-specific experience.

| ID | MVP objective |
| --- | --- |
| OBJ-01 | Collect current occupation and described professional experience. |
| OBJ-02 | Collect the user's target career field. |
| OBJ-03 | Use an external AI language-model API for contextual analysis. |
| OBJ-04 | Explain skill transfers using evidence from the user's description. |
| OBJ-05 | Display readable results that can be copied as text. |
| OBJ-06 | Avoid unsupported claims of experience, credentials, or proficiency. |

## 3. Scope

### 3.1 In scope for the MVP

1. One-page application for entering a current occupation, free-text work experience,
   and a target career field.
2. Input validation and clear actionable feedback.
3. On-demand, live analysis through a configurable AI model API.
4. Identification of transferable competencies supported by the input, with a clear
   connection to the target field and a written explanation.
5. A readable, copyable results section.
6. Handling of missing credentials, insufficient evidence, API problems, and
   malformed or unusable responses.
7. Local execution, tests, documentation, and deployment suitable for a course
   demonstration.

### 3.2 Out of scope for the initial MVP

- Resume rewriting
- Skills gap analysis
- Certification recommendations
- Personalized learning plans
- Job posting comparisons
- Career recommendations
- User accounts, saved profiles, or persistent user history

Any expansion of application scope requires discussion and an explicit decision.

## 4. Functional requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-01 | The application shall allow users to enter their current occupation. | Must |
| FR-02 | The application shall allow users to describe responsibilities and relevant work experience in free text. | Must |
| FR-03 | The application shall allow users to enter their target career field. | Must |
| FR-04 | The application shall validate required fields and length limits before analysis. | Must |
| FR-05 | The application shall submit validated inputs to a configured live AI language-model API on explicit user request. | Must |
| FR-06 | The application shall identify only transferable competencies reasonably supported by the supplied experience. | Must |
| FR-07 | For each returned competency, the application shall show the source-experience evidence, possible target-career application, and an explanation of relevance. | Must |
| FR-08 | The application shall present results in an organized, readable, copyable text format. | Must |
| FR-09 | The application shall handle missing API configuration, API failure or timeout, insufficient supporting evidence, and unusable responses with understandable feedback. | Must |

**Interpretation of FR-06 and FR-07:** Evidence is based on the user's
self-reported experience, not independently verified employment history.
An analysis may return no supported skills when the description is insufficient.
The app must not claim that the user already possesses target-field certifications,
work experience, or technical proficiency that the user did not describe.

## 5. Non-functional requirements

| ID | Category | Requirement |
| --- | --- | --- |
| NFR-01 | Credential security | API keys shall be provided through environment variables or Streamlit secrets and excluded from the repository, visible output, and error messages. |
| NFR-02 | Privacy | The app shall not intentionally persist personal career descriptions in a database or application logs. The user shall be informed that submitted text is sent to an external AI provider. |
| NFR-03 | Reliability | Expected configuration errors, HTTP/API failures, and timeouts shall be handled without an uncaught error shown to the user. |
| NFR-04 | Maintainability | Input validation, API communication/analysis, and user-interface code shall be separable and documented. |
| NFR-05 | Usability | All input controls shall have clear labels; progress, errors, and results shall be easy to understand. Results shall be readable at common desktop and mobile browser widths. |
| NFR-06 | Performance | A submission shall show a visible processing indicator promptly; a configurable API timeout shall prevent indefinite waiting. Initial proposed timeout: 45 seconds. |
| NFR-07 | Testability | Input validation and AI-response parsing/validation shall support automated testing with mocked API responses, without making paid requests. |
| NFR-08 | Cost control | Request and response sizes shall be bounded, and each user submission shall ordinarily initiate at most one billable analysis request. Automatic repeated calls are not part of the MVP. |
| NFR-09 | Transparency | Results shall clearly identify AI-generated analysis as an interpretation, not verification of work history or professional qualifications. |

The third-party provider may process or retain transmitted text under its own terms.
The application cannot promise that an external provider retains no data.

## 6. Proposed input and output rules

These values and behaviors are provisional until reviewed and tested.

| Field | Proposed constraint |
| --- | --- |
| Current occupation | Required; 2-100 characters after trimming whitespace |
| Professional responsibilities and experience | Required; 20-4,000 characters after trimming whitespace |
| Target career field | Required; 2-100 characters after trimming whitespace |

**Proposed result structure:** Zero or more transferable-skill entries, each with
(1) competency name, (2) evidence from the user's description, (3) potential
application in the target career, and (4) an explanation. When supporting
information is inadequate, show a clear insufficiency message. Show a
notice about limitations of AI-generated analysis. The specific response format
and parser will be selected during system design.

## 7. Acceptance criteria and verification plan

| ID | Related requirement(s) | Acceptance criterion | Proposed verification |
| --- | --- | --- | --- |
| AC-01 | FR-01 to FR-04 | Blank or whitespace-only required fields block submission and identify the problem field. | Automated boundary tests and manual UI check |
| AC-02 | FR-04 | The application enforces the proposed field-length limits, including exactly-at-limit and over-limit cases. | Automated boundary tests |
| AC-03 | FR-05 | A valid submission triggers a live request to the configured AI API and displays its processed response. | Integration test with a test API credential |
| AC-04 | FR-06, FR-07 | Each displayed skill includes explicit supporting experience and an explanation of its target-field relevance. | Response-shape tests and manual content review |
| AC-05 | FR-06, NFR-09 | In the curated evaluation set, accepted outputs do not invent certifications, experience, or target-field proficiency. | Manual evaluation using a grounding checklist |
| AC-06 | FR-06, FR-09 | When experience is insufficient, the result may state insufficient evidence rather than inventing entries. | Mock response and manual scenario test |
| AC-07 | FR-08, NFR-05 | A user can copy the complete resulting analysis as text; the layout remains usable on desktop and mobile. | Manual browser check |
| AC-08 | FR-09, NFR-01, NFR-03 | Missing credentials, simulated provider failures, malformed responses, and timeouts produce understandable feedback with no disclosed secrets. | Mocked failure tests and manual UI check |
| AC-09 | NFR-04, NFR-07 | Automated tests for input validation and response processing pass without any live model request. | Test suite run |
| AC-10 | FR-06, FR-07, NFR-09 | A minimum of 10 representative career-transition examples are reviewed for evidence, explanation quality, and unsupported claims. The results and any failures are documented. | Manual evaluation log |
| AC-11 | NFR-02, NFR-08 | Code review finds no app-controlled persistent storage of user descriptions, no input text in logs, no hardcoded secrets, and bounded request sizes. | Security/privacy checklist and code review |
| AC-12 | NFR-05, NFR-06 | The app shows processing feedback after submission and exits its processing state with a result or usable error after the configured timeout. | Manual and mocked timeout checks |
| AC-13 | Deployment objective | The app runs locally and, once deployed, is reachable at a documented public URL. | Local smoke test and hosted smoke test |

Acceptance is evaluated only after actual tests are executed and recorded.

## 8. Assumptions and constraints

1. Initial UI and implementation will likely use Python and Streamlit; this is
   provisional until Phase 2 design review.
2. A live external AI model API and usable credentials will be available for
   development and demonstration. API costs and provider limits must be checked.
3. The user's professional information is self-reported; the tool does not verify
   resumes, employment histories, licensing, or qualifications.
4. Users should avoid submitting confidential or sensitive employer information.
5. A lightweight single-user interaction model is sufficient for the MVP. User
   accounts and persistent storage are excluded.
6. GitHub Pages may showcase and link to the project but cannot execute the
   Python/Streamlit application. The app requires a Python-capable host.
7. Project milestones and calendar deadlines will be documented in the separate
   Project Planning Document after the course deadline is established.
8. The app must demonstrate genuine live AI analysis; hardcoded sample mappings
   alone cannot satisfy FR-05.

## 9. Preliminary technology assessment (not yet finalized)

| Component | Proposal | Rationale / risk |
| --- | --- | --- |
| Language | Python | Readable and suitable for API requests and unit testing |
| User interface | Streamlit | Low implementation overhead, but design flexibility is more limited than a custom frontend |
| Analysis | Configurable model-provider API | Genuine context-sensitive analysis; incurs cost and introduces provider latency and privacy considerations |
| Source control | Git and GitHub | Supports graded commit history and public portfolio evidence |
| Application hosting | Streamlit Community Cloud, subject to final review | GitHub-connected Python hosting; hosting limits and service reliability must be considered |
| Portfolio hosting | GitHub Pages | Static project summary and link to hosted application, not a Python execution environment |

## 10. Documentation and course compliance

The course assignment calls for a Project Planning Document (problem statement,
objectives, functional requirements, features, software design, stack, and timeline),
`requirements.md`, `README.md` (overview, features, installation, usage,
screenshots, technologies, future enhancements), an AI Usage Log with at least
10 documented prompts, Git/GitHub history with at least 10 meaningful commits
(15-25 recommended), full code, demonstration materials, and a working app.

This file is the **requirements specification**, not a substitute for the
Project Planning Document, README, testing evidence, or AI Usage Log.

## 11. Open decisions for Phase 2

- Confirm or revise input length limits and the 45-second timeout.
- Choose the AI provider/model based on price, response quality, supported
  structured outputs, and privacy terms.
- Select response schema and a policy for checking required fields and evidence.
- Confirm a feasible public-hosting approach and how to control API costs for
  an unauthenticated public demo.
- Confirm testing standards and any assignment-specific demonstration deadline.

## 12. Change history

| Version | Date | Change | Status |
| --- | --- | --- | --- |
| 0.1 | 2026-11-14 | Initial AI-assisted draft based on student project brief and assignment instructions; approved unchanged by student on 2026-11-15 | Approved |

## References

- *AI-Assisted Software Development Project*, COSC 4272 assignment, provided by student (5 pages).
- Streamlit secrets management: https://docs.streamlit.io/develop/concepts/connections/secrets-management
- Streamlit Community Cloud: https://docs.streamlit.io/deploy/streamlit-community-cloud
- GitHub Pages documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- API costs and model choice: https://platform.openai.com/pricing/
