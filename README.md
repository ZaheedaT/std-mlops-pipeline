# MLOps Pipeline

An object-oriented MLOps platform designed to manage the machine learning lifecycle from **training and validation through model registration, deployment, and production monitoring** utilising Wrappers.

The project separates the reusable **MLOps platform** from the project-specific **machine learning logic**. 
This allows the same platform architecture to be reused across different machine learning projects.

The design is based on OOP principles commonly used in C++, including:

* Abstract base classes
* Pure virtual functions
* Inheritance
* Polymorphism
* Encapsulation
* Composition
* Dependency injection
* Dependency inversion
* Factory patterns where appropriate

---

# Architecture

The project is divided into two main layers:

```text
                        std-mlops-pipeline
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
              ┌─────────────┐             ┌─────────────┐
              │  platform/  │             │  project/   │
              │             │             │             │
              │ REUSABLE    │             │ PROJECT     │
              │ MLOps       │             │ SPECIFIC    │
              │ INFRASTRUCTURE│           │ ML LOGIC    │
              └──────┬──────┘             └─────────────┘
                     │
                     ▼
              ┌─────────────┐
              │  Pipeline   │
              │             │
              │ ORCHESTRATOR│
              └──────┬──────┘
                     │
       ┌─────────────┼─────────────┬──────────────┐
       │             │             │              │
       ▼             ▼             ▼              ▼
   Training      Validation    Registry       Deployment
       │             │             │              │
       └─────────────┴─────────────┴──────────────┘
                             │
                             ▼
                        Monitoring
```

The platform uses **abstract base classes** to separate what a component must do from how that component performs the operation.

---

# Project Structure

```text
mlops-pipeline/
│
├── platform/
│   │
│   ├── core/
│   │   ├── result.py
│   │   └── exceptions.py
│   │
│   ├── interfaces/
│   │   ├── trainer.py
│   │   ├── validator.py
│   │   ├── registry.py
│   │   ├── deployer.py
│   │   └── monitor.py
│   │
│   ├── training/
│   │   └── trainer.py
│   │
│   ├── validation/
│   │   └── validator.py
│   │
│   ├── registry/
│   │   └── registry.py
│   │
│   ├── deployment/
│   │   └── deployer.py
│   │
│   ├── monitoring/
│   │   └── monitor.py
│   │
│   ├── pipeline/
│   │   └── pipeline.py
│   │
│   └── config/
│       └── loader.py
│
├── project/
│   ├── config.yaml
│   ├── project.py
│   ├── train.py
│   └── predict.py
│
├── templates/
│   ├── Dockerfile
│   ├── deployment.yaml
│   └── service.yaml
│
├── tests/
│
└── setup/
    ├── requirements.txt
    └── setup.sh
```

---

Running Python Modules

Run Python modules from the project root using the `-m` flag.

For example:

```bash
python -m tests.test_config
```

This is preferred over running the file directly:

```bash
python tests/test_config.py
```

Running with `-m` allows Python to treat the project root as the module search path, so project packages such as `platform` can be imported correctly.

### Running Tests

From the project root:

```bash
python -m tests.test_config
```

To run another test module:

```bash
python -m tests.test_entrypoint
```

### Run Your Project 
##### Run Entrypoint Code
Tells the framework where it should enter your project's code.

```bash
python -m <your_project>.<your_train_dir>:<your_trainfunc?
```
```text
project.train:train
│      │      │
│      │      └── function: train
│      └───────── module: project.train
└──────────────── package: project
```

```bash
pipeline.run(project)
```
-------------------------------------

# OOP Architecture

The central idea of the architecture is:

```text
                         ABSTRACT DEFINITION
                                  │
                                  │
                                  ▼
                         platform/interfaces/
                                  │
                                  │ INHERITANCE
                                  ▼
                        CONCRETE IMPLEMENTATION
                                  │
                                  ▼
                    training / validation / registry
                    deployment / monitoring
                                  │
                                  │
                                  ▼
                             Pipeline
```

The `interfaces/` directory defines the **abstract base classes**.

The other platform components provide the **concrete implementations**.

The `pipeline/` directory then uses those components through their abstract types.

This allows the pipeline to remain independent of the specific implementation being used.

---


## Interface Files

| File                               | Abstract Base Class | Operation    |
| ---------------------------------- | ------------------- | ------------ |
| `platform/interfaces/trainer.py`   | `Trainer`           | `train()`    |
| `platform/interfaces/validator.py` | `Validator`         | `validate()` |
| `platform/interfaces/registry.py`  | `Registry`          | `register()` |
| `platform/interfaces/deployer.py`  | `Deployer`          | `deploy()`   |
| `platform/interfaces/monitor.py`   | `Monitor`           | `monitor()`  |

