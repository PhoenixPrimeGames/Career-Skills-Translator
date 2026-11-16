# Career Skills Translator: Project Planning Document

**Course:** COSC 4272 Senior Seminar, Lamar University  
**Project:** Career Skills Translator  
**Document version:** 0.2 (deployment status update)
**Prepared:** November 15, 2026  
**Project type:** Individual, AI-assisted software development  
**Planning baseline:** Student-approved `requirements.md` v0.1  
**Repository:** https://github.com/PhoenixPrimeGames/Career-Skills-Translator  
**Course submission deadline:** Not established in the reviewed project materials


> **Document purpose and status:** Version 0.1 was approved by
> the student on November 15, 2026. Version 0.2 updates the
> recorded implementation, documentation, and deployment status
> without changing the approved project objectives or scope.
> The MVP is deployed on Streamlit Community Cloud with
> restricted access. Public, unrestricted access and portfolio
> integration remain pending.


## 1. Problem statement

Professionals exploring career changes may find it difficult to identify skills developed in one occupation that could apply to another field. Career Skills Translator analyzes a user's self-described professional responsibilities and explains plausible, evidence-supported transferable competencies for a user-selected career field. Its analysis must not invent work experience, certifications, technical proficiency, or qualifications for the target field.

The application offers exploratory career insight. It does not independently verify experience, assess hiring eligibility, or guarantee employment outcomes.

## 2. Project objectives

| ID | Objective | Intended outcome |
| --- | --- | --- |
| OBJ-01 | Collect current occupation and professional responsibilities | Users can describe experience in their own words. |
| OBJ-02 | Collect the target career field | Users can choose a field to explore. |
| OBJ-03 | Use a live language-model API | Results are generated from submitted context rather than a static lookup table. |
| OBJ-04 | Explain evidence-supported skill transfer | Each listed competency includes source evidence, a potential application, an explanation, and limitations. |
| OBJ-05 | Make results accessible and copyable | Users can read a structured result and copy its complete plain-text version. |
| OBJ-06 | Limit unsupported claims | Insufficient evidence can produce a zero-skill result; the interface discloses AI-analysis limitations. |

**Intended audience:** Adults with professional experience who are exploring different occupations or industries, including people whose existing experience does not directly match the target field.

## 3. MVP scope and features

### In scope

1. A single-page Streamlit form with current occupation, responsibilities/experience, and target career field.
2. Server-side validation of required inputs and length limits before an API request.
3. On-demand analysis using the OpenAI Responses API and a configurable model identifier in application code.
4. Structured results with an overall status, explanatory summary, and evidence-grounded transferable skills.
5. For each skill: competency, source evidence, target application, explanation, and limitations.
6. A visible insufficient-information outcome when no meaningful competency is supported.
7. Readable error messages for missing credentials, API failures, and invalid responses.
8. A complete, copyable plain-text analysis, including an AI-generated-content disclaimer.
9. Local automated testing, fictional live evaluation scenarios, documentation, source control, and demonstration preparation.

### Out of scope for this MVP

Resume rewriting; skills-gap analysis; certification or learning-plan recommendations; job posting comparison; automatic career recommendations; user accounts; saved career histories; and persistent user profiles. Any expansion requires a separately reviewed scope decision.

## 4. Functional requirements

The approved `requirements.md` is the authoritative requirements baseline. The IDs below are repeated here for planning and traceability.

| ID | Required capability | Planned verification |
| --- | --- | --- |
| FR-01 | Enter current occupation | Form inspection and UI test |
| FR-02 | Describe responsibilities and experience | Form inspection and UI test |
| FR-03 | Enter target career field | Form inspection and UI test |
| FR-04 | Validate required inputs and limits | Pydantic boundary tests and manual checks |
| FR-05 | Call a live AI API on explicit submission | Live integration test and browser check |
| FR-06 | Identify only reasonably supported transferable skills | Evidence verification and human-scored fictional scenarios |
| FR-07 | Show evidence, potential application, and explanation for each skill | Schema tests and result review |
| FR-08 | Display an organized, copyable result | Streamlit tests and copy-to-text manual check |
| FR-09 | Handle missing configuration, timeout, insufficient evidence, and unusable responses | Mocked failures, schema checks, and targeted live evaluation |

## 5. Non-functional requirements and constraints

