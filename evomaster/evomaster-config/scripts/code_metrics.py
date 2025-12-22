"""
Comprehensive Java Test Code Quality Metrics Analyzer
Analyzes Java test files without requiring compilation.

Usage: python3 code_metrics.py <JavaFile.java> [--json] [--html]
"""

import re
import sys
import json
import math
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Optional
from collections import Counter

# =============================================================================
# FRAMEWORK DEFINITIONS (JUnit 5 + Spring Boot Test)
# =============================================================================

JUNIT5_ANNOTATIONS = {
    '@Test', '@BeforeEach', '@AfterEach', '@BeforeAll', '@AfterAll',
    '@DisplayName', '@Nested', '@Disabled', '@ParameterizedTest',
    '@RepeatedTest', '@TestFactory', '@TestTemplate', '@Timeout'
}

SPRING_TEST_ANNOTATIONS = {
    '@SpringBootTest', '@WebMvcTest', '@DataJpaTest', '@AutoConfigureMockMvc',
    '@MockBean', '@SpyBean', '@ActiveProfiles', '@TestConfiguration',
    '@WithMockUser', '@WithAnonymousUser'
}

VALID_ASSERT_METHODS = {
    # JUnit 5
    'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
    'assertNull', 'assertNotNull', 'assertThrows', 'assertDoesNotThrow',
    'assertAll', 'assertArrayEquals', 'assertIterableEquals',
    'assertLinesMatch', 'assertTimeout', 'assertTimeoutPreemptively',
    'fail',
    # Spring MockMvc
    'andExpect', 'andDo', 'andReturn',
    # Hamcrest
    'assertThat',
    # AssertJ
    'assertThat', 'isEqualTo', 'isNotNull', 'isNull', 'isTrue', 'isFalse',
    'hasSize', 'contains', 'containsExactly'
}

MOCKMVC_METHODS = {
    'perform', 'get', 'post', 'put', 'delete', 'patch',
    'andExpect', 'andDo', 'andReturn',
    'status', 'content', 'jsonPath', 'header'
}

SPRING_BEANS = {'mockMvc', 'MockMvc', 'WebTestClient', 'TestRestTemplate'}

JAVA_RESERVED_WORDS = {
    'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
    'char', 'class', 'const', 'continue', 'default', 'do', 'double',
    'else', 'enum', 'extends', 'final', 'finally', 'float', 'for',
    'goto', 'if', 'implements', 'import', 'instanceof', 'int',
    'interface', 'long', 'native', 'new', 'package', 'private',
    'protected', 'public', 'return', 'short', 'static', 'strictfp',
    'super', 'switch', 'synchronized', 'this', 'throw', 'throws',
    'transient', 'try', 'void', 'volatile', 'while', 'var'
}

# =============================================================================
# DATA CLASSES FOR METRICS
# =============================================================================

@dataclass
class SizeMetrics:
    total_lines: int = 0
    logical_loc: int = 0
    blank_lines: int = 0
    comment_lines: int = 0
    comment_ratio: float = 0.0

@dataclass
class ComplexityMetrics:
    cyclomatic_complexity: Dict[str, int] = field(default_factory=dict)
    avg_cyclomatic: float = 0.0
    max_cyclomatic: int = 0
    cognitive_complexity: Dict[str, int] = field(default_factory=dict)
    avg_cognitive: float = 0.0
    max_cognitive: int = 0
    maintainability_index: float = 0.0

@dataclass
class TestMetrics:
    test_method_count: int = 0
    nested_class_count: int = 0
    assert_count: int = 0
    asserts_per_test: float = 0.0
    long_tests: List[str] = field(default_factory=list)
    long_test_count: int = 0
    aaa_organized_count: int = 0
    aaa_percentage: float = 0.0
    tests_with_exception_handling: int = 0
    exception_handling_percentage: float = 0.0
    exception_handling_needed: bool = False

@dataclass
class DuplicationMetrics:
    duplicate_segments: int = 0
    duplicate_lines: int = 0
    duplicate_percentage: float = 0.0
    duplicated_blocks: List[str] = field(default_factory=list)

@dataclass
class CodeSmellMetrics:
    code_smell_count: int = 0
    code_smells: List[Dict] = field(default_factory=list)
    todo_fixme_count: int = 0
    wildcard_imports: int = 0
    dead_code_percentage: float = 0.0
    dead_code_items: List[str] = field(default_factory=list)

@dataclass
class ConventionMetrics:
    follows_conventions: bool = True
    convention_violations: List[Dict] = field(default_factory=list)
    violation_count: int = 0

@dataclass
class FrameworkMetrics:
    framework_keyword_violations: int = 0
    invalid_assertions: List[str] = field(default_factory=list)
    non_framework_methods: List[str] = field(default_factory=list)
    valid_framework_assertions: bool = True

@dataclass
class TypeMetrics:
    type_errors: int = 0
    undefined_variables: List[str] = field(default_factory=list)
    type_annotation_errors: int = 0
    generic_type_misuses: List[str] = field(default_factory=list)

