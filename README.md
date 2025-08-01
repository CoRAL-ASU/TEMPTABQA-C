# LLM-Symbolic Integration for Robust Temporal Tabular Reasoning

This repository contains the implementation and datasets associated with the paper "LLM-Symbolic Integration for Robust Temporal Tabular Reasoning." The project addresses the challenges of temporal tabular reasoning using large language models (LLMs), focusing on structured, symbolic approaches to improve performance, robustness, and scalability.

## Overview

Temporal tabular question answering requires reasoning over structured data with time-dependent attributes. Traditional LLM approaches struggle with limitations such as sensitivity to table size, reliance on memorized patterns, and reduced performance on complex queries. To address these gaps, we propose:

1. TEMPTABQA-C: A large-scale synthetic dataset designed for controlled and systematic evaluation of temporal reasoning tasks.
2. Symbolic Intermediate Representation: A structured framework where LLMs generate and execute SQL queries on database schemas, improving reasoning and mitigating biases.
3. Adaptive Few-Shot Prompting: Dynamically tailored examples that enhance model performance in diverse scenarios.

## TEMPTABQA-C Dataset

### Overview

TEMPTABQA-C is a large-scale, semi-automatically generated dataset tailored for evaluating temporal reasoning in LLMs. It overcomes limitations of traditional human-curated datasets by allowing controlled variations in data characteristics and enabling scalable generation of diverse and challenging scenarios.

### Dataset Features

- Controlled Evaluation: Enables systematic testing across diverse data characteristics.
- Scalability: Comprises over 200,000 questions spanning a wide range of contexts and complexities.
- Fine-Grained Analysis: Supports benchmarking for model biases, robustness, and limitations in temporal reasoning.

### Dataset Composition and Splits

#### Original Questions

- Table Sizes:
  - Small Tables: Concise data representing limited records.
  - Large Tables: Extensive datasets with higher complexity.
- Question Complexity:
  - Easy: Basic fact retrieval or single-step reasoning.
  - Medium: Multi-step temporal reasoning, calculations, or comparisons.
  - Hard: Complex, multi-hop temporal reasoning.

#### Counterfactual Questions

-  Questions that modify specific facts in the dataset to challenge robustness.

### Dataset Statistics

| Category           | Examples |
| ------------------ | -------- |
| Original Questions | 578      |
| Counterfactual     | 699      |
| Small Tables       | 855      |
| Large Tables       | 538      |
| Easy               | 732      |
| Medium             | 507      |
| Hard               | 719      |

### Dataset Creation Pipeline

1. **Extracting Temporal Information**

   - Temporal data (e.g., athletes, tournaments, achievements) was extracted from Wikipedia infoboxes.
   - Attributes like "Name," "Date of Birth," "Tournaments Played," and "Medals Won" were converted into a structured format.

2. **Relational Database Construction**

   - The structured data was organized into a relational schema with the following key tables:
     - Athlete Table: Contains unique `athlete_id` and athlete names.
     - Personal Information Table: Captures details like birth year, month, and day, linked to `athlete_id`.
     - Tournament Table: Stores tournament names, linked to `athlete_id`.
     - Format Table: Represents event formats, linked to tournaments.
     - Medal Table: Documents medals, including type (e.g., Gold), year, and location.

3. **Question and Answer Generation**

   - Questions were generated using predefined templates. Examples include:
     - "At what age did [Athlete] win their most recent [Tournament] [Medal Type]?"
     - "In which city did [Athlete] win their most recent [Tournament] medal?"
   - Answers were derived using SQL-based logic to query the relational database.
   - Counterfactual questions were generated by modifying specific attributes to create hypothetical scenarios.

4. **SQL-Based Answer Generation**

   - For each question, an SQL query was generated to retrieve the correct answer from the relational database.
   - This approach ensures consistency, scalability, and precision in dataset generation.

## Key Contributions

1. TEMPTABQA-C: A synthetic dataset enabling precise evaluation of temporal tabular reasoning tasks.
2. Symbolic Intermediate Representation: Transforming unstructured tables into database schemas for SQL-based reasoning.
3. Adaptive Few-Shot Prompting: Dynamically tailoring examples to improve model robustness in diverse contexts.

## Experimental Setup

### Evaluation Metrics

- **Exact Match Score (EMS)**: Measures the accuracy of predicted answers against ground truth (0 or 1).
- **Relaxed Exact Match Score (REMS)**: A relaxed version of EMS, tolerating partial accuracy (any number between 0 or 1).

### Baselines and Methods

