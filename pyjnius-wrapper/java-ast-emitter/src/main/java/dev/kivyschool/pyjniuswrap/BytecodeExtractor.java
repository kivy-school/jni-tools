package dev.kivyschool.pyjniuswrap;

import org.objectweb.asm.ClassReader;
import org.objectweb.asm.ClassVisitor;
import org.objectweb.asm.FieldVisitor;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;
import org.objectweb.asm.Type;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

/**
 * Builds an {@link AstDtos.Document} by reading compiled JVM bytecode via ASM.
 *
 * <p>Accepts {@code .jar}, {@code .aar} (extracts {@code classes.jar}), individual
 * {@code .class} files, or directories containing any of those. Mirrors the JSON
 * schema produced by {@link ClassExtractor} so the same Swift code-gen consumes it.
 *
 * <p>What you give up vs. the source path: parameter names default to {@code arg0},
 * {@code arg1}, ... unless the class was compiled with {@code -parameters}; javadoc
 * is unavailable.
 *
 * <p>What you get: generic erasure already baked in, full method overload visibility
 * including compiler-synthesised enum {@code values()}/{@code valueOf}, and the
 * ability to wrap closed-source SDKs (AdMob, Play Services, {@code android.jar}).
 */
public final class BytecodeExtractor {

    /** All discovered classes keyed by internal slash-name (e.g. com/example/Foo$Bar). */
    private final Map<String, AstDtos.ClassNode> byInternal = new LinkedHashMap<>();
    /** Internal-name → outer internal-name, from the InnerClasses attribute. */
    private final Map<String, String> outerOf = new HashMap<>();

    /** Read everything we can from a list of inputs (jars/aars/dirs/.class files). */
    public AstDtos.Document extractAll(List<Path> inputs) throws IOException {
        for (Path p : inputs) {
            ingest(p);
        }
        return assembleTree();
    }

    /* ---------- ingestion ---------- */

    private void ingest(Path p) throws IOException {
        if (Files.isDirectory(p)) {
            try (var walk = Files.walk(p)) {
                List<Path> children = walk.sorted().toList();
                for (Path c : children) ingestSingle(c);
            }
            return;
        }
        ingestSingle(p);
    }

    private void ingestSingle(Path p) throws IOException {
        String name = p.getFileName().toString().toLowerCase();
        if (Files.isDirectory(p)) return;
        if (name.endsWith(".class")) {
            ingestClass(Files.readAllBytes(p));
        } else if (name.endsWith(".jar")) {
            ingestZip(Files.readAllBytes(p), /*aar=*/false);
        } else if (name.endsWith(".aar")) {
            ingestZip(Files.readAllBytes(p), /*aar=*/true);
        }
    }

    private void ingestZip(byte[] bytes, boolean aar) throws IOException {
        try (var zin = new ZipInputStream(new java.io.ByteArrayInputStream(bytes))) {
            ZipEntry e;
            while ((e = zin.getNextEntry()) != null) {
                if (e.isDirectory()) continue;
                String n = e.getName();
                if (aar && n.equals("classes.jar")) {
                    ingestZip(readAll(zin), /*aar=*/false);
                } else if (!aar && n.endsWith(".class")
                        && !n.equals("module-info.class")
                        && !n.endsWith("package-info.class")) {
                    ingestClass(readAll(zin));
                }
            }
        }
    }

    private static byte[] readAll(InputStream in) throws IOException {
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        byte[] buf = new byte[8192];
        int n;
        while ((n = in.read(buf)) > 0) bos.write(buf, 0, n);
        return bos.toByteArray();
    }

    private void ingestClass(byte[] bytes) {
        ClassReader cr = new ClassReader(bytes);
        ClassReaderVisitor visitor = new ClassReaderVisitor();
        // Note: do NOT pass SKIP_DEBUG — MethodParameters lives in a separate
        // attribute but some ASM versions short-circuit param visits with that
        // flag. SKIP_CODE is enough to keep parsing fast.
        cr.accept(visitor, ClassReader.SKIP_CODE | ClassReader.SKIP_FRAMES);
        AstDtos.ClassNode raw = visitor.out;
        if (raw.jniName == null) return;
        // Key by the raw internal name (with '$' for nested) so outerOf lookups
        // line up. The user-facing jniName (with '/') stays on the node.
        byInternal.put(visitor.thisInternal, raw);
    }

    /* ---------- post-pass: build nested tree ---------- */

