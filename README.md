# System-Design-Patterns
An attempt to curate concise notes on system design.

## Composite Pattern - Note-Taking System

This repository demonstrates the **Composite Pattern** applied to a note-taking system that supports various content types including headings, subheadings, text, code blocks, and diagrams.

### Features

The note-taking system supports:
- **Headings** (H1-H6): Hierarchical titles and sections
- **Text**: Plain text content with multi-line support
- **Code Blocks**: Syntax-highlighted code snippets
- **Diagrams**: ASCII art, flowcharts, or other visual representations
- **Sections**: Nested groupings of content elements
- **Metadata**: Author, date, tags, and custom fields

### Design Pattern: Composite

The Composite Pattern is a structural design pattern that:
- Composes objects into tree structures to represent part-whole hierarchies
- Allows clients to treat individual objects and compositions uniformly
- Makes it easy to add new component types without changing existing code

### Quick Start

```python
from composite_pattern_notes import Note, Heading, Text, CodeBlock, Diagram

# Create a note
note = Note("My Study Notes")
note.set_metadata("author", "John Doe")

# Add various components
note.add(Heading("Introduction"))
note.add(Text("This is my introduction paragraph."))

note.add(Heading("Code Example"))
note.add(CodeBlock("print('Hello, World!')", language="python"))

note.add(Heading("Architecture Diagram"))
note.add(Diagram("""
    Client --> Server
    Server --> Database
""", diagram_type="ascii"))

# Render and save
print(note.render())
note.save_to_file("my_notes.md")
```

### Usage

Run the example demonstration:
```bash
python composite_pattern_notes.py
```

This will create a comprehensive example note demonstrating all features and save it to `composite_pattern_notes_example.md`.

### Component Hierarchy

```
NoteComponent (Abstract)
├── Leaf Components
│   ├── Heading
│   ├── Subheading
│   ├── Text
│   ├── CodeBlock
│   └── Diagram
└── Composite Components
    ├── Section (can contain multiple components)
    └── Note (top-level container)
```

### Why Composite Pattern?

This pattern is ideal for note-taking because:
1. **Flexibility**: Mix and match different content types freely
2. **Extensibility**: Add new component types (tables, images, etc.) easily
3. **Uniformity**: All components share the same interface
4. **Composability**: Nest sections and subsections arbitrarily deep
5. **Simplicity**: Client code doesn't need to distinguish between leaf and composite nodes

### Example Output

The system generates well-formatted markdown output:

```markdown
# System Design Patterns - Composite Pattern

---
author: System Design Notes
date: 2026-02-27
---

## Introduction

The Composite Pattern is a structural design pattern...

## Code Example

```python
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass
```

[Diagram: ascii]
    ┌─────────────┐
    │  Component  │
    └─────────────┘
[End Diagram]
```

### License

This is an educational project for learning system design patterns.
