from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureClassLoader"]

class SecureClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureClassLoader"
    __javaconstructor__ = [("(Ljava/lang/ClassLoader;)V", False), ("()V", False)]
    defineClass = JavaMultipleMethod([("(Ljava/lang/String;[BIILjava/security/CodeSource;)Ljava/lang/Class;", False, False), ("(Ljava/lang/String;Ljava/nio/ByteBuffer;Ljava/security/CodeSource;)Ljava/lang/Class;", False, False)])
    getPermissions = JavaMethod("(Ljava/security/CodeSource;)Ljava/security/PermissionCollection;")