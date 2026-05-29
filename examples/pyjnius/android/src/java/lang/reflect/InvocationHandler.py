from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvocationHandler"]

class InvocationHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/InvocationHandler"
    invoke = JavaMethod("(Ljava/lang/Object;Ljava/lang/reflect/Method;[Ljava/lang/Object;)Ljava/lang/Object;")
    invokeDefault = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/reflect/Method;[Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)