from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProfilingManager"]

class ProfilingManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ProfilingManager"
    PROFILING_TYPE_HEAP_PROFILE = JavaStaticField("I")
    PROFILING_TYPE_JAVA_HEAP_DUMP = JavaStaticField("I")
    PROFILING_TYPE_STACK_SAMPLING = JavaStaticField("I")
    PROFILING_TYPE_SYSTEM_TRACE = JavaStaticField("I")
    addProfilingTriggers = JavaMethod("(Ljava/util/List;)V")
    clearProfilingTriggers = JavaMethod("()V")
    registerForAllProfilingResults = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    removeProfilingTriggersByType = JavaMethod("([I)V")
    requestProfiling = JavaMethod("(ILandroid/os/Bundle;Ljava/lang/String;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    unregisterForAllProfilingResults = JavaMethod("(Ljava/util/function/Consumer;)V")