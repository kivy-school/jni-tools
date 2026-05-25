from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceLoader"]

class ServiceLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ServiceLoader"
    iterator = JavaMethod("()Ljava/util/Iterator;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    load = JavaMultipleMethod([("(Ljava/lang/Class;Ljava/lang/ClassLoader;)Ljava/util/ServiceLoader;", True, False), ("(Ljava/lang/Class;)Ljava/util/ServiceLoader;", True, False)])
    loadInstalled = JavaStaticMethod("(Ljava/lang/Class;)Ljava/util/ServiceLoader;")
    findFirst = JavaMethod("()Ljava/util/Optional;")
    reload = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Provider(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/ServiceLoader/Provider"
        type = JavaMethod("()Ljava/lang/Class;")
        get = JavaMethod("()Ljava/lang/Object;")