from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PhantomReference"]

class PhantomReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/PhantomReference"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/ref/ReferenceQueue;)V", False)]
    get = JavaMethod("()Ljava/lang/Object;")