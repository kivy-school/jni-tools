from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Wrapper"]

class Wrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Wrapper"
    isWrapperFor = JavaMethod("(Ljava/lang/Class;)Z")
    unwrap = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")