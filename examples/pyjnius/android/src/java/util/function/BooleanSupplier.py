from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BooleanSupplier"]

class BooleanSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BooleanSupplier"
    getAsBoolean = JavaMethod("()Z")