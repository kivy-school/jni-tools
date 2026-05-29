from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderScript"]

class RenderScript(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/RenderScript"
    CREATE_FLAG_LOW_LATENCY = JavaStaticField("I")
    CREATE_FLAG_LOW_POWER = JavaStaticField("I")
    CREATE_FLAG_NONE = JavaStaticField("I")
    getMinorVersion = JavaStaticMethod("()J")
    getErrorHandler = JavaMethod("()Landroid/renderscript/RenderScript$RSErrorHandler;")
    setErrorHandler = JavaMethod("(Landroid/renderscript/RenderScript$RSErrorHandler;)V")
    contextDump = JavaMethod("()V")
    createMultiContext = JavaStaticMethod("(Landroid/content/Context;Landroid/renderscript/RenderScript$ContextType;II)Landroid/renderscript/RenderScript;")
    getMessageHandler = JavaMethod("()Landroid/renderscript/RenderScript$RSMessageHandler;")
    releaseAllContexts = JavaStaticMethod("()V")
    setMessageHandler = JavaMethod("(Landroid/renderscript/RenderScript$RSMessageHandler;)V")
    setPriority = JavaMethod("(Landroid/renderscript/RenderScript$Priority;)V")
    destroy = JavaMethod("()V")
    finish = JavaMethod("()V")
    create = JavaMultipleMethod([("(Landroid/content/Context;Landroid/renderscript/RenderScript$ContextType;)Landroid/renderscript/RenderScript;", True, False), ("(Landroid/content/Context;)Landroid/renderscript/RenderScript;", True, False), ("(Landroid/content/Context;Landroid/renderscript/RenderScript$ContextType;I)Landroid/renderscript/RenderScript;", True, False)])
    sendMessage = JavaMethod("(I[I)V")
    getApplicationContext = JavaMethod("()Landroid/content/Context;")

    class RSMessageHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript$RSMessageHandler"
        __javaconstructor__ = [("()V", False)]
        run = JavaMethod("()V")

    class RSErrorHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript$RSErrorHandler"
        __javaconstructor__ = [("()V", False)]
        run = JavaMethod("()V")

    class Priority(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript$Priority"
        LOW = JavaStaticField("Landroid/renderscript/RenderScript$Priority;")
        NORMAL = JavaStaticField("Landroid/renderscript/RenderScript$Priority;")
        values = JavaStaticMethod("()[Landroid/renderscript/RenderScript$Priority;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/renderscript/RenderScript$Priority;")
        LOW = JavaStaticField("Landroid/renderscript/RenderScript$Priority;")
        NORMAL = JavaStaticField("Landroid/renderscript/RenderScript$Priority;")

    class ContextType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript$ContextType"
        DEBUG = JavaStaticField("Landroid/renderscript/RenderScript$ContextType;")
        NORMAL = JavaStaticField("Landroid/renderscript/RenderScript$ContextType;")
        PROFILE = JavaStaticField("Landroid/renderscript/RenderScript$ContextType;")
        values = JavaStaticMethod("()[Landroid/renderscript/RenderScript$ContextType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/renderscript/RenderScript$ContextType;")
        DEBUG = JavaStaticField("Landroid/renderscript/RenderScript$ContextType;")
        NORMAL = JavaStaticField("Landroid/renderscript/RenderScript$ContextType;")
        PROFILE = JavaStaticField("Landroid/renderscript/RenderScript$ContextType;")