    private AstDtos.Document assembleTree() {
        // Apply visibility floor: drop any class whose access is not public/protected.
        // We keep nested classes regardless because the InnerClasses attribute carries
        // their declared access, which we already set on the node.
        AstDtos.Document doc = new AstDtos.Document();
        doc.classes = new ArrayList<>();

        // Stable order: by internal name.
        List<String> keys = new ArrayList<>(byInternal.keySet());
        Collections.sort(keys);

        // First, hang each nested class under its outer.
        for (String key : keys) {
            String outer = outerOf.get(key);
            if (outer == null) continue;
            AstDtos.ClassNode parent = byInternal.get(outer);
            AstDtos.ClassNode child = byInternal.get(key);
            if (parent == null || child == null) continue;
            if (!hasValidSimpleName(child)) continue; // skip anonymous classes ("1", "2", ...)
            parent.nested.add(child);
        }

        // Then emit top-level classes that pass the visibility floor.
        for (String key : keys) {
            if (outerOf.containsKey(key)) continue; // nested — already attached
            AstDtos.ClassNode top = byInternal.get(key);
            if (top == null) continue;
            if (!hasValidSimpleName(top)) continue; // skip anonymous classes
            if (!isPublicOrProtected(top.modifiers)) continue;
            stripPrivateMembers(top);
            doc.classes.add(top);
        }

        // Stable nested ordering.
        for (AstDtos.ClassNode n : byInternal.values()) {
            n.nested.sort(Comparator.comparing(c -> c.simpleName));
        }
        return doc;
    }

    private static boolean isPublicOrProtected(List<AstDtos.Modifier> mods) {
        if (mods == null) return false;
        return mods.contains(AstDtos.Modifier.PUBLIC) || mods.contains(AstDtos.Modifier.PROTECTED);
    }

    /** Anonymous Java classes get a numeric simple name (e.g. "1").  These cannot
     *  become valid Python class names, so we skip them. */
    private static boolean hasValidSimpleName(AstDtos.ClassNode node) {
        if (node.simpleName == null || node.simpleName.isEmpty()) return false;
        return !Character.isDigit(node.simpleName.charAt(0));
    }

    /** Recursively drop nested entries that are not public/protected. */
    private static void stripPrivateMembers(AstDtos.ClassNode node) {
        if (node.nested == null) return;
        List<AstDtos.ClassNode> keep = new ArrayList<>();
        for (AstDtos.ClassNode n : node.nested) {
            if (!isPublicOrProtected(n.modifiers)) continue;
            stripPrivateMembers(n);
            keep.add(n);
        }
        node.nested = keep;
    }

    /* ---------- visitors ---------- */

    private final class ClassReaderVisitor extends ClassVisitor {
        final AstDtos.ClassNode out = new AstDtos.ClassNode();
        String thisInternal;
        private boolean isInterface;
        private boolean isEnum;

        ClassReaderVisitor() {
            super(Opcodes.ASM9);
            out.fields = new ArrayList<>();
            out.constructors = new ArrayList<>();
            out.methods = new ArrayList<>();
            out.nested = new ArrayList<>();
            out.interfaces = new ArrayList<>();
        }

        @Override
        public void visit(int version, int access, String name, String signature,
                          String superName, String[] interfaces) {
            thisInternal = name;
            isInterface = (access & Opcodes.ACC_INTERFACE) != 0;
            isEnum = (access & Opcodes.ACC_ENUM) != 0;
            boolean isAnnotation = (access & Opcodes.ACC_ANNOTATION) != 0;

            out.fqcn = name.replace('/', '.').replace('$', '.');
            // pyjnius slash form uses '/' for nested separator too; the source-side
            // extractor produces the same format.
            out.jniName = name.replace('$', '/');
            int slash = name.lastIndexOf('/');
            int dollar = name.lastIndexOf('$');
            int sep = Math.max(slash, dollar);
            out.simpleName = sep < 0 ? name : name.substring(sep + 1);

            if (isAnnotation) out.kind = AstDtos.ClassKind.ANNOTATION;
            else if (isEnum) out.kind = AstDtos.ClassKind.ENUM;
            else if (isInterface) out.kind = AstDtos.ClassKind.INTERFACE;
            else out.kind = AstDtos.ClassKind.CLASS;

            out.modifiers = decodeModifiers(access, /*isMethod=*/false);
            out.superclass = (superName == null || "java/lang/Object".equals(superName))
                    ? null
                    : superName.replace('/', '.').replace('$', '.');
            if (isEnum && out.superclass == null) {
                out.superclass = "java.lang.Enum";
            }
            if (interfaces != null) {
                for (String i : interfaces) {
                    out.interfaces.add(i.replace('/', '.').replace('$', '.'));
                }
            }
            if (isEnum) {
                out.enumConstants = new ArrayList<>();
            }
        }

        @Override
        public void visitInnerClass(String name, String outerName, String innerName, int access) {
            // The current class's own entry tells us its declared access and outer.
            if (!name.equals(thisInternal)) return;
            if (innerName == null) return; // anonymous
            if (outerName == null) return; // local class
            outerOf.put(name, outerName);
            // The InnerClasses entry carries the *declared* access modifiers, which
            // are the ones a wrapper-author cares about.
            out.modifiers = decodeModifiers(access, /*isMethod=*/false);
        }

        @Override
        public FieldVisitor visitField(int access, String name, String descriptor,
                                       String signature, Object value) {
            if ((access & (Opcodes.ACC_SYNTHETIC | Opcodes.ACC_BRIDGE)) != 0) return null;
            // Enum constants are emitted as ACC_PUBLIC|ACC_STATIC|ACC_FINAL|ACC_ENUM.
            if ((access & Opcodes.ACC_ENUM) != 0 && out.enumConstants != null) {
                AstDtos.EnumConstantNode k = new AstDtos.EnumConstantNode();
                k.name = name;
                out.enumConstants.add(k);
                return null;
            }
            if (!isAccessible(access)) return null;
            AstDtos.FieldNode f = new AstDtos.FieldNode();
            f.name = name;
            f.jniDescriptor = descriptor;
            f.typeFqcn = descriptorToFqcn(descriptor);
            f.isStatic = (access & Opcodes.ACC_STATIC) != 0;
            f.modifiers = decodeModifiers(access, /*isMethod=*/false);
            out.fields.add(f);
            return null;
        }

