package dev.kivyschool.pyjniuswrap;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ParserConfiguration;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.symbolsolver.JavaSymbolSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.CombinedTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.JavaParserTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.ReflectionTypeSolver;
import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;
import picocli.CommandLine.Parameters;

import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.stream.Stream;

/**
 * CLI entry point. Walks an input folder for {@code .java} files, parses each one
 * with JavaParser (with reflection-based symbol resolution), and prints a single
 * JSON document to stdout (or to {@code --output} if provided).
 *
 * <pre>
 *   java -jar java-ast-emitter.jar &lt;input-dir&gt; [--output ast.json] [--pretty]
 * </pre>
 */
@Command(
        name = "java-ast-emitter",
        description = "Emit a JSON AST document for Java sources, intended as input "
                + "to the pyjnius-wrap Swift code generator.",
        mixinStandardHelpOptions = true,
        version = "0.1.0"
)
public final class JavaAstEmitter implements Callable<Integer> {

    @Parameters(index = "0", paramLabel = "INPUT",
            description = "Input to wrap. Either: (a) a directory of .java source "
                    + "files, or (b) a .jar / .aar / .class file, or (c) a directory "
                    + "containing those compiled artifacts.")
    private Path inputDir;

    @Option(names = {"-o", "--output"},
            description = "Write JSON to this file instead of stdout.")
    private Path output;

    @Option(names = {"--pretty"}, description = "Pretty-print JSON output.")
    private boolean pretty;

    @Option(names = {"--bytecode"},
            description = "Force the bytecode (ASM) backend even if the input looks "
                    + "like a source tree. Use this when a directory contains both "
                    + ".java and .class and you want the compiled view.")
    private boolean forceBytecode;

    public static void main(String[] args) {
        int code = new CommandLine(new JavaAstEmitter()).execute(args);
        System.exit(code);
    }

    @Override
    public Integer call() throws Exception {
        if (!Files.exists(inputDir)) {
            System.err.println("Input does not exist: " + inputDir);
            return 2;
        }

        AstDtos.Document doc;
        if (forceBytecode || isBytecodeInput(inputDir)) {
            doc = runBytecode(inputDir);
        } else {
            doc = runSources(inputDir);
        }

        ObjectMapper mapper = new ObjectMapper();
        if (pretty) mapper.enable(SerializationFeature.INDENT_OUTPUT);
        String json = mapper.writeValueAsString(doc);

        if (output != null) {
            Files.writeString(output, json);
        } else {
            try (PrintWriter pw = new PrintWriter(System.out, true)) {
                pw.println(json);
            }
        }
        return 0;
    }

    private static boolean isBytecodeInput(Path p) throws IOException {
        if (Files.isRegularFile(p)) {
            String n = p.getFileName().toString().toLowerCase();
            return n.endsWith(".jar") || n.endsWith(".aar") || n.endsWith(".class");
        }
        // Directory: choose bytecode if it has any .class/.jar/.aar but no .java.
        boolean hasJava = false, hasBytecode = false;
        try (Stream<Path> walk = Files.walk(p)) {
            for (Path c : (Iterable<Path>) walk::iterator) {
                String n = c.getFileName().toString().toLowerCase();
                if (n.endsWith(".java")) hasJava = true;
                if (n.endsWith(".class") || n.endsWith(".jar") || n.endsWith(".aar")) hasBytecode = true;
                if (hasJava && hasBytecode) break;
            }
        }
        return hasBytecode && !hasJava;
    }

    private static AstDtos.Document runSources(Path inputDir) throws IOException {
        if (!Files.isDirectory(inputDir)) {
            throw new IOException("Source mode requires a directory: " + inputDir);
        }
        CombinedTypeSolver solver = new CombinedTypeSolver();
        solver.add(new ReflectionTypeSolver());
        solver.add(new JavaParserTypeSolver(inputDir));
        ParserConfiguration config = new ParserConfiguration()
                .setSymbolResolver(new JavaSymbolSolver(solver));
        JavaParser parser = new JavaParser(config);
        ClassExtractor extractor = new ClassExtractor();

        AstDtos.Document doc = new AstDtos.Document();
        doc.classes = new ArrayList<>();

        List<Path> javaFiles = new ArrayList<>();
        try (Stream<Path> walk = Files.walk(inputDir)) {
            walk.filter(p -> p.toString().endsWith(".java"))
                    .sorted()
                    .forEach(javaFiles::add);
        }

        for (Path file : javaFiles) {
            var result = parser.parse(file);
            if (!result.isSuccessful() || result.getResult().isEmpty()) {
                System.err.println("Parse failed: " + file);
                result.getProblems().forEach(p -> System.err.println("  " + p));
                continue;
            }
            CompilationUnit cu = result.getResult().get();
            doc.classes.addAll(extractor.extract(cu));
        }
        return doc;
    }

    private static AstDtos.Document runBytecode(Path input) throws IOException {
        return new BytecodeExtractor().extractAll(List.of(input));
    }
}
