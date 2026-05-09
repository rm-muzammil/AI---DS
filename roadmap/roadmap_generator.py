from openpyxl import Workbook
from openpyxl.styles import (Font, PatternFill, Alignment, Border, Side,
                              GradientFill)
from openpyxl.utils import get_column_letter
from datetime import date, timedelta

wb = Workbook()

# ── Palette ──────────────────────────────────────────────────────────────────
C = {
    "purple_h":  "7F77DD", "purple_l":  "EEEDFE",
    "teal_h":    "1D9E75", "teal_l":    "E1F5EE",
    "amber_h":   "BA7517", "amber_l":   "FAEEDA",
    "coral_h":   "D85A30", "coral_l":   "FAECE7",
    "blue_h":    "378ADD", "blue_l":    "E6F1FB",
    "gray_h":    "888780", "gray_l":    "F1EFE8",
    "green_h":   "639922", "green_l":   "EAF3DE",
    "white":     "FFFFFF", "black":     "000000",
    "header_bg": "2C2C2A", "header_fg": "FFFFFF",
    "mern_h":    "D4537E", "mern_l":    "FBEAF0",
    "german_h":  "0F6E56", "german_l":  "E1F5EE",
}

def fill(hex_): return PatternFill("solid", fgColor=hex_)
def font(bold=False, color="000000", sz=10, italic=False):
    return Font(bold=bold, color=color, size=sz, italic=italic, name="Arial")
def align(h="left", v="center", wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)
def thin_border():
    s = Side(style="thin", color="D3D1C7")
    return Border(left=s, right=s, top=s, bottom=s)

def hdr_cell(ws, row, col, val, bg=None, fg="FFFFFF", sz=10, bold=True,
             h="center"):
    c = ws.cell(row=row, column=col, value=val)
    c.font = font(bold=bold, color=fg, sz=sz)
    if bg: c.fill = fill(bg)
    c.alignment = align(h=h)
    c.border = thin_border()
    return c

def data_cell(ws, row, col, val, bg="FFFFFF", fg="000000", sz=9,
              bold=False, h="left", italic=False):
    c = ws.cell(row=row, column=col, value=val)
    c.font = Font(bold=bold, color=fg, size=sz, italic=italic, name="Arial")
    c.fill = fill(bg)
    c.alignment = align(h=h, wrap=True)
    c.border = thin_border()
    return c

# ══════════════════════════════════════════════════════════════════════════════
# Sheet 1 — MASTER ROADMAP (week-by-week)
# ══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "Master Roadmap"
ws1.sheet_view.showGridLines = False
ws1.freeze_panes = "A3"

# Column widths
col_widths = [6, 12, 10, 28, 28, 24, 24, 22, 22, 22, 18, 18]
col_headers = [
    "Wk #", "Week Start", "Phase", "AI / ML Focus",
    "Cloud + DevOps", "Backend Engineering", "Data Engineering",
    "Portfolio Project", "MERN / Finance Work", "German Language",
    "Tools & Apps", "Sunday Review Goal"
]
for i, (w, h) in enumerate(zip(col_widths, col_headers), 1):
    ws1.column_dimensions[get_column_letter(i)].width = w
    hdr_cell(ws1, 2, i, h, bg=C["header_bg"], sz=9)

# Title row
ws1.merge_cells("A1:L1")
t = ws1.cell(row=1, column=1,
             value="🗺  2-Year German Tech Roadmap  |  10 May 2026 → 10 May 2028  |  Top 0.1% Path")
t.font = Font(bold=True, color="FFFFFF", size=13, name="Arial")
t.fill = fill(C["purple_h"])
t.alignment = align(h="center")
ws1.row_dimensions[1].height = 28
ws1.row_dimensions[2].height = 30

# ── Phase definitions ─────────────────────────────────────────────────────────
PHASES = {
    # (week_start_index, week_end_index): (label, color_bg, color_fg)
    (1,  8):   ("Phase 0 — Uni + Foundation", C["gray_l"],   C["gray_h"]),
    (9, 16):   ("Phase 1 — Python & ML Core", C["purple_l"], C["purple_h"]),
    (17, 25):  ("Phase 2 — Cloud Basics",     C["blue_l"],   C["blue_h"]),
    (26, 35):  ("Phase 3 — First Projects",   C["amber_l"],  C["amber_h"]),
    (36, 46):  ("Phase 4 — ML Depth",         C["purple_l"], C["purple_h"]),
    (47, 57):  ("Phase 5 — Data Engineering", C["coral_l"],  C["coral_h"]),
    (58, 70):  ("Phase 6 — Backend Mastery",  C["teal_l"],   C["teal_h"]),
    (71, 82):  ("Phase 7 — Senior Projects",  C["amber_l"],  C["amber_h"]),
    (83, 96):  ("Phase 8 — Specialise",       C["purple_l"], C["purple_h"]),
    (97, 104): ("Phase 9 — Job Hunt",         C["green_l"],  C["green_h"]),
}

def get_phase(wk):
    for (s, e), v in PHASES.items():
        if s <= wk <= e:
            return v
    return ("", C["white"], C["black"])

# ── Week data ─────────────────────────────────────────────────────────────────
START = date(2026, 5, 10)
UNI_END = date(2026, 7, 1)   # 4th sem + Arabic ends
TOTAL = 104

rows = []

