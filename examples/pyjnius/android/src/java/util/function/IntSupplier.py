from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntSupplier"]

class IntSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntSupplier"
    getAsInt = JavaMethod("()I")