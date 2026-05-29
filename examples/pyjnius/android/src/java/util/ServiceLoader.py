from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceLoader"]

class ServiceLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ServiceLoader"
    toString = JavaMethod("()Ljava/lang/String;")
    load = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/ServiceLoader;", True, False), ("(Ljava/lang/ModuleLayer;Ljava/lang/Class;)Ljava/util/ServiceLoader;", True, False), ("(Ljava/lang/Class;Ljava/lang/ClassLoader;)Ljava/util/ServiceLoader;", True, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    reload = JavaMethod("()V")
    loadInstalled = JavaStaticMethod("(Ljava/lang/Class;)Ljava/util/ServiceLoader;")
    findFirst = JavaMethod("()Ljava/util/Optional;")

    class Provider(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/ServiceLoader$Provider"
        type = JavaMethod("()Ljava/lang/Class;")
        get = JavaMethod("()Ljava/lang/Object;")