for wk in range(1, TOTAL + 1):
    wd = START + timedelta(weeks=wk - 1)
    phase_label, ph_bg, ph_fg = get_phase(wk)
    uni_active = wd < UNI_END

    # ── AI/ML ────────────────────────────────────────────────────────────────
    ml_map = {
        1: "Python refresher: numpy, pandas, matplotlib (3 h/d)",
        2: "Python OOP, virtual envs, Git workflow",
        3: "Math refresh: linear algebra (3Blue1Brown)",
        4: "Math: probability & statistics for ML",
        5: "Intro to ML: sklearn pipelines, train/test split",
        6: "Supervised learning: regression & classification",
        7: "Model evaluation: cross-val, confusion matrix, ROC",
        8: "Unsupervised: k-means, PCA — Anki deck started",
        9: "PyTorch tensors & autograd",
        10: "Neural nets: forward + backward pass from scratch",
        11: "Training loops, optimizers, learning rate schedulers",
        12: "CNNs: conv layers, pooling, batch norm",
        13: "Transfer learning: fine-tune ResNet on custom data",
        14: "RNNs & LSTMs: sequence modelling",
        15: "Transformers: attention mechanism deep dive",
        16: "HuggingFace Transformers: load, tokenize, infer",
        17: "HuggingFace datasets + trainer API",
        18: "Fine-tuning BERT for text classification",
        19: "LoRA / QLoRA: parameter-efficient fine-tuning",
        20: "RAG architecture: embeddings + vector DBs",
        21: "LangChain: chains, agents, memory",
        22: "Build RAG chatbot on German docs (Project 1 start)",
        23: "MLflow: experiment tracking, model registry",
        24: "GDPR-compliant ML data handling",
        25: "Model serving: FastAPI + Docker",
        26: "Time-series fundamentals (for Project 2)",
        27: "Anomaly detection: isolation forest, autoencoders",
        28: "Sensor data preprocessing pipeline",
        29: "Predictive maintenance model training (Project 2)",
        30: "Model evaluation & deployment (Project 2 done)",
        31: "Revisit: LLM architectures (GPT, T5, Mistral)",
        32: "Prompt engineering & system prompts",
        33: "Open-source LLM: Mistral local inference",
        34: "Fine-tune Mistral on German domain (Project 4 start)",
        35: "LoRA training run + evaluation metrics",
        36: "Publish fine-tuned model to HuggingFace Hub",
        37: "MLOps: CI/CD for ML models",
        38: "Monitoring: data drift, concept drift",
        39: "A/B testing for ML models",
        40: "Feature stores: Feast basics",
        41: "Advanced RAG: re-ranking, hybrid search",
        42: "Multi-modal: CLIP, image+text pipelines",
        43: "Reinforcement learning fundamentals",
        44: "RL from human feedback (RLHF) concepts",
        45: "Capstone: end-to-end MLOps pipeline",
        46: "Review all ML concepts — update Anki deck",
        47: "Spark: RDDs, DataFrames, SparkSQL",
        48: "Spark ML: scalable training",
        49: "Stream processing: Kafka + Spark Streaming",
        50: "Real-time ML inference on streams",
        51: "Feature engineering at scale",
        52: "ML for tabular data: XGBoost, LightGBM",
        53: "Hyperparameter tuning: Optuna",
        54: "Interpretability: SHAP, LIME",
        55: "Fairness & bias in ML",
        56: "ML system design patterns",
        57: "Review + update portfolio ML projects",
        58: "Bayesian ML basics",
        59: "Graph neural networks intro",
        60: "Advanced NLP: NER, relation extraction",
        61: "LLM agents: tool use, ReAct pattern",
        62: "Multi-agent systems",
        63: "LLM evaluation: benchmarks, human eval",
        64: "Production LLM: latency, cost optimisation",
        65: "ML platform design (Uber Michelangelo style)",
        66: "Read: Designing ML Systems (Chip Huyen) ch 1–4",
        67: "Read: Designing ML Systems ch 5–8",
        68: "Read: Designing ML Systems ch 9–12",
        69: "Mock ML system design interview",
        70: "Mock ML system design interview #2",
        71: "Advanced fine-tuning: DPO, PPO",
        72: "LLM security: prompt injection, jailbreaks",
        73: "Multimodal LLMs: GPT-4V style architectures",
        74: "Diffusion models: DDPM, Stable Diffusion",
        75: "AI agents: LangGraph, AutoGen",
        76: "German-language NLP models: deepset/gbert",
        77: "Build: German-language AI product (unique portfolio)",
        78: "Submit to German AI conference / blog post",
        79: "Revisit: all 6 projects — update READMEs",
        80: "ML technical blog: write 2 articles",
        81: "Open source: submit PR to HuggingFace / LangChain",
        82: "Mock interviews: ML coding (Leetcode + ML)",
        83: "System design: ML infra at BMW / Bosch scale",
        84: "Advanced: retrieval-augmented generation v2",
        85: "Advanced: Constitutional AI concepts",
        86: "Study: recent ML papers (Arxiv weekly)",
        87: "Study: recent ML papers #2",
        88: "Build new mini-project from paper",
        89: "Technical writing: ADR for ML system",
        90: "Portfolio review: update all projects + GitHub",
        91: "Mock ML interviews × 3 this week",
        92: "Mock system design × 3 this week",
        93: "Prepare HuggingFace profile + model cards",
        94: "Final portfolio polish",
        95: "Apply to German ML roles (10 applications)",
        96: "Apply + follow up",
        97: "Interview prep: coding (daily Leetcode)",
        98: "Interview prep: ML concepts flashcards",
        99: "Interview prep: system design",
        100: "Interview prep: behavioural (German culture)",
        101: "Final interviews",
        102: "Final interviews",
        103: "Negotiate offer / Visa prep",
        104: "START — Top 0.1% achieved",
    }

    cloud_map = {
        1: "Set up: Linux (WSL2), Git, VS Code, SSH keys",
        2: "Bash scripting fundamentals",
        3: "Docker: images, containers, volumes",
        4: "Docker Compose: multi-service apps",
        5: "AWS free tier setup: EC2, S3, IAM basics",
        6: "AWS VPC, security groups, Route53",
        7: "AWS RDS + managed services overview",
        8: "AWS CLI + SDK (boto3) scripting",
        9: "Terraform basics: providers, resources, state",
        10: "Terraform: modules, variables, outputs",
        11: "Terraform: deploy EC2 + S3 + RDS stack",
        12: "GitHub Actions CI/CD: build → test → deploy",
        13: "Kubernetes: pods, deployments, services (Minikube)",
        14: "Kubernetes: ConfigMaps, Secrets, Ingress",
        15: "Helm charts: package K8s apps",
        16: "AWS EKS: managed Kubernetes",
        17: "AWS EKS + Terraform (Project 3 infra)",
        18: "Observability: Prometheus + Grafana",
        19: "Logging: ELK stack basics",
        20: "Datadog: APM, dashboards, alerts",
        21: "GDPR-compliant architecture on AWS (data residency)",
        22: "AWS Frankfurt region + Hetzner: German data sovereignty",
        23: "Cost optimisation: spot instances, reserved",
        24: "Security: IAM policies, least privilege, AWS GuardDuty",
        25: "AWS Solutions Architect study — begin",
        26: "SAA-C03: VPC deep dive",
        27: "SAA-C03: compute (EC2, Lambda, ECS)",
        28: "SAA-C03: storage (S3, EFS, FSx)",
        29: "SAA-C03: databases",
        30: "SAA-C03: practice exam 1",
        31: "SAA-C03: practice exam 2 + review weak areas",
        32: "AWS SAA Exam (schedule this week)",
        33: "Azure: AZ-900 fundamentals (German corps use Azure)",
        34: "Azure: AKS, Azure ML, DevOps pipelines",
        35: "Azure: AZ-104 study start",
        36: "AZ-104: identity & governance",
        37: "AZ-104: storage + compute",
        38: "AZ-104: networking",
        39: "AZ-104: monitoring + practice exam",
        40: "Azure AZ-104 Exam",
        41: "CKA prep: K8s cluster setup from scratch",
        42: "CKA prep: workloads & scheduling",
        43: "CKA prep: networking (CNI, DNS)",
        44: "CKA prep: storage (PV, PVC)",
        45: "CKA prep: troubleshooting + practice exam",
        46: "CKA Exam",
        47: "Service mesh: Istio basics",
        48: "GitOps: ArgoCD",
        49: "Secrets management: Vault",
        50: "SRE principles: SLI, SLO, error budgets",
        51: "Chaos engineering: Chaos Monkey concepts",
        52: "Multi-cloud strategy patterns",
        53: "FinOps: cloud cost governance",
        54: "Platform engineering: Internal Dev Portals",
        55: "Infrastructure as Product mindset",
        56: "Cloud-native security: SAST, DAST, SBOM",
        57: "ISO 27001 + BSI IT-Grundschutz overview",
        58: "GDPR technical controls deep dive",
        59: "Zero-trust architecture",
        60: "Cloud resume challenge (public portfolio)",
        61: "AWS Advanced Networking study",
        62: "AWS DevOps Professional study",
        63: "AWS DevOps Pro practice exam",
        64: "AWS DevOps Pro Exam (schedule)",
        65: "Review all cloud certs achieved",
        66: "Design: GDPR-first multi-tenant SaaS (cloud arch doc)",
        67: "Build: cloud architecture diagram for portfolio",
        68: "Write ADR: cloud platform decision",
        69: "Mock cloud architect interview",
        70: "Mock cloud + system design interview",
        71: "Advanced K8s: operators, CRDs",
        72: "Advanced K8s: multi-cluster federation",
        73: "eBPF: observability at kernel level",
        74: "WebAssembly on the edge",
        75: "Serverless: AWS Lambda patterns",
        76: "Event-driven architecture on AWS",
        77: "AWS Well-Architected review of all projects",
        78: "Contribute to Terraform registry module",
        79: "Blog: GDPR-compliant AWS architecture",
        80: "Blog: Kubernetes cost optimisation",
        81: "Cloud portfolio: all projects on Hetzner + AWS",
        82: "Mock cloud interviews × 3",
        83: "Advanced: eBPF for ML workload observability",
        84: "Advanced: Kubernetes for ML (Kubeflow)",
        85: "Kubeflow pipelines for ML training",
        86: "Cloud-native ML deployment patterns",
        87: "Review: all cloud projects + update READMEs",
        88: "Prepare cloud architecture diagrams for interviews",
        89: "Review certs + renew if needed",
        90: "Final infra polish",
        91: "Target: German DevOps/Cloud roles applied",
        92: "Cloud interview prep: scenario questions",
        93: "Cloud interview prep: cost + GDPR scenarios",
        94: "Cloud final review",
        95: "Apply cloud roles — 10 applications",
        96: "Follow-up + LinkedIn outreach German engineers",
        97: "Interview: cloud architecture deep dive",
        98: "Interview: K8s troubleshooting",
        99: "Interview: GDPR technical controls",
        100: "Interview: cost optimisation scenarios",
        101: "Final cloud interviews",
        102: "Offer evaluation",
        103: "Offer negotiation",
        104: "HIRED",
    }

    backend_map = {
        1: "—  (uni phase: focus on Python basics)",
        2: "—  (uni phase)",
        3: "FastAPI: routing, Pydantic models",
        4: "FastAPI: auth (JWT), middleware, background tasks",
        5: "PostgreSQL: schema design, indexes, transactions",
        6: "Redis: caching, pub/sub, sessions",
        7: "REST API best practices + OpenAPI docs",
        8: "Testing: pytest, test coverage",
        9: "Java basics (German enterprise requirement)",
        10: "Java OOP: classes, interfaces, generics",
        11: "Spring Boot: controllers, services, repositories",
        12: "Spring Boot: JPA + Hibernate",
        13: "Spring Security: OAuth2, JWT",
        14: "Spring Boot testing: JUnit 5, Mockito",
        15: "Microservices patterns: API Gateway, service discovery",
        16: "Message queues: Kafka producer/consumer",
        17: "Kafka: topics, partitions, consumer groups",
        18: "gRPC: protocol buffers, streaming",
        19: "GraphQL with Spring Boot",
        20: "Database migrations: Flyway / Liquibase",
        21: "API versioning strategies",
        22: "Rate limiting + circuit breakers",
        23: "Distributed tracing: OpenTelemetry",
        24: "Performance: JVM tuning, profiling",
        25: "System design: scalable REST APIs",
        26: "Build: backend for Project 1 (RAG chatbot API)",
        27: "Build: auth service with GDPR consent management",
        28: "Build: event-driven order service (Kafka)",
        29: "Build: multi-tenant data isolation layer",
        30: "Code review + refactor all backend code",
        31: "Kotlin basics (preferred for new Java projects)",
        32: "Kotlin coroutines + Flow",
        33: "Ktor: Kotlin web framework",
        34: "Go basics (Berlin startup ecosystem)",
        35: "Go: goroutines, channels, REST API",
        36: "System design: DDIA chapters 1–4",
        37: "System design: DDIA chapters 5–7 (replication)",
        38: "System design: DDIA chapters 8–9 (distributed)",
        39: "System design: DDIA chapters 10–12 (derived data)",
        40: "Mock system design: design Twitter",
        41: "Mock system design: design YouTube",
        42: "Mock system design: design Booking.com (German)",
        43: "Leetcode: arrays & strings (30 mins/day)",
        44: "Leetcode: trees & graphs",
        45: "Leetcode: dynamic programming",
        46: "Leetcode: hard problems × 5",
        47: "SAP integration: RFC, BAPIs, IDoc basics",
        48: "SAP REST APIs: oData services",
        49: "Legacy modernisation patterns",
        50: "Event sourcing + CQRS pattern",
        51: "Domain-driven design (DDD) basics",
        52: "Hexagonal architecture",
        53: "Clean code + SOLID principles deep dive",
        54: "Code quality: SonarQube, static analysis",
        55: "Tech debt management strategies",
        56: "API security: OWASP Top 10",
        57: "Build: SAP integration connector (Project 5)",
        58: "Build: real-time data pipeline API",
        59: "Build: multi-tenant SaaS backend (Project 3)",
        60: "API gateway + rate limiting implementation",
        61: "Backend + ML integration: serving predictions",
        62: "Backend for RAG: document ingestion API",
        63: "Backend: async job processing system",
        64: "Backend: webhooks + event streaming",
        65: "Backend: GDPR right-to-erasure endpoint",
        66: "Code review: all 6 projects backend",
        67: "Write RFC: backend architecture decisions",
        68: "Write ADR: database selection",
        69: "Mock coding interview: Java/Python",
        70: "Mock system design × 2",
        71: "Advanced: reactive programming (WebFlux)",
        72: "Advanced: database internals (B-trees, WAL)",
        73: "Advanced: distributed consensus (Raft)",
        74: "Advanced: CRDTs for conflict resolution",
        75: "Performance engineering: load testing (k6)",
        76: "Backend scaling: horizontal vs vertical",
        77: "API design: OpenAPI 3.1 spec-first",
        78: "Technical blog: Java vs Kotlin in German enterprise",
        79: "Open source: contribute to Spring ecosystem",
        80: "Backend portfolio: all projects documented",
        81: "Mock: senior backend interview",
        82: "Mock: system design at Bosch scale",
        83: "Advanced system design: ML serving infrastructure",
        84: "Advanced: event mesh architecture",
        85: "Advanced: polyglot persistence patterns",
        86: "Revisit all projects: add observability",
        87: "Revisit all projects: add integration tests",
        88: "Final code quality pass",
        89: "Prepare code samples for interviews",
        90: "Portfolio: GitHub pinned repos + READMEs",
        91: "Apply backend roles: 10 applications",
        92: "Interview prep: Java Spring deep dive",
        93: "Interview prep: system design scenarios",
        94: "Interview: live coding practice",
        95: "Applications + follow-up",
        96: "Technical interviews",
        97: "Technical interviews",
        98: "Technical interviews",
        99: "Offer evaluation",
        100: "Offer negotiation",
        101: "Paperwork + visa",
        102: "Relocation prep",
        103: "Notice period start",
        104: "START at German company",
    }

    data_map = {
        1: "—",
        2: "SQL refresher: joins, window functions, CTEs",
        3: "Advanced SQL: recursive CTEs, lateral joins",
        4: "Data modeling: star schema, snowflake",
        5: "dbt: models, tests, documentation",
        6: "dbt: sources, seeds, snapshots",
        7: "Airflow: DAGs, operators, sensors",
        8: "Airflow: XComs, templating, best practices",
        9: "Snowflake: architecture, virtual warehouses",
        10: "Snowflake: data sharing, time travel",
        11: "Build: EV charging data pipeline (Project 5)",
        12: "EV pipeline: dbt transformations",
        13: "EV pipeline: Airflow scheduling",
        14: "EV pipeline: Grafana dashboard",
        15: "EV pipeline: deploy on Hetzner + document",
        16: "Apache Kafka: streaming fundamentals",
        17: "Kafka: schema registry, Avro",
        18: "Apache Spark: DataFrames, SparkSQL",
        19: "Spark: performance tuning, caching",
        20: "Spark: streaming with Kafka",
        21: "Delta Lake: ACID transactions on data lake",
        22: "Apache Iceberg: table format",
        23: "Data lakehouse architecture",
        24: "SAP data extraction: Python pyRFC",
        25: "SAP → Snowflake pipeline",
        26: "Great Expectations: data quality testing",
        27: "Data contracts: schema enforcement",
        28: "Data lineage: OpenLineage",
        29: "Data governance: GDPR in data platform",
        30: "Build: GDPR-compliant data platform (Project 6 start)",
        31: "Data platform: ingestion layer",
        32: "Data platform: transformation layer (dbt)",
        33: "Data platform: serving layer + BI",
        34: "Data platform: data quality checks",
        35: "Data platform: documentation + deploy",
        36: "Azure Data Factory: pipelines",
        37: "Azure Synapse Analytics",
        38: "Azure Data Engineer cert (DP-203) study",
        39: "DP-203: data storage",
        40: "DP-203: data processing",
        41: "DP-203: data security + practice exam",
        42: "DP-203 Exam",
        43: "Databricks: unified analytics",
        44: "Databricks: MLflow integration",
        45: "Databricks: Delta Live Tables",
        46: "dbt advanced: macros, packages, exposures",
        47: "Data mesh principles",
        48: "Data product thinking",
        49: "Reverse ETL: census, hightouch",
        50: "Real-time analytics: ClickHouse",
        51: "Feature engineering for ML pipelines",
        52: "Feature store: Feast implementation",
        53: "ML feature pipelines with Spark",
        54: "Data infrastructure cost optimisation",
        55: "Data platform reliability: SLOs",
        56: "Data team collaboration: DataHub catalog",
        57: "Review all data projects + update docs",
        58: "Advanced Spark: custom UDFs",
        59: "Streaming ML: online learning",
        60: "Build: real-time ML feature pipeline",
        61: "Data engineering for LLMs: pre-training data",
        62: "Data engineering for RAG: vector pipeline",
        63: "Advanced dbt: unit tests",
        64: "Benchmark: Spark vs Flink",
        65: "Data engineering blog post",
        66: "Mock data engineering interview",
        67: "Mock: design a data platform for Bosch",
        68: "Mock: streaming pipeline design",
        69: "Data portfolio: all projects documented",
        70: "Open source: contribute to dbt-core or Airflow",
        71: "Advanced: distributed query engines",
        72: "Advanced: data compression & encoding",
        73: "Advanced: storage systems internals",
        74: "Advanced: column-oriented databases",
        75: "Performance: 1B row challenge",
        76: "Data architecture: medallion architecture",
        77: "Data architecture: Kappa vs Lambda",
        78: "Write: data architecture decision blog",
        79: "Data portfolio final polish",
        80: "GitHub: all data projects pinned",
        81: "Apply data engineering roles: 5 applications",
        82: "Data interviews × 2",
        83: "Advanced data + ML intersection",
        84: "Final data project updates",
        85: "Data engineering mock interview",
        86: "Review DP-203 + Azure certs",
        87: "Prepare data architecture diagrams",
        88: "Data engineering final prep",
        89: "Applications: 10 data roles",
        90: "Technical interviews",
        91: "Technical interviews",
        92: "Data system design interview",
        93: "Offer comparison",
        94: "Offer negotiation",
        95: "Final prep",
        96: "Final prep",
        97: "Final prep",
        98: "Final prep",
        99: "Offer accepted",
        100: "Notice period",
        101: "Relocation prep",
        102: "Relocation prep",
        103: "Final week",
        104: "START",
    }

    project_map = {
        1:  "—  (setup dev environment, GitHub profile)",
        2:  "—  (Python portfolio starter repo)",
        3:  "P1 planning: GDPR-RAG chatbot — write spec",
        4:  "P1: set up FastAPI backend skeleton",
        5:  "P1: document ingestion + chunking",
        6:  "P1: vector DB (ChromaDB on Hetzner)",
        7:  "P1: RAG query chain (LangChain)",
        8:  "P1: add GDPR consent layer + data deletion",
        9:  "P1: frontend (React) + deploy",
        10: "P1: write README + blog post → PUBLISHED",
        11: "P2 planning: predictive maintenance spec",
        12: "P2: synthetic sensor dataset generation",
        13: "P2: EDA + feature engineering",
        14: "P2: anomaly detection model (Isolation Forest)",
        15: "P2: dashboard (Streamlit)",
        16: "P2: deploy on AWS → PUBLISHED",
        17: "P3 planning: multi-tenant SaaS spec",
        18: "P3: IaC with Terraform (VPC, EKS, RDS)",
        19: "P3: CI/CD pipeline (GitHub Actions)",
        20: "P3: multi-tenancy implementation",
        21: "P3: observability (Datadog)",
        22: "P3: load test + cost analysis → PUBLISHED",
        23: "P5 planning: EV charging pipeline spec",
        24: "P5: Airflow + dbt setup",
        25: "P5: data ingestion from open API",
        26: "P5: dbt transformations + tests",
        27: "P5: Grafana dashboard → PUBLISHED",
        28: "P4 planning: LLM fine-tune spec",
        29: "P4: dataset preparation (German domain)",
        30: "P4: LoRA fine-tuning run",
        31: "P4: evaluation + benchmark",
        32: "P4: HuggingFace publish → PUBLISHED",
        33: "P6 planning: GDPR data platform spec",
        34: "P6: data ingestion layer",
        35: "P6: dbt + quality checks",
        36: "P6: data catalog + lineage",
        37: "P6: GDPR audit trail → PUBLISHED",
        38: "OSS: first PR to open-source project",
        39: "OSS: second contribution",
        40: "All 6 projects: update READMEs with metrics",
        41: "Blog post: ML lessons from Project 2",
        42: "Blog post: GDPR architecture decisions",
        43: "Add: unit tests to all projects",
        44: "Add: integration tests to 2 projects",
        45: "Portfolio site: personal site with projects",
        46: "Portfolio: German-language project description",
        47: "P7 planning: German-language AI product",
        48: "P7: German NLP model + API",
        49: "P7: deploy + blog post in English & German",
        50: "Conference: submit abstract to PyData Berlin",
        51: "Conference: prepare talk slides",
        52: "All projects: add Docker Compose setup",
        53: "All projects: add Terraform deployment",
        54: "All projects: add observability",
        55: "All projects: cost analysis added",
        56: "Portfolio audit: every project has README, demo, blog",
        57: "LinkedIn: case study for each project",
        58: "GitHub stars goal: 50+ on top project",
        59: "OSS: major contribution (new feature)",
        60: "OSS: PR merged into significant project",
        61: "Build: new mini-project from Arxiv paper",
        62: "Mini-project: blog post",
        63: "Collaboration: find German dev partner on GitHub",
        64: "Collaboration: joint project or review",
        65: "All projects: performance benchmarks added",
        66: "All projects: security review",
        67: "All projects: GDPR compliance checklist",
        68: "All projects: cost optimisation applied",
        69: "Portfolio v2: redesigned personal site",
        70: "Portfolio: add video demos",
        71: "Blog: publish on dev.to + LinkedIn",
        72: "Blog: cross-post on Medium",
        73: "Tech talk: local Python meetup (Berlin/Hamburg prep)",
        74: "Apply to speak at PyData 2027",
        75: "All projects: final architecture diagrams",
        76: "All projects: final documentation",
        77: "GitHub: ensure all repos public + pinned",
        78: "GitHub profile README: showcase projects",
        79: "LinkedIn: update with all projects + certs",
        80: "Prepare interview project walk-through (30 min)",
        81: "Mock interview: present Project 1",
        82: "Mock interview: present Project 2",
        83: "Mock interview: present Project 4 (LLM)",
        84: "Mock interview: present Project 3 (infra)",
        85: "Mock interview: present Projects 5+6 (data)",
        86: "Mock interview: present OSS contributions",
        87: "Final portfolio review",
        88: "Final portfolio: all links working",
        89: "Submit 10 targeted applications with tailored cover",
        90: "Submit 10 more applications",
        91: "Follow up on all applications",
        92: "First-round interviews",
        93: "Technical interviews",
        94: "Final interviews",
        95: "Offer + negotiation",
        96: "Offer signed",
        97: "Visa / Blue Card application",
        98: "Relocation preparation",
        99: "Apartment search in target city",
        100: "Language prep: workplace German",
        101: "Final weeks in home country",
        102: "Move to Germany",
        103: "Onboarding prep",
        104: "DAY 1 at German company — TOP 0.1% ACHIEVED",
    }

    mern_map = {
        1:  "MERN audit: document current skill level",
        2:  "Polish existing MERN project for portfolio",
        3:  "Freelance: set up Fiverr + Upwork profile",
        4:  "Freelance: write 3 service proposals",
        5:  "Freelance: land first small gig ($50–200)",
        6:  "Deliver gig #1 on time + ask for review",
        7:  "Build: MERN SaaS starter template (sell/use)",
        8:  "Freelance: pitch 5 new clients",
        9:  "Build: React component library (reuse across gigs)",
        10: "Freelance: deliver gig #2 → target $100–300",
        11: "Build: admin dashboard template (sell on Gumroad)",
        12: "Gumroad: publish + market dashboard template",
        13: "Freelance: gig #3 → build momentum ($200–500)",
        14: "Build: MERN + AI integration (add ChatGPT to MERN)",
        15: "Market: AI-powered MERN app to clients",
        16: "Freelance: aim for $300–500/month total",
        17: "Build: SaaS boilerplate with auth + payments (Stripe)",
        18: "Sell boilerplate: Gumroad / LemonSqueezy",
        19: "Freelance: larger project ($500–1000)",
        20: "Automate: client onboarding workflow",
        21: "Build: client-specific MERN + ML dashboard",
        22: "Integrate RAG chatbot (Project 1) into MERN app",
        23: "Sell: AI chatbot integration service to SMBs",
        24: "Freelance: target $500–800/month",
        25: "Build: multi-client CMS (reusable)",
        26: "Freelance: raise rates ($30–50/hr)",
        27: "Build: German-market landing page template",
        28: "Market to German Mittelstand via LinkedIn",
        29: "Freelance: target €600/month",
        30: "Build: MERN + data viz dashboard (use D3/Recharts)",
        31: "Integrate Project 5 (EV data) into MERN dashboard",
        32: "Sell dashboard service: energy / logistics clients",
        33: "Freelance: €700–1000/month target",
        34: "Build: MERN + ML inference API client",
        35: "Market: AI-powered web apps to German SMBs",
        36: "Freelance: raise hourly rate to €40–60/hr",
        37: "Systemize: standard contract + invoice templates",
        38: "Systemize: project delivery checklist",
        39: "Systemize: client communication templates",
        40: "Freelance: €1000/month target → financial cushion",
        41: "Build: Next.js 14 portfolio for German market",
        42: "SEO: German-keyword optimized landing page",
        43: "Network: join German developer Slack communities",
        44: "Network: LinkedIn connect with 20 German devs",
        45: "Freelance: €1200/month",
        46: "Build: MERN + authentication (Clerk / Auth0)",
        47: "Add AI features to existing client projects",
        48: "Upsell: add AI features at €200–500 extra",
        49: "Freelance: €1500/month",
        50: "Productize: offer fixed-price AI integration packages",
        51: "Market: cold email 20 German SMBs",
        52: "Market: cold email 20 more",
        53: "Freelance: €1800/month",
        54: "Build: German-language AI chatbot SaaS (B2B)",
        55: "SaaS: MVP launch + first paying user",
        56: "SaaS: iterate on feedback",
        57: "Freelance + SaaS: €2000/month combined",
        58: "Delegate: simple gigs to junior devs (scale)",
        59: "Focus: German enterprise clients (higher rates)",
        60: "German enterprise: target €80–100/hr Freiberufler",
        61: "Register: Freiberufler status in Germany (prep)",
        62: "Legal: understand Scheinselbstständigkeit rules",
        63: "Freelance: €2500/month target",
        64: "Portfolio: add German case studies",
        65: "LinkedIn: German-language content posts",
        66: "XING: German professional network profile",
        67: "Freelance: €3000/month",
        68: "Reduce MERN hours as ML job approaches",
        69: "Transition plan: freelance → full-time German job",
        70: "Freelance: maintain €2000/month minimal effort",
        71: "Automate: recurring client retainer setup",
        72: "Hand off small clients to trusted junior dev",
        73: "Focus: only high-value German enterprise gigs",
        74: "MERN: €2000/month passive-ish income",
        75: "Save: 3-month Germany relocation fund",
        76: "Save: visa + apartment deposit fund",
        77: "Save: built up relocation budget",
        78: "Reduce freelance load: 10 hrs/week only",
        79: "Maintain: 1–2 retainer clients",
        80: "MERN income: financial runway secured",
        81: "Freelance: wind down to 5 hrs/week",
        82: "Maintain: 1 retainer client during job hunt",
        83: "Job hunt funded by savings + 1 retainer",
        84: "MERN income: cover expenses during interviews",
        85: "Financial: calculate Germany relocation costs",
        86: "Financial: Blue Card salary threshold (€45,552)",
        87: "Financial: city comparison (Munich vs Berlin cost)",
        88: "Financial: savings runway = 6 months",
        89: "Freelance: fully wound down",
        90: "Freelance: final invoice sent",
        91: "Focus 100%: job applications only",
        92: "Focus 100%: interviews",
        93: "Focus 100%: interviews",
        94: "Focus 100%: final interviews",
        95: "OFFER RECEIVED",
        96: "Negotiate: €80–100k+ salary",
        97: "Sign contract",
        98: "Financial: relocation package negotiation",
        99: "Financial: first German payslip projection",
        100: "Finances: set up German bank (N26/Deutsche Bank)",
        101: "Register: Anmeldung (address registration)",
        102: "Setup: German health insurance (TK/AOK)",
        103: "Setup: tax number + Steuerklasse",
        104: "FINANCIAL FREEDOM — German salary + savings",
    }

    german_map = {
        1:  "Arabic: final semester — focus on exams",
        2:  "Arabic: revision + grammar",
        3:  "Arabic: exam prep",
        4:  "Arabic: exam week",
        5:  "Arabic: done — begin German A1 immediately",
        6:  "German A1: alphabet, pronunciation, Duolingo start",
        7:  "German A1: numbers, greetings, basic phrases",
        8:  "German A1: articles (der/die/das), plural forms",
        9:  "German A1: verbs (sein, haben), present tense",
        10: "German A1: word order (SVO) + W-questions",
        11: "German A1: daily routine vocabulary (Anki deck)",
        12: "German A1: modal verbs (können, müssen, wollen)",
        13: "German A1: cases intro: Nominativ + Akkusativ",
        14: "German A1: prepositions + Dativ",
        15: "German A1: complete A1 Anki deck (200 cards)",
        16: "German A2: past tense (Perfekt)",
        17: "German A2: Präteritum (haben/sein/modals)",
        18: "German A2: separable verbs",
        19: "German A2: subordinate clauses (dass, weil, wenn)",
        20: "German A2: relative clauses",
        21: "German A2: adjective endings",
        22: "German A2: Genitiv case",
        23: "German A2: tech vocabulary (Computer, Software, Daten)",
        24: "German A2: complete A2 Anki deck (400 cards)",
        25: "German B1: Konjunktiv II (würde, könnte, wäre)",
        26: "German B1: Passiv voice",
        27: "German B1: Infinitivkonstruktionen (um…zu)",
        28: "German B1: business German (Bewerbung = job application)",
        29: "German B1: tech interview phrases",
        30: "German B1: practice speaking (italki tutor 1×/week)",
        31: "German B1: Goethe B1 practice test #1",
        32: "German B1: Goethe B1 practice test #2 + review",
        33: "Goethe B1 Exam (register + sit)",
        34: "German B2: advanced grammar review",
        35: "German B2: complex sentence structures",
        36: "German B2: technical writing in German",
        37: "German B2: German tech news reading (Heise Online)",
        38: "German B2: podcasts (Langsam gesprochene Nachrichten)",
        39: "German B2: workplace German (meetings, emails)",
        40: "German B2: German CV + Anschreiben (cover letter)",
        41: "German B2: practice job interview in German",
        42: "German B2: practice test #1",
        43: "German B2: practice test #2 + review",
        44: "Goethe B2 Exam (register + sit)",
        45: "German: maintain with 20 Anki cards/day",
        46: "German: listen to German tech podcasts daily",
        47: "German: read 1 German tech article/day (Heise)",
        48: "German: italki tutor 2×/week",
        49: "German: watch German TV (Dark, How to Sell Drugs)",
        50: "German: join German-speaking Discord",
        51: "German: write LinkedIn post in German",
        52: "German: translate 1 project README to German",
        53: "German: practice technical explanations auf Deutsch",
        54: "German: describe system architecture in German",
        55: "German: write blog post in German",
        56: "German: Anki 20 cards + 1 podcast",
        57: "German: Anki 20 cards + 1 article",
        58: "German: Anki 20 cards + 1 podcast",
        59: "German: German startup podcast (Gründerszene)",
        60: "German: network in German on XING",
        61: "German: practice cold email auf Deutsch",
        62: "German: German workplace culture study",
        63: "German: Pünktlichkeit, Direktheit, formality norms",
        64: "German: italki conversation practice",
        65: "German: Anki + podcast",
        66: "German: Anki + article",
        67: "German: Anki + podcast",
        68: "German: Anki + article",
        69: "German: Anki + podcast",
        70: "German: mock job interview auf Deutsch",
        71: "German: C1 prep — advanced grammar",
        72: "German: C1 — academic/technical writing",
        73: "German: C1 — formal presentations",
        74: "German: C1 — practice test",
        75: "German: C1 Exam prep final",
        76: "Goethe C1 Exam (optional but powerful)",
        77: "German: daily maintenance 20 Anki + podcast",
        78: "German: daily maintenance",
        79: "German: daily maintenance",
        80: "German: daily maintenance",
        81: "German: job interview practice auf Deutsch × 2",
        82: "German: job interview practice × 2",
        83: "German: company research in German",
        84: "German: prepare German-language answers",
        85: "German: salary negotiation phrases auf Deutsch",
        86: "German: email templates auf Deutsch",
        87: "German: cover letter final review by native",
        88: "German: phone interview practice",
        89: "German: interview day preparation",
        90: "German: daily maintenance",
        91: "German: maintenance + interview",
        92: "German: maintenance + interview",
        93: "German: maintenance + interview",
        94: "German: maintenance + interview",
        95: "German: celebrate — B2/C1 ACHIEVED",
        96: "German: relocation vocabulary",
        97: "German: bureaucracy vocabulary (Anmeldung etc.)",
        98: "German: apartment hunting phrases",
        99: "German: banking / insurance vocabulary",
        100: "German: workplace day-1 preparation",
        101: "German: final review — conversational fluency",
        102: "German: daily use in Germany BEGINS",
        103: "German: immersion mode",
        104: "German: FLUENT — B2/C1 — massive career advantage",
    }

    tools_map = {
        1:  "Notion setup, Anki install, Toggl Track",
        2:  "Obsidian vault setup + linking",
        3:  "VS Code: extensions (Python, Pylance, GitLens)",
        4:  "GitHub profile: README + contribution graph",
        5:  "Forest app: 90-min deep work sessions",
        6:  "Duolingo + Anki daily habit confirmed",
        7:  "Toggl: track all deep work hours",
        8:  "Weekly review: Notion template first use",
        9:  "Notion: set up weekly kanban (3 cols only)",
        10: "Anki: ML deck growing (20 cards/day)",
        11: "Toggl: check hours — aim 21 hrs/week deep work",
        12: "Obsidian: daily note habit",
        13: "GitHub: daily commit streak — start now",
        14: "Notion: project tracker for all 6 projects",
        15: "Review: all tools working well?",
        16: "Add: Jupyter notebooks to Obsidian links",
        17: "Add: Datadog free trial for Project 3",
        18: "Add: Terraform Cloud for state management",
        19: "Add: HuggingFace account + profile",
        20: "Add: MLflow local server",
        21: "Review: GitHub streak — keep going",
        22: "Review: Anki stats — retention rate >85%?",
        23: "Review: Toggl — is deep work hitting 3 hrs/day?",
        24: "Add: LinkedIn premium (1 month trial)",
        25: "Review: Notion — all 6 projects tracked?",
        26: "Add: Upwork/Fiverr for MERN freelance",
        27: "Add: Gumroad account for digital products",
        28: "Review: Anki retention + add missed concepts",
        29: "Review: GitHub — are projects getting stars?",
        30: "Review: MERN income tracking in Notion",
        31: "Tools audit: remove anything not being used",
        32: "Tools: set up German learning tracker in Notion",
        33: "Add: italki account for German tutors",
        34: "Add: Heise Online RSS feed",
        35: "Review: all tools — Q4 2026 audit",
        36: "Add: XING profile (German LinkedIn)",
        37: "Add: dev.to account for blog posts",
        38: "Add: Medium account",
        39: "Add: Hashnode for tech blog",
        40: "Review: blog posts published — target: 2 done",
        41: "Add: LeetCode account + streak",
        42: "Review: Notion — phases on track?",
        43: "Review: GitHub contributions heatmap",
        44: "Review: HuggingFace profile",
        45: "Tools: half-year audit — Q1 2027",
        46: "Add: Obsidian publish (optional — public notes)",
        47: "Review: LinkedIn SSI score",
        48: "Review: Toggl hours — 21+ hrs deep work/week?",
        49: "Review: German Anki retention",
        50: "Review: all 6 projects — GitHub stars?",
        51: "Add: portfolio site analytics (Plausible)",
        52: "Review: blog traffic",
        53: "Review: freelance income vs target",
        54: "Review: certs achieved vs plan",
        55: "Tools: Q2 2027 audit",
        56: "Review: total learning hours logged (Toggl)",
        57: "Review: GitHub contributions — 365 day streak?",
        58: "Review: job application tracker in Notion",
        59: "Review: interview pipeline",
        60: "Review: German level — B1 done?",
        61: "Review: MERN income runway",
        62: "Review: portfolio completeness",
        63: "Tools: Q3 2027 audit",
        64: "Add: Cal.com for interview scheduling",
        65: "Review: all certs on LinkedIn",
        66: "Review: projects on personal site",
        67: "Review: GitHub profile README",
        68: "Review: XING + LinkedIn both updated",
        69: "Review: German B2 on track?",
        70: "Tools: Q4 2027 audit — are you on track?",
        71: "Add: Notion job tracker (company, role, status)",
        72: "Review: application → interview conversion rate",
        73: "Review: referrals from German network",
        74: "Review: cover letter effectiveness",
        75: "Review: all tools for job hunt phase",
        76: "Review: savings runway in Notion",
        77: "Review: visa requirements checklist",
        78: "Review: Blue Card salary threshold clarity",
        79: "Review: target companies list (20 companies)",
        80: "Tools: Q1 2028 audit",
        81: "Job hunt: Notion tracker — 20 applications logged",
        82: "Job hunt: interview feedback logged",
        83: "Job hunt: referral pipeline tracked",
        84: "Job hunt: offer comparison matrix in Notion",
        85: "Job hunt: negotiation notes in Obsidian",
        86: "Job hunt: relocation checklist in Notion",
        87: "Job hunt: visa checklist in Notion",
        88: "Job hunt: apartment checklist",
        89: "Job hunt: banking checklist",
        90: "Job hunt: health insurance comparison",
        91: "Job hunt: tax setup checklist",
        92: "Job hunt: all logistics planned",
        93: "Job hunt: relocation budget confirmed",
        94: "Job hunt: offer signed",
        95: "Job hunt: paperwork submitted",
        96: "Job hunt: visa application in progress",
        97: "Relocation: apartment viewing scheduled",
        98: "Relocation: moving logistics",
        99: "Relocation: utilities setup",
        100: "Relocation: German bank account open",
        101: "Relocation: health insurance signed",
        102: "Day 1 prep: commute, dress code, team research",
        103: "Day 1 prep: first 30-60-90 day plan written",
        104: "DONE — all tools served their purpose",
    }

    review_map = {
        1:  "Did I set up all tools? GitHub commit?",
        2:  "Is my Anki habit formed? 3 weeks to go.",
        3:  "Deep work habit: hitting 3 hrs/day?",
        4:  "MERN freelance profile live?",
        5:  "First Fiverr/Upwork gig pitched?",
        6:  "Project 1 spec written?",
        7:  "German A1 started? Duolingo streak?",
        8:  "8 weeks in — review Toggl hours vs target",
        9:  "PyTorch basics solid?",
        10: "P1 — is the RAG pipeline working?",
        11: "P2 started? Sensor data EDA done?",
        12: "First freelance income received?",
        13: "Java Spring Boot setup done?",
        14: "Airflow DAG running?",
        15: "EV pipeline deployed?",
        16: "P1 + P2 + P5 all PUBLISHED?",
        17: "Terraform deployed real infra?",
        18: "CI/CD pipeline working end-to-end?",
        19: "P3 SaaS infra live?",
        20: "GDPR architecture understood deeply?",
        21: "Kafka producer/consumer working?",
        22: "RAG chatbot demo-able?",
        23: "SAA-C03 study started?",
        24: "German A2 reached? Anki 400 cards done?",
        25: "Snowflake account set up?",
        26: "SAA-C03 exam scheduled?",
        27: "P4 (LLM fine-tune) dataset ready?",
        28: "Freelance income: $300+/month?",
        29: "P4 LoRA run completed?",
        30: "P4 on HuggingFace Hub?  6 PROJECTS DONE!",
        31: "AWS SAA exam sat?",
        32: "Azure AZ-900 started?",
        33: "German B1 exam registered?",
        34: "Spring Boot microservices pattern implemented?",
        35: "Freelance income: $500+/month?",
        36: "AZ-104 study started?",
        37: "DDIA chapters 1–4 read?",
        38: "OSS first PR merged?",
        39: "Blog: 2 posts published?",
        40: "Freelance: $1000/month?  MAJOR MILESTONE",
        41: "CKA prep started?",
        42: "German B1 exam SAT?",
        43: "Leetcode: 50 problems done?",
        44: "DP-203 study started?",
        45: "Portfolio site live?",
        46: "CKA exam SAT?",
        47: "German B2 study started?",
        48: "Databricks account set up?",
        49: "Freelance: €1500/month?",
        50: "PyData Berlin talk submitted?",
        51: "Leetcode: 100 problems done?",
        52: "All projects Docker Compose?",
        53: "All projects Terraform deploy?",
        54: "AWS DevOps Pro study started?",
        55: "SaaS MVP launched?",
        56: "Freelance: €2000/month?",
        57: "German B2 exam registered?",
        58: "Advanced Spark UDFs working?",
        59: "Streaming ML pipeline built?",
        60: "German B2 exam SAT?",
        61: "Kubeflow pipeline running?",
        62: "Freiberufler registration researched?",
        63: "Freelance: €2500/month?",
        64: "All projects updated with observability?",
        65: "All certs on LinkedIn?",
        66: "XING profile complete?",
        67: "Freelance: €3000/month?",
        68: "Blog: 5+ posts published?",
        69: "OSS: 2+ PRs merged?",
        70: "HALFWAY — 70 weeks done! Celebrate + big review",
        71: "Advanced K8s operators working?",
        72: "C1 German prep started?",
        73: "Load tests on all projects?",
        74: "30 job applications sent?",
        75: "Relocation savings: 3 months runway?",
        76: "C1 exam registered?",
        77: "All 6 projects: GitHub stars growing?",
        78: "LinkedIn: 500+ connections?",
        79: "XING: active in German tech groups?",
        80: "Financial runway: 6 months confirmed?",
        81: "20 applications sent this week?",
        82: "First interview feedback received?",
        83: "Mock ML system design × 3 done?",
        84: "Offer comparison matrix started?",
        85: "Salary negotiation prepared?",
        86: "Visa checklist complete?",
        87: "Apartment search started?",
        88: "Banking + insurance researched?",
        89: "10 more applications sent?",
        90: "Financial: all costs planned?",
        91: "First-round interviews happening?",
        92: "Technical interviews scheduled?",
        93: "Final interviews this week?",
        94: "Offer received?",
        95: "OFFER SIGNED — celebrate!",
        96: "Visa applied?",
        97: "Apartment found?",
        98: "Moving date set?",
        99: "All logistics confirmed?",
        100: "German bank account open?",
        101: "Health insurance signed?",
        102: "In Germany — Anmeldung done?",
        103: "Day 1 plan written?",
        104: "TOP 0.1% — DONE. You made it.",
    }

    ml = ml_map.get(wk, "—")
    cloud = cloud_map.get(wk, "—")
    backend = backend_map.get(wk, "—")
    data = data_map.get(wk, "—")
    project = project_map.get(wk, "—")
    mern = mern_map.get(wk, "—")
    german = german_map.get(wk, "—")
    tools = tools_map.get(wk, "—")
    review = review_map.get(wk, "—")

    rows.append((wk, wd, phase_label, ph_bg, ph_fg,
                 ml, cloud, backend, data, project,
                 mern, german, tools, review))