These classes define **what operations are available**, without defining the implementation details.

---

# 2. Concrete Classes

The corresponding directories contain the concrete implementations.

For example:

```text
                         INHERITANCE
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/interfaces/trainer.py          │
│                                         │
│              Trainer                    │
│                                         │
│        ABSTRACT BASE CLASS              │
│                                         │
│        train()                          │
│        @abstractmethod                  │
└────────────────────┬────────────────────┘
                     ▲
                     │
                     │ inherits from
                     │
┌────────────────────┴────────────────────┐
│ platform/training/trainer.py            │
│                                         │
│           ModelTrainer                  │
│                                         │
│          CONCRETE CLASS                 │
│                                         │
│          train()                        │
│          actual implementation          │
└─────────────────────────────────────────┘
```

The concrete class inherits from the abstract base class and implements the required operation.

Conceptually:

```python
class ModelTrainer(Trainer):

    def train(self) -> Result:
        # actual training implementation
        ...
```

In C++ terminology, this is equivalent to:

```cpp
class ModelTrainer : public Trainer {
public:
    Result train() override {
        // actual training implementation
    }
};
```

Python does not use the `override` keyword, but the derived class is implementing the inherited abstract method.

---

## Concrete Implementation Files

| File                               | Concrete Class       | Inherits From |
| ---------------------------------- | -------------------- | ------------- |
| `platform/training/trainer.py`     | `ModelTrainer`       | `Trainer`     |
| `platform/validation/validator.py` | `ModelValidator`     | `Validator`   |
| `platform/registry/registry.py`    | `MLflowRegistry`     | `Registry`    |
| `platform/deployment/deployer.py`  | `KubernetesDeployer` | `Deployer`    |
| `platform/monitoring/monitor.py`   | `DriftMonitor`       | `Monitor`     |

The inheritance relationships are:

```text
                         INHERITANCE
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/interfaces/trainer.py          │
│ Trainer                                 │
│ ABSTRACT BASE CLASS                     │
└────────────────────┬────────────────────┘
                     ▲
                     │ inherits from
                     │
┌────────────────────┴────────────────────┐
│ platform/training/trainer.py            │
│ ModelTrainer                            │
│ CONCRETE CLASS                          │
└─────────────────────────────────────────┘


                         INHERITANCE
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/interfaces/validator.py        │
│ Validator                               │
│ ABSTRACT BASE CLASS                     │
└────────────────────┬────────────────────┘
                     ▲
                     │ inherits from
                     │
┌────────────────────┴────────────────────┐
│ platform/validation/validator.py        │
│ ModelValidator                          │
│ CONCRETE CLASS                          │
└─────────────────────────────────────────┘


                         INHERITANCE
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/interfaces/registry.py         │
│ Registry                                │
│ ABSTRACT BASE CLASS                     │
└────────────────────┬────────────────────┘
                     ▲
                     │ inherits from
                     │
┌────────────────────┴────────────────────┐
│ platform/registry/registry.py           │
│ MLflowRegistry                          │
│ CONCRETE CLASS                          │
└─────────────────────────────────────────┘


                         INHERITANCE
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/interfaces/deployer.py         │
│ Deployer                                │
│ ABSTRACT BASE CLASS                     │
└────────────────────┬────────────────────┘
                     ▲
                     │ inherits from
                     │
┌────────────────────┴────────────────────┐
│ platform/deployment/deployer.py         │
│ KubernetesDeployer                      │
│ CONCRETE CLASS                          │
└─────────────────────────────────────────┘


                         INHERITANCE
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/interfaces/monitor.py          │
│ Monitor                                 │
│ ABSTRACT BASE CLASS                     │
└────────────────────┬────────────────────┘
                     ▲
                     │ inherits from
                     │
┌────────────────────┴────────────────────┐
│ platform/monitoring/monitor.py          │
│ DriftMonitor                            │
│ CONCRETE CLASS                          │
└─────────────────────────────────────────┘
```

---

# 3. Polymorphism

The pipeline does not need to know the exact concrete class being used.

For example, it can work with:

```python
trainer: Trainer
```

while the actual object may be:

```python
ModelTrainer()
```

This is polymorphism.

```text
                         POLYMORPHISM
                              │
                              ▼

                     ┌─────────────────┐
                     │    Pipeline     │
                     │                 │
                     │ expects Trainer │
                     └────────┬────────┘
                              │
                              │ receives
                              ▼
                     ┌─────────────────┐
                     │  ModelTrainer   │
                     │                 │
                     │ concrete object │
                     └─────────────────┘
```

