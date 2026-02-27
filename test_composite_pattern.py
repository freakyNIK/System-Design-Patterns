"""
Unit tests for the Composite Pattern note-taking system
"""

from composite_pattern_notes import (
    Note, Heading, Subheading, Text, CodeBlock, Diagram, Section
)


def test_heading():
    """Test Heading component"""
    h = Heading("Test Heading")
    assert "# Test Heading" in h.render()
    assert h.get_text_content() == "Test Heading"
    print("✓ Heading test passed")


def test_subheading():
    """Test Subheading component with different levels"""
    h2 = Subheading("Level 2", level=2)
    assert "## Level 2" in h2.render()
    
    h3 = Subheading("Level 3", level=3)
    assert "### Level 3" in h3.render()
    
    h6 = Subheading("Level 6", level=6)
    assert "######" in h6.render()
    print("✓ Subheading test passed")


def test_text():
    """Test Text component"""
    t = Text("Sample text content")
    assert "Sample text content" in t.render()
    assert t.get_text_content() == "Sample text content"
    
    # Test multiline
    mt = Text("Line 1\nLine 2\nLine 3")
    rendered = mt.render()
    assert "Line 1" in rendered and "Line 2" in rendered
    print("✓ Text test passed")


def test_code_block():
    """Test CodeBlock component"""
    code = CodeBlock("print('hello')", language="python")
    rendered = code.render()
    assert "```python" in rendered
    assert "print('hello')" in rendered
    assert "```" in rendered
    print("✓ CodeBlock test passed")


def test_diagram():
    """Test Diagram component"""
    diag = Diagram("A --> B", diagram_type="flowchart")
    rendered = diag.render()
    assert "[Diagram: flowchart]" in rendered
    assert "A --> B" in rendered
    assert "[End Diagram]" in rendered
    print("✓ Diagram test passed")


def test_section():
    """Test Section composite component"""
    section = Section("My Section")
    section.add(Text("Content 1"))
    section.add(Text("Content 2"))
    
    rendered = section.render()
    assert "## My Section" in rendered
    assert "Content 1" in rendered
    assert "Content 2" in rendered
    
    # Test chaining
    section2 = Section().add(Text("Item 1")).add(Text("Item 2"))
    assert len(section2.components) == 2
    print("✓ Section test passed")


def test_note():
    """Test Note top-level composite"""
    note = Note("Test Note")
    note.set_metadata("author", "Test Author")
    note.add(Heading("Introduction"))
    note.add(Text("Some text"))
    
    rendered = note.render()
    assert "# Test Note" in rendered
    assert "author: Test Author" in rendered
    assert "# Introduction" in rendered
    assert "Some text" in rendered
    
    # Test chaining
    note2 = Note("Chain Test").add(Text("Test")).set_metadata("key", "value")
    assert len(note2.components) == 1
    assert "key" in note2.metadata
    print("✓ Note test passed")


def test_nested_structure():
    """Test complex nested structure"""
    note = Note("Complex Note")
    
    section1 = Section("Section 1")
    section1.add(Text("Text in section 1"))
    section1.add(CodeBlock("code", "python"))
    
    section2 = Section("Section 2")
    section2.add(Subheading("Subsection", level=3))
    section2.add(Diagram("diagram content", "ascii"))
    
    note.add(section1)
    note.add(section2)
    
    rendered = note.render()
    assert "# Complex Note" in rendered
    assert "## Section 1" in rendered
    assert "## Section 2" in rendered
    assert "Text in section 1" in rendered
    assert "### Subsection" in rendered
    print("✓ Nested structure test passed")


def test_save_to_file():
    """Test saving note to file"""
    import os
    import tempfile
    
    note = Note("File Test")
    note.add(Text("Content"))
    
    # Use temp directory
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        temp_file = f.name
    
    try:
        note.save_to_file(temp_file)
        assert os.path.exists(temp_file)
        
        with open(temp_file, 'r') as f:
            content = f.read()
            assert "# File Test" in content
            assert "Content" in content
        print("✓ Save to file test passed")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)


def test_empty_components():
    """Test empty or minimal components"""
    # Empty section
    section = Section()
    rendered = section.render()
    assert rendered == ""
    
    # Empty note
    note = Note("Empty")
    rendered = note.render()
    assert "# Empty" in rendered
    print("✓ Empty components test passed")


def test_get_text_content():
    """Test extracting plain text from components"""
    note = Note("Test")
    note.add(Text("Hello"))
    note.add(CodeBlock("code", "python"))
    note.add(Text("World"))
    
    text = note.get_text_content()
    assert "Test" in text
    assert "Hello" in text
    assert "World" in text
    print("✓ Get text content test passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("Running Unit Tests")
    print("=" * 60 + "\n")
    
    tests = [
        test_heading,
        test_subheading,
        test_text,
        test_code_block,
        test_diagram,
        test_section,
        test_note,
        test_nested_structure,
        test_save_to_file,
        test_empty_components,
        test_get_text_content,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
