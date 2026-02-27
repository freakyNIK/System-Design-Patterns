"""
Composite Pattern for Note-Taking System

The Composite Pattern allows you to compose objects into tree structures to represent
part-whole hierarchies. This pattern lets clients treat individual objects and 
compositions of objects uniformly.

In this implementation, we create a note-taking system where:
- Individual elements (Heading, Text, CodeBlock, Diagram) are leaf components
- Sections/Notes are composite components that can contain multiple elements
- All components share a common interface

This allows for flexible, hierarchical note structures with various content types.
"""

from abc import ABC, abstractmethod
from typing import List


class NoteComponent(ABC):
    """Abstract base class for all note components (Composite Pattern)"""
    
    @abstractmethod
    def render(self, indent: int = 0) -> str:
        """Render the component as formatted text"""
        pass
    
    @abstractmethod
    def get_text_content(self) -> str:
        """Get plain text content without formatting"""
        pass


class Heading(NoteComponent):
    """Leaf component: Represents a top-level heading (H1)"""
    
    def __init__(self, text: str):
        self.text = text
    
    def render(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}# {self.text}\n"
    
    def get_text_content(self) -> str:
        return self.text


class Subheading(NoteComponent):
    """Leaf component: Represents a subheading (H2, H3, etc.)"""
    
    def __init__(self, text: str, level: int = 2):
        self.text = text
        self.level = max(2, min(6, level))  # Levels 2-6
    
    def render(self, indent: int = 0) -> str:
        prefix = "  " * indent
        hashes = "#" * self.level
        return f"{prefix}{hashes} {self.text}\n"
    
    def get_text_content(self) -> str:
        return self.text


class Text(NoteComponent):
    """Leaf component: Represents plain text content"""
    
    def __init__(self, content: str):
        self.content = content
    
    def render(self, indent: int = 0) -> str:
        prefix = "  " * indent
        lines = self.content.split('\n')
        return '\n'.join(f"{prefix}{line}" for line in lines) + "\n"
    
    def get_text_content(self) -> str:
        return self.content


class CodeBlock(NoteComponent):
    """Leaf component: Represents a code block with syntax highlighting"""
    
    def __init__(self, code: str, language: str = ""):
        self.code = code
        self.language = language
    
    def render(self, indent: int = 0) -> str:
        prefix = "  " * indent
        lines = [f"{prefix}```{self.language}"]
        code_lines = self.code.split('\n')
        lines.extend(f"{prefix}{line}" for line in code_lines)
        lines.append(f"{prefix}```")
        return '\n'.join(lines) + "\n"
    
    def get_text_content(self) -> str:
        return self.code


class Diagram(NoteComponent):
    """Leaf component: Represents a diagram (could be ASCII art, Mermaid, etc.)"""
    
    def __init__(self, content: str, diagram_type: str = "ascii"):
        self.content = content
        self.diagram_type = diagram_type
    
    def render(self, indent: int = 0) -> str:
        prefix = "  " * indent
        lines = [f"{prefix}[Diagram: {self.diagram_type}]"]
        diagram_lines = self.content.split('\n')
        lines.extend(f"{prefix}{line}" for line in diagram_lines)
        lines.append(f"{prefix}[End Diagram]")
        return '\n'.join(lines) + "\n"
    
    def get_text_content(self) -> str:
        return self.content


class Section(NoteComponent):
    """Composite component: Can contain multiple note components"""
    
    def __init__(self, title: str = ""):
        self.title = title
        self.components: List[NoteComponent] = []
    
    def add(self, component: NoteComponent) -> 'Section':
        """Add a component to this section (returns self for chaining)"""
        self.components.append(component)
        return self
    
    def remove(self, component: NoteComponent) -> 'Section':
        """Remove a component from this section"""
        self.components.remove(component)
        return self
    
    def render(self, indent: int = 0) -> str:
        """Render all components in this section"""
        result = []
        if self.title:
            prefix = "  " * indent
            result.append(f"{prefix}## {self.title}\n")
        
        for component in self.components:
            result.append(component.render(indent))
        
        return ''.join(result)
    
    def get_text_content(self) -> str:
        """Get all text content from this section"""
        parts = [self.title] if self.title else []
        parts.extend(component.get_text_content() for component in self.components)
        return ' '.join(parts)


