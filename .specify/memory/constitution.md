<!--
---
Sync Impact Report
---
- **Version change**: 0.0.0 → 1.0.0
- **Summary**: Initial creation of the project constitution based on user-provided principles.
- **Modified Principles**:
  - N/A (Initial creation)
- **Added Sections**:
  - Principle I: Backend-Only Focus
  - Principle II: No-Testing Policy
  - Principle III: Manual Git & Database Operations
  - Principle IV: No Mock Data or Placeholders
  - Principle V: Minimalist Dependency Policy
  - Principle VI: Simplicity and Readability
  - Principle VII: Strict Architectural Separation
  - Principle VIII: Clear and Simple Comments
  - Principle IX: Secure Coding Practices
  - Principle X: No Generation of Secrets
  - Principle XI: Consistent Naming Conventions
  - Principle XII: Avoid Premature Optimization
  - Principle XIII: Code-Only Output
  - Principle XIV: Developer-Led Decisions
- **Removed Sections**:
  - All generic template placeholders.
- **Templates Requiring Updates**:
  - ✅ `.specify/templates/plan-template.md`
  - ✅ `.specify/templates/spec-template.md`
  - ✅ `.specify/templates/tasks-template.md`
  - ✅ `.gemini/commands/speckit.constitution.toml` (self-update)
- **Follow-up TODOs**:
  - None
-->
# BarberShop-AIBot Constitution

## Core Principles

### I. Backend-Only Focus
All code must be clean, maintainable, and scalable, designed exclusively for backend services. The agent must not generate any frontend code (HTML, CSS, client-side JavaScript).

### II. No-Testing Policy
A strict no-testing policy is enforced. The agent MUST NOT generate any unit tests, integration tests, or any form of automated testing scripts. The developer assumes full responsibility for all testing.

### III. Manual Git & Database Operations
The agent's interaction with the version control system and database is strictly limited.
- **Git**: The agent MUST NOT perform any Git operations (commit, push, merge, etc.). The developer handles all version control actions manually. Agent can only create new branches.
- **Database**: The agent MUST NOT generate or execute database migrations (e.g., using an ORM's migration tool). The developer is solely responsible for all database schema changes and data migrations.

### IV. No Mock Data or Placeholders
The agent MUST NOT invent, generate, or use any mock data, dummy values, or placeholders for any feature or data structure. If data is required to proceed, the agent MUST stop and ask the developer to provide the necessary details.

### V. Minimalist Dependency Policy
The agent must adhere to a minimal-dependency approach. External libraries or third-party packages should only be introduced when they are strictly necessary to meet a core requirement and there is no simple, native solution.

### VI. Simplicity and Readability
The agent's code generation must prioritize simplicity, predictability, and explicitness.
- Prefer simple, linear control flows over complex, "smart," or dynamic patterns.
- Favor explicit, highly readable logic over clever, one-line, or implicit abstractions.

### VII. Strict Architectural Separation
The agent must maintain a strict separation of concerns and adhere to SOLID principles. Code should be organized into logical layers (e.g., models, services, controllers, repositories, utilities) as established in the existing project structure.

### VIII. Clear and Simple Comments
The agent must add comments to the code sparingly. Comments should be simple, written in clear English, and used only to explain the "why" behind complex or non-obvious logic, making it easier for the developer to understand.

### IX. Secure Coding Practices
The agent must enforce secure coding practices at all times. This includes, but is not limited to, validating and sanitizing all external inputs, preventing the leakage of sensitive data in logs or exceptions, and handling data securely.

### X. No Generation of Secrets
The agent MUST NEVER generate, invent, or hardcode any credentials, API keys, tokens, or other secrets. It must always ask the developer to provide these values.

### XI. Consistent Naming Conventions
The agent must follow consistent and predictable naming conventions for all variables, functions, classes, and files, adhering to the style of the existing codebase.

### XII. Avoid Premature Optimization
The agent should write clear and correct code first. Optimization should only be performed when explicitly required by the project's performance criteria. Avoid introducing complexity for unproven performance gains.

### XIII. Code-Only Output
The agent's primary output should be code. Explanations, summaries, or conversational text are to be avoided unless explicitly requested by the developer.

### XIV. Developer-Led Decisions
When faced with multiple valid or equally viable implementation approaches, the agent must stop and ask the developer for a decision rather than making an assumption.

## Governance

This Constitution is the highest-level guidance document and supersedes all other practices or conventions. All generated code and agent actions must comply with these principles. Amendments to this document must be approved by the developer and will trigger a review of all dependent templates and processes.

**Version**: 1.0.0 | **Ratified**: 2025-11-21 | **Last Amended**: 2025-11-21