# Write rows
for i, r in enumerate(rows):
    wk, wd, phase_label, ph_bg, ph_fg = r[0], r[1], r[2], r[3], r[4]
    row = i + 3

    alt = i % 2 == 1
    base_bg = "F8F7F4" if alt else C["white"]

    data_cell(ws1, row, 1, wk, bg=ph_bg, fg=ph_fg, bold=True, h="center")
    data_cell(ws1, row, 2, wd.strftime("%d %b %Y"), bg=base_bg, fg="5F5E5A")
    data_cell(ws1, row, 3, phase_label, bg=ph_bg, fg=ph_fg, sz=8)

    col_configs = [
        (r[5],  C["purple_l"] if not alt else "E8E6FC", C["purple_h"]),
        (r[6],  C["blue_l"]   if not alt else "D8EBF8", C["blue_h"]),
        (r[7],  C["amber_l"]  if not alt else "F5E6C8", C["amber_h"]),
        (r[8],  C["coral_l"]  if not alt else "F5E0D8", C["coral_h"]),
        (r[9],  C["teal_l"]   if not alt else "D4EEE6", C["teal_h"]),
        (r[10], C["mern_l"]   if not alt else "F0D8E4", C["mern_h"]),
        (r[11], C["german_l"] if not alt else "D4EEE6", C["german_h"]),
        (r[12], C["gray_l"]   if not alt else "E8E7E2", C["gray_h"]),
        (r[13], C["green_l"]  if not alt else "DCE9CC", C["green_h"]),
    ]
    for col_i, (val, bg, fg) in enumerate(col_configs, 4):
        data_cell(ws1, row, col_i, val, bg=bg, fg=fg, sz=8)

    ws1.row_dimensions[row].height = 38

