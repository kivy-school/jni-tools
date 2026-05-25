from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntSupplier"]

class IntSupplier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntSupplier"
    getAsInt = JavaMethod("()I")