from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Proxy"]

class Proxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Proxy"
    getProxyClass = JavaStaticMethod("(Ljava/lang/ClassLoader;[Ljava/lang/Class;)Ljava/lang/Class;", varargs=True)
    newProxyInstance = JavaStaticMethod("(Ljava/lang/ClassLoader;[Ljava/lang/Class;Ljava/lang/reflect/InvocationHandler;)Ljava/lang/Object;")
    isProxyClass = JavaStaticMethod("(Ljava/lang/Class;)Z")
    getInvocationHandler = JavaStaticMethod("(Ljava/lang/Object;)Ljava/lang/reflect/InvocationHandler;")