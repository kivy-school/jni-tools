from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BooleanSupplier"]

class BooleanSupplier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BooleanSupplier"
    getAsBoolean = JavaMethod("()Z")