The pipeline interacts with the object through the `Trainer` interface.

Therefore, the concrete implementation can change without requiring the pipeline itself to change.

---

# 4. Composition

The `Pipeline` class does not inherit from `Trainer`, `Validator`, `Registry`, or the other components.

Instead, it **uses** them.

This is composition.

```text
                         COMPOSITION
                             │
                             ▼

┌─────────────────────────────────────────┐
│ platform/pipeline/pipeline.py           │
│                                         │
│               Pipeline                  │
│                                         │
│          CONCRETE CLASS                 │
└────────────────────┬────────────────────┘
                     │
                     │ uses
       ┌─────────────┼─────────────┬─────────────┐
       │             │             │             │
       ▼             ▼             ▼             ▼
   Trainer       Validator      Registry      Deployer
       │             │             │             │
       ▼             ▼             ▼             ▼
ModelTrainer   ModelValidator MLflowRegistry KubernetesDeployer
```

The pipeline is therefore responsible for **orchestrating** the components rather than implementing every operation itself.

---

# 5. Dependency Injection

The concrete components can be supplied to the pipeline rather than created directly inside it.

For example:

```python
pipeline = Pipeline(
    trainer=trainer,
    validator=validator,
    registry=registry,
    deployer=deployer,
    monitor=monitor,
)
```

Conceptually:

```text
                     Pipeline
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
     Trainer         Validator         Registry
        ▲               ▲                ▲
        │               │                │
 ModelTrainer    ModelValidator    MLflowRegistry
```

This is dependency injection.

The pipeline receives its dependencies instead of being tightly coupled to specific implementations.

---

# 6. Pipeline Orchestration

The `platform/pipeline/pipeline.py` file is responsible for coordinating the lifecycle.

The general flow is:

```text
                         Pipeline
                            │
                            ▼
                         Training
                            │
                            ▼
                        Validation
                            │
                            ▼
                    Model Registration
                            │
                            ▼
                        Deployment
                            │
                            ▼
                       Monitoring
```

Each stage performs its own responsibility.

The pipeline coordinates the order in which those responsibilities are executed.

---

# 7. Result Handling

The `platform/core/result.py` file contains the shared `Result` type used by pipeline operations.

```python
@dataclass
class Result:
    """
    Represents the success or failure of an MLOps pipeline operation.
    """
```

A successful operation can return:

```python
Result.ok(
    message="Training completed successfully.",
    data=model,
)
```

A failed operation can return:

```python
Result.failure(
    message="Training failed.",
)
```

The `Result` object provides a consistent return type for pipeline operations.

```text
                   Pipeline Operation
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
          SUCCESS                  FAILURE
              │                       │
              ▼                       ▼
       Result.ok(...)          Result.failure(...)
              │                       │
              └───────────┬───────────┘
                          ▼
                       Result
```

The return annotation:

```python
def train(self) -> Result:
```

means that the method is expected to return a `Result` object.

The quoted form:

```python
def train(self) -> "Result":
```

is a forward reference to the `Result` class.

---

# 8. Core Components

The `platform/core/` directory contains shared infrastructure used throughout the platform.

### `result.py`

Provides the standard `Result` return type.

### `exceptions.py`

Contains platform-specific exceptions used when an operation needs to signal an exceptional condition.

These components are not part of the inheritance hierarchy of trainers, validators, or deployers.

They are shared infrastructure.

---

# 9. Configuration

The `platform/config/loader.py` file is responsible for loading platform/project configuration.

Project-specific configuration is stored in:

```text
project/config.yaml
```

This keeps configuration separate from the implementation code.

Conceptually:

```text
project/config.yaml
        │
        ▼
platform/config/loader.py
        │
        ▼
    Configuration
        │
        ▼
   Platform Components
```

---

# 10. Project Layer

The `project/` directory contains logic specific to the machine learning project.

```text
┌─────────────────────────────────────────┐
│ project/                                │
│                                         │
│ config.yaml                             │
│ project.py                              │
│ train.py                                │
│ predict.py                              │
└─────────────────────────────────────────┘
```

The purpose of this separation is that the reusable MLOps platform does not need to contain project-specific model logic.

For example, another ML project could provide its own:

```text
project/config.yaml
project/project.py
project/train.py
project/predict.py
```

while continuing to use the same platform architecture.

---

# 11. Deployment

The deployment layer packages and deploys the model service using containerisation and Kubernetes.

The deployment architecture is:

