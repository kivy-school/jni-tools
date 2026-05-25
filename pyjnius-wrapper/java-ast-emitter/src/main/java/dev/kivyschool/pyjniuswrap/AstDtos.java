package dev.kivyschool.pyjniuswrap;

import com.fasterxml.jackson.annotation.JsonInclude;
import java.util.List;

/**
 * DTO tree mirrored by the Swift Codable schema in PyjniusWrapCore.
 * Field order here is the canonical wire order — keep it stable.
 */
public final class AstDtos {
    private AstDtos() {}

    public enum ClassKind { CLASS, INTERFACE, ENUM, ANNOTATION }

    public enum Modifier { PUBLIC, PROTECTED, PRIVATE, STATIC, FINAL, ABSTRACT, DEFAULT }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class Document {
        public List<ClassNode> classes;
    }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class ClassNode {
        public String fqcn;
        public String jniName;
        public String simpleName;
        public ClassKind kind;
        public List<Modifier> modifiers;
        public String superclass;       // FQCN or null
        public List<String> interfaces; // FQCNs
        public String javadoc;          // null if absent
        public List<FieldNode> fields;
        public List<ConstructorNode> constructors;
        public List<MethodNode> methods;
        public List<ClassNode> nested;
        public List<EnumConstantNode> enumConstants;
    }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class FieldNode {
        public String name;
        public String jniDescriptor; // e.g. "Ljava/lang/String;"
        public String typeFqcn;      // resolved type FQCN (best-effort)
        public boolean isStatic;
        public List<Modifier> modifiers;
        public String javadoc;
    }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class ParamNode {
        public String name;
        public String jniDescriptor;
        public String typeFqcn;
    }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class ConstructorNode {
        public String jniDescriptor;
        public boolean isVarargs;
        public List<Modifier> modifiers;
        public List<ParamNode> parameters;
        public String javadoc;
    }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class MethodNode {
        public String name;
        public String jniDescriptor;
        public boolean isStatic;
        public boolean isVarargs;
        public List<Modifier> modifiers;
        public List<ParamNode> parameters;
        public String returnTypeFqcn;
        public String javadoc;
    }

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public static final class EnumConstantNode {
        public String name;
        public String javadoc;
    }
}
