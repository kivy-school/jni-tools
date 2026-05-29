from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Supplier"]

class Supplier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Supplier"
    get = JavaMethod("()Ljava/lang/Object;")