# ══════════════════════════════════════════════════════════════════════════════
# Sheet 2 — DAILY SCHEDULE
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Daily Schedule")
ws2.sheet_view.showGridLines = False

ws2.merge_cells("A1:F1")
t2 = ws2.cell(row=1, column=1, value="Daily Schedule System — Student with 3–4 hrs Deep Work")
t2.font = Font(bold=True, color="FFFFFF", size=13, name="Arial")
t2.fill = fill(C["teal_h"])
t2.alignment = align(h="center")
ws2.row_dimensions[1].height = 28

headers2 = ["Time", "Block Type", "Activity", "Tool Used", "Output", "Phase Notes"]
widths2  = [12, 18, 35, 20, 25, 30]
for i, (h, w) in enumerate(zip(headers2, widths2), 1):
    ws2.column_dimensions[get_column_letter(i)].width = w
    hdr_cell(ws2, 2, i, h, bg=C["header_bg"], sz=9)

schedule = [
    ("6:30–6:50", "Morning boot", "No phone. Write ONE goal for today. Write 3 tasks max.", "Notion (daily note)", "Daily goal set", "Every day, always"),
    ("7:00–12:00", "University", "Attend lectures, labs, tutorials", "Physical notebook", "Class notes", "Until 1 Jul 2026, then this slot = Deep Work"),
    ("12:00–12:30", "Anki + Lunch", "Spaced repetition review while eating", "Anki app", "20–30 cards reviewed", "Zero extra time cost — do this every day"),
    ("12:30–13:00", "Admin / Break", "Emails, quick tasks, short walk", "—", "Inbox zero", "Protect this — no deep work here"),
    ("14:00–15:30", "Deep Work 1 — LEARN", "ML course / cloud tutorial / Java / German. Phone in another room. Timer running.", "Forest app + Toggl", "1 concept learned + Anki card added", "90 min = one complete topic unit"),
    ("15:30–15:50", "Hard Break", "Walk outside. No screens. Brain consolidates.", "—", "Refreshed", "Non-negotiable. Skipping kills afternoon block"),
    ("16:00–17:30", "Deep Work 2 — BUILD", "Work on active portfolio project. Commit code. Ship something small.", "VS Code + GitHub", "1 GitHub commit minimum", "Mon/Sat: ML build. Tue/Thu: project. Wed: infra"),
    ("17:30–18:30", "Exercise", "Walk, run, gym. Protects tomorrow's energy.", "—", "Physical health", "Non-negotiable. Top performers exercise."),
    ("19:00–20:00", "Freelance (MERN)", "Client work, gigs, Fiverr delivery, building templates", "VS Code + Figma", "Client deliverable or template progress", "This funds your journey — treat it seriously"),
    ("20:00–20:30", "German Study", "Duolingo + Anki German deck + italki prep", "Duolingo + Anki", "German vocabulary", "After 1 Jul: increase to 45 mins"),
    ("20:30–20:45", "Evening Review", "Did I hit ONE goal? What is tomorrow's goal? Log hours.", "Notion + Toggl", "Tomorrow's goal written", "Takes 15 min, saves 1 hr of confusion tomorrow"),
    ("21:00+", "Wind down", "Reading (DDIA, Chip Huyen), NOT social media", "Kindle / physical book", "1 chapter", "This is how you compound knowledge passively"),
]

