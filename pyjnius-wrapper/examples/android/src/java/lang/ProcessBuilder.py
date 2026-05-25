from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProcessBuilder"]

class ProcessBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ProcessBuilder"
    __javaconstructor__ = [("(Ljava/util/List;)V", False), ("([Ljava/lang/String;)V", True)]
    command = JavaMultipleMethod([("(Ljava/util/List;)Ljava/lang/ProcessBuilder;", False, False), ("([Ljava/lang/String;)Ljava/lang/ProcessBuilder;", False, True), ("()Ljava/util/List;", False, False)])
    environment = JavaMethod("()Ljava/util/Map;")
    directory = JavaMultipleMethod([("()Ljava/io/File;", False, False), ("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False)])
    redirectInput = JavaMultipleMethod([("(Ljava/lang/ProcessBuilder$Redirect;)Ljava/lang/ProcessBuilder;", False, False), ("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False), ("()Ljava/lang/ProcessBuilder$Redirect;", False, False)])
    redirectOutput = JavaMultipleMethod([("(Ljava/lang/ProcessBuilder$Redirect;)Ljava/lang/ProcessBuilder;", False, False), ("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False), ("()Ljava/lang/ProcessBuilder$Redirect;", False, False)])
    redirectError = JavaMultipleMethod([("(Ljava/lang/ProcessBuilder$Redirect;)Ljava/lang/ProcessBuilder;", False, False), ("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False), ("()Ljava/lang/ProcessBuilder$Redirect;", False, False)])
    inheritIO = JavaMethod("()Ljava/lang/ProcessBuilder;")
    redirectErrorStream = JavaMultipleMethod([("()Z", False, False), ("(Z)Ljava/lang/ProcessBuilder;", False, False)])
    start = JavaMethod("()Ljava/lang/Process;")

    class Redirect(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/ProcessBuilder/Redirect"
        INHERIT = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect;")
        PIPE = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect;")
        type = JavaMethod("()Ljava/lang/ProcessBuilder$Redirect$Type;")
        file = JavaMethod("()Ljava/io/File;")
        from = JavaStaticMethod("(Ljava/io/File;)Ljava/lang/ProcessBuilder$Redirect;")
        to = JavaStaticMethod("(Ljava/io/File;)Ljava/lang/ProcessBuilder$Redirect;")
        appendTo = JavaStaticMethod("(Ljava/io/File;)Ljava/lang/ProcessBuilder$Redirect;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

        class Type(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "java/lang/ProcessBuilder/Redirect/Type"
            values = JavaStaticMethod("()[Ljava/lang/ProcessBuilder$Redirect$Type;")
            valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/ProcessBuilder$Redirect$Type;")
            PIPE = JavaStaticField("Ljava/lang/ProcessBuilder/Redirect/Type;")
            INHERIT = JavaStaticField("Ljava/lang/ProcessBuilder/Redirect/Type;")
            READ = JavaStaticField("Ljava/lang/ProcessBuilder/Redirect/Type;")
            WRITE = JavaStaticField("Ljava/lang/ProcessBuilder/Redirect/Type;")
            APPEND = JavaStaticField("Ljava/lang/ProcessBuilder/Redirect/Type;")