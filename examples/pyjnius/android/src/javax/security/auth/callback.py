from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PasswordCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/PasswordCallback"
    __javaconstructor__ = [("(Ljava/lang/String;Z)V", False)]
    getPassword = JavaMethod("()[C")
    clearPassword = JavaMethod("()V")
    isEchoOn = JavaMethod("()Z")
    getPrompt = JavaMethod("()Ljava/lang/String;")
    setPassword = JavaMethod("([C)V")

class UnsupportedCallbackException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/UnsupportedCallbackException"
    __javaconstructor__ = [("(Ljavax/security/auth/callback/Callback;)V", False), ("(Ljavax/security/auth/callback/Callback;Ljava/lang/String;)V", False)]
    getCallback = JavaMethod("()Ljavax/security/auth/callback/Callback;")

class CallbackHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/CallbackHandler"
    handle = JavaMethod("([Ljavax/security/auth/callback/Callback;)V")

class Callback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/Callback"