type_colors = {
    "Morning boot": C["amber_l"],
    "University": C["gray_l"],
    "Anki + Lunch": C["teal_l"],
    "Admin / Break": C["gray_l"],
    "Deep Work 1 — LEARN": C["purple_l"],
    "Hard Break": C["gray_l"],
    "Deep Work 2 — BUILD": C["purple_l"],
    "Exercise": C["green_l"],
    "Freelance (MERN)": C["mern_l"],
    "German Study": C["german_l"],
    "Evening Review": C["amber_l"],
    "Wind down": C["blue_l"],
}
type_fg = {
    "Morning boot": C["amber_h"],
    "University": C["gray_h"],
    "Anki + Lunch": C["teal_h"],
    "Admin / Break": C["gray_h"],
    "Deep Work 1 — LEARN": C["purple_h"],
    "Hard Break": C["gray_h"],
    "Deep Work 2 — BUILD": C["purple_h"],
    "Exercise": C["green_h"],
    "Freelance (MERN)": C["mern_h"],
    "German Study": C["german_h"],
    "Evening Review": C["amber_h"],
    "Wind down": C["blue_h"],
}

for i, row_data in enumerate(schedule, 3):
    time_, type_, act, tool, out, note = row_data
    bg = type_colors.get(type_, C["white"])
    fg = type_fg.get(type_, C["black"])
    data_cell(ws2, i, 1, time_, bg=bg, fg=fg, bold=True, h="center")
    data_cell(ws2, i, 2, type_, bg=bg, fg=fg, bold=True)
    data_cell(ws2, i, 3, act, bg=bg, fg=fg)
    data_cell(ws2, i, 4, tool, bg=bg, fg="5F5E5A", italic=True)
    data_cell(ws2, i, 5, out, bg=bg, fg=fg)
    data_cell(ws2, i, 6, note, bg=bg, fg="5F5E5A")
    ws2.row_dimensions[i].height = 42

