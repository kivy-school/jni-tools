from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Process"]

class Process(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Process"
    __javaconstructor__ = [("()V", False)]
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getErrorStream = JavaMethod("()Ljava/io/InputStream;")
    waitFor = JavaMultipleMethod([("()I", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    exitValue = JavaMethod("()I")
    destroy = JavaMethod("()V")
    destroyForcibly = JavaMethod("()Ljava/lang/Process;")
    isAlive = JavaMethod("()Z")