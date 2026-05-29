import Foundation

/// Tiny line+indent builder. We emit Cython source as plain text rather
/// than via the CySwiftAst node graph for v1 — per jni_core-plan.md
/// "Further Considerations #2", the upstream parser currently preserves
/// source verbatim, so a string-based shape lets us iterate today and
/// swap to AST nodes mechanically once the grammar lands.
struct CythonSource {
    private(set) var lines: [String] = []
    private var indent: String = ""

    mutating func line(_ s: String = "") {
        if s.isEmpty {
            lines.append("")
        } else {
            lines.append(indent + s)
        }
    }

    mutating func lines(_ many: [String]) {
        for l in many { line(l) }
    }

    mutating func block(_ header: String, _ body: (inout CythonSource) -> Void) {
        line(header)
        let save = indent
        indent += "    "
        body(&self)
        indent = save
    }

    func render() -> String {
        lines.joined(separator: "\n") + "\n"
    }
}