ws2.row_dimensions[2].height = 28

# ══════════════════════════════════════════════════════════════════════════════
# Sheet 3 — WEEKLY ROTATION
# ══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Weekly Focus Rotation")
ws3.sheet_view.showGridLines = False

ws3.merge_cells("A1:H1")
t3 = ws3.cell(row=1, column=1, value="Weekly Focus Rotation — Never Wonder What to Work On")
t3.font = Font(bold=True, color="FFFFFF", size=13, name="Arial")
t3.fill = fill(C["purple_h"])
t3.alignment = align(h="center")
ws3.row_dimensions[1].height = 28

days_hdr = ["Day", "DW1 Focus (14:00–15:30)", "DW2 Focus (16:00–17:30)", "Freelance Focus", "German Focus", "Key Deliverable", "Review Question"]
days_w   = [10, 28, 28, 22, 22, 28, 32]
for i, (h, w) in enumerate(zip(days_hdr, days_w), 1):
    ws3.column_dimensions[get_column_letter(i)].width = w
    hdr_cell(ws3, 2, i, h, bg=C["header_bg"], sz=9)

weekly = [
    ("Monday",    "AI/ML — new concept or course lesson",         "ML build — train model, run notebook",          "—",                              "20 Anki cards + Duolingo",          "1 ML concept mastered + Anki card added",     "What ML concept did I learn today?",           C["purple_l"], C["purple_h"]),
    ("Tuesday",   "Backend / Java / Spring Boot",                  "Portfolio project — backend feature",           "Client gig work (30 min)",       "20 Anki cards + Duolingo",          "1 GitHub commit + backend progress",          "Is the project moving forward?",               C["amber_l"],  C["amber_h"]),
    ("Wednesday", "Cloud / DevOps — tutorial or cert study",       "Infra project — Terraform / K8s",              "MERN freelance (60 min)",        "20 Anki cards + article auf Deutsch","1 infra component deployed",                  "Did I deploy something real today?",           C["blue_l"],   C["blue_h"]),
    ("Thursday",  "Data Engineering — Spark / dbt / Airflow",     "Portfolio project — data pipeline",            "Client gig work (30 min)",       "20 Anki cards + Duolingo",          "1 pipeline step working",                     "Is the data flowing?",                         C["coral_l"],  C["coral_h"]),
    ("Friday",    "German language — grammar + speaking",          "Light: blog post / docs / README writing",     "MERN product (template/SaaS)",   "45 min — italki or podcast",        "German practice + 1 blog/doc written",        "Can I explain my project auf Deutsch?",         C["german_l"], C["german_h"]),
    ("Saturday",  "Deep project sprint — pick hardest problem",    "Deep project sprint — ship something",         "MERN: bigger client project",    "20 Anki cards",                     "Major project milestone — commit + push",     "Did I ship something I'm proud of?",           C["teal_l"],   C["teal_h"]),
    ("Sunday",    "30-min planning: review last week + plan next", "OSS reading / Arxiv / tech articles",         "Invoice + admin (15 min)",       "20 Anki review only",               "Next week's ONE goal written in Notion",      "Am I on track for the 2-year plan?",           C["gray_l"],   C["gray_h"]),
]