@dataclass
class SyntaxMetrics:
    syntax_errors: int = 0
    syntax_error_details: List[Dict] = field(default_factory=list)
    linting_violations: int = 0
    linting_details: List[Dict] = field(default_factory=list)

@dataclass
class DesignPatternMetrics:
    adheres_to_patterns: bool = True
    patterns_detected: List[str] = field(default_factory=list)
    pattern_violations: List[str] = field(default_factory=list)

@dataclass
class AllMetrics:
    file_name: str = ""
    size: SizeMetrics = field(default_factory=SizeMetrics)
    complexity: ComplexityMetrics = field(default_factory=ComplexityMetrics)
    test: TestMetrics = field(default_factory=TestMetrics)
    duplication: DuplicationMetrics = field(default_factory=DuplicationMetrics)
    code_smells: CodeSmellMetrics = field(default_factory=CodeSmellMetrics)
    conventions: ConventionMetrics = field(default_factory=ConventionMetrics)
    framework: FrameworkMetrics = field(default_factory=FrameworkMetrics)
    types: TypeMetrics = field(default_factory=TypeMetrics)
    syntax: SyntaxMetrics = field(default_factory=SyntaxMetrics)
    design_patterns: DesignPatternMetrics = field(default_factory=DesignPatternMetrics)

# =============================================================================
# ANALYZER CLASS
# =============================================================================

