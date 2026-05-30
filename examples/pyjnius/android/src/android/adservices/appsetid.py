from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AppSetIdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/appsetid/AppSetIdManager"
    getAppSetId = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/appsetid/AppSetIdManager;")

class AppSetId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/appsetid/AppSetId"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    SCOPE_APP = JavaStaticField("I")
    SCOPE_DEVELOPER = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getScope = JavaMethod("()I")