for i, row_d in enumerate(weekly, 3):
    day, dw1, dw2, fl, de, deliv, rev, bg, fg = row_d
    data_cell(ws3, i, 1, day,   bg=bg, fg=fg, bold=True, h="center")
    data_cell(ws3, i, 2, dw1,   bg=bg, fg=fg)
    data_cell(ws3, i, 3, dw2,   bg=bg, fg=fg)
    data_cell(ws3, i, 4, fl,    bg=bg, fg="5F5E5A")
    data_cell(ws3, i, 5, de,    bg=bg, fg=fg)
    data_cell(ws3, i, 6, deliv, bg=bg, fg=fg, bold=True)
    data_cell(ws3, i, 7, rev,   bg=bg, fg="5F5E5A", italic=True)
    ws3.row_dimensions[i].height = 44

ws3.row_dimensions[2].height = 28

# ══════════════════════════════════════════════════════════════════════════════
# Sheet 4 — TOOLS & APPS GUIDE
# ══════════════════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet("Tools & Apps Guide")
ws4.sheet_view.showGridLines = False

ws4.merge_cells("A1:G1")
t4 = ws4.cell(row=1, column=1, value="Complete Tools & Apps Guide — When, Why, How to Use Each")
t4.font = Font(bold=True, color="FFFFFF", size=13, name="Arial")
t4.fill = fill(C["amber_h"])
t4.alignment = align(h="center")
ws4.row_dimensions[1].height = 28

hdr4 = ["Tool", "Category", "When to Use It", "How to Use It", "Time Per Day", "When to Add", "Cost"]
wid4 = [16, 16, 30, 38, 12, 18, 10]
for i, (h, w) in enumerate(zip(hdr4, wid4), 1):
    ws4.column_dimensions[get_column_letter(i)].width = w
    hdr_cell(ws4, 2, i, h, bg=C["header_bg"], sz=9)

tools_data = [
    ("Notion", "Productivity", "Weekly planning, project tracking, job applications", "1 kanban board (3 cols only). 1 daily note page. 1 project page per project. Sunday: fill next week.", "15 min", "Week 1 — immediately", "Free", C["amber_l"], C["amber_h"]),
    ("Anki", "Learning", "Every new concept you learn → flashcard. German vocab. ML terms.", "Add 5–10 cards per deep work session. Review 20 cards at lunch. Keep retention >85%.", "20–30 min", "Week 1 — immediately", "Free", C["teal_l"], C["teal_h"]),
    ("Toggl Track", "Tracking", "Track every deep work session. Review weekly: are you hitting 21+ hrs?", "Start timer when deep work begins. Stop when done. Weekly report every Sunday.", "Passive", "Week 1 — immediately", "Free", C["blue_l"], C["blue_h"]),
    ("Obsidian", "Second Brain", "Detailed notes, concept connections, research. Links between ideas.", "Daily note for each deep work session. Link concepts. Folder per domain.", "10–15 min", "Week 2", "Free", C["purple_l"], C["purple_h"]),
    ("Forest App", "Focus", "Lock phone during deep work. Growing tree = accountability.", "Set 90-min session. Phone locked. Tree dies if you open another app.", "Passive", "Week 1", "~$2", C["green_l"], C["green_h"]),
    ("VS Code", "Dev", "All coding. Python, Java, JS, Terraform, Docker.", "Extensions: Python, Pylance, GitLens, Docker, Terraform, ESLint, Prettier.", "Active", "Week 1", "Free", C["gray_l"], C["gray_h"]),
    ("GitHub", "Dev", "All code. Daily commit streak. Portfolio visibility.", "Commit something every day. Pin 6 projects. Write READMEs. Public profile = resume.", "Passive", "Week 1", "Free", C["gray_l"], C["gray_h"]),
    ("Duolingo", "German", "Daily German habit formation. Streak accountability.", "5–10 min/day minimum. Never break the streak. Supplement with Anki.", "10 min", "Week 5 (after Arabic)", "Free", C["german_l"], C["german_h"]),
    ("italki", "German", "Speaking practice with native German tutors.", "Book 1× per week from B1 level (Week 30+). 2× per week from B2.", "60 min/wk", "Week 30 (B1 phase)", "€15–25/hr", C["german_l"], C["german_h"]),
    ("HuggingFace", "ML", "Publish fine-tuned models. Show ML portfolio.", "Create profile Week 1. Publish models from Projects 1 and 4. Write model cards.", "Passive", "Week 1 (profile)", "Free", C["purple_l"], C["purple_h"]),
    ("MLflow", "ML", "Track ML experiments: params, metrics, artifacts.", "Set up local server. Log every training run. Compare experiments.", "Passive", "Week 23", "Free", C["purple_l"], C["purple_h"]),
    ("Fiverr / Upwork", "Freelance", "Find MERN freelance clients. Fund your journey.", "Set up profile Week 3. Write 3 gig proposals. Respond within 1 hr. 5-star = growth.", "30–60 min", "Week 3", "Free", C["mern_l"], C["mern_h"]),
    ("Gumroad", "Freelance", "Sell MERN templates, boilerplates, digital products.", "Set up account. Publish dashboard template. Market on LinkedIn/Twitter.", "Passive", "Week 12", "Free (5% fee)", C["mern_l"], C["mern_h"]),
    ("LeetCode", "Interviews", "Daily coding practice for German tech interviews.", "1 problem per day from Week 43. Easy × 3 days, Medium × 3 days, Hard × 1 day.", "30 min", "Week 43", "Free/Pro", C["coral_l"], C["coral_h"]),
    ("LinkedIn", "Career", "Build German tech network. Post content. Job search.", "Connect with 5 German devs/week. Post 1 update/week from Week 36. Apply directly.", "15 min", "Week 1 (profile)", "Free", C["blue_l"], C["blue_h"]),
    ("XING", "Career (DE)", "German-specific professional network. Many German companies use it.", "Create profile at Week 36. Join German dev groups. Active in discussions.", "10 min", "Week 36", "Free", C["german_l"], C["german_h"]),
    ("dev.to / Hashnode", "Content", "Publish technical blog posts for visibility.", "1 post per month from Week 37. Cross-post to Medium and LinkedIn.", "2 hrs/post", "Week 37", "Free", C["blue_l"], C["blue_h"]),
    ("Terraform Cloud", "Cloud", "State management for Terraform. Free tier sufficient.", "Connect to GitHub. Auto-plan on PR. Merge = apply. Use for all cloud projects.", "Passive", "Week 18", "Free", C["blue_l"], C["blue_h"]),
    ("Datadog", "Cloud", "APM, dashboards, alerts for Project 3.", "Free trial. Add to Project 3. Set up dashboards. Screenshot for portfolio.", "Passive", "Week 20", "Free trial", C["blue_l"], C["blue_h"]),
    ("Heise Online", "German", "German tech news. Read 1 article daily from B1 level.", "heise.de — bookmark it. Read with Google Translate assist at first.", "15 min", "Week 33", "Free", C["german_l"], C["german_h"]),
]

for i, row_d in enumerate(tools_data, 3):
    tool, cat, when, how, time_, add, cost = row_d[:7]
    bg, fg = row_d[7], row_d[8]
    data_cell(ws4, i, 1, tool,  bg=bg, fg=fg, bold=True)
    data_cell(ws4, i, 2, cat,   bg=bg, fg=fg)
    data_cell(ws4, i, 3, when,  bg=bg, fg=fg)
    data_cell(ws4, i, 4, how,   bg=bg, fg="2C2C2A")
    data_cell(ws4, i, 5, time_, bg=bg, fg=fg, h="center")
    data_cell(ws4, i, 6, add,   bg=bg, fg=fg)
    data_cell(ws4, i, 7, cost,  bg=bg, fg=fg, h="center")
    ws4.row_dimensions[i].height = 44

ws4.row_dimensions[2].height = 28

# ══════════════════════════════════════════════════════════════════════════════
# Sheet 5 — MERN FINANCE PLAN
# ══════════════════════════════════════════════════════════════════════════════
ws5 = wb.create_sheet("MERN Finance Plan")
ws5.sheet_view.showGridLines = False

ws5.merge_cells("A1:F1")
t5 = ws5.cell(row=1, column=1, value="MERN / Full-Stack Finance Plan — How It Funds Your German Journey")
t5.font = Font(bold=True, color="FFFFFF", size=13, name="Arial")
t5.fill = fill(C["mern_h"])
t5.alignment = align(h="center")
ws5.row_dimensions[1].height = 28

hdr5 = ["Period", "Weeks", "MERN Strategy", "Monthly Income Target", "What It Funds", "Action This Period"]
wid5 = [20, 10, 35, 22, 28, 35]
for i, (h, w) in enumerate(zip(hdr5, wid5), 1):
    ws5.column_dimensions[get_column_letter(i)].width = w
    hdr_cell(ws5, 2, i, h, bg=C["header_bg"], sz=9)

