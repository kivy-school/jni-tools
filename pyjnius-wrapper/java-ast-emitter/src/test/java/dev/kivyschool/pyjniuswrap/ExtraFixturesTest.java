package dev.kivyschool.pyjniuswrap;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParserConfiguration;
import com.github.javaparser.symbolsolver.JavaSymbolSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.CombinedTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.JavaParserTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.ReflectionTypeSolver;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

class ExtraFixturesTest {

    private static AstDtos.Document doc;

    @BeforeAll
    static void parseFixtures() throws Exception {
        Path dir = Path.of("").toAbsolutePath().getParent().resolve("fixtures").resolve("java");
        CombinedTypeSolver solver = new CombinedTypeSolver();
        solver.add(new ReflectionTypeSolver());
        solver.add(new JavaParserTypeSolver(dir));
        ParserConfiguration config = new ParserConfiguration()
                .setSymbolResolver(new JavaSymbolSolver(solver));
        JavaParser parser = new JavaParser(config);
        ClassExtractor extractor = new ClassExtractor();

        doc = new AstDtos.Document();
        doc.classes = new ArrayList<>();
        List<Path> files = new ArrayList<>();
        try (Stream<Path> walk = Files.walk(dir)) {
            walk.filter(p -> p.toString().endsWith(".java")).sorted().forEach(files::add);
        }
        for (Path f : files) {
            var r = parser.parse(f);
            assertTrue(r.isSuccessful(), "parse failed: " + r.getProblems());
            doc.classes.addAll(extractor.extract(r.getResult().orElseThrow()));
        }
    }

    private static AstDtos.ClassNode byFqcn(String fqcn) {
        return doc.classes.stream().filter(c -> c.fqcn.equals(fqcn)).findFirst().orElseThrow();
    }

    @Test
    void interfaceFixture() {
        AstDtos.ClassNode listener = byFqcn("com.example.fixture.Listener");
        assertEquals(AstDtos.ClassKind.INTERFACE, listener.kind);
        // Interface members are implicitly public — both methods must surface.
        assertEquals(2, listener.methods.size(), "expected 2 methods, got " + listener.methods);
        assertTrue(listener.methods.stream().anyMatch(m ->
                m.name.equals("onEvent") && m.jniDescriptor.equals("(Ljava/lang/String;I)V")));
        assertTrue(listener.methods.stream().anyMatch(m -> m.name.equals("isReady")));
        // Implicit constant
        assertEquals(1, listener.fields.size());
        AstDtos.FieldNode tag = listener.fields.get(0);
        assertEquals("TAG", tag.name);
        assertTrue(tag.isStatic, "interface field must be implicitly static");
    }

    @Test
    void nestedClassFixture() {
        AstDtos.ClassNode content = byFqcn("com.example.fixture.Content");
        assertEquals(1, content.nested.size());
        AstDtos.ClassNode builder = content.nested.get(0);
        assertEquals("Builder", builder.simpleName);
        assertEquals("com.example.fixture.Content.Builder", builder.fqcn);
        assertEquals("com/example/fixture/Content/Builder", builder.jniName);
        assertTrue(builder.methods.stream().anyMatch(m ->
                m.name.equals("setBody")
                        && m.jniDescriptor.equals("(Ljava/lang/String;)Lcom/example/fixture/Content/Builder;")));
        assertTrue(builder.methods.stream().anyMatch(m ->
                m.name.equals("build")
                        && m.jniDescriptor.equals("()Lcom/example/fixture/Content;")));
    }

    @Test
    void enumFixture() {
        AstDtos.ClassNode color = byFqcn("com.example.fixture.Color");
        assertEquals(AstDtos.ClassKind.ENUM, color.kind);
        assertNotNull(color.enumConstants);
        assertEquals(3, color.enumConstants.size());
        assertEquals("RED", color.enumConstants.get(0).name);
        // describe() should be present as a regular method.
        assertTrue(color.methods.stream().anyMatch(m -> m.name.equals("describe")));
    }
}