| Area | Design constraint or quality objective |
| --- | --- |
| Security | Keep API keys in `OPENAI_API_KEY` or Streamlit secrets, outside source control; do not display them in errors. |
| Privacy | Do not intentionally maintain a user-profile database or application-managed history. Notify users that their description is sent to an external provider. Provider retention is governed separately. |
| Reliability | Use safe error handling and a bounded API request timeout. Do not present invalid or fabricated fallback results as genuine analysis. |
| Usability | Clearly labeled inputs, validation feedback, progress indicator, readable mobile and desktop layouts, and copyable results. |
| Maintainability | Keep UI (`app.py`), validation (`validation.py`), schemas (`schemas.py`), and AI integration (`analysis.py`) separate. |
| Testability | Mock API calls in automated tests; reserve billable live requests for explicit, controlled integration and evaluation checks. |
| Cost control | Bound user input sizes, set a finite output-token budget, avoid automatic retries, and evaluate budget/abuse controls before public hosting. |
| Transparency | Identify output as interpretation of self-reported experience rather than verified qualifications. |

**Implemented input limits:** Occupation 2 to 100 characters; experience description 20 to 4,000 characters; target field 2 to 100 characters, evaluated after stripping surrounding whitespace.

## 6. Software design and data flow

```text
User browser
    |
    v
Streamlit UI (app.py)
    |
    +--> Pydantic input validation (validation.py)
    |
    +--> AI request orchestration (analysis.py)
             |
             +--> instructions + serialized user input
             +--> OpenAI Responses API (configured model: gpt-6-luna)
             +--> structured parsing (schemas.py)
             +--> source-evidence checks and error handling
    |
    v
Streamlit results renderer (app.py)
    |
    +--> status and summary
    +--> skills with evidence, application, explanation, limitations
    +--> complete copyable text and disclaimer
```

**Runtime behavior:** A user submits the form; invalid input prevents API submission. For valid inputs and available credentials, the application sends a request to the external provider and parses the result into Pydantic models. It verifies evidence excerpts against the user's experience text, rejects unusable responses, and renders a validated result or a safe error message. User text is treated as untrusted source data rather than instructions to the application.

**Structured response:** `AnalysisResult` contains `status`, `summary`, and `skills`. Each `SkillTranslation` has `skill`, `source_evidence`, `target_application`, `explanation`, and `limitations`. A `completed` result requires at least one skill; `insufficient_information` requires zero skills.

**Verified implementation settings:** Configured model `gpt-6-luna`; API timeout 45 seconds; maximum output tokens 2,500; reasoning effort `low`; API response storage requested with `store=False`. This does not imply the provider retains no information.


**Deployment architecture:** Career Skills Translator is hosted
on Streamlit Community Cloud at
https://career-skills-translator-main.streamlit.app/.

Application access is restricted to explicitly authorized viewers.
The OpenAI API key is configured through Streamlit's hosted
Secrets settings and is not committed to Git.

The student verified successful application startup, safe
handling of missing API credentials, and one completed hosted
AI analysis on November 15, 2026.

An enforced $5 spending limit is configured for the OpenAI API
project. Minor spending beyond the limit may still be possible
due to enforcement delays.

The application has not been approved for unrestricted public
access. GitHub Pages portfolio integration remains pending.


## 7. Technology stack

| Technology | Role | Basis |
| --- | --- | --- |
| Python 3.14.5 | Application and test execution environment | Student-reported successful local runs |
| Streamlit `>=1.61,<2` | Web interface | `app.py` and `requirements.txt` |
| Pydantic `>=2,<3` | Input and output validation | `validation.py`, `schemas.py`, requirements |
| OpenAI Python SDK `>=3.51,<4` | Responses API integration and structured parsing | `analysis.py`, `requirements.txt` |
| GPT-6 Luna | Initial analysis model | Student-approved selection and configured model ID |
| pytest `>=8,<10` | Automated test execution | `requirements-dev.txt`; latest student-reported run: 56 passed |
| Git and GitHub | Version control and project evidence | 15 verified commits through `2f432eb` |
| Streamlit Community Cloud | Restricted application hosting | Deployed; startup and live AI integration verified |

## 8. Development method and milestone schedule

Development follows an incremental, student-reviewed AI-assisted process. Each milestone introduces limited changes, records tests and actual results, and uses Git commits as traceable checkpoints. The dates below are **historical completion evidence**, not a fabricated future schedule. Remaining milestones are ordered by dependency; target dates await confirmation of the course deadline.