1. Direct Prompting: Natural language prompts with answers directly generated by LLMs.
2. Symbolic Intermediate Representation: LLMs generate SQL queries that are executed on the database to retrieve answers.
3. Few-Shot Prompting:
   - Zero-Shot: No examples provided.
   - Non-Adaptive Few-Shot: Static examples provided for all queries.
   - Adaptive Few-Shot: Examples dynamically selected based on query context.

#### Prompts Used for Evaluation:

1. **Zero-Shot Prompting Without Context**:

   - The model generates answers based solely on the question without relying on any external data or context.

2. **(Direct Prompting with CoT) Zero-Shot Prompting with Infobox Context**:

   - The model answers questions by referring to an infobox, leveraging chain-of-thought reasoning for step-by-step answer generation.

3. **(Direct Prompting with CoT) Static Few-Shot Prompting with Infobox Context**:

   - Few-shot examples are statically selected, providing consistent infobox data and chain-of-thought reasoning templates to guide the model.

4. **(Direct Prompting with CoT) Dynamic Few-Shot Prompting with Infobox Context**:

   - Few-shot examples are dynamically selected based on the question context, ensuring the most relevant prompts for infobox-based reasoning.

5. **Plan and Solve**:

   - Encourages the model to generate a structured plan before solving the problem, improving reasoning consistency over complex tabular data.

6. **Clear Reasoning**:

   - The model breaks down questions into smaller sub-questions, solving them step-by-step to derive a final answer in a clear and systematic manner.

7. **Faithful Chain-of-Thought (Faithful CoT)**:

   - The model generates step-by-step reasoning in Python-like pseudocode, ensuring logical coherence before arriving at the answer.

8. **Program of Thought (PoT)**:

   - The model directly generates Python code as a response, executing it for accurate computation-based answers.

9. **Zero-Shot SQL Generation**:

   - The model generates SQL queries based on a schema without any prior examples, producing answers directly from structured database queries.

10. **Static Few-Shot SQL Generation**:

    - SQL queries are constructed using static few-shot examples, providing guidance for database interactions.

11. **Dynamic Few-Shot SQL Generation**:

    - SQL queries are dynamically generated using few-shot examples tailored to the specific query type, improving adaptability and precision.





## Results and Findings

## Evaluation Results for GPT-4o

| Reasoning | Context | Method Type          | Metric | Original | CounterFact | Gap (Original - CounterFact) | Large  | Small  | Gap (Small - Large) | Easy   | Medium | Hard   |
|--------|---------|----------------------|--------|----------|-------------|------------------------------|--------|--------|---------------------|--------|--------|--------|
| None   | -       | -                    | REMS   | 23.91    | 14.12       | 9.79                         | 23.84  | 25.79  | 1.95                | 28.67  | 25.55  | 23.83  |
|        |         |                      | EMS    | 22.96    | 12.92       | 10.04                        | 23.05  | 24.68  | 1.63                | 27.26  | 24.06  | 22.35  |
| Text   | Table   | zero shots (CoT)     | REMS   | 52.14    | 41.18       | 10.96                        | 45.24  | 67.81  | 22.57               | 72.34  | 59.43  | 52.90  |
|        |         |                      | EMS    | 49.70    | 39.29       | 10.41                        | 43.31  | 64.56  | 21.25               | 69.86  | 57.20  | 49.02  |
| Text   | Table   | Static (CoT)         | REMS   | 56.16    | 43.96       | 12.20                        | 48.96  | 73.57  | 24.61               | 73.45  | 65.39  | 56.97  |
|        |         |                      | EMS    | 53.95    | 41.91       | 12.04                        | 46.84  | 71.11  | 24.27               | 71.18  | 63.12  | 53.35  |
| Text   | Table   | Adaptive (CoT)       | REMS   | 57.51    | 43.93       | 13.58                        | 51.41  | 76.97  | 25.56               | 76.89  | 66.00  | 58.00  |
|        |         |                      | EMS    | 54.92    | 41.70       | 13.22                        | 48.88  | 73.92  | 25.04               | 74.38  | 63.91  | 54.17  |
| Text   | Table   | Clear                | REMS   | 66.84    | 50.17       | 16.67                        | 55.54  | 77.86  | 22.32               | 78.97  | 72.70  | 64.72  |
|        |         |                      | EMS    | 65.57    | 48.21       | 17.36                        | 53.53  | 76.49  | 22.96               | 76.40  | 71.99  | 62.62  |
| Text   | Table   | Plan And Solve       | REMS   | 70.36    | 48.62       | 21.74                        | 57.14  | 76.91  | 19.77               | 80.30  | 72.30  | 62.64  |
|        |         |                      | EMS    | 69.55    | 46.50       | 23.05                        | 55.20  | 75.44  | 20.24               | 77.96  | 70.81  | 60.25  |
| Symbolic | Table   | Program of Thought | REMS   | 59.05    | 50.28       | 8.77                         | 51.66  | 64.35  | 12.69               | 72.65  | 60.85  | 52.89  |
|        |         |                      | EMS    | 56.40    | 47.07       | 9.33                         | 50.19  | 62.22  | 12.03               | 69.94  | 57.20  | 48.81  |
| Symbolic | Table   | Faithful CoT       | REMS   | 60.02    | 50.90       | 9.12                         | 51.76  | 64.85  | 13.09               | 72.02  | 59.78  | 51.25  |
|        |         |                      | EMS    | 57.44    | 47.78       | 9.66                         | 50.19  | 62.69  | 12.50               | 69.24  | 56.02  | 47.17  |
| SQL    | Schema  | zero shots           | REMS   | 49.40    | 47.41       | 1.99                         | 55.99  | 58.58  | 2.59                | 63.53  | 65.20  | 45.46  |
|        |         |                      | EMS    | 47.27    | 45.27       | 2.00                         | 54.09  | 56.14  | 2.05                | 61.21  | 63.12  | 42.02  |
| SQL    | Schema  | Static               | REMS   | 62.90    | 61.65       | 1.25                         | 72.01  | 73.67  | 1.66                | 80.96  | 76.27  | 64.69  |
|        |         |                      | EMS    | 61.36    | 60.40       | 0.96                         | 70.82  | 71.93  | 1.11                | 78.58  | 75.54  | 62.62  |
| SQL    | Schema  | Adaptive             | REMS   | 68.41    | 67.42       | 0.99                         | 73.42  | 72.80  | -0.62               | 79.94  | 74.55  | 66.97  |
|        |         |                      | EMS    | 68.04    | 67.02       | 1.02                         | 73.23  | 72.16  | -1.07               | 79.83  | 73.57  | 66.32  |

