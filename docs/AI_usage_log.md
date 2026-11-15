# Career Skills Translator — AI Usage Log

**Record format:** Entries group related prompts and follow-ups by development decision. Original conversation remains the primary chronological evidence. AI-response descriptions labeled “summary” are summaries, not verbatim transcripts. Only verified results and commits are recorded.

### AI-001: Initial Requirements Analysis

**Date initiated:** November 14, 2026  
**Requirements approved:** November 15, 2026  
**Development phase:** Phase 1: Requirements Analysis

**Original student prompt (verbatim transcription):**

```text
COSC 4272: Career Skills Translator | AI-Assisted Software Development Project

I am developing an application called Career Skills Translator for my COSC 4272 Senior Seminar AI-Assisted Software Development Project at Lamar University.

I want you to serve as my AI-assisted software development partner, technical advisor, and documentation assistant throughout this project.

Important: This conversation will serve as part of my official AI Usage Log for the assignment. We need to preserve an accurate, chronological record of our development process, including my prompts, your responses, my modifications, and the actual implementation results.

1. Project Overview

Project Name: Career Skills Translator

Purpose: Develop an AI-powered application that helps professionals identify how skills and competencies gained through their current occupations can transfer to different career fields.

Many experienced professionals underestimate how applicable their existing skills are outside their current industry. This application will help users recognize these transferable competencies and understand how they relate to other occupations.

Example:

A professional working as an Engineering Specialist wants to explore software development.

The application might identify transferable competencies such as:

- Technical troubleshooting → Software debugging
- Root-cause analysis → Defect investigation
- Process documentation → Technical documentation
- System analysis → Software systems analysis
- Continuous improvement → Software process optimization

Each translation must include an explanation of why the skill is relevant.

The application must not invent experience, exaggerate qualifications, or imply that possessing a transferable skill establishes proficiency in a new technical discipline.

2. Minimum Viable Product (MVP)

Our initial application will have five core functions:

1. Allow users to enter their current occupation and describe their professional responsibilities and experience.
2. Allow users to select or enter a target career field.
3. Use an AI language model to identify transferable skills supported by their experience.
4. Explain how those skills could apply to the target career.
5. Display the results in a clear, organized, readable format that users can copy.

The MVP should be functional, reasonably intuitive, and suitable for demonstration to a professor or prospective employer.

Features excluded from the initial MVP

We may add these in later versions:

- Resume rewriting
- Skills gap analysis
- Certification recommendations
- Personalized learning plans
- Job posting comparisons
- Career recommendations
- User accounts and saved profiles

Do not expand the scope without discussing it with me first.

3. Technology and Architecture

Our preliminary technology preference is:

- Python for application development
- Streamlit for the user interface
- An AI language-model API for skills analysis
- Git and GitHub for version control
- GitHub repository for project publication and documentation

These are preliminary choices. Evaluate their appropriateness before implementation, considering cost, simplicity, security, deployment, and ease of maintenance.

We want to produce a genuine working application with AI-powered analysis, not merely a static lookup table.

Follow appropriate practices for API key security, input validation, error handling, and protecting user-supplied career information.

4. Assignment Requirements

The professor requires:

Project Planning Document

- Problem statement
- Project objectives
- Functional requirements
- System features
- Software design
- Technology stack
- Development timeline

Technical Documentation

- "requirements.md", including functional requirements, non-functional requirements, assumptions, and project scope
- "README.md", including overview, features, installation, usage, screenshots, technologies, and future enhancements

Source Control

- At least 10 meaningful Git commits
- Preferably 15 to 25 incremental commits

AI Usage Log

- At least 10 genuine AI interactions
- Each entry must include the submitted prompt, AI-generated response, student modifications or refinements, and actual implementation result

Final Deliverables

- Complete source code
- GitHub repository link
- "requirements.md"
- "README.md"
- AI Usage Log
- Screenshots or demonstration materials
- Working software application

The application will also be showcased in my professional GitHub Pages portfolio.

5. AI Development and Documentation Rules

Please follow these rules throughout our collaboration:

1. Work incrementally through requirements, design, implementation, testing, debugging, and documentation.
2. Explain major technical decisions, including why we selected particular approaches.
3. Help me understand the code rather than simply generating a complete application without explanation.
4. Recommend logical Git commit points as features are completed.
5. Help maintain a chronological AI Usage Log.
6. Preserve my actual prompts and your responses accurately.
7. Record my modifications and decisions separately from AI recommendations.
8. Do not fabricate student contributions, testing results, commits, or completed functionality.
9. Clearly distinguish planned features, generated code, tested functionality, and completed deliverables.
10. Keep the MVP focused and avoid unnecessary technical complexity.

At the completion of each meaningful development milestone, help me prepare an AI Usage Log entry documenting:

- Interaction number
- Development phase
- My original prompt
- Summary or exact record of the AI response
- My modifications, corrections, or decisions
- Actual implementation result
- Related Git commit, if applicable

When an implementation result is not yet available, mark it as pending. When I have made no modifications, record that accurately.

The original conversation will remain the primary source of evidence for the AI-assisted development process.

6. Development Approach

We will use the following sequence:

Phase 1: Requirements Analysis
Define the problem, users, application scope, requirements, and measurable acceptance criteria.

Phase 2: System Design
Determine the architecture, technology stack, AI interaction workflow, and interface design.

Phase 3: MVP Implementation
Develop the application incrementally, testing individual components as they are completed.

Phase 4: Testing and Refinement
Evaluate the accuracy and usefulness of skills translations, input validation, error handling, and user experience.

Phase 5: Documentation and GitHub
Complete the required documentation, verify the commit history, and prepare the repository.

Phase 6: Demonstration and Portfolio Integration
Prepare screenshots, demonstrate the working application, and integrate it into the GitHub Pages portfolio.

7. How We Should Begin

Start with Phase 1: Requirements Analysis.

First, provide:

1. A concise problem statement.
2. The proposed MVP objectives.
3. A draft list of functional and non-functional requirements.
4. Measurable acceptance criteria.
5. A short assessment of the proposed technology stack.

Then help me develop our initial "requirements.md".

Do not generate the entire application immediately. We will make design decisions together, implement features incrementally, and document the actual development process as we proceed.

Our priorities are assignment compliance, practical usefulness, maintainable code, and genuine understanding of the software we develop.
```

