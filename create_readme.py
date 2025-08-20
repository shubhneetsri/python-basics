import os
import ast

README_FILE = "README.md"   # 📌 Output file name

# 📌 Excluded directories
EXCLUDE_DIRS = {"venv", ".venv", "__pycache__", ".git", ".idea", ".vscode"}

def list_methods_in_file(filepath):
    """Parse a Python file and return all functions & class methods."""
    with open(filepath, "r", encoding="utf-8") as file:
        try:
            tree = ast.parse(file.read(), filename=filepath)
        except SyntaxError as e:
            print(f"⚠️ Skipping {filepath}, SyntaxError: {e}")
            return [], {}

    functions = []
    classes = {}

    for node in ast.walk(tree):
        # Top-level functions
        if isinstance(node, ast.FunctionDef) and isinstance(getattr(node, "parent", None), ast.Module):
            functions.append(node.name)

        # Classes and their methods
        elif isinstance(node, ast.ClassDef):
            methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            classes[node.name] = methods

    return functions, classes


def add_parents(tree):
    """Attach parent references to AST nodes for easier inspection."""
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node
    return tree


def scan_directory(directory):
    """Scan all .py files in the directory and list methods with file name."""
    result = {}
    for root, dirs, files in os.walk(directory):
        # 🚫 Remove excluded dirs from traversal
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read(), filename=filepath)
                        add_parents(tree)
                        functions, classes = list_methods_in_file(filepath)
                        if functions or classes:
                            result[filepath] = {"functions": functions, "classes": classes}
                except Exception as e:
                    print(f"⚠️ Error reading {filepath}: {e}")
    return result


if __name__ == "__main__":
    directory = "."   # change this to your project path
    output = scan_directory(directory)

    with open(README_FILE, "w", encoding="utf-8") as readme:
        readme.write("# 📌 Project Python Methods Overview\n\n")
        
        for file, content in output.items():
            readme.write(f"## 📄 File: `{file}`\n\n")
            
            if content["functions"]:
                readme.write("### 🔹 Functions:\n")
                for func in content["functions"]:
                    readme.write(f"- {func}\n")
                readme.write("\n")
            
            if content["classes"]:
                readme.write("### 🏷️ Classes:\n")
                for cls, methods in content["classes"].items():
                    readme.write(f"- **{cls}**\n")
                    for m in methods:
                        readme.write(f"  - {m}\n")
                readme.write("\n")

    print(f"✅ Methods overview written to {README_FILE}")