1. **Robustness to Counterfactual Data**

   - SQL-based methods exhibited significantly smaller performance gaps compared to direct prompting.
   - Adaptive few-shot prompting further improved robustness.

2. **Scalability with Table Size**

   - SQL methods consistently handled large tables with minimal performance degradation.

3. **Handling Question Complexity**

   - SQL-based reasoning outperformed direct prompting across easy, medium, and hard questions.

## Repository Structure

- `Test_Dataset_with_Splits/`: Contains the TEMPTABQA-C dataset with the 7 splits.
- `Dataset_Creation/`: Stores files required to make the dataset
    - `Data_Extraction/`: Extracts data from wikipidea.
    - `Database_Generation/`: creates the database and inputs the data into the database.
    - `Questions/`: Stores the Question Templates used for the Questions in the dataset.
    - `Questions_Answers_with_SQL_Logic/`: Stores the SQL code and sample data required to generate the answers of questions of the dataset.
- `Prompts/`: Prompts the models were evaluated on.
- `Evaluation_Metrics/`: Code to generate the REMS and EMS scores.

## Citation
```bibtex
@inproceedings{kulkarni-etal-2025-llm,
    title = "{LLM}-Symbolic Integration for Robust Temporal Tabular Reasoning",
    author = "Kulkarni, Atharv  and
      Dixit, Kushagra  and
      Srikumar, Vivek  and
      Roth, Dan  and
      Gupta, Vivek",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-acl.1022/",
    pages = "19914--19940",
    ISBN = "979-8-89176-256-5",
    abstract = "Temporal tabular question answering presents a significant challenge for Large Language Models (LLMs), requiring robust reasoning over structured data{---}a task where traditional prompting methods often fall short. These methods face challenges such as memorization, sensitivity to table size, and reduced performance on complex queries. To overcome these limitations, we introduce TEMPTABQA-C, a synthetic dataset designed for systematic and controlled evaluations, alongside a symbolic intermediate representation that transforms tables into database schemas. This structured approach allows LLMs to generate and execute SQL queries, enhancing generalization and mitigating biases. By incorporating adaptive fewshot prompting with contextually tailored examples, our method achieves superior robustness, scalability, and performance. Experimental results consistently highlight improvements across key challenges, setting a new benchmark for robust temporal reasoning with LLMs. Code and TEMPTABQA-C dataset: https:// coral-lab-asu.github.io/llm{\_}symbolic."
}
