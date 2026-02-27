"""
Additional examples demonstrating the note-taking system
"""

from composite_pattern_notes import (
    Note, Heading, Subheading, Text, CodeBlock, Diagram, Section
)


def example_1_simple_note():
    """Example 1: Simple note with basic components"""
    print("=" * 60)
    print("Example 1: Simple Note")
    print("=" * 60)
    
    note = Note("Quick Start Guide")
    note.set_metadata("tags", "tutorial, getting-started")
    
    note.add(Subheading("Overview"))
    note.add(Text("This guide will help you get started quickly."))
    
    note.add(Subheading("Installation"))
    note.add(Text("Run the following command:"))
    note.add(CodeBlock("pip install my-package", language="bash"))
    
    print(note.render())
    return note


def example_2_nested_sections():
    """Example 2: Note with nested sections"""
    print("=" * 60)
    print("Example 2: Nested Sections")
    print("=" * 60)
    
    note = Note("Database Design Patterns")
    note.set_metadata("author", "DB Expert")
    note.set_metadata("category", "databases")
    
    # Repository Pattern section
    repo_section = Section("Repository Pattern")
    repo_section.add(Text("The Repository pattern mediates between the domain and data mapping layers."))
    repo_section.add(Subheading("Benefits", level=3))
    repo_section.add(Text("• Decouples business logic from data access\n• Centralizes data access logic"))
    note.add(repo_section)
    
    # Active Record section
    active_section = Section("Active Record Pattern")
    active_section.add(Text("Active Record is an object that wraps a row in a database table."))
    active_section.add(Subheading("Example", level=3))
    active_section.add(CodeBlock(
        """class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def save(self):
        # Save to database
        pass
    
    @classmethod
    def find(cls, id):
        # Load from database
        pass""",
        language="python"
    ))
    note.add(active_section)
    
    print(note.render())
    return note


def example_3_technical_documentation():
    """Example 3: Technical documentation with diagrams"""
    print("=" * 60)
    print("Example 3: Technical Documentation")
    print("=" * 60)
    
    note = Note("Microservices Architecture")
    note.set_metadata("author", "Architect Team")
    note.set_metadata("date", "2026-02-27")
    note.set_metadata("version", "1.0")
    
    note.add(Subheading("Architecture Overview"))
    note.add(Text(
        "Our system uses a microservices architecture with the following components:"
    ))
    
    note.add(Diagram(
        """┌─────────┐     ┌─────────┐     ┌─────────┐
│  API    │────▶│ Service │────▶│Database │
│ Gateway │     │  Layer  │     │         │
└─────────┘     └─────────┘     └─────────┘
     │               │
     │               ▼
     │          ┌─────────┐
     └─────────▶│  Cache  │
                └─────────┘""",
        diagram_type="architecture"
    ))
    
    note.add(Subheading("Service Communication"))
    note.add(Text("Services communicate using REST APIs:"))
    note.add(CodeBlock(
        """GET /api/v1/users/{id}
POST /api/v1/users
PUT /api/v1/users/{id}
DELETE /api/v1/users/{id}""",
        language="http"
    ))
    
    note.add(Subheading("Configuration"))
    note.add(Text("Example configuration file:"))
    note.add(CodeBlock(
        """{
  "service": {
    "name": "user-service",
    "port": 8080,
    "database": {
      "host": "localhost",
      "port": 5432
    }
  }
}""",
        language="json"
    ))
    
    print(note.render())
    return note


def example_4_study_notes():
    """Example 4: Study notes with multiple topics"""
    print("=" * 60)
    print("Example 4: Study Notes")
    print("=" * 60)
    
    note = Note("Data Structures & Algorithms")
    note.set_metadata("subject", "Computer Science")
    note.set_metadata("semester", "Fall 2026")
    
    # Arrays section
    arrays = Section("Arrays")
    arrays.add(Text("Contiguous memory locations storing elements of the same type."))
    arrays.add(Subheading("Time Complexity", level=3))
    arrays.add(Text("• Access: O(1)\n• Search: O(n)\n• Insert: O(n)\n• Delete: O(n)"))
    arrays.add(Subheading("Example", level=3))
    arrays.add(CodeBlock(
        """# Python array operations
arr = [1, 2, 3, 4, 5]
arr[0]        # Access: O(1)
arr.append(6) # Insert at end: O(1)
arr.insert(0, 0)  # Insert at start: O(n)""",
        language="python"
    ))
    note.add(arrays)
    
    # Linked Lists section
    linked_lists = Section("Linked Lists")
    linked_lists.add(Text("Sequential collection of nodes, each containing data and reference to next node."))
    linked_lists.add(Diagram(
        """┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│ data │───▶│ data │───▶│ data │───▶│ NULL │
│ next │    │ next │    │ next │    └──────┘
└──────┘    └──────┘    └──────┘""",
        diagram_type="data-structure"
    ))
    linked_lists.add(Subheading("Advantages", level=3))
    linked_lists.add(Text("• Dynamic size\n• Efficient insertions/deletions"))
    note.add(linked_lists)
    
    print(note.render())
    return note


def example_5_api_documentation():
    """Example 5: API documentation"""
    print("=" * 60)
    print("Example 5: API Documentation")
    print("=" * 60)
    
    note = Note("REST API Documentation")
    note.set_metadata("api_version", "v2.0")
    note.set_metadata("base_url", "https://api.example.com")
    
    note.add(Subheading("Authentication"))
    note.add(Text("All requests require an API key in the header:"))
    note.add(CodeBlock(
        """Authorization: Bearer YOUR_API_KEY""",
        language="http"
    ))
    
    # Endpoints section
    endpoints = Section("Endpoints")
    
    # Users endpoint
    endpoints.add(Subheading("GET /users", level=3))
    endpoints.add(Text("Retrieve all users."))
    endpoints.add(CodeBlock(
        """curl -X GET https://api.example.com/users \\
  -H "Authorization: Bearer YOUR_API_KEY" """,
        language="bash"
    ))
    endpoints.add(Text("Response:"))
    endpoints.add(CodeBlock(
        """{
  "users": [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
  ]
}""",
        language="json"
    ))
    
    # Create user endpoint
    endpoints.add(Subheading("POST /users", level=3))
    endpoints.add(Text("Create a new user."))
    endpoints.add(CodeBlock(
        """curl -X POST https://api.example.com/users \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{"name": "New User", "email": "user@example.com"}'""",
        language="bash"
    ))
    
    note.add(endpoints)
    
    note.add(Subheading("Error Codes"))
    note.add(Text("• 400 - Bad Request\n• 401 - Unauthorized\n• 404 - Not Found\n• 500 - Server Error"))
    
    print(note.render())
    return note


def main():
    """Run all examples"""
    examples = [
        example_1_simple_note,
        example_2_nested_sections,
        example_3_technical_documentation,
        example_4_study_notes,
        example_5_api_documentation
    ]
    
    print("\n" + "=" * 60)
    print("Running All Examples")
    print("=" * 60 + "\n")
    
    for i, example_func in enumerate(examples, 1):
        note = example_func()
        filename = f"example_{i}_{example_func.__name__}.md"
        note.save_to_file(filename)
        print(f"\n✓ Saved to {filename}\n")
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
