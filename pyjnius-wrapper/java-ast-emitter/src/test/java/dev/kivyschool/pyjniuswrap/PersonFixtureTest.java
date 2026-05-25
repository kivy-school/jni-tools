package dev.kivyschool.pyjniuswrap;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ParserConfiguration;
import com.github.javaparser.symbolsolver.JavaSymbolSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.CombinedTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.JavaParserTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.ReflectionTypeSolver;
import org.junit.jupiter.api.Test;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

class PersonFixtureTest {

    /** Resolve the fixtures dir from the repo root (CWD at gradle test time is the gradle project dir). */
    private static Path fixturesDir() {
        Path here = Path.of("").toAbsolutePath();
        Path candidate = here.getParent().resolve("fixtures").resolve("java");
        assertTrue(Files.isDirectory(candidate), "expected fixtures dir: " + candidate);
        return candidate;
    }

    @Test
    void personFixtureRoundTrips() throws Exception {
        Path dir = fixturesDir();

        CombinedTypeSolver solver = new CombinedTypeSolver();
        solver.add(new ReflectionTypeSolver());
        solver.add(new JavaParserTypeSolver(dir));
        ParserConfiguration config = new ParserConfiguration()
                .setSymbolResolver(new JavaSymbolSolver(solver));
        JavaParser parser = new JavaParser(config);
        ClassExtractor extractor = new ClassExtractor();

        AstDtos.Document doc = new AstDtos.Document();
        doc.classes = new ArrayList<>();
        List<Path> files = new ArrayList<>();
        try (Stream<Path> walk = Files.walk(dir)) {
            walk.filter(p -> p.toString().endsWith(".java")).sorted().forEach(files::add);
        }
        for (Path f : files) {
            var r = parser.parse(f);
            assertTrue(r.isSuccessful(), "parse failed for " + f + ": " + r.getProblems());
            doc.classes.addAll(extractor.extract(r.getResult().orElseThrow()));
        }

        AstDtos.ClassNode person = doc.classes.stream()
                .filter(c -> c.fqcn.equals("com.example.fixture.Person"))
                .findFirst().orElseThrow();
        assertEquals("com/example/fixture/Person", person.jniName);
        assertEquals(AstDtos.ClassKind.CLASS, person.kind);

        // Fields: SPECIES (static), name (public), age (protected)
        assertEquals(3, person.fields.size());
        AstDtos.FieldNode species = person.fields.get(0);
        assertEquals("SPECIES", species.name);
        assertTrue(species.isStatic);
        assertEquals("Ljava/lang/String;", species.jniDescriptor);

        // Two ctors: (String) and (String, int)
        assertEquals(2, person.constructors.size());
        assertEquals("(Ljava/lang/String;)V", person.constructors.get(0).jniDescriptor);
        assertEquals("(Ljava/lang/String;I)V", person.constructors.get(1).jniDescriptor);

        // greet overloaded twice, anonymous static, getAge, addTags(varargs)
        long greetCount = person.methods.stream().filter(m -> m.name.equals("greet")).count();
        assertEquals(2, greetCount);
        AstDtos.MethodNode anon = person.methods.stream()
                .filter(m -> m.name.equals("anonymous")).findFirst().orElseThrow();
        assertTrue(anon.isStatic);
        assertEquals("()Lcom/example/fixture/Person;", anon.jniDescriptor);
        AstDtos.MethodNode addTags = person.methods.stream()
                .filter(m -> m.name.equals("addTags")).findFirst().orElseThrow();
        assertTrue(addTags.isVarargs);
        assertEquals("([Ljava/lang/String;)V", addTags.jniDescriptor);

        // JSON round-trip is stable Codable input
        ObjectMapper mapper = new ObjectMapper();
        String json = mapper.writeValueAsString(doc);
        JsonNode tree = mapper.readTree(json);
        assertTrue(tree.has("classes"));
    }
}