| Phase / milestone | Deliverable | Verified or reported status | Date / target |
| --- | --- | --- | --- |
| 1. Requirements analysis | `requirements.md` and approved MVP baseline | Complete; commit `5ad45d2` | Drafted Nov 14, approved Nov 15, 2026 |
| 2. Architecture design | Modular design, model selection, response contract | Complete; architecture commit `c84eb05` | Nov 15, 2026 |
| 3.1 Response schemas | Pydantic analysis result models | Complete; commit `701c109` | Nov 15, 2026 |
| 3.2 Input validation | Required fields and boundary checks | Complete; commit `d0f02b9` | Nov 15, 2026 |
| 3.3 Analysis integration | Prompt, evidence checks, Responses API, safe errors, live smoke test | Complete; commits `097eb9a` through `fe17881` | Nov 15, 2026 |
| 3.4 User interface | Streamlit form and analysis display | Complete; commits `a444bab` and `aa15944` | Nov 15, 2026 |
| 3.5 User experience | Copyable output, mobile readability, manual checks | Checks reported complete | Nov 15, 2026 |
| 4.1 Quality evaluation | Ten fictional initial attempts, scored and reviewed | Complete; nine passes, EV-09 failure documented | Nov 15, 2026 |
| 4.2 Refinement | Prompt adjustment, two new tests, three regression attempts | Complete; commit `51862b0`; 56 automated tests passed | Nov 15, 2026 |
| 4.3 Documentation | README, planning document, AI Usage Log, architecture and evaluation documentation | Complete; commit `cb37f90` | Nov 15, 2026 |
| 4.4 Demonstration materials | Three application screenshots and README image references | Complete; commit `2f432eb` | Nov 15, 2026 |
| 4.5 Restricted deployment | Streamlit hosting, access restrictions, API secrets, spending controls, hosted integration test | Restricted deployment verified; unrestricted public access not approved | Nov 15, 2026 |
| 6. Final submission and portfolio | Final documentation review, course demonstration, submission packaging, portfolio integration | Pending | Date TBD |


**Schedule dependency:** Final submission dates and any required presentation date must be taken from the instructor's course schedule. Do not infer a due date from the preparation date of this document.

## 9. Quality assurance and acceptance

### Automated verification

The latest student-provided pytest output reported **56 tests passed, 0 failed, in 3.30 seconds** on Windows with Python 3.14.5. Tests cover schema invariants, input limits, request construction, source-evidence verification, API failure handling, and Streamlit behavior. These results reflect the reported local run and are not a substitute for a final submission-day rerun.

### Live integration and user experience

A live model smoke test and an end-to-end Streamlit analysis were completed. The student also reported successful checks for complete text copying into Notepad, presence of all five skill fields, usability at mobile width, and behavior after subsequent submissions. A restricted Streamlit Community Cloud deployment was verified
on November 15, 2026. The hosted application loaded successfully,
displayed the expected missing-API-key message, and subsequently
completed one live AI analysis after secure API configuration.
Unrestricted public access has not been enabled.

### Manual content evaluation

Ten fictional scenarios were evaluated using an approved four-part per-skill rubric: **source grounding**, **target-career relevance**, **explanation quality**, and **limitations**, each scored 0 to 2. Passing skills require grounding 2 and each other dimension at least 1, with no identified critical fabrication or prompt-injection failure.

The ten original attempts yielded **nine approved passes and one approved failure (EV-09)**. EV-09 incorrectly produced a generic skill from insufficient evidence. After revising the relevance instructions, **EV-09 Attempt 02**, **EV-01 Attempt 02**, and **EV-10 Attempt 02** each passed and were approved by the student. Original failures remain preserved. These 13 observed outputs do not establish population-level accuracy or generalized prompt-injection resistance. Detailed results are in `docs/EVALUATION_RESULTS.md`.

### Final acceptance checks

| Check | Verified or reported status |
| --- | --- |
| Functional Streamlit form, validation, and live analysis | Verified locally and through a hosted integration test |
| Structured output, source-excerpt validation, and safe API errors | Automated tests passed; live testing performed |
| Copyable results and mobile-width readability | Manual checks reported passed |
| Ten required fictional evaluation cases and follow-up regression testing | Completed and documented |
| Local automated test suite | 56 passed in latest reported run |
| Approved documentation and complete AI Usage Log | Committed in `cb37f90` |
| Screenshots or demonstration materials | Three screenshots committed in `2f432eb` |
| Restricted hosting and hosted smoke test | Verified; $5 API hard spending limit configured |
| Unrestricted public access | Not approved or enabled |
| Course-specific due date and presentation arrangements | Not established in reviewed materials |

## 10. Key risks and mitigation strategy

