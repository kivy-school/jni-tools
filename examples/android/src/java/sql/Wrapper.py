from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Wrapper"]

class Wrapper(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Wrapper"
    unwrap = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    isWrapperFor = JavaMethod("(Ljava/lang/Class;)Z")