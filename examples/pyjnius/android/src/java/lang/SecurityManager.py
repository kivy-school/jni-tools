from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecurityManager"]

class SecurityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/SecurityManager"
    __javaconstructor__ = [("()V", False)]
    checkCreateClassLoader = JavaMethod("()V")
    getThreadGroup = JavaMethod("()Ljava/lang/ThreadGroup;")
    checkAccess = JavaMultipleMethod([("(Ljava/lang/ThreadGroup;)V", False, False), ("(Ljava/lang/Thread;)V", False, False)])
    checkPermission = JavaMultipleMethod([("(Ljava/security/Permission;)V", False, False), ("(Ljava/security/Permission;Ljava/lang/Object;)V", False, False)])
    checkExit = JavaMethod("(I)V")
    getSecurityContext = JavaMethod("()Ljava/lang/Object;")
    checkExec = JavaMethod("(Ljava/lang/String;)V")
    checkLink = JavaMethod("(Ljava/lang/String;)V")
    checkRead = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False)])
    checkWrite = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False)])
    checkDelete = JavaMethod("(Ljava/lang/String;)V")
    checkConnect = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;ILjava/lang/Object;)V", False, False)])
    checkListen = JavaMethod("(I)V")
    checkAccept = JavaMethod("(Ljava/lang/String;I)V")
    checkMulticast = JavaMultipleMethod([("(Ljava/net/InetAddress;)V", False, False), ("(Ljava/net/InetAddress;B)V", False, False)])
    checkPropertiesAccess = JavaMethod("()V")
    checkPropertyAccess = JavaMethod("(Ljava/lang/String;)V")
    checkPrintJobAccess = JavaMethod("()V")
    checkPackageAccess = JavaMethod("(Ljava/lang/String;)V")
    checkPackageDefinition = JavaMethod("(Ljava/lang/String;)V")
    checkSetFactory = JavaMethod("()V")
    checkSecurityAccess = JavaMethod("(Ljava/lang/String;)V")