| Risk | Consequence | Mitigation and current limitation |
| --- | --- | --- |
| Unsupported AI-generated qualifications | Misleading career guidance | Ground skills in supplied excerpts, require limitations, conduct scenario-based manual review; semantic accuracy still cannot be guaranteed. |
| Vague experience descriptions | Generic or irrelevant results | Use a meaningful relevance threshold and `insufficient_information`; EV-09 was corrected in a targeted regression test. |
| Prompt-injection text in user input | Model may follow untrusted instructions | Pass input separately as data and instruct model to ignore embedded commands; EV-10 passed two observed attempts, not a universal guarantee. |
| API downtime, quota, timeout, or cost | Failed or delayed analysis and unexpected spending | Use a 45-second timeout, mapped errors, bounded inputs/output, disabled SDK automatic retries, and account-side cost monitoring. |
| Public abuse of a billable endpoint | Unexpected API charges | Restricted Streamlit viewer access and an enforced $5 API project spending limit are configured. Unrestricted public access remains disabled until additional protections are evaluated. |
| Sensitive user or employer information | Confidential information sent to a third party | Provide an explicit notice, avoid app-controlled history, keep credentials outside Git, and discourage confidential submissions. |
| Documentation drift | Inconsistent submission evidence | Reconcile requirements, architecture, README, evaluation records, AI log, and actual code before final commit. |
| Deadline uncertainty | Incomplete deliverables | Confirm instructor deadline and prioritize mandatory artifacts and demonstration evidence. |

## 11. Required deliverables and submission checklist

The project brief summarized in the student-approved requirements and AI Usage Log calls for the following:

| Deliverable | Current status / evidence |
| --- | --- |
| Project Planning Document | Version 0.1 approved and committed in `cb37f90`; version 0.2 updates deployment status |
| `requirements.md` | Approved requirements baseline committed |
| `README.md` | Committed with features, installation, usage, screenshots, technologies, and future enhancements |
| AI Usage Log | 32 documented AI interactions committed in `cb37f90` |
| Complete working application source | Implemented, tested, and committed |
| Automated and manual testing evidence | 56 automated tests passed; ten initial evaluations and three regression attempts documented |
| Git history | 15 meaningful commits through `2f432eb` |
| Screenshots and demonstration materials | Three application screenshots committed in `2f432eb` |
| Hosted application | Restricted Streamlit deployment verified, including one successful live AI analysis |
| Public portfolio integration | Pending |
| Final course demonstration and submission | Pending |

The 15–25 commit range is a recommendation in the reviewed assignment summary, not a reason to create artificial commits. New commits should correspond to meaningful remaining work.

## 12. Remaining actions and decision gates


1. **Documentation consistency:** Finalize the deployment-status updates
   in `README.md`, `docs/PROJECT_PLANNING_DOCUMENT.md`, and
   `docs/ARCHITECTURE.md`.

2. **Requirements reconciliation:** Preserve the approved requirements
   baseline. Any substantive requirements changes must be reviewed
   separately.

3. **Final verification:** Rerun automated tests, inspect staged
   changes, and verify that no API credentials or confidential
   information are included in the repository.

4. **Deployment security:** Maintain restricted Streamlit access and
   the configured API spending limit. Reassess authentication,
   rate limiting, and abuse prevention before enabling unrestricted
   public access.

5. **Course demonstration:** Prepare a short demonstration using
   fictional experience descriptions, including a successful analysis
   and an insufficient-information response.

6. **Submission requirements:** Confirm the instructor's deadline,
   required submission format, and presentation arrangements.

7. **Portfolio integration:** Add the project to the GitHub Pages
   portfolio when appropriate. Clearly indicate if live application
   access remains restricted.


## 13. Project governance and AI assistance

The student owns project decisions, reviews AI suggestions, runs or verifies tests, and approves evaluation scoring. AI assistance has supported requirements drafting, architecture, code implementation, troubleshooting, test development, and documentation. The chronological `docs/AI_usage_log.md` records original prompts or faithful summaries, AI output, student choices, observed implementation results, and commit links. The Git repository remains the authoritative record of committed source and documentation.

**Change management:** New MVP features and alterations to previously approved requirements require an explicit decision. Failures and unsuccessful model attempts must remain visible in the testing record, including the original EV-09 failure.

## 14. References and revision history

**Internal project references:** `requirements.md`, `docs/ARCHITECTURE.md`, `docs/EVALUATION_PLAN.md`, `docs/EVALUATION_RESULTS.md`, `evaluation/scenarios.json`, `docs/AI_usage_log.md`, and implemented source/test files.

**Course source:** *AI-Assisted Software Development Project*, COSC 4272 assignment as described in the project requirements and original student prompt. Exact deadline and submission format remain unverified in the materials reviewed here.

| Version | Date | Description | Status |
| --- | --- | --- | --- |
| 0.1 | 2026-11-15 | Initial consolidated planning document reflecting approved baseline and verified progress | Student-approved baseline |
| 0.2 | 2026-11-15 | Recorded completed documentation, screenshots, restricted Streamlit deployment, and hosted verification | Student-approved deployment update |
