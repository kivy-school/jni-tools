from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InMemoryDexClassLoader"]

class InMemoryDexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/InMemoryDexClassLoader"
    __javaconstructor__ = [("(Ljava/nio/ByteBuffer;Ljava/lang/ClassLoader;)V", False), ("([Ljava/nio/ByteBuffer;Ljava/lang/ClassLoader;)V", False), ("([Ljava/nio/ByteBuffer;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]