        @Override
        public MethodVisitor visitMethod(int access, String name, String descriptor,
                                         String signature, String[] exceptions) {
            if ((access & (Opcodes.ACC_SYNTHETIC | Opcodes.ACC_BRIDGE)) != 0) return null;
            if ("<clinit>".equals(name)) return null;
            if (!isAccessible(access)) return null;

            boolean isVarargs = (access & Opcodes.ACC_VARARGS) != 0;
            List<AstDtos.Modifier> mods = decodeModifiers(access, /*isMethod=*/true);
            if (isInterface
                    && (access & Opcodes.ACC_ABSTRACT) == 0
                    && (access & Opcodes.ACC_STATIC) == 0) {
                if (!mods.contains(AstDtos.Modifier.DEFAULT)) mods.add(AstDtos.Modifier.DEFAULT);
            }

            Type mt = Type.getMethodType(descriptor);
            Type[] argTypes = mt.getArgumentTypes();
            List<AstDtos.ParamNode> params = new ArrayList<>(argTypes.length);
            for (int i = 0; i < argTypes.length; i++) {
                AstDtos.ParamNode p = new AstDtos.ParamNode();
                p.name = "arg" + i;
                p.jniDescriptor = argTypes[i].getDescriptor();
                p.typeFqcn = descriptorToFqcn(argTypes[i].getDescriptor());
                params.add(p);
            }

            if ("<init>".equals(name)) {
                AstDtos.ConstructorNode c = new AstDtos.ConstructorNode();
                c.jniDescriptor = descriptor;
                c.isVarargs = isVarargs;
                c.modifiers = mods;
                c.parameters = params;
                out.constructors.add(c);
            } else {
                AstDtos.MethodNode m = new AstDtos.MethodNode();
                m.name = name;
                m.jniDescriptor = descriptor;
                m.isStatic = (access & Opcodes.ACC_STATIC) != 0;
                m.isVarargs = isVarargs;
                m.modifiers = mods;
                m.parameters = params;
                m.returnTypeFqcn = descriptorToFqcn(mt.getReturnType().getDescriptor());
                out.methods.add(m);
            }
            // Capture parameter names if -parameters was used.
            return new MethodVisitor(Opcodes.ASM9) {
                int idx = 0;
                @Override public void visitParameter(String pname, int pAccess) {
                    if (pname != null && idx < params.size()) {
                        params.get(idx).name = pname;
                    }
                    idx++;
                }
            };
        }
    }

    /* ---------- helpers ---------- */

    private static boolean isAccessible(int access) {
        return (access & Opcodes.ACC_PUBLIC) != 0 || (access & Opcodes.ACC_PROTECTED) != 0;
    }

    private static List<AstDtos.Modifier> decodeModifiers(int access, boolean isMethod) {
        List<AstDtos.Modifier> out = new ArrayList<>();
        if ((access & Opcodes.ACC_PUBLIC) != 0)    out.add(AstDtos.Modifier.PUBLIC);
        if ((access & Opcodes.ACC_PROTECTED) != 0) out.add(AstDtos.Modifier.PROTECTED);
        if ((access & Opcodes.ACC_PRIVATE) != 0)   out.add(AstDtos.Modifier.PRIVATE);
        if ((access & Opcodes.ACC_STATIC) != 0)    out.add(AstDtos.Modifier.STATIC);
        if ((access & Opcodes.ACC_FINAL) != 0)     out.add(AstDtos.Modifier.FINAL);
        if ((access & Opcodes.ACC_ABSTRACT) != 0)  out.add(AstDtos.Modifier.ABSTRACT);
        return out;
    }

    /** {@code Ljava/lang/String;} → {@code java.lang.String}, {@code [I} → {@code int[]}, etc. */
    static String descriptorToFqcn(String d) {
        int dims = 0;
        while (dims < d.length() && d.charAt(dims) == '[') dims++;
        String core = d.substring(dims);
        String base;
        switch (core.charAt(0)) {
            case 'V': base = "void"; break;
            case 'Z': base = "boolean"; break;
            case 'B': base = "byte"; break;
            case 'C': base = "char"; break;
            case 'S': base = "short"; break;
            case 'I': base = "int"; break;
            case 'J': base = "long"; break;
            case 'F': base = "float"; break;
            case 'D': base = "double"; break;
            case 'L':
                base = core.substring(1, core.length() - 1).replace('/', '.').replace('$', '.');
                break;
            default:
                base = "java.lang.Object";
        }
        StringBuilder sb = new StringBuilder(base);
        for (int i = 0; i < dims; i++) sb.append("[]");
        return sb.toString();
    }
}
