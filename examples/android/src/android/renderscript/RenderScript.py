from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderScript"]

class RenderScript(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/RenderScript"
    CREATE_FLAG_LOW_LATENCY = JavaStaticField("I")
    CREATE_FLAG_LOW_POWER = JavaStaticField("I")
    CREATE_FLAG_NONE = JavaStaticField("I")
    getMinorVersion = JavaStaticMethod("()J")
    setMessageHandler = JavaMethod("(Landroid/renderscript/RenderScript$RSMessageHandler;)V")
    getMessageHandler = JavaMethod("()Landroid/renderscript/RenderScript$RSMessageHandler;")
    sendMessage = JavaMethod("(I[I)V")
    setErrorHandler = JavaMethod("(Landroid/renderscript/RenderScript$RSErrorHandler;)V")
    getErrorHandler = JavaMethod("()Landroid/renderscript/RenderScript$RSErrorHandler;")
    setPriority = JavaMethod("(Landroid/renderscript/RenderScript$Priority;)V")
    getApplicationContext = JavaMethod("()Landroid/content/Context;")
    create = JavaMultipleMethod([("(Landroid/content/Context;)Landroid/renderscript/RenderScript;", True, False), ("(Landroid/content/Context;Landroid/renderscript/RenderScript$ContextType;)Landroid/renderscript/RenderScript;", True, False), ("(Landroid/content/Context;Landroid/renderscript/RenderScript$ContextType;I)Landroid/renderscript/RenderScript;", True, False)])
    releaseAllContexts = JavaStaticMethod("()V")
    createMultiContext = JavaStaticMethod("(Landroid/content/Context;Landroid/renderscript/RenderScript$ContextType;II)Landroid/renderscript/RenderScript;")
    contextDump = JavaMethod("()V")
    finish = JavaMethod("()V")
    finalize = JavaMethod("()V")
    destroy = JavaMethod("()V")

    class ContextType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript/ContextType"
        values = JavaStaticMethod("()[Landroid/renderscript/RenderScript$ContextType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/renderscript/RenderScript$ContextType;")
        NORMAL = JavaStaticField("Landroid/renderscript/RenderScript/ContextType;")
        DEBUG = JavaStaticField("Landroid/renderscript/RenderScript/ContextType;")
        PROFILE = JavaStaticField("Landroid/renderscript/RenderScript/ContextType;")

    class Priority(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript/Priority"
        values = JavaStaticMethod("()[Landroid/renderscript/RenderScript$Priority;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/renderscript/RenderScript$Priority;")
        LOW = JavaStaticField("Landroid/renderscript/RenderScript/Priority;")
        NORMAL = JavaStaticField("Landroid/renderscript/RenderScript/Priority;")

    class RSErrorHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript/RSErrorHandler"
        __javaconstructor__ = [("()V", False)]
        mErrorMessage = JavaField("Ljava/lang/String;")
        mErrorNum = JavaField("I")
        run = JavaMethod("()V")

    class RSMessageHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/RenderScript/RSMessageHandler"
        __javaconstructor__ = [("()V", False)]
        mData = JavaField("[I")
        mID = JavaField("I")
        mLength = JavaField("I")
        run = JavaMethod("()V")