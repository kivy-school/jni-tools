from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Process"]

class Process(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Process"
    __javaconstructor__ = [("()V", False)]
    info = JavaMethod("()Ljava/lang/ProcessHandle$Info;")
    close = JavaMethod("()V")
    isAlive = JavaMethod("()Z")
    destroy = JavaMethod("()V")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    pid = JavaMethod("()J")
    getErrorStream = JavaMethod("()Ljava/io/InputStream;")
    waitFor = JavaMultipleMethod([("()I", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/time/Duration;)Z", False, False)])
    onExit = JavaMethod("()Ljava/util/concurrent/CompletableFuture;")
    toHandle = JavaMethod("()Ljava/lang/ProcessHandle;")
    destroyForcibly = JavaMethod("()Ljava/lang/Process;")
    outputWriter = JavaMultipleMethod([("(Ljava/nio/charset/Charset;)Ljava/io/BufferedWriter;", False, False), ("()Ljava/io/BufferedWriter;", False, False)])
    inputReader = JavaMultipleMethod([("()Ljava/io/BufferedReader;", False, False), ("(Ljava/nio/charset/Charset;)Ljava/io/BufferedReader;", False, False)])
    errorReader = JavaMultipleMethod([("()Ljava/io/BufferedReader;", False, False), ("(Ljava/nio/charset/Charset;)Ljava/io/BufferedReader;", False, False)])
    exitValue = JavaMethod("()I")
    descendants = JavaMethod("()Ljava/util/stream/Stream;")
    supportsNormalTermination = JavaMethod("()Z")
    children = JavaMethod("()Ljava/util/stream/Stream;")