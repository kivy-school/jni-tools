package dev.kivyschool.pyjniuswrap;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Modifier.Keyword;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.BodyDeclaration;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.ConstructorDeclaration;
import com.github.javaparser.ast.body.EnumConstantDeclaration;
import com.github.javaparser.ast.body.EnumDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.github.javaparser.ast.body.VariableDeclarator;
import com.github.javaparser.ast.nodeTypes.NodeWithJavadoc;
import com.github.javaparser.ast.nodeTypes.NodeWithModifiers;

import java.util.ArrayList;
import java.util.List;

/**
 * Walks a {@link CompilationUnit} and produces {@link AstDtos.ClassNode}s for every
 * top-level type declared in it. Skips members below protected visibility.
 */
public final class ClassExtractor {

    /** Visibility floor — we emit only public/protected members. */
    private static boolean isAccessible(NodeWithModifiers<?> n) {
        return n.hasModifier(Keyword.PUBLIC) || n.hasModifier(Keyword.PROTECTED);
    }

    /**
     * Interface members are implicitly public when no explicit visibility
     * modifier is declared. {@link #isAccessible} only checks explicit modifiers,
     * so this wrapper handles the interface case.
     */
    private static boolean isAccessibleIn(NodeWithModifiers<?> n, boolean parentIsInterface) {
        if (isAccessible(n)) return true;
        if (!parentIsInterface) return false;
        return !n.hasModifier(Keyword.PRIVATE);
    }

    public List<AstDtos.ClassNode> extract(CompilationUnit cu) {
        List<AstDtos.ClassNode> out = new ArrayList<>();
        for (TypeDeclaration<?> td : cu.getTypes()) {
            AstDtos.ClassNode node = extractType(td);
            if (node != null) out.add(node);
        }
        return out;
    }

    private AstDtos.ClassNode extractType(TypeDeclaration<?> td) {
        if (td instanceof ClassOrInterfaceDeclaration) {
            return extractClass((ClassOrInterfaceDeclaration) td);
        }
        if (td instanceof EnumDeclaration) {
            return extractEnum((EnumDeclaration) td);
        }
        return null;
    }

    private AstDtos.ClassNode extractClass(ClassOrInterfaceDeclaration cd) {
        AstDtos.ClassNode n = new AstDtos.ClassNode();
        n.fqcn = cd.getFullyQualifiedName().orElse(cd.getNameAsString());
        n.jniName = n.fqcn.replace('.', '/');
        n.simpleName = cd.getNameAsString();
        n.kind = cd.isInterface() ? AstDtos.ClassKind.INTERFACE : AstDtos.ClassKind.CLASS;
        n.modifiers = modifiers(cd);
        n.javadoc = javadocOf(cd);

        n.superclass = cd.getExtendedTypes().isEmpty()
                ? null
                : JniDescriptor.fqcnOf(cd.getExtendedTypes(0));
        n.interfaces = new ArrayList<>();
        for (var t : cd.getImplementedTypes()) {
            n.interfaces.add(JniDescriptor.fqcnOf(t));
        }

        n.fields = new ArrayList<>();
        n.constructors = new ArrayList<>();
        n.methods = new ArrayList<>();
        n.nested = new ArrayList<>();
        final boolean parentIsInterface = cd.isInterface();

        for (BodyDeclaration<?> member : cd.getMembers()) {
            if (member instanceof FieldDeclaration) {
                FieldDeclaration fd = (FieldDeclaration) member;
                if (!isAccessibleIn(fd, parentIsInterface)) continue;
                for (VariableDeclarator v : fd.getVariables()) {
                    AstDtos.FieldNode f = new AstDtos.FieldNode();
                    f.name = v.getNameAsString();
                    f.jniDescriptor = JniDescriptor.of(v.getType());
                    f.typeFqcn = JniDescriptor.fqcnOf(v.getType());
                    // Interface fields are implicitly public static final.
                    f.isStatic = fd.isStatic() || parentIsInterface;
                    f.modifiers = modifiers(fd);
                    f.javadoc = javadocOf(fd);
                    n.fields.add(f);
                }
            } else if (member instanceof ConstructorDeclaration) {
                ConstructorDeclaration ctor = (ConstructorDeclaration) member;
                if (!isAccessibleIn(ctor, parentIsInterface)) continue;
                AstDtos.ConstructorNode c = new AstDtos.ConstructorNode();
                c.parameters = paramsOf(ctor.getParameters());
                c.jniDescriptor = "(" + paramsDescriptor(ctor.getParameters()) + ")V";
                c.isVarargs = !ctor.getParameters().isEmpty()
                        && ctor.getParameters().get(ctor.getParameters().size() - 1).isVarArgs();
                c.modifiers = modifiers(ctor);
                c.javadoc = javadocOf(ctor);
                n.constructors.add(c);
            } else if (member instanceof MethodDeclaration) {
                MethodDeclaration md = (MethodDeclaration) member;
                if (!isAccessibleIn(md, parentIsInterface)) continue;
                AstDtos.MethodNode m = new AstDtos.MethodNode();
                m.name = md.getNameAsString();
                m.parameters = paramsOf(md.getParameters());
                String ret = JniDescriptor.of(md.getType());
                m.jniDescriptor = "(" + paramsDescriptor(md.getParameters()) + ")" + ret;
                m.returnTypeFqcn = JniDescriptor.fqcnOf(md.getType());
                m.isStatic = md.isStatic();
                m.isVarargs = !md.getParameters().isEmpty()
                        && md.getParameters().get(md.getParameters().size() - 1).isVarArgs();
                m.modifiers = modifiers(md);
                m.javadoc = javadocOf(md);
                n.methods.add(m);
            } else if (member instanceof TypeDeclaration) {
                AstDtos.ClassNode nested = extractType((TypeDeclaration<?>) member);
                if (nested != null) n.nested.add(nested);
            }
        }
        return n;
    }

