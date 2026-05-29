from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Proxy"]

class Proxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Proxy"
    __javaconstructor__ = [("(Ljava/lang/reflect/InvocationHandler;)V", False)]
    h = JavaField("Ljava/lang/reflect/InvocationHandler;")
    getProxyClass = JavaStaticMethod("(Ljava/lang/ClassLoader;[Ljava/lang/Class;)Ljava/lang/Class;", varargs=True)
    newProxyInstance = JavaStaticMethod("(Ljava/lang/ClassLoader;[Ljava/lang/Class;Ljava/lang/reflect/InvocationHandler;)Ljava/lang/Object;")
    isProxyClass = JavaStaticMethod("(Ljava/lang/Class;)Z")
    getInvocationHandler = JavaStaticMethod("(Ljava/lang/Object;)Ljava/lang/reflect/InvocationHandler;")