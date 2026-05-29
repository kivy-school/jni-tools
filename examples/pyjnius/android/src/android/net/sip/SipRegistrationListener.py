from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipRegistrationListener"]

class SipRegistrationListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipRegistrationListener"
    onRegistering = JavaMethod("(Ljava/lang/String;)V")
    onRegistrationDone = JavaMethod("(Ljava/lang/String;J)V")
    onRegistrationFailed = JavaMethod("(Ljava/lang/String;ILjava/lang/String;)V")