    private AstDtos.ClassNode extractEnum(EnumDeclaration ed) {
        AstDtos.ClassNode n = new AstDtos.ClassNode();
        n.fqcn = ed.getFullyQualifiedName().orElse(ed.getNameAsString());
        n.jniName = n.fqcn.replace('.', '/');
        n.simpleName = ed.getNameAsString();
        n.kind = AstDtos.ClassKind.ENUM;
        n.modifiers = modifiers(ed);
        n.javadoc = javadocOf(ed);
        n.superclass = "java.lang.Enum";
        n.interfaces = new ArrayList<>();
        for (var t : ed.getImplementedTypes()) {
            n.interfaces.add(JniDescriptor.fqcnOf(t));
        }
        n.fields = new ArrayList<>();
        n.constructors = new ArrayList<>();
        n.methods = new ArrayList<>();
        n.nested = new ArrayList<>();
        n.enumConstants = new ArrayList<>();
        for (EnumConstantDeclaration ec : ed.getEntries()) {
            AstDtos.EnumConstantNode k = new AstDtos.EnumConstantNode();
            k.name = ec.getNameAsString();
            k.javadoc = javadocOf(ec);
            n.enumConstants.add(k);
        }
        for (BodyDeclaration<?> member : ed.getMembers()) {
            if (member instanceof MethodDeclaration) {
                MethodDeclaration md = (MethodDeclaration) member;
                if (!isAccessible(md)) continue;
                AstDtos.MethodNode m = new AstDtos.MethodNode();
                m.name = md.getNameAsString();
                m.parameters = paramsOf(md.getParameters());
                String ret = JniDescriptor.of(md.getType());
                m.jniDescriptor = "(" + paramsDescriptor(md.getParameters()) + ")" + ret;
                m.returnTypeFqcn = JniDescriptor.fqcnOf(md.getType());
                m.isStatic = md.isStatic();
                m.modifiers = modifiers(md);
                m.javadoc = javadocOf(md);
                n.methods.add(m);
            }
        }
        return n;
    }

    private static List<AstDtos.ParamNode> paramsOf(NodeList<Parameter> params) {
        List<AstDtos.ParamNode> out = new ArrayList<>();
        for (Parameter p : params) {
            AstDtos.ParamNode pn = new AstDtos.ParamNode();
            pn.name = p.getNameAsString();
            pn.jniDescriptor = p.isVarArgs()
                    ? "[" + JniDescriptor.of(p.getType())
                    : JniDescriptor.of(p.getType());
            pn.typeFqcn = JniDescriptor.fqcnOf(p.getType()) + (p.isVarArgs() ? "[]" : "");
            out.add(pn);
        }
        return out;
    }

    private static String paramsDescriptor(NodeList<Parameter> params) {
        StringBuilder sb = new StringBuilder();
        for (Parameter p : params) {
            if (p.isVarArgs()) {
                sb.append('[').append(JniDescriptor.of(p.getType()));
            } else {
                sb.append(JniDescriptor.of(p.getType()));
            }
        }
        return sb.toString();
    }

    private static List<AstDtos.Modifier> modifiers(NodeWithModifiers<?> n) {
        List<AstDtos.Modifier> out = new ArrayList<>();
        if (n.hasModifier(Keyword.PUBLIC))    out.add(AstDtos.Modifier.PUBLIC);
        if (n.hasModifier(Keyword.PROTECTED)) out.add(AstDtos.Modifier.PROTECTED);
        if (n.hasModifier(Keyword.PRIVATE))   out.add(AstDtos.Modifier.PRIVATE);
        if (n.hasModifier(Keyword.STATIC))    out.add(AstDtos.Modifier.STATIC);
        if (n.hasModifier(Keyword.FINAL))     out.add(AstDtos.Modifier.FINAL);
        if (n.hasModifier(Keyword.ABSTRACT))  out.add(AstDtos.Modifier.ABSTRACT);
        if (n.hasModifier(Keyword.DEFAULT))   out.add(AstDtos.Modifier.DEFAULT);
        return out;
    }

    private static String javadocOf(NodeWithJavadoc<?> n) {
        return n.getJavadoc().map(jd -> jd.getDescription().toText().trim())
                .filter(s -> !s.isEmpty())
                .orElse(null);
    }
}
