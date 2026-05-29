from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Supplier"]

class Supplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Supplier"
    get = JavaMethod("()Ljava/lang/Object;")