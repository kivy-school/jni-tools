from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProcessBuilder"]

class ProcessBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ProcessBuilder"
    __javaconstructor__ = [("(Ljava/util/List;)V", False), ("([Ljava/lang/String;)V", True)]
    directory = JavaMultipleMethod([("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False), ("()Ljava/io/File;", False, False)])
    start = JavaMethod("()Ljava/lang/Process;")
    command = JavaMultipleMethod([("()Ljava/util/List;", False, False), ("([Ljava/lang/String;)Ljava/lang/ProcessBuilder;", False, True), ("(Ljava/util/List;)Ljava/lang/ProcessBuilder;", False, False)])
    environment = JavaMethod("()Ljava/util/Map;")
    redirectInput = JavaMultipleMethod([("()Ljava/lang/ProcessBuilder$Redirect;", False, False), ("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False), ("(Ljava/lang/ProcessBuilder$Redirect;)Ljava/lang/ProcessBuilder;", False, False)])
    redirectOutput = JavaMultipleMethod([("(Ljava/lang/ProcessBuilder$Redirect;)Ljava/lang/ProcessBuilder;", False, False), ("()Ljava/lang/ProcessBuilder$Redirect;", False, False), ("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False)])
    redirectError = JavaMultipleMethod([("(Ljava/io/File;)Ljava/lang/ProcessBuilder;", False, False), ("()Ljava/lang/ProcessBuilder$Redirect;", False, False), ("(Ljava/lang/ProcessBuilder$Redirect;)Ljava/lang/ProcessBuilder;", False, False)])
    redirectErrorStream = JavaMultipleMethod([("(Z)Ljava/lang/ProcessBuilder;", False, False), ("()Z", False, False)])
    inheritIO = JavaMethod("()Ljava/lang/ProcessBuilder;")
    startPipeline = JavaStaticMethod("(Ljava/util/List;)Ljava/util/List;")

    class Redirect(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/ProcessBuilder$Redirect"
        PIPE = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect;")
        INHERIT = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect;")
        DISCARD = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect;")
        appendTo = JavaStaticMethod("(Ljava/io/File;)Ljava/lang/ProcessBuilder$Redirect;")
        type = JavaMethod("()Ljava/lang/ProcessBuilder$Redirect$Type;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        from = JavaStaticMethod("(Ljava/io/File;)Ljava/lang/ProcessBuilder$Redirect;")
        to = JavaStaticMethod("(Ljava/io/File;)Ljava/lang/ProcessBuilder$Redirect;")
        file = JavaMethod("()Ljava/io/File;")

        class Type(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "java/lang/ProcessBuilder$Redirect$Type"
            PIPE = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            INHERIT = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            READ = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            WRITE = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            APPEND = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            values = JavaStaticMethod("()[Ljava/lang/ProcessBuilder$Redirect$Type;")
            valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/ProcessBuilder$Redirect$Type;")
            PIPE = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            INHERIT = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            READ = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            WRITE = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")
            APPEND = JavaStaticField("Ljava/lang/ProcessBuilder$Redirect$Type;")