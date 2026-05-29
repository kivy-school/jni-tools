from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvocationHandler"]

class InvocationHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/InvocationHandler"
    invoke = JavaMethod("(Ljava/lang/Object;Ljava/lang/reflect/Method;[Ljava/lang/Object;)Ljava/lang/Object;")