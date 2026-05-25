package dev.kivyschool.pyjniuswrap;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import javax.tools.JavaCompiler;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.jar.JarEntry;
import java.util.jar.JarOutputStream;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Compile the fixture sources to {@code .class}, pack them into a jar, and verify
 * the {@link BytecodeExtractor} produces a document that lines up with the
 * source-based {@link ClassExtractor}.
 */
class BytecodeExtractorTest {

    private static AstDtos.Document bytecodeDoc;

    @BeforeAll
    static void compileAndExtract(@org.junit.jupiter.api.io.TempDir Path tmp) throws Exception {
        Path fixtureDir = Path.of("").toAbsolutePath().getParent().resolve("fixtures").resolve("java");
        Path classesDir = tmp.resolve("classes");
        Files.createDirectories(classesDir);

        List<Path> sources = new ArrayList<>();
        try (Stream<Path> walk = Files.walk(fixtureDir)) {
            walk.filter(p -> p.toString().endsWith(".java")).forEach(sources::add);
        }
        assertFalse(sources.isEmpty(), "fixture .java files must exist");

        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        assertNotNull(compiler, "JDK with javac is required to run this test");
        try (StandardJavaFileManager fm = compiler.getStandardFileManager(null, null, null)) {
            Iterable<? extends javax.tools.JavaFileObject> units = fm.getJavaFileObjectsFromPaths(sources);
            List<String> opts = List.of(
                    "-d", classesDir.toString(),
                    "-parameters",      // preserve parameter names
                    "-g:none"
            );
            boolean ok = compiler.getTask(null, fm, null, opts, null, units).call();
            assertTrue(ok, "javac must succeed on the fixture sources");
        }

        Path jar = tmp.resolve("fixtures.jar");
        packJar(classesDir, jar);

        bytecodeDoc = new BytecodeExtractor().extractAll(List.of(jar));
        assertNotNull(bytecodeDoc.classes);
    }

    @Test
    void discoversAllPublicTopLevelClasses() {
        Set<String> fqcns = bytecodeDoc.classes.stream()
                .map(c -> c.fqcn).collect(Collectors.toSet());
        assertEquals(Set.of(
                "com.example.fixture.Color",
                "com.example.fixture.Content",
                "com.example.fixture.Listener",
                "com.example.fixture.Person"
        ), fqcns);
    }

    @Test
    void personHasExpectedConstructorsAndVarargsMethod() {
        AstDtos.ClassNode person = byFqcn("com.example.fixture.Person");
        assertEquals(AstDtos.ClassKind.CLASS, person.kind);
        assertEquals(2, person.constructors.size());
        AstDtos.MethodNode addTags = person.methods.stream()
                .filter(m -> m.name.equals("addTags")).findFirst().orElseThrow();
        assertTrue(addTags.isVarargs, "addTags should be marked varargs");
        // Parameter names preserved because we compiled with -parameters.
        assertEquals("tags", addTags.parameters.get(0).name);
    }

    @Test
    void interfaceKindAndDefaultMethodFlag() {
        AstDtos.ClassNode listener = byFqcn("com.example.fixture.Listener");
        assertEquals(AstDtos.ClassKind.INTERFACE, listener.kind);
        AstDtos.MethodNode isReady = listener.methods.stream()
                .filter(m -> m.name.equals("isReady")).findFirst().orElseThrow();
        assertTrue(isReady.modifiers.contains(AstDtos.Modifier.DEFAULT),
                "isReady() declared with default body should carry DEFAULT modifier");
        AstDtos.FieldNode tag = listener.fields.stream()
                .filter(f -> f.name.equals("TAG")).findFirst().orElseThrow();
        assertTrue(tag.isStatic, "interface fields are implicitly static");
    }

    @Test
    void nestedBuilderAttachedToOuterContent() {
        AstDtos.ClassNode content = byFqcn("com.example.fixture.Content");
        assertEquals(1, content.nested.size());
        AstDtos.ClassNode builder = content.nested.get(0);
        assertEquals("Builder", builder.simpleName);
        assertEquals("com/example/fixture/Content/Builder", builder.jniName);
    }

    @Test
    void enumKindEnumConstantsAndDescribeMethod() {
        AstDtos.ClassNode color = byFqcn("com.example.fixture.Color");
        assertEquals(AstDtos.ClassKind.ENUM, color.kind);
        assertEquals(List.of("RED", "GREEN", "BLUE"),
                color.enumConstants.stream().map(e -> e.name).toList());
        assertTrue(color.methods.stream().anyMatch(m -> m.name.equals("describe")),
                "describe() should be present");
        // Compiler-synthesised values()/valueOf are visible from bytecode and that's OK.
        assertTrue(color.methods.stream().anyMatch(m -> m.name.equals("values")));
        assertTrue(color.methods.stream().anyMatch(m -> m.name.equals("valueOf")));
    }

    @Test
    void descriptorsAreJniForm() {
        AstDtos.ClassNode content = byFqcn("com.example.fixture.Content");
        AstDtos.ConstructorNode ctor = content.constructors.get(0);
        assertEquals("(Ljava/lang/String;)V", ctor.jniDescriptor);
        // Bytecode produces the canonical JNI form with '$' for nested types.
        AstDtos.ClassNode builder = content.nested.get(0);
        AstDtos.MethodNode setBody = builder.methods.stream()
                .filter(m -> m.name.equals("setBody")).findFirst().orElseThrow();
        assertEquals(
                "(Ljava/lang/String;)Lcom/example/fixture/Content$Builder;",
                setBody.jniDescriptor);
    }

    private static AstDtos.ClassNode byFqcn(String fqcn) {
        return bytecodeDoc.classes.stream()
                .filter(c -> c.fqcn.equals(fqcn))
                .findFirst()
                .orElseThrow(() -> new AssertionError("Class not found: " + fqcn));
    }

    private static void packJar(Path classesDir, Path jar) throws IOException {
        try (JarOutputStream jos = new JarOutputStream(Files.newOutputStream(jar))) {
            Files.walkFileTree(classesDir, new SimpleFileVisitor<>() {
                @Override public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                    if (!file.toString().endsWith(".class")) return FileVisitResult.CONTINUE;
                    String name = classesDir.relativize(file).toString().replace('\\', '/');
                    jos.putNextEntry(new JarEntry(name));
                    jos.write(Files.readAllBytes(file));
                    jos.closeEntry();
                    return FileVisitResult.CONTINUE;
                }
            });
        }
    }
}