class Note(NoteComponent):
    """Top-level composite: Represents a complete note document"""
    
    def __init__(self, title: str):
        self.title = title
        self.components: List[NoteComponent] = []
        self.metadata = {}
    
    def add(self, component: NoteComponent) -> 'Note':
        """Add a component to this note (returns self for chaining)"""
        self.components.append(component)
        return self
    
    def remove(self, component: NoteComponent) -> 'Note':
        """Remove a component from this note"""
        self.components.remove(component)
        return self
    
    def set_metadata(self, key: str, value: str) -> 'Note':
        """Set metadata for this note (returns self for chaining)"""
        self.metadata[key] = value
        return self
    
    def render(self, indent: int = 0) -> str:
        """Render the complete note"""
        result = []
        
        # Add title
        result.append(f"# {self.title}\n\n")
        
        # Add metadata if present
        if self.metadata:
            result.append("---\n")
            for key, value in self.metadata.items():
                result.append(f"{key}: {value}\n")
            result.append("---\n\n")
        
        # Add all components
        for component in self.components:
            result.append(component.render(indent))
            result.append("\n")  # Add spacing between components
        
        return ''.join(result)
    
    def get_text_content(self) -> str:
        """Get all text content from this note"""
        parts = [self.title]
        parts.extend(component.get_text_content() for component in self.components)
        return ' '.join(parts)
    
    def save_to_file(self, filename: str):
        """Save the rendered note to a file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.render())


def main():
    """Demonstration of the Composite Pattern for note-taking"""
    
    print("=" * 60)
    print("Composite Pattern - Note-Taking System Demo")
    print("=" * 60)
    print()
    
    # Create a note with various components
    note = Note("System Design Patterns - Composite Pattern")
    note.set_metadata("author", "System Design Notes")
    note.set_metadata("date", "2026-02-27")
    
    # Add introduction
    note.add(Subheading("Introduction", level=2))
    note.add(Text(
        "The Composite Pattern is a structural design pattern that lets you compose "
        "objects into tree structures to represent part-whole hierarchies. It allows "
        "clients to treat individual objects and compositions uniformly."
    ))
    
    # Add a section on structure
    structure_section = Section("Pattern Structure")
    structure_section.add(Text(
        "The pattern consists of three main components:"
    ))
    structure_section.add(Text(
        "1. Component - Abstract interface for all objects in the composition\n"
        "2. Leaf - Individual objects with no children\n"
        "3. Composite - Objects that can have children"
    ))
    note.add(structure_section)
    
    # Add code example
    note.add(Subheading("Code Example", level=2))
    note.add(Text("Here's a simple implementation in Python:"))
    note.add(CodeBlock(
        """class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite({', '.join(results)})" """,
        language="python"
    ))
    
    # Add diagram
    note.add(Subheading("Class Diagram", level=2))
    note.add(Diagram(
        """    ┌─────────────┐
    │  Component  │ (Abstract)
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │             │
┌───┴────┐   ┌────┴─────┐
│  Leaf  │   │Composite │
└────────┘   └────┬─────┘
                  │
              ┌───┴───┐
              │ children│
              └─────────┘""",
        diagram_type="ascii"
    ))
    
    # Add use cases
    note.add(Subheading("Common Use Cases", level=2))
    use_cases = Section()
    use_cases.add(Text(
        "• File systems (files and directories)\n"
        "• UI component hierarchies (containers and widgets)\n"
        "• Document structures (sections, paragraphs, images)\n"
        "• Organization charts (employees and departments)"
    ))
    note.add(use_cases)
    
    # Add benefits and drawbacks
    note.add(Subheading("Benefits", level=3))
    note.add(Text(
        "✓ Simplifies client code - treat all objects uniformly\n"
        "✓ Makes it easy to add new component types\n"
        "✓ Provides flexibility in building complex structures"
    ))
    
    note.add(Subheading("Drawbacks", level=3))
    note.add(Text(
        "✗ Can make design overly general\n"
        "✗ May be difficult to restrict component types in composites"
    ))
    
    # Render and display the note
    print(note.render())
    
    # Save to file
    note.save_to_file("composite_pattern_notes_example.md")
    print("\n" + "=" * 60)
    print("Note saved to: composite_pattern_notes_example.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