**AI-generated response:** Proposed the problem statement, MVP objectives, functional and non-functional requirements, measurable acceptance criteria, and preliminary technology stack. Generated `requirements.md` v0.1.

**Student modifications, corrections, or decisions:** The student approved the requirements without modifications, stating: "I approve the requirements as drafted."

**Actual implementation result:** Initial requirements document generated and approved. Application implementation and testing have not begun.

**Related Git commit:** `5ad45d2` — `docs: add approved MVP requirements` (committed after requirements approval; also described in AI-002).

### AI-002: Repository Initialization and Requirements Commit

**Date:** November 15, 2026  
**Development phase:** Phase 1, Project Setup

**Original student prompt (verbatim):**

> The repository is new and empty, and I have an empty folder on my computer for the local repository: [https://github.com/PhoenixPrimeGames/Career-Skills-Translator](https://github.com/PhoenixPrimeGames/Career-Skills-Translator)

**Follow-up student evidence:** The student submitted actual outputs from `git status`, `git remote -v`, `dir requirements.md`, `git add`, `git commit`, `git push`, and `git log`. The student also reported a file-download failure, then successfully placed the requirements document in the local project folder. These additional prompts and terminal transcripts are preserved verbatim in the original conversation; the log summarizes them rather than counting them as separate numbered entries.

**AI-generated response:** Provided Git cloning instructions, Git status and remote verification commands, requirements-file placement instructions, and commands for committing and pushing the approved requirements.

**Student modifications or decisions:** The student followed the proposed Git workflow. No modifications to the requirements were reported.

**Actual implementation result:** The local Git repository was successfully connected to GitHub. The approved `requirements.md` was committed and pushed to the `main` branch. Immediately following that push, the working tree was clean and synchronized with the remote. Subsequent untracked documentation files are recorded in later entries.

**Verified Git commit:** `5ad45d2` — `docs: add approved MVP requirements`.

### AI-003: Initial System Architecture

**Date:** November 15, 2026  
**Development phase:** Phase 2: System Design

**Original student prompt:** "I approve this starting architecture"

**AI-generated response:** Recorded approval of the proposed modular Python and Streamlit architecture, separating user interface, input validation, AI integration, and automated tests. Initiated evaluation of potential language-model API providers.

**Student modifications or decisions:** Approved the architecture proposed in the preceding AI response without requesting changes.

**Actual implementation result:** Architecture approved as the initial system design baseline. No source code has been implemented or tested.

**Related Git commit:** None for this approval itself; `c84eb05` later recorded the finalized architecture document (see AI-006).

### AI-004: Language-Model API Reevaluation and Selection

**Date:** November 15, 2026

**Development phase:** Phase 2: System Design

**Original student prompt:**

"**OpenAI GPT-4.1 mini** is deprecated. GPT-6 Luna is the current iteration of a model of that size. https://developers.openai.com/api/docs/models/gpt-6-luna . Let's reevaluate the API choices based on non-deprecated AI models."

**AI-generated response summary:**

Compared currently available language models, including GPT-6 Luna, Claude Haiku 5.5, Gemini 3.5 Flash-Lite, and GPT-6.1 Terra. Evaluated pricing, structured outputs, privacy considerations, and suitability for Career Skills Translator. Recommended GPT-6 Luna provisionally.

**Student follow-up:**

"Your choice seems a little biased, but it also makes sense for this case. I approve using Luna as the initial AI model."

**Student modifications, corrections, or decisions:**

- Corrected the AI's earlier recommendation of a deprecated model.
- Requested an evaluation using non-deprecated alternatives.
- Identified potential provider bias in the recommendation.
- Approved GPT-6 Luna as the initial AI model.

**Actual implementation result:**

GPT-6 Luna selected for the initial MVP. API integration, accuracy testing, and performance evaluation have not yet occurred.

**Related Git commit:** None.

### AI-005: Response Schema Approval and Extensibility

**Date:** November 15, 2026

**Development phase:** Phase 2: System Design

**Original student prompt:**

"I approve this response structure, so long as we also have the ability to easily add to the structure later with minimal changes to the application."

**AI-generated response summary:**

Accepted the approved five-field transferable-skills structure and proposed extending the initial architecture with a dedicated `schemas.py` module. Recommended Pydantic models as centralized response definitions, a schema-driven results renderer, and separate AI behavioral instructions. Drafted initial response models and explained extensibility limitations.

**Student modifications, corrections, or decisions:**

Approved the proposed response structure with the additional requirement that future response fields should be easy to introduce without extensive application modifications.

**Actual implementation result:**

The five-field response structure and extensibility requirement are approved. A preliminary Pydantic schema and model behavior rules have been proposed. No schema module has been implemented or tested.

**Related Git commit:** None.

### AI-006: Architecture Documentation and AI Instruction Design

**Date:** November 15, 2026  
**Development phase:** Phase 2: System Design

**Original student prompt:** "let's continue with the next development step"

**AI-generated response summary:** Formalized the approved modular architecture, prepared `ARCHITECTURE.md`, proposed AI instructions and evidence-validation rules, and documented error handling, security, extensibility, and testing considerations.

**Student modifications or decisions:** The student stated, "I approve the architecture document as written." No content changes were reported.

**Actual implementation result:** `docs/ARCHITECTURE.md` was placed in the local repository, verified with `dir docs` and `git status`, approved without reported changes, committed, and pushed to GitHub. The follow-up `git status` showed `docs/AI_usage_log.md` still untracked. No application code has been implemented or tested.

**Related Git commit:** `c84eb05` — `docs: document approved system architecture`.