```text
                     Model
                       │
                       ▼
                 Docker Image
                       │
                       ▼
                    Registry
                       │
                       ▼
                  Kubernetes
                       │
                       ▼
                     Pods
                       │
                       ▼
                  Model API
```

The current Kubernetes deployment environment is **AWS EKS**.

Kubernetes manifests are maintained under:

```text
templates/
├── deployment.yaml
└── service.yaml
```

The Docker container definition is:

```text
templates/Dockerfile
```

---

# 12. Monitoring

The monitoring component is responsible for observing the deployed model and its production data.

The monitoring architecture is:

```text
                     Production
                         │
                         ▼
                    Model Service
                         │
                         ▼
                  Prediction Data
                         │
                         ▼
                    Monitoring
                         │
                         ▼
                  Drift Detection
                         │
                         ▼
                 Pipeline Actions
```

The platform is designed to support production monitoring and data/model drift detection.

---

# 13. Factory Pattern

A factory can be introduced when the platform needs to create different concrete implementations dynamically.

For example:

```text
                    Factory
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     ModelTrainer  OtherTrainer  CustomTrainer
```

The factory would decide which concrete class to instantiate while the rest of the pipeline continues to depend on the abstract base class.

A factory is **not required simply because the project uses OOP**. It should be introduced when object creation becomes complex or implementation selection needs to be configurable.

---

# 14. C++ OOP Concept Mapping

The architecture maps closely to concepts used in C++ OOP.

| C++ Concept           | Python Implementation                                   |
| --------------------- | ------------------------------------------------------- |
| Abstract base class   | `ABC`                                                   |
| Pure virtual function | `@abstractmethod`                                       |
| Derived class         | `class ModelTrainer(Trainer)`                           |
| `override`            | Implementing the inherited abstract method              |
| Virtual dispatch      | Python method dispatch / polymorphism                   |
| Inheritance           | Concrete class → abstract base class                    |
| Composition           | `Pipeline` contains/uses components                     |
| Dependency injection  | Dependencies passed into `Pipeline`                     |
| Encapsulation         | Implementation details kept inside classes              |
| Return type           | `-> Result`                                             |
| Factory               | Factory class/function when object creation requires it |
| `friend`              | Not used; Python has no direct equivalent               |

---

# 15. Overall OOP Structure

The core architecture can be represented as:

```text
                         ABSTRACT BASE CLASSES
                                  │
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │ platform/interfaces/     │
                    │                          │
                    │ trainer.py               │
                    │ validator.py             │
                    │ registry.py              │
                    │ deployer.py              │
                    │ monitor.py               │
                    └────────────┬─────────────┘
                                 │
                                 │ INHERITANCE
                                 ▼
                    ┌──────────────────────────┐
                    │ CONCRETE IMPLEMENTATIONS │
                    │                          │
                    │ training/trainer.py      │
                    │ validation/validator.py  │
                    │ registry/registry.py     │
                    │ deployment/deployer.py   │
                    │ monitoring/monitor.py    │
                    └────────────┬─────────────┘
                                 │
                                 │ POLYMORPHISM
                                 ▼
                    ┌──────────────────────────┐
                    │ pipeline/pipeline.py     │
                    │                          │
                    │ Pipeline                 │
                    │                          │
                    │ ORCHESTRATOR             │
                    └────────────┬─────────────┘
                                 │
                                 │ COMPOSITION
                                 ▼
                    ┌──────────────────────────┐
                    │ MLOps Lifecycle          │
                    │                          │
                    │ Train                    │
                    │ Validate                 │
                    │ Register                 │
                    │ Deploy                   │
                    │ Monitor                  │
                    └──────────────────────────┘
```

The key principle is:

```text
       WHAT
        │
        ▼
Abstract Base Class
        │
        │ inheritance
        ▼
       HOW
        │
        ▼
Concrete Class
        │
        │ polymorphism
        ▼
    Pipeline
        │
        │ composition
        ▼
MLOps Lifecycle
```

---

# Goals

This project is intended to demonstrate a production-oriented, reusable MLOps architecture with:

* Object-oriented software design
* Abstract base classes
* Inheritance and polymorphism
* Dependency injection
* Modular pipeline components
* Automated model training
* Model validation
* Model registration and versioning
* Containerised model serving
* Kubernetes deployment
* AWS EKS infrastructure
* Production monitoring
* Data and model drift detection
* Automated CI/CD
* Reusable platform components

The long-term goal is to create a reusable MLOps platform where a new machine learning project supplies its **project-specific model logic and configuration**, while the underlying MLOps infrastructure can be reused.