finance_periods = [
    ("Phase 0 — Setup", "1–8", "Polish MERN portfolio. Set up Fiverr/Upwork. First 2–3 gig proposals. Deliver first small gig.", "$50–200", "Courses, tools, Anki subscriptions", "Set up Fiverr profile. Write 3 gig descriptions. Deliver first gig on time.", C["mern_l"], C["mern_h"]),
    ("Phase 1 — Momentum", "9–16", "Deliver 2–3 gigs. Build reusable React component library. Publish admin dashboard template on Gumroad.", "$200–500", "Living expenses top-up, AWS free tier upgrades", "Hit $300/month. Collect 5-star reviews. Launch Gumroad product.", C["mern_l"], C["mern_h"]),
    ("Phase 2 — Growth", "17–26", "Raise rates to $30–40/hr. Build MERN + AI integration service. Target German SMB clients on LinkedIn.", "$500–800", "AWS costs, italki tutors ($60/month), cert prep materials", "First AI-integrated MERN project. LinkedIn outreach to 10 German SMBs.", C["mern_l"], C["mern_h"]),
    ("Phase 3 — Scale", "27–36", "MERN SaaS boilerplate (sell on Gumroad). Larger client projects ($500–1000 each). German-market landing pages.", "$800–1200", "AWS SAA exam fee (€330), cert study materials, savings start", "Launch SaaS boilerplate. Sit AWS SAA exam. Reach €1000/month.", C["mern_l"], C["mern_h"]),
    ("Phase 4 — Stable", "37–57", "2–3 retainer clients (€300–400 each). MERN + ML dashboards as premium service. Raise to €40–60/hr.", "€1200–2000", "CKA exam (€395), Azure certs, savings (3-month runway)", "Land first retainer client. Reach €1500/month. Start saving €300/month.", C["mern_l"], C["mern_h"]),
    ("Phase 5 — Productize", "58–75", "German B2B AI chatbot SaaS MVP. German enterprise Freiberufler prep (€80–100/hr). Delegate small gigs.", "€2000–3000", "Relocation savings fund (€3000 target), Goethe exams, visa fund", "Launch SaaS. Register Freiberufler intent. Savings: €3000 total.", C["mern_l"], C["mern_h"]),
    ("Phase 6 — Wind Down", "76–88", "Reduce to 10 hrs/week. Only high-value retainers. All energy on job hunt. €2000/month minimal effort.", "€1500–2000", "Living expenses during job hunt. Visa application fee. Apartment deposit.", "Reduce clients. Maintain 1 retainer. Full focus on interviews.", C["mern_l"], C["mern_h"]),
    ("Phase 7 — Funded Job Hunt", "89–104", "1 retainer client only (5 hrs/week). Savings cover 6 months. 100% focus on landing German job.", "€500–1000 (retainer)", "All costs covered by savings. German salary starts at €80–100k", "Accept offer. Savings = financial security. German salary replaces MERN income.", C["mern_l"], C["mern_h"]),
]

for i, row_d in enumerate(finance_periods, 3):
    period, wks, strat, income, funds, action = row_d[:6]
    bg, fg = row_d[6], row_d[7]
    data_cell(ws5, i, 1, period, bg=bg, fg=fg, bold=True)
    data_cell(ws5, i, 2, wks,    bg=bg, fg=fg, h="center")
    data_cell(ws5, i, 3, strat,  bg=bg, fg=fg)
    data_cell(ws5, i, 4, income, bg=bg, fg=fg, bold=True, h="center")
    data_cell(ws5, i, 5, funds,  bg=bg, fg="2C2C2A")
    data_cell(ws5, i, 6, action, bg=bg, fg=fg)
    ws5.row_dimensions[i].height = 50

ws5.row_dimensions[2].height = 28

# ══════════════════════════════════════════════════════════════════════════════
# Sheet 6 — MILESTONES DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
ws6 = wb.create_sheet("Milestones Dashboard")
ws6.sheet_view.showGridLines = False

ws6.merge_cells("A1:E1")
t6 = ws6.cell(row=1, column=1, value="Key Milestones — Track These to Know You're on Pace")
t6.font = Font(bold=True, color="FFFFFF", size=13, name="Arial")
t6.fill = fill(C["green_h"])
t6.alignment = align(h="center")
ws6.row_dimensions[1].height = 28

hdr6 = ["Milestone", "Target Week", "Target Date", "Category", "Why It Matters"]
wid6 = [40, 14, 14, 18, 38]
for i, (h, w) in enumerate(zip(hdr6, wid6), 1):
    ws6.column_dimensions[get_column_letter(i)].width = w
    hdr_cell(ws6, 2, i, h, bg=C["header_bg"], sz=9)

milestones = [
    ("4th semester exams DONE. Arabic learning complete.", 8, "1 Jul 2026", "Life", "Full 3–4 hrs/day now available for learning"),
    ("Project 1 PUBLISHED — GDPR-RAG chatbot on GitHub", 10, "13 Jul 2026", "Portfolio", "First portfolio proof of concept"),
    ("Project 2 PUBLISHED — Predictive maintenance on AWS", 16, "24 Aug 2026", "Portfolio", "Industrial ML = German employer magnet"),
    ("Project 3 PUBLISHED — Multi-tenant SaaS on EKS", 22, "5 Oct 2026", "Portfolio", "Cloud infra project proves DevOps skills"),
    ("Project 5 PUBLISHED — EV charging data pipeline", 27, "9 Nov 2026", "Portfolio", "Data engineering portfolio piece"),
    ("Project 4 PUBLISHED — LLM fine-tune on HuggingFace", 32, "14 Dec 2026", "Portfolio", "LLM project = top 1% differentiation"),
    ("Project 6 PUBLISHED — GDPR data platform", 37, "18 Jan 2027", "Portfolio", "ALL 6 PROJECTS DONE — portfolio complete"),
    ("AWS Solutions Architect Associate (SAA-C03) PASSED", 32, "14 Dec 2026", "Certification", "Germany's most-valued cloud cert"),
    ("Azure AZ-104 PASSED", 40, "15 Feb 2027", "Certification", "German enterprise Azure shops"),
    ("CKA (Kubernetes) PASSED", 46, "29 Mar 2027", "Certification", "K8s = must-have for DevOps roles"),
    ("Azure DP-203 Data Engineer PASSED", 42, "1 Mar 2027", "Certification", "Data engineering credential"),
    ("Goethe B1 German Exam PASSED", 33, "21 Dec 2026", "German", "Opens Mittelstand doors"),
    ("Goethe B2 German Exam PASSED", 44, "15 Mar 2027", "German", "Salary multiplier — very few expats reach B2"),
    ("Goethe C1 German Exam PASSED (optional)", 76, "25 Oct 2027", "German", "Elite tier — almost no expat engineers reach C1"),
    ("MERN freelance: $1000/month reached", 40, "15 Feb 2027", "Finance", "Journey is financially self-funded"),
    ("MERN freelance: €2000/month reached", 57, "14 Jun 2027", "Finance", "Relocation savings accumulating"),
    ("Relocation savings: €5000 saved", 75, "25 Oct 2027", "Finance", "Covers visa + apartment deposit + flights"),
    ("OSS first PR merged", 38, "1 Feb 2027", "Portfolio", "Open source = trust signal for German employers"),
    ("Personal portfolio site live", 45, "22 Mar 2027", "Portfolio", "Professional online presence"),
    ("Technical blog: 3 posts published", 50, "26 Apr 2027", "Portfolio", "Thought leadership"),
    ("LinkedIn: 500+ connections (German tech)", 70, "13 Sep 2027", "Network", "German referral network activated"),
    ("XING profile active in German tech groups", 36, "18 Jan 2027", "Network", "German-specific professional presence"),
    ("Mock system design interviews × 10 done", 82, "5 Jan 2028", "Interview", "Prepared for senior German interviews"),
    ("30 job applications sent to German companies", 90, "2 Mar 2028", "Job Hunt", "Numbers game — need pipeline"),
    ("First German technical interview", 92, "16 Mar 2028", "Job Hunt", "Validation of all work"),
    ("Offer received from German company", 95, "6 Apr 2028", "Job Hunt", "The goal"),
    ("Offer signed — €80–100k+ salary", 96, "13 Apr 2028", "Job Hunt", "Top 0.1% salary in Germany for your background"),
    ("Blue Card visa application submitted", 97, "20 Apr 2028", "Relocation", "Legal right to work in Germany"),
    ("Moved to Germany", 102, "25 May 2028", "Relocation", "Phase complete"),
    ("DAY 1 at German tech company — TOP 0.1% ACHIEVED", 104, "10 May 2028", "GOAL", "You made it"),
]

cat_colors = {
    "Life": (C["gray_l"], C["gray_h"]),
    "Portfolio": (C["teal_l"], C["teal_h"]),
    "Certification": (C["blue_l"], C["blue_h"]),
    "German": (C["german_l"], C["german_h"]),
    "Finance": (C["mern_l"], C["mern_h"]),
    "Network": (C["amber_l"], C["amber_h"]),
    "Interview": (C["purple_l"], C["purple_h"]),
    "Job Hunt": (C["coral_l"], C["coral_h"]),
    "Relocation": (C["green_l"], C["green_h"]),
    "GOAL": (C["purple_h"], "FFFFFF"),
}

for i, ms in enumerate(milestones, 3):
    label, wk, dt, cat, why = ms
    bg, fg = cat_colors.get(cat, (C["white"], C["black"]))
    data_cell(ws6, i, 1, label, bg=bg, fg=fg, bold=(cat == "GOAL"))
    data_cell(ws6, i, 2, f"Week {wk}", bg=bg, fg=fg, h="center")
    data_cell(ws6, i, 3, dt, bg=bg, fg=fg, h="center")
    data_cell(ws6, i, 4, cat, bg=bg, fg=fg, bold=True, h="center")
    data_cell(ws6, i, 5, why, bg=bg, fg="2C2C2A")
    ws6.row_dimensions[i].height = 30

ws6.row_dimensions[2].height = 28

# ── save ──────────────────────────────────────────────────────────────────────
out = "outputs/German_Tech_Roadmap_2026_2028.xlsx"
wb.save(out)
print("saved:", out)