class JavaTestAnalyzer:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()
        self.lines = self.content.split('\n')
        self.metrics = AllMetrics(file_name=self.filepath.name)
        self.methods = self._extract_methods()
        self.test_methods = self._extract_test_methods()
        
    def analyze(self) -> AllMetrics:
        """Run all analyses and return metrics."""
        self._analyze_size()
        self._analyze_complexity()
        self._analyze_tests()
        self._analyze_duplication()
        self._analyze_code_smells()
        self._analyze_conventions()
        self._analyze_framework()
        self._analyze_types()
        self._analyze_syntax()
        self._analyze_design_patterns()
        return self.metrics
    
    # -------------------------------------------------------------------------
    # SIZE METRICS
    # -------------------------------------------------------------------------
    def _analyze_size(self):
        m = self.metrics.size
        m.total_lines = len(self.lines)
        m.blank_lines = sum(1 for l in self.lines if not l.strip())
        m.comment_lines = sum(1 for l in self.lines if self._is_comment_line(l))
        m.logical_loc = m.total_lines - m.blank_lines - m.comment_lines
        m.comment_ratio = round(m.comment_lines / m.total_lines * 100, 1) if m.total_lines > 0 else 0
    
    def _is_comment_line(self, line: str) -> bool:
        stripped = line.strip()
        return (stripped.startswith('//') or 
                stripped.startswith('/*') or 
                stripped.startswith('*') or
                stripped.startswith('*/'))
    
    # -------------------------------------------------------------------------
    # COMPLEXITY METRICS
    # -------------------------------------------------------------------------
    def _analyze_complexity(self):
        m = self.metrics.complexity
        
        for name, body in self.methods.items():
            cc = self._calc_cyclomatic(body)
            cog = self._calc_cognitive(body)
            m.cyclomatic_complexity[name] = cc
            m.cognitive_complexity[name] = cog
        
        if m.cyclomatic_complexity:
            values = list(m.cyclomatic_complexity.values())
            m.avg_cyclomatic = round(sum(values) / len(values), 1)
            m.max_cyclomatic = max(values)
        
        if m.cognitive_complexity:
            values = list(m.cognitive_complexity.values())
            m.avg_cognitive = round(sum(values) / len(values), 1)
            m.max_cognitive = max(values)
        
        # Maintainability Index: MI = 171 - 5.2*ln(V) - 0.23*G - 16.2*ln(LOC)
        loc = max(self.metrics.size.logical_loc, 1)
        avg_cc = max(m.avg_cyclomatic, 1)
        halstead_volume = loc * math.log2(max(len(set(self.content.split())), 1))
        mi = 171 - 5.2 * math.log(halstead_volume) - 0.23 * avg_cc - 16.2 * math.log(loc)
        m.maintainability_index = round(max(0, min(100, mi * 100 / 171)), 1)
    
    def _calc_cyclomatic(self, code: str) -> int:
        """CC = E - N + 2P, simplified: 1 + decision points"""
        patterns = [
            r'\bif\b', r'\belse\s+if\b', r'\bfor\b', r'\bwhile\b',
            r'\bcase\b', r'\bcatch\b', r'\b\?\s*:', r'\b&&\b', r'\b\|\|\b'
        ]
        count = 1
        for p in patterns:
            count += len(re.findall(p, code))
        return count
    
    def _calc_cognitive(self, code: str) -> int:
        """Cognitive complexity: nesting increases weight"""
        score = 0
        nesting = 0
        for line in code.split('\n'):
            stripped = line.strip()
            # Nesting increasers
            if re.search(r'\b(if|for|while|switch|try)\b', stripped):
                score += 1 + nesting
                if '{' in stripped:
                    nesting += 1
            elif re.search(r'\b(else|catch|finally)\b', stripped):
                score += 1
            # Nesting decreasers
            if stripped == '}':
                nesting = max(0, nesting - 1)
            # Boolean operators
            score += len(re.findall(r'&&|\|\|', stripped))
        return score
    
    # -------------------------------------------------------------------------
    # TEST METRICS
    # -------------------------------------------------------------------------
    def _analyze_tests(self):
        m = self.metrics.test
        m.test_method_count = len(self.test_methods)
        m.nested_class_count = len(re.findall(r'@Nested', self.content))
        m.assert_count = self._count_assertions()
        m.asserts_per_test = round(m.assert_count / max(m.test_method_count, 1), 1)
        
        # Long tests (>20 lines)
        for name, body in self.test_methods.items():
            line_count = len([l for l in body.split('\n') if l.strip()])
            if line_count > 20:
                m.long_tests.append(f"{name} ({line_count} lines)")
        m.long_test_count = len(m.long_tests)
        
        # AAA pattern detection
        m.aaa_organized_count = self._count_aaa_organized()
        m.aaa_percentage = round(m.aaa_organized_count / max(m.test_method_count, 1) * 100, 1)
        
        # Exception handling in tests
        for name, body in self.test_methods.items():
            if re.search(r'throws\s+\w+|try\s*\{|assertThrows', body):
                m.tests_with_exception_handling += 1
        m.exception_handling_percentage = round(
            m.tests_with_exception_handling / max(m.test_method_count, 1) * 100, 1
        )
        
        # Is exception handling needed?
        m.exception_handling_needed = bool(re.search(
            r'\.perform\(|mockMvc|WebTestClient|RestTemplate|throws\s+Exception',
            self.content
        ))
    
    def _count_assertions(self) -> int:
        patterns = [
            r'assert\w+\s*\(',
            r'\.andExpect\s*\(',
            r'assertThat\s*\(',
            r'verify\s*\(',
            r'\.is\w+\s*\('
        ]
        count = 0
        for p in patterns:
            count += len(re.findall(p, self.content))
        return count
    
    def _count_aaa_organized(self) -> int:
        """Check for AAA (Arrange/Act/Assert) or GWT (Given/When/Then) organization"""
        count = 0
        for name, body in self.test_methods.items():
            # Check for explicit comments
            has_aaa = bool(re.search(r'//\s*(arrange|act|assert|given|when|then)', body, re.I))
            # Check for structural pattern: setup, action, verification
            has_structure = (
                re.search(r'(=\s*new\s+|@Autowired|mock\()', body) and  # Arrange
                re.search(r'\.(perform|execute|call|invoke|get|post|put)', body) and  # Act
                re.search(r'(assert|verify|andExpect)', body)  # Assert
            )
            if has_aaa or has_structure:
                count += 1
        return count
    
    # -------------------------------------------------------------------------
    # DUPLICATION METRICS
    # -------------------------------------------------------------------------
    def _analyze_duplication(self):
        m = self.metrics.duplication
        
        # Extract meaningful lines (>15 chars, non-trivial)
        meaningful_lines = []
        for i, line in enumerate(self.lines):
            stripped = line.strip()
            if (len(stripped) > 15 and 
                not self._is_comment_line(line) and
                not stripped.startswith('import') and
                not stripped.startswith('package') and
                stripped not in {'{', '}', '});', ''}):
                meaningful_lines.append((i + 1, stripped))
        
        # Find duplicates
        line_counts = Counter(l[1] for l in meaningful_lines)
        duplicates = {line: count for line, count in line_counts.items() if count > 1}
        
        m.duplicate_lines = sum(count - 1 for count in duplicates.values())
        m.duplicate_segments = len(duplicates)
        m.duplicate_percentage = round(
            m.duplicate_lines / max(len(meaningful_lines), 1) * 100, 1
        )
        m.duplicated_blocks = list(duplicates.keys())[:5]  # Top 5
    
    # -------------------------------------------------------------------------
    # CODE SMELL METRICS
    # -------------------------------------------------------------------------
    def _analyze_code_smells(self):
        m = self.metrics.code_smells
        smells = []
        
        # Long methods
        for name, body in self.methods.items():
            lines = len([l for l in body.split('\n') if l.strip()])
            if lines > 30:
                smells.append({'type': 'Long Method', 'location': name, 'detail': f'{lines} lines'})
        
        # Too many parameters
        for match in re.finditer(r'(\w+)\s*\([^)]{100,}\)', self.content):
            smells.append({'type': 'Too Many Parameters', 'location': match.group(1)})
        
        # Magic numbers
        for match in re.finditer(r'[^0-9\.]([2-9]\d{2,}|[1-9]\d{3,})[^0-9\.]', self.content):
            if not re.search(r'(port|year|status|code)', self.content[max(0, match.start()-20):match.start()], re.I):
                smells.append({'type': 'Magic Number', 'detail': match.group(1)})
        
        # Deep nesting
        max_nesting = 0
        current_nesting = 0
        for line in self.lines:
            current_nesting += line.count('{') - line.count('}')
            max_nesting = max(max_nesting, current_nesting)
        if max_nesting > 4:
            smells.append({'type': 'Deep Nesting', 'detail': f'Max depth: {max_nesting}'})
        
        # TODO/FIXME
        m.todo_fixme_count = len(re.findall(r'\b(TODO|FIXME|HACK|XXX)\b', self.content))
        
        # Wildcard imports
        m.wildcard_imports = len(re.findall(r'^import\s+[\w.]+\.\*;', self.content, re.MULTILINE))
        if m.wildcard_imports > 0:
            smells.append({'type': 'Wildcard Import', 'count': m.wildcard_imports})
        
        # Dead code detection (unused private methods/variables)
        dead_items = self._detect_dead_code()
        m.dead_code_items = dead_items
        m.dead_code_percentage = round(len(dead_items) / max(len(self.methods), 1) * 100, 1)
        
        m.code_smells = smells
        m.code_smell_count = len(smells)
    
    def _detect_dead_code(self) -> List[str]:
        """Detect potentially unused private methods and variables"""
        dead = []
        
        # Find private methods
        private_methods = re.findall(r'private\s+\w+\s+(\w+)\s*\(', self.content)
        for method in private_methods:
            # Check if called elsewhere (excluding definition)
            calls = len(re.findall(rf'\b{method}\s*\(', self.content))
            if calls <= 1:  # Only the definition
                dead.append(f"Unused method: {method}")
        
        # Find private fields
        private_fields = re.findall(r'private\s+(?:final\s+)?[\w<>,\s]+\s+(\w+)\s*[;=]', self.content)
        for field in private_fields:
            uses = len(re.findall(rf'\b{field}\b', self.content))
            if uses <= 1:
                dead.append(f"Unused field: {field}")
        
        return dead
    
    # -------------------------------------------------------------------------
    # CONVENTION METRICS
    # -------------------------------------------------------------------------
    def _analyze_conventions(self):
        m = self.metrics.conventions
        violations = []
        
        # Class name should be PascalCase
        class_names = re.findall(r'class\s+(\w+)', self.content)
        for name in class_names:
            if not re.match(r'^[A-Z][a-zA-Z0-9]*$', name):
                violations.append({'rule': 'Class naming', 'detail': f'{name} should be PascalCase'})
        
        # Method names should be camelCase
        method_names = re.findall(r'(?:public|private|protected)\s+\w+\s+(\w+)\s*\(', self.content)
        for name in method_names:
            if not re.match(r'^[a-z][a-zA-Z0-9]*$', name) and name not in {'main'}:
                violations.append({'rule': 'Method naming', 'detail': f'{name} should be camelCase'})
        
        # Constants should be UPPER_SNAKE_CASE
        constants = re.findall(r'static\s+final\s+\w+\s+(\w+)\s*=', self.content)
        for name in constants:
            if not re.match(r'^[A-Z][A-Z0-9_]*$', name):
                violations.append({'rule': 'Constant naming', 'detail': f'{name} should be UPPER_SNAKE_CASE'})
        
        # Line length > 120
        for i, line in enumerate(self.lines):
            if len(line) > 120:
                violations.append({'rule': 'Line length', 'line': i + 1, 'length': len(line)})
        
        # Missing @DisplayName on test methods
        for name in self.test_methods.keys():
            # Check if @DisplayName precedes @Test
            pattern = rf'@DisplayName\s*\([^)]+\)\s*\n\s*@Test|@Test\s*\n\s*@DisplayName'
            if name not in str(re.findall(pattern, self.content)):
                # Simplified check
                pass
        
        m.convention_violations = violations
        m.violation_count = len(violations)
        m.follows_conventions = len(violations) == 0
    
    # -------------------------------------------------------------------------
    # FRAMEWORK METRICS
    # -------------------------------------------------------------------------
    def _analyze_framework(self):
        m = self.metrics.framework
        
        # Check for valid JUnit/Spring annotations
        used_annotations = set(re.findall(r'@(\w+)', self.content))
        valid_annotations = {a.replace('@', '') for a in JUNIT5_ANNOTATIONS | SPRING_TEST_ANNOTATIONS}
        
        # Framework keyword violations
        violations = 0
        for annotation in used_annotations:
            if annotation.startswith(('Test', 'Before', 'After', 'Mock', 'Spring')):
                if annotation not in valid_annotations and f'@{annotation}' not in JUNIT5_ANNOTATIONS | SPRING_TEST_ANNOTATIONS:
                    violations += 1
        m.framework_keyword_violations = violations
        
        # Invalid assertions
        assert_calls = re.findall(r'(assert\w+|verify\w*)\s*\(', self.content)
        for call in assert_calls:
            if call not in VALID_ASSERT_METHODS and not call.startswith('assert'):
                m.invalid_assertions.append(call)
        
        # Non-framework test methods (methods in test class without @Test)
        all_methods = set(self.methods.keys())
        test_methods = set(self.test_methods.keys())
        lifecycle_pattern = re.compile(r'@(BeforeEach|AfterEach|BeforeAll|AfterAll)')
        
        for name in all_methods - test_methods:
            method_context = self._get_method_context(name)
            if not lifecycle_pattern.search(method_context):
                if not name.startswith(('get', 'set', 'is', 'has', 'setup', 'teardown', 'init', 'create', 'build', 'mock')):
                    m.non_framework_methods.append(name)
        
        m.valid_framework_assertions = len(m.invalid_assertions) == 0
    
    def _get_method_context(self, method_name: str) -> str:
        """Get the lines around a method definition"""
        pattern = rf'(\w+\s+)+{method_name}\s*\('
        match = re.search(pattern, self.content)
        if match:
            start = max(0, match.start() - 100)
            return self.content[start:match.end()]
        return ""
    
    # -------------------------------------------------------------------------
    # TYPE METRICS
    # -------------------------------------------------------------------------
    def _analyze_types(self):
        m = self.metrics.types
        
        # Undefined variables (basic check - variables used before declaration)
        declared_vars = set(re.findall(r'(?:int|String|boolean|long|double|float|var|final)\s+(\w+)\s*[;=]', self.content))
        declared_vars.update(re.findall(r'@\w+\s*(?:\([^)]*\))?\s*\n\s*(?:private|public|protected)?\s*\w+\s+(\w+)\s*;', self.content))
        
        # Add common framework injected fields
        declared_vars.update(['mockMvc', 'webTestClient', 'restTemplate'])
        
        # Find potential undefined (simplified - won't catch all)
        used_vars = set(re.findall(r'\b([a-z]\w*)\s*[.\(]', self.content))
        for var in used_vars:
            if var not in declared_vars and var not in JAVA_RESERVED_WORDS and len(var) > 2:
                # Check if it's a method call on known object
                if not re.search(rf'\w+\.{var}\s*\(', self.content):
                    if var not in {'status', 'content', 'put', 'get', 'post', 'delete', 'jsonPath'}:
                        pass  # Simplified - would need full parsing for accuracy
        
        # Generic type misuse
        raw_types = re.findall(r'\b(List|Map|Set|Collection|Optional)\s+\w+\s*[;=]', self.content)
        for raw in raw_types:
            m.generic_type_misuses.append(f"Raw type usage: {raw}")
        
        # Type annotation errors (basic)
        m.type_annotation_errors = len(re.findall(r'@\w+\s*\(\s*\)', self.content))  # Empty annotations
        m.type_errors = len(m.generic_type_misuses) + m.type_annotation_errors
    
    # -------------------------------------------------------------------------
    # SYNTAX METRICS
    # -------------------------------------------------------------------------
    def _analyze_syntax(self):
        m = self.metrics.syntax
        errors = []
        linting = []
        
        # Unbalanced braces
        open_braces = self.content.count('{')
        close_braces = self.content.count('}')
        if open_braces != close_braces:
            errors.append({'type': 'Unbalanced braces', 'open': open_braces, 'close': close_braces})
        
        # Unbalanced parentheses
        open_parens = self.content.count('(')
        close_parens = self.content.count(')')
        if open_parens != close_parens:
            errors.append({'type': 'Unbalanced parentheses', 'open': open_parens, 'close': close_parens})
        
        # Missing semicolons (simplified check)
        for i, line in enumerate(self.lines):
            stripped = line.strip()
            if (stripped and 
                not stripped.endswith(('{', '}', '(', ')', ',', ';', '*/', '//')) and
                not stripped.startswith(('@', '//', '/*', '*', 'import', 'package', 'public class', 'class')) and
                not re.match(r'^(public|private|protected|if|else|for|while|try|catch|finally|switch)', stripped)):
                if re.match(r'^\w+\s+\w+\s*=\s*.+[^;]$', stripped):
                    errors.append({'type': 'Possible missing semicolon', 'line': i + 1})
        
        # Linting: trailing whitespace
        for i, line in enumerate(self.lines):
            if line.endswith(' ') or line.endswith('\t'):
                linting.append({'type': 'Trailing whitespace', 'line': i + 1})
        
        # Linting: multiple empty lines
        prev_empty = False
        for i, line in enumerate(self.lines):
            is_empty = not line.strip()
            if is_empty and prev_empty:
                linting.append({'type': 'Multiple consecutive empty lines', 'line': i + 1})
            prev_empty = is_empty
        
        # Linting: space after keywords
        for i, line in enumerate(self.lines):
            if re.search(r'\b(if|for|while|switch|catch)\(', line):
                linting.append({'type': 'Missing space after keyword', 'line': i + 1})
        
        m.syntax_errors = len(errors)
        m.syntax_error_details = errors
        m.linting_violations = len(linting)
        m.linting_details = linting[:20]  # Limit to first 20
    
    # -------------------------------------------------------------------------
    # DESIGN PATTERN METRICS
    # -------------------------------------------------------------------------
    def _analyze_design_patterns(self):
        m = self.metrics.design_patterns
        patterns = []
        violations = []
        
        # Builder pattern
        if re.search(r'\.builder\(\)|Builder\s+\w+\s*=', self.content):
            patterns.append('Builder')
        
        # Factory pattern
        if re.search(r'Factory|create\w+\(\)', self.content):
            patterns.append('Factory')
        
        # Singleton (in test helper)
        if re.search(r'getInstance\(\)|private\s+static\s+final\s+\w+\s+INSTANCE', self.content):
            patterns.append('Singleton')
        
        # Test patterns
        # AAA pattern
        if self.metrics.test.aaa_percentage > 50:
            patterns.append('AAA (Arrange-Act-Assert)')
        
        # Page Object pattern (for UI tests)
        if re.search(r'Page\s*{|PageObject|@FindBy', self.content):
            patterns.append('Page Object')
        
        # Test Data Builder
        if re.search(r'TestDataBuilder|with\w+\([^)]+\)\.build\(\)', self.content):
            patterns.append('Test Data Builder')
        
        # Nested test classes (organizational pattern)
        if self.metrics.test.nested_class_count > 0:
            patterns.append('Nested Test Classes')
        
        # Violations
        # God class (too many methods)
        if len(self.methods) > 20:
            violations.append(f'Possible God Class: {len(self.methods)} methods')
        
        # Test class without proper structure
        if self.metrics.test.nested_class_count == 0 and self.metrics.test.test_method_count > 10:
            violations.append('Consider organizing tests into @Nested classes')
        
        # Mixed concerns
        if re.search(r'@Service|@Repository|@Controller', self.content):
            violations.append('Production annotations in test class')
        
        m.patterns_detected = patterns
        m.pattern_violations = violations
        m.adheres_to_patterns = len(violations) == 0
    
    # -------------------------------------------------------------------------
    # HELPER METHODS
    # -------------------------------------------------------------------------
    def _extract_methods(self) -> Dict[str, str]:
        """Extract all methods with their bodies"""
        methods = {}
        pattern = r'(?:@\w+(?:\([^)]*\))?\s*)*(?:public|private|protected)?\s*(?:static\s+)?(?:final\s+)?[\w<>,\[\]\s]+\s+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{'
        
        for match in re.finditer(pattern, self.content):
            name = match.group(1)
            start = match.end() - 1
            body = self._extract_block(start)
            methods[name] = body
        
        return methods
    
    def _extract_test_methods(self) -> Dict[str, str]:
        """Extract only @Test annotated methods"""
        test_methods = {}
        pattern = r'@Test\s*(?:\([^)]*\))?\s*(?:@\w+(?:\([^)]*\))?\s*)*(?:public|private|protected)?\s*(?:void\s+)?(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{'
        
        for match in re.finditer(pattern, self.content):
            name = match.group(1)
            start = match.end() - 1
            body = self._extract_block(start)
            test_methods[name] = body
        
        return test_methods
    
    def _extract_block(self, start_brace: int) -> str:
        """Extract code block starting from opening brace"""
        depth = 0
        end = start_brace
        
        for i in range(start_brace, len(self.content)):
            if self.content[i] == '{':
                depth += 1
            elif self.content[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        
        return self.content[start_brace:end]

# =============================================================================
# OUTPUT FORMATTERS
# =============================================================================

def print_metrics(metrics: AllMetrics):
    """Print metrics in a formatted console output"""
    
    print(f"\n{'='*70}")
    print(f"  JAVA TEST CODE QUALITY METRICS REPORT")
    print(f"  File: {metrics.file_name}")
    print(f"{'='*70}")
    
    # Size Metrics
    s = metrics.size
    print(f"\nSIZE METRICS")
    print(f"   {'Logical LOC:':<35} {s.logical_loc}")
    print(f"   {'Total Lines:':<35} {s.total_lines}")
    print(f"   {'Blank Lines:':<35} {s.blank_lines}")
    print(f"   {'Comment Lines:':<35} {s.comment_lines}")
    print(f"   {'Comment Ratio:':<35} {s.comment_ratio}%")
    
    # Complexity Metrics
    c = metrics.complexity
    print(f"\nCOMPLEXITY METRICS")
    print(f"   {'Avg Cyclomatic Complexity:':<35} {c.avg_cyclomatic}")
    print(f"   {'Max Cyclomatic Complexity:':<35} {c.max_cyclomatic}")
    print(f"   {'Avg Cognitive Complexity:':<35} {c.avg_cognitive}")
    print(f"   {'Max Cognitive Complexity:':<35} {c.max_cognitive}")
    print(f"   {'Maintainability Index:':<35} {c.maintainability_index}/100")
    
    # Test Metrics
    t = metrics.test
    print(f"\nTEST METRICS")
    print(f"   {'Test Method Count:':<35} {t.test_method_count}")
    print(f"   {'Nested Test Classes:':<35} {t.nested_class_count}")
    print(f"   {'Assert Statements:':<35} {t.assert_count}")
    print(f"   {'Asserts Per Test:':<35} {t.asserts_per_test}")
    print(f"   {'Long Tests (>20 lines):':<35} {t.long_test_count}")
    if t.long_tests:
        for lt in t.long_tests[:3]:
            print(f"      - {lt}")
    print(f"   {'AAA Organized Tests:':<35} {t.aaa_organized_count} ({t.aaa_percentage}%)")
    print(f"   {'Tests with Exception Handling:':<35} {t.tests_with_exception_handling} ({t.exception_handling_percentage}%)")
    print(f"   {'Exception Handling Needed:':<35} {'Yes' if t.exception_handling_needed else 'No'}")
    
    # Duplication Metrics
    d = metrics.duplication
    print(f"\nDUPLICATION METRICS")
    print(f"   {'Duplicate Code Segments:':<35} {d.duplicate_segments}")
    print(f"   {'Duplicate Lines:':<35} {d.duplicate_lines}")
    print(f"   {'Duplication Percentage:':<35} {d.duplicate_percentage}%")
    
    # Code Smell Metrics
    cs = metrics.code_smells
    print(f"\nCODE SMELL METRICS")
    print(f"   {'Code Smell Count:':<35} {cs.code_smell_count}")
    print(f"   {'TODO/FIXME Count:':<35} {cs.todo_fixme_count}")
    print(f"   {'Wildcard Imports:':<35} {cs.wildcard_imports}")
    print(f"   {'Dead Code Percentage:':<35} {cs.dead_code_percentage}%")
    if cs.code_smells:
        print(f"   Detected Smells:")
        for smell in cs.code_smells[:5]:
            print(f"      - {smell.get('type')}: {smell.get('detail', smell.get('location', ''))}")
    
    # Convention Metrics
    cv = metrics.conventions
    print(f"\nCONVENTION METRICS")
    print(f"   {'Follows Conventions:':<35} {'Yes' if cv.follows_conventions else 'No'}")
    print(f"   {'Violation Count:':<35} {cv.violation_count}")
    if cv.convention_violations:
        print(f"   Violations:")
        for v in cv.convention_violations[:5]:
            line_info = f"Line {v.get('line', '?')}"
            detail = v.get('detail', line_info)
            print(f"      - {v.get('rule')}: {detail}")
    
    # Framework Metrics
    f = metrics.framework
    print(f"\nFRAMEWORK METRICS")
    print(f"   {'Framework Keyword Violations:':<35} {f.framework_keyword_violations}")
    print(f"   {'Invalid Assertions:':<35} {len(f.invalid_assertions)}")
    print(f"   {'Non-Framework Methods:':<35} {len(f.non_framework_methods)}")
    print(f"   {'Valid Framework Assertions:':<35} {'Yes' if f.valid_framework_assertions else 'No'}")
    if f.non_framework_methods:
        print(f"   Non-framework methods:")
        for m in f.non_framework_methods[:5]:
            print(f"      - {m}")
    
    # Type Metrics
    ty = metrics.types
    print(f"\nTYPE METRICS")
    print(f"   {'Type Errors:':<35} {ty.type_errors}")
    print(f"   {'Undefined Variables:':<35} {len(ty.undefined_variables)}")
    print(f"   {'Type Annotation Errors:':<35} {ty.type_annotation_errors}")
    print(f"   {'Generic Type Misuses:':<35} {len(ty.generic_type_misuses)}")
    if ty.generic_type_misuses:
        for g in ty.generic_type_misuses[:3]:
            print(f"      - {g}")
    
    # Syntax Metrics
    sx = metrics.syntax
    print(f"\nSYNTAX METRICS")
    print(f"   {'Syntax Errors:':<35} {sx.syntax_errors}")
    print(f"   {'Linting Violations:':<35} {sx.linting_violations}")
    if sx.syntax_error_details:
        print(f"   Syntax errors:")
        for e in sx.syntax_error_details:
            print(f"      - {e.get('type')}")
    
    # Design Pattern Metrics
    dp = metrics.design_patterns
    print(f"\nDESIGN PATTERN METRICS")
    print(f"   {'Adheres to Patterns:':<35} {'Yes' if dp.adheres_to_patterns else 'No'}")
    print(f"   {'Patterns Detected:':<35} {', '.join(dp.patterns_detected) if dp.patterns_detected else 'None'}")
    if dp.pattern_violations:
        print(f"   Pattern Violations:")
        for v in dp.pattern_violations:
            print(f"      - {v}")
    
    # Summary
    print(f"\n{'='*70}")
    print(f"  SUMMARY SCORE")
    print(f"{'='*70}")
    
    score = calculate_quality_score(metrics)
    print(f"   {'Overall Quality Score:':<35} {score}/100")
    print_score_bar(score)
    print(f"{'='*70}\n")


def calculate_quality_score(metrics: AllMetrics) -> int:
    """Calculate an overall quality score from 0-100"""
    score = 100
    
    # Deductions
    # Complexity (max -20)
    if metrics.complexity.avg_cyclomatic > 10:
        score -= min(20, (metrics.complexity.avg_cyclomatic - 10) * 2)
    
    # Code smells (max -15)
    score -= min(15, metrics.code_smells.code_smell_count * 3)
    
    # Duplication (max -15)
    score -= min(15, metrics.duplication.duplicate_percentage)
    
    # Convention violations (max -10)
    score -= min(10, metrics.conventions.violation_count)
    
    # Long tests (max -10)
    score -= min(10, metrics.test.long_test_count * 2)
    
    # Low AAA percentage (max -10)
    if metrics.test.aaa_percentage < 50:
        score -= 10
    
    # Syntax errors (max -10)
    score -= min(10, metrics.syntax.syntax_errors * 5)
    
    # Framework violations (max -10)
    score -= min(10, metrics.framework.framework_keyword_violations * 2)
    
    return max(0, min(100, int(score)))


def print_score_bar(score: int):
    """Print a visual score bar"""
    filled = score // 5
    empty = 20 - filled
    
    if score >= 80:
        color = "green"
    elif score >= 60:
        color = "orange"
    else:
        color = "red"
    
    bar = f"   {color} [{'█' * filled}{'░' * empty}] {score}%"
    print(bar)

def to_html(metrics: AllMetrics) -> str:
    """Generate an HTML report"""
    score = calculate_quality_score(metrics)
    
    html = f"""<!DOCTYPE html>
                <html>
                <head>
                    <title>Code Quality Report - {metrics.file_name}</title>
                    <style>
                        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; background: #f5f5f5; }}
                        .container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                        h1 {{ color: #333; border-bottom: 2px solid #4CAF50; padding-bottom: 10px; }}
                        h2 {{ color: #555; margin-top: 30px; }}
                        .metric {{ display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee; }}
                        .metric-name {{ color: #666; }}
                        .metric-value {{ font-weight: bold; color: #333; }}
                        .score {{ font-size: 48px; text-align: center; margin: 20px 0; }}
                        .score.good {{ color: #4CAF50; }}
                        .score.medium {{ color: #FF9800; }}
                        .score.bad {{ color: #f44336; }}
                        .section {{ margin: 20px 0; padding: 15px; background: #fafafa; border-radius: 5px; }}
                        .warning {{ color: #f44336; }}
                        .ok {{ color: #4CAF50; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Code Quality Report</h1>
                        <p><strong>File:</strong> {metrics.file_name}</p>
                        
                        <div class="score {'good' if score >= 80 else 'medium' if score >= 60 else 'bad'}">
                            {score}/100
                        </div>
                        
                        <div class="section">
                            <h2>Size Metrics</h2>
                            <div class="metric"><span class="metric-name">Logical LOC</span><span class="metric-value">{metrics.size.logical_loc}</span></div>
                            <div class="metric"><span class="metric-name">Comment Ratio</span><span class="metric-value">{metrics.size.comment_ratio}%</span></div>
                        </div>
                        
                        <div class="section">
                            <h2>Complexity</h2>
                            <div class="metric"><span class="metric-name">Avg Cyclomatic</span><span class="metric-value">{metrics.complexity.avg_cyclomatic}</span></div>
                            <div class="metric"><span class="metric-name">Avg Cognitive</span><span class="metric-value">{metrics.complexity.avg_cognitive}</span></div>
                            <div class="metric"><span class="metric-name">Maintainability Index</span><span class="metric-value">{metrics.complexity.maintainability_index}/100</span></div>
                        </div>
                        
                        <div class="section">
                            <h2>Test Metrics</h2>
                            <div class="metric"><span class="metric-name">Test Methods</span><span class="metric-value">{metrics.test.test_method_count}</span></div>
                            <div class="metric"><span class="metric-name">Assert Statements</span><span class="metric-value">{metrics.test.assert_count}</span></div>
                            <div class="metric"><span class="metric-name">AAA Organized</span><span class="metric-value">{metrics.test.aaa_percentage}%</span></div>
                            <div class="metric"><span class="metric-name">Long Tests</span><span class="metric-value {'warning' if metrics.test.long_test_count > 0 else 'ok'}">{metrics.test.long_test_count}</span></div>
                        </div>
                        
                        <div class="section">
                            <h2>Code Smells</h2>
                            <div class="metric"><span class="metric-name">Code Smells</span><span class="metric-value">{metrics.code_smells.code_smell_count}</span></div>
                            <div class="metric"><span class="metric-name">Wildcard Imports</span><span class="metric-value">{metrics.code_smells.wildcard_imports}</span></div>
                            <div class="metric"><span class="metric-name">Duplication</span><span class="metric-value">{metrics.duplication.duplicate_percentage}%</span></div>
                        </div>
                    </div>
                </body>
                </html>"""
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 code_metrics.py <JavaFile.java> [--json] [--html]")
        print("\nOptions:")
        print("  --json    Output as JSON")
        print("  --html    Generate HTML report (saves to <filename>_report.html)")
        sys.exit(1)
    
    filepath = sys.argv[1]
    output_json = '--json' in sys.argv
    output_html = '--html' in sys.argv
    
    if not Path(filepath).exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    analyzer = JavaTestAnalyzer(filepath)
    metrics = analyzer.analyze()
    
    if output_json:
        data_path = Path(filepath).stem + '_report.json'
        with open(data_path, "w") as f:
            json.dump(asdict(metrics), f, indent=4)
        print(f"Report saved to: {data_path}")
    elif output_html:
        html_path = Path(filepath).stem + '_report.html'
        with open(html_path, 'w') as f:
            f.write(to_html(metrics))
        print(f"HTML report saved to: {html_path}")
    else:
        print_metrics(metrics)

if __name__ == '__main__':
    main()