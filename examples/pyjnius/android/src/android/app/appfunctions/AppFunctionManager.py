from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppFunctionManager"]

class AppFunctionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appfunctions/AppFunctionManager"
    APP_FUNCTION_STATE_DEFAULT = JavaStaticField("I")
    APP_FUNCTION_STATE_DISABLED = JavaStaticField("I")
    APP_FUNCTION_STATE_ENABLED = JavaStaticField("I")
    executeAppFunction = JavaMethod("(Landroid/app/appfunctions/ExecuteAppFunctionRequest;Ljava/util/concurrent/Executor;Landroid/os/CancellationSignal;Landroid/os/OutcomeReceiver;)V")
    isAppFunctionEnabled = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    setAppFunctionEnabled = JavaMethod("(Ljava/lang/String;ILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")