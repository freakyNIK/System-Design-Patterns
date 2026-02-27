# Quick Start Guide

## Installation

No external dependencies required - just standard Python 3.6+.

## Basic Usage

### 1. Create a Simple Note

```python
from composite_pattern_notes import Note, Text, CodeBlock

# Create a note
note = Note("My First Note")
note.add(Text("This is my first note using the Composite Pattern!"))
note.add(CodeBlock("print('Hello, World!')", "python"))

# Display the note
print(note.render())

# Save to file
note.save_to_file("my_note.md")
```

### 2. Add Headings and Subheadings

```python
from composite_pattern_notes import Note, Heading, Subheading, Text

note = Note("Study Notes")
note.add(Heading("Introduction"))
note.add(Text("This is the introduction section."))
note.add(Subheading("Background", level=2))
note.add(Text("Background information goes here."))
note.add(Subheading("Details", level=3))
note.add(Text("Detailed information."))
```

### 3. Organize with Sections

```python
from composite_pattern_notes import Note, Section, Text, CodeBlock

note = Note("Programming Guide")

# Create a section
python_section = Section("Python Basics")
python_section.add(Text("Python is a high-level programming language."))
python_section.add(CodeBlock("x = 10\nprint(x)", "python"))

# Add section to note
note.add(python_section)
```

### 4. Add Diagrams

```python
from composite_pattern_notes import Note, Diagram, Text

note = Note("System Architecture")
note.add(Text("Here's our system architecture:"))
note.add(Diagram("""
┌─────────┐
│ Client  │
└────┬────┘
     │
     ▼
┌─────────┐
│ Server  │
└─────────┘
""", diagram_type="architecture"))
```

### 5. Use Metadata

```python
from composite_pattern_notes import Note, Text

note = Note("Project Documentation")
note.set_metadata("author", "John Doe")
note.set_metadata("date", "2026-02-27")
note.set_metadata("version", "1.0")
note.set_metadata("tags", "documentation, project")

note.add(Text("Project content here..."))
```

### 6. Method Chaining

```python
from composite_pattern_notes import Note, Text, CodeBlock

note = (Note("Chained Note")
    .set_metadata("author", "Developer")
    .add(Text("First paragraph"))
    .add(CodeBlock("code here", "python"))
    .add(Text("Second paragraph")))

note.save_to_file("chained_note.md")
```

## Running Examples

### Main Demo
```bash
python composite_pattern_notes.py
```

### All Examples
```bash
python examples.py
```

### Run Tests
```bash
python test_composite_pattern.py
```

## Component Types

| Component | Purpose | Example |
|-----------|---------|---------|
| `Heading` | Top-level heading (H1) | `Heading("Title")` |
| `Subheading` | Sub-headings (H2-H6) | `Subheading("Subtitle", level=2)` |
| `Text` | Plain text content | `Text("Content here")` |
| `CodeBlock` | Code with syntax highlighting | `CodeBlock("code", "python")` |
| `Diagram` | Visual diagrams | `Diagram("A -> B", "flowchart")` |
| `Section` | Group related components | `Section("Section Title")` |
| `Note` | Top-level document | `Note("Document Title")` |

## Output Format

All notes are rendered as markdown, which can be:
- Viewed in any markdown viewer
- Converted to PDF, HTML, or other formats
- Committed to version control
- Shared and collaborated on

## Tips

1. **Use Sections** for organizing complex notes
2. **Chain methods** for cleaner code
3. **Add metadata** for better organization
4. **Specify language** in code blocks for syntax highlighting
5. **Use descriptive diagram types** to clarify their purpose
6. **Save frequently** to avoid losing work

## Advanced Usage

### Custom Rendering
You can extend the base `NoteComponent` class to create custom components:

```python
from composite_pattern_notes import NoteComponent

class CustomComponent(NoteComponent):
    def __init__(self, content):
        self.content = content
    
    def render(self, indent=0):
        prefix = "  " * indent
        return f"{prefix}[CUSTOM: {self.content}]\n"
    
    def get_text_content(self):
        return self.content
```

### Extracting Text
Get plain text from any component:

```python
note = Note("Test")
note.add(Text("Hello"))
note.add(CodeBlock("code", "python"))

# Extract all text
text = note.get_text_content()
print(text)  # "Test Hello code"
```

## Support

For issues or questions, refer to the documentation in the source files:
- `composite_pattern_notes.py` - Core implementation with detailed docstrings
- `examples.py` - 5 comprehensive examples
- `test_composite_pattern.py` - Test cases showing usage patterns
