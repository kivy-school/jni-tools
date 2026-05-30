from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ServiceConnectionLeakedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ServiceConnectionLeakedViolation"

class InstanceCountViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/InstanceCountViolation"
    getNumberOfInstances = JavaMethod("()J")

class Violation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/Violation"
    fillInStackTrace = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    hashCode = JavaMethod("()I")
    setStackTrace = JavaMethod("([Ljava/lang/StackTraceElement;)V")

class CleartextNetworkViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/CleartextNetworkViolation"

class NetworkViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/NetworkViolation"

class ResourceMismatchViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ResourceMismatchViolation"

class DiskReadViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/DiskReadViolation"

class UntaggedSocketViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/UntaggedSocketViolation"

class IntentReceiverLeakedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/IntentReceiverLeakedViolation"

class FileUriExposedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/FileUriExposedViolation"

class ContentUriWithoutPermissionViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ContentUriWithoutPermissionViolation"

class ExplicitGcViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ExplicitGcViolation"

class SqliteObjectLeakedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/SqliteObjectLeakedViolation"

class CustomViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/CustomViolation"

class DiskWriteViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/DiskWriteViolation"

class ImplicitDirectBootViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ImplicitDirectBootViolation"

class NonSdkApiUsedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/NonSdkApiUsedViolation"

class IncorrectContextUseViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/IncorrectContextUseViolation"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class UnbufferedIoViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/UnbufferedIoViolation"

class CredentialProtectedWhileLockedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/CredentialProtectedWhileLockedViolation"

class UnsafeIntentLaunchViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/UnsafeIntentLaunchViolation"
    __javaconstructor__ = [("(Landroid/content/Intent;)V", False)]
    getIntent = JavaMethod("()Landroid/content/Intent;")

class LeakedClosableViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/LeakedClosableViolation"

class WebViewMethodCalledOnWrongThreadViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/WebViewMethodCalledOnWrongThreadViolation"